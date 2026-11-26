#!/usr/bin/env python3
"""Check the declared checkpoint archive without executing historical scripts.

Python 3.10+, standard library only. Run with --check to compare the exact
generated report with results/archive-import-20261126.json without writing.
This verifies file integrity and syntax, not the mathematics of the records.
"""
from __future__ import annotations

import argparse
import ast
from collections import Counter
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT / 'archive'
OUTPUT = ROOT / 'results' / 'archive-import-20261126.json'


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def verify():
    manifest_bytes = (ARCHIVE / 'manifest.json').read_bytes()
    manifest = json.loads(manifest_bytes)
    records = manifest['records']
    standalone = manifest['standalone_files']
    bundles = manifest['bundles']
    require(len(records) == manifest['expected_records'] == manifest['published_records'] == 90,
            'Narrative count differs from the declared source collection')
    require(len(standalone) == 32 and len(bundles) == 29, 'Source category count differs')
    source_names = [item['original_filename'] for item in records + standalone + bundles]
    require(len(source_names) == len(set(source_names)) == manifest['expected_source_files']
            == manifest['published_source_files'] == 151, 'Source inventory differs')
    counts = Counter()
    dates = Counter()
    paths = set()
    total_bytes = 0

    def read(item):
        nonlocal total_bytes
        path = (ARCHIVE / item['path']).resolve()
        require(path.is_relative_to(ARCHIVE.resolve()), 'Path escapes the archive')
        require(item['path'] not in paths, 'Duplicate manifest file')
        paths.add(item['path'])
        data = path.read_bytes()
        require(len(data) == item['bytes'], f'Wrong size: {item["path"]}')
        require(digest(data) == item['sha256'], f'Hash mismatch: {item["path"]}')
        total_bytes += len(data)
        return data.decode('utf-8')

    def check_asset(item):
        content = read(item)
        kind = item['content_type']
        if kind == 'python':
            ast.parse(content, filename=item['path'])
            counts['python_syntax_checked_not_executed'] += 1
        elif kind in ('json', 'jsonl'):
            if item['format_check'] == 'json_lines_parse_pass':
                for line in content.splitlines():
                    if line.strip():
                        json.loads(line)
                counts['json_lines_files_parsed'] += 1
            else:
                json.loads(content)
                counts['json_files_parsed'] += 1
        elif kind == 'text':
            counts['text_files_hash_checked'] += 1
        else:
            raise RuntimeError(f'Unexpected content type {kind}')

    for record in records:
        read(record)
        dates[record['recorded_time_label'][:10]] += 1
        files = record['files']
        require(len(files) == record['embedded_block_count'], 'Embedded block count differs')
        require([a['block'] for a in files] == list(range(1, len(files)+1)), 'Block sequence differs')
        for item in files:
            check_asset(item)
    for item in standalone:
        check_asset(item)
    for bundle in bundles:
        read(bundle)
        require(len(bundle['files']) == bundle['member_count'], 'Bundle member count differs')
        for item in bundle['files']:
            check_asset(item)
    embedded_count = sum(len(r['files']) for r in records)
    member_count = sum(len(b['files']) for b in bundles)
    require(embedded_count == manifest['embedded_block_count'] == 220, 'Embedded asset count differs')
    require(member_count == 335 and sum(counts.values()) == 587, 'Total asset count differs')
    actual = {str(p.relative_to(ARCHIVE)) for p in (ARCHIVE / 'riemann').rglob('*') if p.is_file()}
    require(actual == paths, 'Missing or unlisted files in the checkpoint archive')
    return {
        'schema_version': 1,
        'date': '2026-11-26',
        'status': 'pass',
        'source_sha256': digest(Path(__file__).read_bytes()),
        'manifest_sha256': digest(manifest_bytes),
        'source_files_accounted_for': len(source_names),
        'record_count': len(records),
        'script_bundle_count': len(bundles),
        'zip_members_preserved': member_count,
        'standalone_files_preserved': len(standalone),
        'embedded_blocks_preserved': embedded_count,
        'asset_count': sum(counts.values()),
        'manifest_files_checked': len(paths),
        'manifest_bytes_checked': total_bytes,
        'records_by_date': dict(dates),
        'format_checks': dict(counts),
        'historical_scripts_executed': 0,
        'scope': 'Sizes, SHA-256 hashes, inventory completeness within the declared 151-source Riemann collection, Python syntax and JSON/JSON Lines parsing. No mathematical correctness or completeness claim for every historical research project.',
        'separate_finite_replay': 'results/archived-units-20261126.json',
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    parser.add_argument('--output', type=Path, default=OUTPUT)
    args = parser.parse_args()
    report = verify()
    encoded = json.dumps(report, indent=2, sort_keys=True) + '\n'
    if args.check:
        require(args.output.read_text() == encoded, 'Recorded import report differs')
    else:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(encoded)
    print(f'PASS: {report["record_count"]} records, {report["asset_count"]} assets, {report["manifest_files_checked"]} file hashes')
    print(f'result_sha256={digest(encoded.encode())}')


if __name__ == '__main__':
    main()
