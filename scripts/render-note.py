#!/usr/bin/env python3
"""Render a reviewed Markdown note and update its existing research portal entries.

This is a build tool, not a mathematical verifier. Install requirements-site.txt.
Run from the repository root:
  python scripts/render-note.py publication/ml-pnp-005.json --source-ref COMMIT_SHA

The published source, code and data are pinned to an already-created commit.
Existing articles retain their own version and provenance. Re-running is idempotent.
"""
from __future__ import annotations

import argparse
from copy import deepcopy
import html as html_escape
import json
from pathlib import Path
import re
from urllib.parse import urlsplit

from lxml import etree, html
import mistune

ROOT = Path(__file__).resolve().parents[1]
REPO = "https://github.com/ErikLachance/mila-math-lab"


def esc(value):
    return html_escape.escape(str(value), quote=True)


def tr(english, french):
    return f'<span data-fr="{esc(french)}">{esc(english)}</span>'


def translated(value):
    return tr(value["en"], value["fr"])


def fragment(value):
    return html.fragment_fromstring(value)


def save(tree, path):
    (ROOT / path).write_text(
        html.tostring(tree, encoding="unicode", doctype="<!doctype html>") + "\n",
        encoding="utf-8",
    )


def collection_version(tree, version):
    for element in tree.xpath("//footer//*[@data-fr]"):
        if element.text and element.text.startswith("Collection "):
            element.text = re.sub(r"Collection \d+\.\d+\.\d+", f"Collection {version}", element.text)
            element.set("data-fr", re.sub(r"Collection \d+\.\d+\.\d+", f"Collection {version}", element.get("data-fr")))


class Renderer(mistune.HTMLRenderer):
    def __init__(self):
        super().__init__(escape=True)
        self.headings = []

    def heading(self, text, level, **attrs):
        if level == 1:
            return ""  # The page heading comes from the reviewed bilingual metadata.
        identifier = ""
        if level == 2:
            identifier = f"section-{len(self.headings) + 1}"
            self.headings.append((identifier, html.fromstring(f"<div>{text}</div>").text_content()))
        attribute = f' id="{identifier}"' if identifier else ""
        return f"<h{level}{attribute}>{text}</h{level}>\n"

    def block_math(self, text):
        return f'<div class="display-math">$$\n{esc(text)}\n$$</div>\n'

    def inline_math(self, text):
        return f'<span class="math-inline">\\({esc(text)}\\)</span>'


def render(meta, source_ref):
    source_url = lambda path: f"{REPO}/blob/{source_ref}/{path}"
    paper_href = Path(meta["output"]).relative_to("docs").as_posix()
    title = translated(meta["title"])
    summary = translated(meta["summary"])
    result = translated(meta["result"])
    scope = translated(meta["scope"])
    kind = tr("Proof and finite verification", "Preuve et vérification finie")
    links = (
        f'<a data-local href="{paper_href}">{tr("Full note (EN)", "Note intégrale (EN)")}</a>'
        f'<a href="{source_url(meta["code"])}">{tr("Code", "Code")}</a>'
        f'<a href="{source_url(meta["data"])}">{tr("Exact data", "Données exactes")}</a>'
    )
    card = fragment(
        f'<article class="paper" data-note-id="{meta["id"]}"><div class="paper-meta">'
        f'<strong>{meta["id"]}</strong><span>P vs NP</span><br>{kind}<br>'
        f'{tr("Verified 26 Nov 2026", "Vérifié le 26 nov. 2026")}</div><div>'
        f'<h3><a data-local href="{paper_href}">{title}</a></h3><p>{summary}</p>'
        f'<p><strong>{tr("Result.", "Résultat.")}</strong> {result}</p>'
        f'<p class="lim"><strong>{tr("Scope.", "Portée.")}</strong> {scope}</p>'
        f'<div class="links">{links}</div></div></article>'
    )

    renderer = Renderer()
    markdown = mistune.create_markdown(renderer=renderer, plugins=["table", "math"])
    article = fragment('<article class="article" lang="en"></article>')
    article.append(fragment('<p class="notice">' + tr("Full note in English; summary and navigation in French.", "Note intégrale en anglais ; résumé et navigation en français.") + '</p>'))
    article.extend(html.fragments_fromstring(markdown((ROOT / meta["source"]).read_text(encoding="utf-8"))))
    source_parent = Path(meta["source"]).parent
    for anchor in article.xpath(".//a[@href]"):
        target = anchor.get("href")
        if not urlsplit(target).scheme and not target.startswith("#"):
            resolved = (ROOT / source_parent / target).resolve().relative_to(ROOT).as_posix()
            anchor.set("href", source_url(resolved))
    for table in article.xpath(".//table"):
        wrapper = etree.Element("div", {"class": "tablewrap"})
        table.addprevious(wrapper)
        wrapper.append(table)

    page = html.fromstring((ROOT / "docs/papers/ml-pnp-004.html").read_text())
    page.xpath("//title")[0].text = meta["title"]["en"] + " | MILA Mathematical Research Lab"
    page.xpath('//meta[@name="description"]')[0].set("content", meta["summary"]["en"])
    for script in page.xpath("//head/script[not(@src)]"):
        if script.text and "MathJax" in script.text:
            script.text = r"window.MathJax={tex:{inlineMath:[['\\(','\\)']],displayMath:[['$$','$$']]},options:{skipHtmlTags:['script','noscript','style','textarea','pre','code']}};"
    main = page.xpath("//main")[0]
    for child in list(main):
        main.remove(child)
    main.text = None
    main.append(fragment('<div class="crumb"><a data-local href="../index.html">' + tr("Overview", "Accueil") + '</a> / <a data-local href="../p-vs-np.html">P vs NP</a> / ' + meta["id"] + '</div>'))
    main.append(fragment(
        '<section class="pagehead"><p class="eyebrow">' + meta["id"] + ' · ' + kind + '</p>'
        '<h1>' + title + '</h1><p class="quiet">2026-11-26 · ' + tr("Not peer reviewed", "Non évalué par les pairs") + '</p>'
        '<div class="abstract"><h2>' + tr("Summary", "Résumé") + '</h2><p>' + summary + '</p>'
        '<p><strong>' + tr("Result.", "Résultat.") + '</strong> ' + result + '</p>'
        '<p><strong>' + tr("Scope.", "Portée.") + '</strong> ' + scope + '</p></div>'
        '<div class="links"><a href="' + source_url(meta["source"]) + '">' + tr("Source Markdown (EN)", "Source Markdown (EN)") + '</a>'
        '<a href="' + source_url(meta["code"]) + '">' + tr("Verification code", "Code de vérification") + '</a>'
        '<a href="' + source_url(meta["data"]) + '">' + tr("Exact data", "Données exactes") + '</a></div></section>'
    ))
    toc = ''.join(f'<li><a href="#{identifier}">{esc(text)}</a></li>' for identifier, text in renderer.headings)
    layout = fragment('<div class="article-layout"><aside><nav aria-label="Contents"><p class="eyebrow">' + tr("Contents (English)", "Sommaire (anglais)") + '</p><ul class="toc">' + toc + '</ul><p class="quiet">' + meta["id"] + '</p></nav></aside></div>')
    layout.append(article)
    main.append(layout)
    collection_version(page, meta["version"])
    save(page, meta["output"])

    for path in ("docs/index.html", "docs/catalog.html", "docs/p-vs-np.html"):
        tree = html.fromstring((ROOT / path).read_text())
        for existing in tree.xpath(f'//article[@data-note-id="{meta["id"]}"]'):
            existing.getparent().remove(existing)
        if path.endswith("index.html"):
            old = tree.xpath('//article[contains(@class,"paper")][.//strong[text()="ML-PNP-004"]]')
            if old:
                old[0].getparent().replace(old[0], deepcopy(card))
            else:
                first = tree.xpath('//article[contains(@class,"paper")]')[0]
                first.addprevious(deepcopy(card))
        else:
            first = tree.xpath('//article[contains(@class,"paper")]')[0]
            entry = deepcopy(card)
            if path.endswith("catalog.html"):
                entry.set("data-paper", "")
                entry.set("data-field", "pnp")
                entry.set("data-type", meta["type"])
                entry.set("data-search", ' '.join([meta["id"], "P vs NP", *[v for key in ("title", "summary", "result", "scope") for v in meta[key].values()]]))
            first.addprevious(entry)
        if path.endswith("catalog.html"):
            note_count = len(tree.xpath("//article[@data-paper]"))
            tree.xpath('//*[@id="count"]')[0].text = f'{note_count} notes'
            tree.xpath('//meta[@name="description"]')[0].set("content", f'Search all {note_count} mathematical research notes and certificates.')
            introduction = tree.xpath('//section[@class="pagehead"]/p[@class="lede"]/span')[0]
            introduction.text = f'{note_count} research notes with stable identifiers, source dates, full English text and verification data. None has been peer reviewed.'
            introduction.set("data-fr", f'{note_count} notes de recherche avec identifiants stables, dates sources, texte intégral anglais et données de vérification. Aucune n’a été évaluée par les pairs.')
        if path.endswith("p-vs-np.html"):
            item = tree.xpath('//ol[@class="list"]/li')[-1]
            item.clear()
            item.append(fragment(tr("Use ML-PNP-005 to rule out independent repetition as degree amplification; specify the circuit class, locality, output stretch and the theorem connecting the chosen invariant to hardness.", "Utiliser ML-PNP-005 pour écarter la répétition indépendante comme amplification du degré ; préciser la classe de circuits, la localité, le nombre de sorties et le théorème reliant l’invariant à la difficulté.")))
        collection_version(tree, meta["version"])
        save(tree, path)

    methods = html.fromstring((ROOT / "docs/methods.html").read_text())
    command = methods.xpath('//pre[@class="command"]')[0]
    new_command = f'python3 {meta["code"]} --check'
    if new_command not in command.text_content():
        command.text = command.text_content().rstrip() + "\n" + new_command
    for existing in methods.xpath('//*[@id="boolean-degree-checks"]'):
        existing.getparent().remove(existing)
    methods.xpath('//*[@class="subgrid"]')[0].append(fragment(
        '<div class="method" id="boolean-degree-checks"><h3>' + tr("Boolean graph degree", "Degré des graphes booléens") + '</h3><p>'
        + tr("Exact finite-field ranks, exhaustive small functions, threshold witnesses and product checks. The general theorems are proved in ML-PNP-005.", "Rangs exacts sur corps fini, petites fonctions exhaustives, témoins pour les seuils et contrôles des produits. Les théorèmes généraux sont démontrés dans ML-PNP-005.")
        + '</p><div class="links"><a href="' + source_url(meta["code"]) + '">' + tr("Script", "Script") + '</a><a href="' + source_url(meta["data"]) + '">' + tr("Exact output", "Résultat exact") + '</a></div></div>'
    ))
    collection_version(methods, meta["version"])
    save(methods, "docs/methods.html")
    print(json.dumps({"article": meta["output"], "source_ref": source_ref, "sections": len(renderer.headings), "portal_entries_updated": 3}))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("metadata", type=Path)
    parser.add_argument("--source-ref", required=True)
    args = parser.parse_args()
    if not re.fullmatch(r"[0-9a-f]{40}", args.source_ref):
        parser.error("--source-ref must be a full commit SHA")
    render(json.loads(args.metadata.read_text(encoding="utf-8")), args.source_ref)
