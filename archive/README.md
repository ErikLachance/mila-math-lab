# Historical scientific research archive

**Archive import 0.5.1 — 26 November 2026.** The scientific contents of **all 151 source files in the inventoried Riemann research collection** are published here. They comprise **90 narrative records, 29 script bundles and 32 standalone Python or JSON files**. The records include 67 named checkpoints and 23 supplements, corrections, addenda and backup documents, dated 7 and 23–25 November 2026. This archive complements the [13 reconstructed research notes](../notes/research-archive.md).

**En français.** Les 151 sources scientifiques du dossier inventorié sont intégrées : 90 comptes rendus, 29 archives de scripts et 32 fichiers Python ou JSON séparés. Le contenu des ZIP est publié sous forme de dossiers consultables. Les résultats anciens restent des résultats consignés à leur date ; un contrôle indépendant ciblé a été refait sur dix normes d’unités et les espaces vectoriels enregistrés sur F₇.

[Browse on the website](https://eriklachance.github.io/mila-math-lab/archive.html) · [Source and file manifest](manifest.json) · [Import verification report](../results/archive-import-20261126.json) · [Finite certificate replay](../results/archived-units-20261126.json)

## Read the corrections with the earlier records

The [23 November 17:48 corrigendum](riemann/supplements/RIEMANN_CORRIGENDUM_2026-11-23_1748_EST/README.md) qualifies an earlier family-membership inference. The [25 November H9/G2 addendum](riemann/supplements/RIEMANN_ADDENDUM_2026-11-25_H9_G2/README.md) makes an upstream dependency explicit. They are part of the archive and should be read alongside the affected earlier arguments. Neither document is a general proof of H9 or RH.

## What is preserved

Each narrative source has a scientific `README.md`. Its embedded code, data and outputs are extracted into linked `files/` entries. Standalone files are preserved in `riemann/standalone/`. Each of the 29 source ZIPs is represented by a directory under `riemann/bundles/`, with a member inventory and every contained file; the original ZIP container itself is not required to read the complete contents.

The **587 code, data and text assets** consist of **220 embedded blocks**, **335 ZIP members** and **32 standalone files**. The current integrity report checks **283 Python files**, **238 JSON files**, **2 JSON Lines files** and **64 text files**. File types are checked from their content role and names, including originally unlabelled fences. Two source fences labelled `json` actually contain JSON Lines; their generated extracted filenames use `.jsonl`.

All embedded and standalone code/data bytes and ZIP-member bytes are unchanged. Public narratives are edited scientific derivatives: private continuity and storage sections, internal identifiers and session scheduling metadata were omitted. They are not byte-identical copies of the original whole documents. Scientific hypotheses, failed methods, counterexamples, mathematical limitations and source citations are retained. The manifest gives every original source filename, its public representation, extracted block or member provenance, file size and SHA-256 hash.

Statements such as “executed”, “verified”, “PASS”, and external verification reports within a record refer to its historical source date. They do not imply a fresh execution or external review during this import. The records contain conditional and exploratory arguments. Their archival publication does not establish RH, general automorphy, or the correctness of all upstream arithmetic identifications.

## What was checked during import

The [archive integrity verifier](../scripts/verify-archive.py) checks **706 manifest-listed public files**: 90 scientific narratives, 29 bundle inventories and 587 assets. It verifies sizes and SHA-256 hashes, matches the declared inventory to the directory contents, parses Python without executing it, and parses JSON and JSON Lines data. The [import report](../results/archive-import-20261126.json) records the scope and manifest hash. The source ledger accounts for each of the 151 inventoried source files exactly once.

A separate [standard-library verifier](../experiments/verify-archived-units.py) reads only three JSON inputs from the 25 November 11:05 and 11:51 records. It independently checks the supplied integer multiplication algebras and ten selected determinants, then recomputes exact linear algebra on the recorded local vectors over F₇. Its [recorded result](../results/archived-units-20261126.json) contains input and source hashes.

| Fresh finite check | q = 683 | q = 907 |
|---|---:|---:|
| Selected determinants matching the recorded ±1 norms | 5 | 5 |
| Integer multiplication-table composition identities | 441 | 441 |
| Rank of the span of recorded vectors and their shift orbits | 20 | 20 |
| Ranks of DⁱU, for i = 0,…,7 | 20, 17, 14, 11, 8, 5, 2, 0 | 20, 17, 14, 11, 8, 5, 2, 0 |
| Ranks of U + im(Dⁱ), for i = 1,…,7 | 38, 35, 32, 29, 26, 23, 20 | 38, 35, 32, 29, 26, 23, 20 |
| Weight-space dimensions, eigenvalues 1,…,6 | 3, 4, 3, 4, 3, 3 | 3, 4, 3, 4, 3, 3 |
| Jordan block lengths on the recorded orbit span | 7, 7, 6 | 7, 7, 6 |

The fresh replay **does not recompute the arithmetic local embeddings** that produced these vectors, compare newly regenerated 7-adic precision levels, identify the number fields, prove order maximality, determine full unit groups, recompute `e_loc` or `e8`, or certify the class-group, Kummer, reciprocity and automorphy hypotheses. Rank 20 here is a verified statement about the supplied finite vectors and operators. The archived arguments connecting them to arithmetic remain subject to review.

To repeat these two bounded checks with Python 3.10+ and no third-party dependencies:

```sh
python3 scripts/verify-archive.py --check
python3 experiments/verify-archived-units.py --check
```

Historical programs remain research source material. Some require SymPy, NumPy, mpmath or SciPy; refer to earlier records or separate bundles; use generic `/mnt/data/` paths; perform timed searches; or generate local caches. They are not a single ready-to-run pipeline. For example, the standalone W24 script expects the companion W25 module under its original short name; a p-curvature supplement imports controls from another bundle; another script uses its historical absolute path for a companion program. The narrative and bundle inventories preserve this context. The two current verification commands above require only the Python standard library and do not execute historical programs.

## Coverage and remaining gaps

The transfer is complete for **all 151 sources in the scoped collection inventoried on 26 November 2026**, with no missing listed file. Its 90 narrative sources, 32 standalone files and 29 ZIP representations are indexed below and in the manifest. Every explicit complete checkpoint filename found in the scoped narrative sources resolves to this inventory, including the alias `RIEMANN_CHECKPOINT_2026-11-23_0543_EST.md`, whose supplied source filename has the prefix `2026-11-23_0526_`.

This is not an inventory of every historical research project or a guarantee that all dynamic script dependencies and omitted intermediate datasets are recoverable. It does not certify every mathematical argument. The original P-vs-NP scripts listed as unrecovered in the [advanced note](../notes/pnp-advanced-20261109.md) remain distinct from later independent reconstructions. The compute engine is a separate project. A complete private research journal is not published.

## Chronological narrative inventory

The dates and time labels come from original filenames. They identify historical records, not priority claims or newly verified results. Some backup and addendum filenames specify a date without a time. Each linked record contains its scientific narrative and extracted-file links.

| Recorded label | Source record | Embedded blocks |
|---|---|---:|
| 2026-11-07 (time not specified in filename) | [RIEMANN_CHECKPOINT_SECOURS_2026-11-07.md](riemann/backups/RIEMANN_CHECKPOINT_SECOURS_2026-11-07/README.md) | 0 |
| 2026-11-07 13:05 EST | [RIEMANN_BACKUP_2026-11-07_1305.md](riemann/supplements/RIEMANN_BACKUP_2026-11-07_1305/README.md) | 0 |
| 2026-11-07 13:09 EST | [RIEMANN_BACKUP_2026-11-07_1309.md](riemann/supplements/RIEMANN_BACKUP_2026-11-07_1309/README.md) | 0 |
| 2026-11-23 04:58 EST | [RIEMANN_CHECKPOINT_2026-11-23_0458_EST.md](riemann/2026-11-23_0458/README.md) | 0 |
| 2026-11-23 05:00 EST | [RIEMANN_CHECKPOINT_2026-11-23_0500_EST.md](riemann/2026-11-23_0500/README.md) | 0 |
| 2026-11-23 05:06 EST | [RIEMANN_DELTA_2026-11-23_0506_EST_LEAN_VERIFICATION.md](riemann/supplements/RIEMANN_DELTA_2026-11-23_0506_EST_LEAN_VERIFICATION/README.md) | 0 |
| 2026-11-23 05:13 EST | [RIEMANN_DELTA_2026-11-23_0513_EST_W24_EXACT.md](riemann/supplements/RIEMANN_DELTA_2026-11-23_0513_EST_W24_EXACT/README.md) | 0 |
| 2026-11-23 05:22 EST | [2026-11-23_RIEMANN_DELTA_2026-11-23_0522_EST_W15_EXACT.md](riemann/supplements/2026-11-23_RIEMANN_DELTA_2026-11-23_0522_EST_W15_EXACT/README.md) | 0 |
| 2026-11-23 05:43 EST | [2026-11-23_0526_RIEMANN_CHECKPOINT_2026-11-23_0543_EST.md](riemann/supplements/2026-11-23_0526_RIEMANN_CHECKPOINT_2026-11-23_0543_EST/README.md) | 0 |
| 2026-11-23 06:13 EST | [RIEMANN_CHECKPOINT_2026-11-23_0613_EST.md](riemann/2026-11-23_0613/README.md) | 0 |
| 2026-11-23 07:09 EST | [RIEMANN_CHECKPOINT_2026-11-23_0709_EST.md](riemann/2026-11-23_0709/README.md) | 0 |
| 2026-11-23 07:18 EST | [RIEMANN_CHECKPOINT_2026-11-23_0718_EST.md](riemann/2026-11-23_0718/README.md) | 0 |
| 2026-11-23 07:29 EST | [RIEMANN_CHECKPOINT_2026-11-23_0729_EST.md](riemann/2026-11-23_0729/README.md) | 0 |
| 2026-11-23 07:41 EST | [RIEMANN_CHECKPOINT_2026-11-23_0741_EST.md](riemann/2026-11-23_0741/README.md) | 0 |
| 2026-11-23 07:57 EST | [RIEMANN_CHECKPOINT_2026-11-23_0757_EST.md](riemann/2026-11-23_0757/README.md) | 0 |
| 2026-11-23 08:10 EST | [RIEMANN_CHECKPOINT_2026-11-23_0810_EST.md](riemann/2026-11-23_0810/README.md) | 0 |
| 2026-11-23 09:19 EST | [RIEMANN_CHECKPOINT_2026-11-23_0919_EST.md](riemann/2026-11-23_0919/README.md) | 0 |
| 2026-11-23 09:30 EST | [RIEMANN_CHECKPOINT_2026-11-23_0930_EST.md](riemann/2026-11-23_0930/README.md) | 0 |
| 2026-11-23 09:43 EST | [RIEMANN_INTERIM_2026-11-23_0943_EST.md](riemann/supplements/RIEMANN_INTERIM_2026-11-23_0943_EST/README.md) | 0 |
| 2026-11-23 09:55 EST | [RIEMANN_CONTINUATION_2026-11-23_0955_EST.md](riemann/supplements/RIEMANN_CONTINUATION_2026-11-23_0955_EST/README.md) | 0 |
| 2026-11-23 10:32 EST | [RIEMANN_CHECKPOINT_2026-11-23_1032_EST.md](riemann/2026-11-23_1032/README.md) | 0 |
| 2026-11-23 10:38 EST | [RIEMANN_SUPPLEMENT_2026-11-23_1038_EST.md](riemann/supplements/RIEMANN_SUPPLEMENT_2026-11-23_1038_EST/README.md) | 0 |
| 2026-11-23 11:03 EST | [RIEMANN_CHECKPOINT_2026-11-23_1103_EST.md](riemann/2026-11-23_1103/README.md) | 0 |
| 2026-11-23 11:10 EST | [RIEMANN_SUPPLEMENT_2026-11-23_1110_EST.md](riemann/supplements/RIEMANN_SUPPLEMENT_2026-11-23_1110_EST/README.md) | 0 |
| 2026-11-23 12:32 EST | [RIEMANN_CHECKPOINT_2026-11-23_1232_EST.md](riemann/2026-11-23_1232/README.md) | 0 |
| 2026-11-23 12:37 EST | [RIEMANN_SUPPLEMENT_2026-11-23_1237_EST.md](riemann/supplements/RIEMANN_SUPPLEMENT_2026-11-23_1237_EST/README.md) | 0 |
| 2026-11-23 12:45 EST | [RIEMANN_SUPPLEMENT_2026-11-23_1245_EST.md](riemann/supplements/RIEMANN_SUPPLEMENT_2026-11-23_1245_EST/README.md) | 0 |
| 2026-11-23 13:13 EST | [RIEMANN_CHECKPOINT_2026-11-23_1313_EST.md](riemann/2026-11-23_1313/README.md) | 0 |
| 2026-11-23 13:55 EST | [RIEMANN_CHECKPOINT_2026-11-23_1355_EST.md](riemann/2026-11-23_1355/README.md) | 0 |
| 2026-11-23 14:06 EST | [RIEMANN_CHECKPOINT_2026-11-23_1406_EST.md](riemann/2026-11-23_1406/README.md) | 0 |
| 2026-11-23 14:14 EST | [RIEMANN_SUPPLEMENT_2026-11-23_1414_EST.md](riemann/supplements/RIEMANN_SUPPLEMENT_2026-11-23_1414_EST/README.md) | 0 |
| 2026-11-23 14:20 EST | [RIEMANN_SUPPLEMENT_2026-11-23_1420_EST.md](riemann/supplements/RIEMANN_SUPPLEMENT_2026-11-23_1420_EST/README.md) | 0 |
| 2026-11-23 14:38 EST | [RIEMANN_CHECKPOINT_2026-11-23_1438_EST.md](riemann/2026-11-23_1438/README.md) | 0 |
| 2026-11-23 14:42 EST | [RIEMANN_SUPPLEMENT_2026-11-23_1442_EST.md](riemann/supplements/RIEMANN_SUPPLEMENT_2026-11-23_1442_EST/README.md) | 0 |
| 2026-11-23 14:52 EST | [RIEMANN_SUPPLEMENT_2026-11-23_1452_EST.md](riemann/supplements/RIEMANN_SUPPLEMENT_2026-11-23_1452_EST/README.md) | 0 |
| 2026-11-23 15:03 EST | [RIEMANN_CHECKPOINT_2026-11-23_1503_EST.md](riemann/2026-11-23_1503/README.md) | 0 |
| 2026-11-23 15:18 EST | [RIEMANN_SUPPLEMENT_2026-11-23_1518_EST.md](riemann/supplements/RIEMANN_SUPPLEMENT_2026-11-23_1518_EST/README.md) | 0 |
| 2026-11-23 15:37 EST | [RIEMANN_CHECKPOINT_2026-11-23_1537_EST.md](riemann/2026-11-23_1537/README.md) | 0 |
| 2026-11-23 16:02 EST | [RIEMANN_CHECKPOINT_2026-11-23_1602_EST.md](riemann/2026-11-23_1602/README.md) | 0 |
| 2026-11-23 16:11 EST | [RIEMANN_SUPPLEMENT_2026-11-23_1611_EST.md](riemann/supplements/RIEMANN_SUPPLEMENT_2026-11-23_1611_EST/README.md) | 0 |
| 2026-11-23 17:06 EST | [RIEMANN_CHECKPOINT_2026-11-23_1706_EST.md](riemann/2026-11-23_1706/README.md) | 0 |
| 2026-11-23 17:19 EST | [RIEMANN_SUPPLEMENT_2026-11-23_1719_EST.md](riemann/supplements/RIEMANN_SUPPLEMENT_2026-11-23_1719_EST/README.md) | 0 |
| 2026-11-23 17:37 EST | [RIEMANN_CHECKPOINT_2026-11-23_1737_EST.md](riemann/2026-11-23_1737/README.md) | 0 |
| 2026-11-23 17:44 EST | [RIEMANN_SUPPLEMENT_2026-11-23_1744_EST.md](riemann/supplements/RIEMANN_SUPPLEMENT_2026-11-23_1744_EST/README.md) | 0 |
| 2026-11-23 17:48 EST | [RIEMANN_CORRIGENDUM_2026-11-23_1748_EST.md](riemann/supplements/RIEMANN_CORRIGENDUM_2026-11-23_1748_EST/README.md) | 0 |
| 2026-11-23 18:39 EST | [RIEMANN_CHECKPOINT_2026-11-23_1839_EST.md](riemann/2026-11-23_1839/README.md) | 0 |
| 2026-11-23 18:50 EST | [RIEMANN_SUPPLEMENT_2026-11-23_1850_EST.md](riemann/supplements/RIEMANN_SUPPLEMENT_2026-11-23_1850_EST/README.md) | 0 |
| 2026-11-23 19:29 EST | [RIEMANN_CHECKPOINT_2026-11-23_1929_EST.md](riemann/2026-11-23_1929/README.md) | 3 |
| 2026-11-23 20:26 EST | [RIEMANN_CHECKPOINT_2026-11-23_2026_EST.md](riemann/2026-11-23_2026/README.md) | 6 |
| 2026-11-23 20:59:24 EST | [RIEMANN_CHECKPOINT_2026-11-23_205924_EST.md](riemann/2026-11-23_205924/README.md) | 4 |
| 2026-11-23 21:41 EST | [RIEMANN_CHECKPOINT_2026-11-23_2141_EST.md](riemann/2026-11-23_2141/README.md) | 4 |
| 2026-11-23 23:20 EST | [RIEMANN_CHECKPOINT_2026-11-23_2320_EST.md](riemann/2026-11-23_2320/README.md) | 4 |
| 2026-11-23 23:48 EST | [RIEMANN_CHECKPOINT_2026-11-23_2348_EST.md](riemann/2026-11-23_2348/README.md) | 4 |
| 2026-11-24 00:41 EST | [RIEMANN_CHECKPOINT_2026-11-24_0041_EST.md](riemann/2026-11-24_0041/README.md) | 6 |
| 2026-11-24 01:56 EST | [RIEMANN_CHECKPOINT_2026-11-24_0156_EST.md](riemann/2026-11-24_0156/README.md) | 4 |
| 2026-11-24 03:13 EST | [RIEMANN_CHECKPOINT_2026-11-24_0313_EST.md](riemann/2026-11-24_0313/README.md) | 2 |
| 2026-11-24 03:48 EST | [RIEMANN_CHECKPOINT_2026-11-24_0348_EST.md](riemann/2026-11-24_0348/README.md) | 2 |
| 2026-11-24 05:20 EST | [RIEMANN_CHECKPOINT_2026-11-24_0520_EST.md](riemann/2026-11-24_0520/README.md) | 1 |
| 2026-11-24 05:37 EST | [RIEMANN_CHECKPOINT_2026-11-24_0537_EST.md](riemann/2026-11-24_0537/README.md) | 2 |
| 2026-11-24 06:35 EST | [RIEMANN_CHECKPOINT_2026-11-24_0635_EST.md](riemann/2026-11-24_0635/README.md) | 4 |
| 2026-11-24 07:57 EST | [RIEMANN_CHECKPOINT_2026-11-24_0757_EST.md](riemann/2026-11-24_0757/README.md) | 4 |
| 2026-11-24 08:46 EST | [RIEMANN_CHECKPOINT_2026-11-24_0846_EST.md](riemann/2026-11-24_0846/README.md) | 2 |
| 2026-11-24 10:17 EST | [RIEMANN_CHECKPOINT_2026-11-24_1017_EST.md](riemann/2026-11-24_1017/README.md) | 1 |
| 2026-11-24 11:10 EST | [RIEMANN_CHECKPOINT_2026-11-24_1110_EST.md](riemann/2026-11-24_1110/README.md) | 1 |
| 2026-11-24 12:01 EST | [RIEMANN_CHECKPOINT_2026-11-24_1201_EST.md](riemann/2026-11-24_1201/README.md) | 1 |
| 2026-11-24 12:40 EST | [RIEMANN_CHECKPOINT_2026-11-24_1240_EST.md](riemann/2026-11-24_1240/README.md) | 1 |
| 2026-11-24 14:12 EST | [RIEMANN_CHECKPOINT_2026-11-24_1412_EST.md](riemann/2026-11-24_1412/README.md) | 2 |
| 2026-11-24 14:40 EST | [RIEMANN_CHECKPOINT_2026-11-24_1440_EST.md](riemann/2026-11-24_1440/README.md) | 2 |
| 2026-11-24 16:24 EST | [RIEMANN_CHECKPOINT_2026-11-24_1624_EST.md](riemann/2026-11-24_1624/README.md) | 2 |
| 2026-11-24 17:17 EST | [RIEMANN_CHECKPOINT_2026-11-24_1717_EST.md](riemann/2026-11-24_1717/README.md) | 1 |
| 2026-11-24 18:31 EST | [RIEMANN_CHECKPOINT_2026-11-24_1831_EST.md](riemann/2026-11-24_1831/README.md) | 1 |
| 2026-11-24 18:37 EST | [RIEMANN_CHECKPOINT_2026-11-24_1837_EST.md](riemann/2026-11-24_1837/README.md) | 1 |
| 2026-11-24 19:35 EST | [RIEMANN_CHECKPOINT_2026-11-24_1935_EST.md](riemann/2026-11-24_1935/README.md) | 1 |
| 2026-11-24 20:44 EST | [RIEMANN_CHECKPOINT_2026-11-24_2044_EST.md](riemann/2026-11-24_2044/README.md) | 1 |
| 2026-11-24 21:53 EST | [RIEMANN_CHECKPOINT_2026-11-24_2153_EST.md](riemann/2026-11-24_2153/README.md) | 1 |
| 2026-11-24 23:15 EST | [RIEMANN_CHECKPOINT_2026-11-24_2315_EST.md](riemann/2026-11-24_2315/README.md) | 1 |
| 2026-11-24 23:36 EST | [RIEMANN_CHECKPOINT_2026-11-24_2336_EST.md](riemann/2026-11-24_2336/README.md) | 1 |
| 2026-11-25 (time not specified in filename) | [RIEMANN_ADDENDUM_2026-11-25_H9_G2.md](riemann/supplements/RIEMANN_ADDENDUM_2026-11-25_H9_G2/README.md) | 0 |
| 2026-11-25 00:40 EST | [RIEMANN_CHECKPOINT_2026-11-25_0040_EST.md](riemann/2026-11-25_0040/README.md) | 1 |
| 2026-11-25 02:16 EST | [RIEMANN_CHECKPOINT_2026-11-25_0216_EST.md](riemann/2026-11-25_0216/README.md) | 1 |
| 2026-11-25 02:59 EST | [RIEMANN_CHECKPOINT_2026-11-25_0259_EST.md](riemann/2026-11-25_0259/README.md) | 1 |
| 2026-11-25 03:35 EST | [RIEMANN_CHECKPOINT_2026-11-25_0335_EST.md](riemann/2026-11-25_0335/README.md) | 2 |
| 2026-11-25 04:54 EST | [RIEMANN_CHECKPOINT_2026-11-25_0454_EST.md](riemann/2026-11-25_0454/README.md) | 3 |
| 2026-11-25 06:19 EST | [RIEMANN_CHECKPOINT_2026-11-25_0619_EST.md](riemann/2026-11-25_0619/README.md) | 12 |
| 2026-11-25 07:20 EST | [RIEMANN_CHECKPOINT_2026-11-25_0720_EST.md](riemann/2026-11-25_0720/README.md) | 5 |
| 2026-11-25 08:15 EST | [RIEMANN_CHECKPOINT_2026-11-25_0815_EST.md](riemann/2026-11-25_0815/README.md) | 7 |
| 2026-11-25 08:46 EST | [RIEMANN_CHECKPOINT_2026-11-25_0846_EST.md](riemann/2026-11-25_0846/README.md) | 30 |
| 2026-11-25 10:04 EST | [RIEMANN_CHECKPOINT_2026-11-25_1004_EST.md](riemann/2026-11-25_1004/README.md) | 24 |
| 2026-11-25 11:05 EST | [RIEMANN_CHECKPOINT_2026-11-25_1105_EST.md](riemann/2026-11-25_1105/README.md) | 28 |
| 2026-11-25 11:51 EST | [RIEMANN_CHECKPOINT_2026-11-25_1151_EST.md](riemann/2026-11-25_1151/README.md) | 36 |

## Script bundles

Every member of each source ZIP is available through its linked directory. The member contents are preserved unchanged.

| Source ZIP | Preserved members |
|---|---:|
| [RIEMANN_AUDIT_SCRIPTS_2026-11-23_0810_EST.zip](riemann/bundles/RIEMANN_AUDIT_SCRIPTS_2026-11-23_0810_EST/README.md) | 14 |
| [RIEMANN_AUDIT_SCRIPTS_2026-11-23_0930_EST.zip](riemann/bundles/RIEMANN_AUDIT_SCRIPTS_2026-11-23_0930_EST/README.md) | 28 |
| [RIEMANN_AUDIT_SCRIPTS_2026-11-23_1406_EST.zip](riemann/bundles/RIEMANN_AUDIT_SCRIPTS_2026-11-23_1406_EST/README.md) | 6 |
| [RIEMANN_CORRIGENDUM_SCRIPTS_2026-11-23_1748_EST.zip](riemann/bundles/RIEMANN_CORRIGENDUM_SCRIPTS_2026-11-23_1748_EST/README.md) | 4 |
| [RIEMANN_RESEARCH_SCRIPTS_2026-11-23_1610_EST.zip](riemann/bundles/RIEMANN_RESEARCH_SCRIPTS_2026-11-23_1610_EST/README.md) | 18 |
| [RIEMANN_RUN_SCRIPTS_2026-11-23_1436_EST.zip](riemann/bundles/RIEMANN_RUN_SCRIPTS_2026-11-23_1436_EST/README.md) | 21 |
| [RIEMANN_SCRIPTS_2026-11-23_0919_EST.zip](riemann/bundles/RIEMANN_SCRIPTS_2026-11-23_0919_EST/README.md) | 10 |
| [RIEMANN_SCRIPTS_2026-11-23_0943_EST.zip](riemann/bundles/RIEMANN_SCRIPTS_2026-11-23_0943_EST/README.md) | 6 |
| [RIEMANN_SCRIPTS_2026-11-23_0955_EST.zip](riemann/bundles/RIEMANN_SCRIPTS_2026-11-23_0955_EST/README.md) | 18 |
| [RIEMANN_SCRIPTS_2026-11-23_1032_EST.zip](riemann/bundles/RIEMANN_SCRIPTS_2026-11-23_1032_EST/README.md) | 12 |
| [RIEMANN_SCRIPTS_2026-11-23_1103_EST.zip](riemann/bundles/RIEMANN_SCRIPTS_2026-11-23_1103_EST/README.md) | 12 |
| [RIEMANN_SCRIPTS_2026-11-23_1232_EST.zip](riemann/bundles/RIEMANN_SCRIPTS_2026-11-23_1232_EST/README.md) | 8 |
| [RIEMANN_SCRIPTS_2026-11-23_1313_EST.zip](riemann/bundles/RIEMANN_SCRIPTS_2026-11-23_1313_EST/README.md) | 24 |
| [RIEMANN_SCRIPTS_2026-11-23_1518_EST.zip](riemann/bundles/RIEMANN_SCRIPTS_2026-11-23_1518_EST/README.md) | 18 |
| [RIEMANN_SCRIPTS_2026-11-23_1537_EST.zip](riemann/bundles/RIEMANN_SCRIPTS_2026-11-23_1537_EST/README.md) | 6 |
| [RIEMANN_SCRIPTS_2026-11-23_1706_EST.zip](riemann/bundles/RIEMANN_SCRIPTS_2026-11-23_1706_EST/README.md) | 16 |
| [RIEMANN_SCRIPTS_2026-11-23_1719_EST.zip](riemann/bundles/RIEMANN_SCRIPTS_2026-11-23_1719_EST/README.md) | 14 |
| [RIEMANN_SCRIPTS_2026-11-23_1737_EST.zip](riemann/bundles/RIEMANN_SCRIPTS_2026-11-23_1737_EST/README.md) | 16 |
| [RIEMANN_SCRIPTS_2026-11-23_1846_EST.zip](riemann/bundles/RIEMANN_SCRIPTS_2026-11-23_1846_EST/README.md) | 8 |
| [RIEMANN_SCRIPTS_2026-11-23_1850_EST.zip](riemann/bundles/RIEMANN_SCRIPTS_2026-11-23_1850_EST/README.md) | 16 |
| [RIEMANN_SUPPLEMENT_SCRIPTS_2026-11-23_1038_EST.zip](riemann/bundles/RIEMANN_SUPPLEMENT_SCRIPTS_2026-11-23_1038_EST/README.md) | 6 |
| [RIEMANN_SUPPLEMENT_SCRIPTS_2026-11-23_1110_EST.zip](riemann/bundles/RIEMANN_SUPPLEMENT_SCRIPTS_2026-11-23_1110_EST/README.md) | 6 |
| [RIEMANN_SUPPLEMENT_SCRIPTS_2026-11-23_1237_EST.zip](riemann/bundles/RIEMANN_SUPPLEMENT_SCRIPTS_2026-11-23_1237_EST/README.md) | 6 |
| [RIEMANN_SUPPLEMENT_SCRIPTS_2026-11-23_1245_EST.zip](riemann/bundles/RIEMANN_SUPPLEMENT_SCRIPTS_2026-11-23_1245_EST/README.md) | 6 |
| [RIEMANN_SUPPLEMENT_SCRIPTS_2026-11-23_1414_EST.zip](riemann/bundles/RIEMANN_SUPPLEMENT_SCRIPTS_2026-11-23_1414_EST/README.md) | 12 |
| [RIEMANN_SUPPLEMENT_SCRIPTS_2026-11-23_1420_EST.zip](riemann/bundles/RIEMANN_SUPPLEMENT_SCRIPTS_2026-11-23_1420_EST/README.md) | 4 |
| [RIEMANN_SUPPLEMENT_SCRIPTS_2026-11-23_1442_EST.zip](riemann/bundles/RIEMANN_SUPPLEMENT_SCRIPTS_2026-11-23_1442_EST/README.md) | 2 |
| [RIEMANN_SUPPLEMENT_SCRIPTS_2026-11-23_1452_EST.zip](riemann/bundles/RIEMANN_SUPPLEMENT_SCRIPTS_2026-11-23_1452_EST/README.md) | 10 |
| [RIEMANN_SUPPLEMENT_SCRIPTS_2026-11-23_1744_EST.zip](riemann/bundles/RIEMANN_SUPPLEMENT_SCRIPTS_2026-11-23_1744_EST/README.md) | 8 |

## Standalone source files

| Original filename | Format check |
|---|---|
| [2026-11-23_0526_gamma_window_check.json](riemann/standalone/2026-11-23_0526_gamma_window_check.json) | json_parse_pass |
| [2026-11-23_0526_gamma_window_check.py](riemann/standalone/2026-11-23_0526_gamma_window_check.py) | python_syntax_pass_not_executed |
| [2026-11-23_0526_main_inequality_scaling.json](riemann/standalone/2026-11-23_0526_main_inequality_scaling.json) | json_parse_pass |
| [2026-11-23_0526_main_inequality_scaling.py](riemann/standalone/2026-11-23_0526_main_inequality_scaling.py) | python_syntax_pass_not_executed |
| [2026-11-23_0526_prime_ramp_audit.json](riemann/standalone/2026-11-23_0526_prime_ramp_audit.json) | json_parse_pass |
| [2026-11-23_0526_prime_ramp_audit.py](riemann/standalone/2026-11-23_0526_prime_ramp_audit.py) | python_syntax_pass_not_executed |
| [2026-11-23_0526_w13_even_two_parameter_exact.json](riemann/standalone/2026-11-23_0526_w13_even_two_parameter_exact.json) | json_parse_pass |
| [2026-11-23_0526_w13_even_two_parameter_exact.py](riemann/standalone/2026-11-23_0526_w13_even_two_parameter_exact.py) | python_syntax_pass_not_executed |
| [2026-11-23_0526_w13_odd_weighted_exact.json](riemann/standalone/2026-11-23_0526_w13_odd_weighted_exact.json) | json_parse_pass |
| [2026-11-23_0526_w13_odd_weighted_exact.py](riemann/standalone/2026-11-23_0526_w13_odd_weighted_exact.py) | python_syntax_pass_not_executed |
| [2026-11-23_0526_w14_even_two_parameter_exact.json](riemann/standalone/2026-11-23_0526_w14_even_two_parameter_exact.json) | json_parse_pass |
| [2026-11-23_0526_w14_even_two_parameter_exact.py](riemann/standalone/2026-11-23_0526_w14_even_two_parameter_exact.py) | python_syntax_pass_not_executed |
| [2026-11-23_0526_w14_odd_weighted_exact.json](riemann/standalone/2026-11-23_0526_w14_odd_weighted_exact.json) | json_parse_pass |
| [2026-11-23_0526_w14_odd_weighted_exact.py](riemann/standalone/2026-11-23_0526_w14_odd_weighted_exact.py) | python_syntax_pass_not_executed |
| [2026-11-23_0526_w15_three_intervals_closed_form.json](riemann/standalone/2026-11-23_0526_w15_three_intervals_closed_form.json) | json_parse_pass |
| [2026-11-23_0526_w15_three_intervals_closed_form.py](riemann/standalone/2026-11-23_0526_w15_three_intervals_closed_form.py) | python_syntax_pass_not_executed |
| [2026-11-23_0526_w15_two_mode_time_domain.json](riemann/standalone/2026-11-23_0526_w15_two_mode_time_domain.json) | json_parse_pass |
| [2026-11-23_0526_w15_two_mode_time_domain.py](riemann/standalone/2026-11-23_0526_w15_two_mode_time_domain.py) | python_syntax_pass_not_executed |
| [2026-11-23_collar_bound_report.json](riemann/standalone/2026-11-23_collar_bound_report.json) | json_parse_pass |
| [2026-11-23_collar_p_optimization.json](riemann/standalone/2026-11-23_collar_p_optimization.json) | json_parse_pass |
| [2026-11-23_collar_p_optimization.py](riemann/standalone/2026-11-23_collar_p_optimization.py) | python_syntax_pass_not_executed |
| [2026-11-23_independent_collar_bound.py](riemann/standalone/2026-11-23_independent_collar_bound.py) | python_syntax_pass_not_executed |
| [2026-11-23_mellin_pole_checks.json](riemann/standalone/2026-11-23_mellin_pole_checks.json) | json_parse_pass |
| [2026-11-23_mellin_pole_checks.py](riemann/standalone/2026-11-23_mellin_pole_checks.py) | python_syntax_pass_not_executed |
| [2026-11-23_w15_adaptive_p_exact.json](riemann/standalone/2026-11-23_w15_adaptive_p_exact.json) | json_parse_pass |
| [2026-11-23_w15_adaptive_p_exact.py](riemann/standalone/2026-11-23_w15_adaptive_p_exact.py) | python_syntax_pass_not_executed |
| [2026-11-23_w16_p_exact_certificate.json](riemann/standalone/2026-11-23_w16_p_exact_certificate.json) | json_parse_pass |
| [2026-11-23_w16_p_exact_certificate.py](riemann/standalone/2026-11-23_w16_p_exact_certificate.py) | python_syntax_pass_not_executed |
| [2026-11-23_w24_exact_bathtub.py](riemann/standalone/2026-11-23_w24_exact_bathtub.py) | python_syntax_pass_not_executed |
| [2026-11-23_w24_exact_bathtub_report.json](riemann/standalone/2026-11-23_w24_exact_bathtub_report.json) | json_parse_pass |
| [2026-11-23_w25_exact_bathtub.py](riemann/standalone/2026-11-23_w25_exact_bathtub.py) | python_syntax_pass_not_executed |
| [2026-11-23_w25_exact_bathtub_report.json](riemann/standalone/2026-11-23_w25_exact_bathtub_report.json) | json_parse_pass |

## Citing or correcting a record

Cite the original filename and recorded timestamp, its public path and the Git commit you used. Cite the new finite replay separately when relying on its results. The import date does not make a historical claim an independently validated theorem. Corrections and missing public research sources can be reported in [Issues](https://github.com/ErikLachance/mila-math-lab/issues).
