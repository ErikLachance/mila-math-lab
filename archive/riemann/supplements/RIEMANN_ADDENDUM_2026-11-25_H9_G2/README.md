# Addendum au checkpoint Riemann du 24 novembre, 19 h 35 EST

> **Historical research record / Archive de recherche.** Imported on 26 November 2026. Mathematical claims, source reports and test outcomes below describe the historical checkpoint. They have not all been independently audited or rerun during this import. No proof of RH is claimed.
> Private operational sections and scheduling metadata have been omitted. All embedded code, data and output blocks have been extracted byte-for-byte into linked files. Source scripts retain their historical paths and dependencies; they are not automatically executed.

**Source record:** `RIEMANN_ADDENDUM_2026-11-25_H9_G2.md`. **Recorded time label:** 2026-11-25 (time not specified in filename) (from the filename).

[Archive index](../../../README.md) · [Manifest](../../../manifest.json) · [Verification scope](../../../README.md#what-was-checked-during-import)

Note de recherche du 25 novembre 2026 (UTC). Complément à RIEMANN_CHECKPOINT_2026-11-24_1935_EST.md.

## Ce que l'étape G2 utilise vraiment

Dans l'exposé de Michael Rubinstein, version 2 du 22 novembre, § III.9, p. 154, poser y = x^ε, b = exp(y), et B₀ = f m b y. À partir de LinkN_at (III.258), vérification algébrique : f m b y² = y B₀, et (log x)² N_c ≤ y N_c sous l'hypothèse (log x)² ≤ y. La somme pondérée V ≤ b ≤ B₀ ≤ y(B₀ + N_c), puisque f, m et y sont au moins 1 et N_c ≥ 0. Avec d_j = D₀, cela donne H_j ≤ D₀ (|C| + 1) y(B₀ + N_c). La borne √b du théorème G est donc plus forte que nécessaire à cette conversion. Cela ne supprime ni LinkN_at, ni les obligations de finitude et de convergence dont dispose HypV. Il ne faut notamment pas traiter une série non sommable comme bornée par convention. Pointeurs du papier vers le code : DivinNOfHypV.lean:76 (divinN_at), et DesWin.lean:29 (appel de divinN_of_hypV).
https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/zeta-paper_v2.pdf#page=155

## Ne pas identifier les deux lemmes

L'énoncé publié de ALG.0060 (UpperTheory.V.Alg.M.main_holds) contrôle la longueur d'un quotient cotangent intégral par des valuations sur des représentants d'orbites mixtes. Entre autres conditions, il demande la finitude du degré zéro modulo I, une condition sur les deux signes dans les fibres, une borne sur la dimension des dérivations aux points mixtes et un élément de degré zéro séparant ces points. Le catalogue renvoie ensuite à GC.1.0105 pour les noyaux de localisation. Ce ne sont pas les entrées de G2. Le seuil plus faible ne dispense donc pas de vérifier les prémisses effectives d'ALG.0060 si cette voie doit fournir la borne pondérée, ni n'identifie D096 à une déclaration Lean.
https://andrewodesky.com/rh/lean/UpperTheory.V.Alg.M.main_holds/

Prochaine micro-passe utile : dresser deux colonnes indépendantes, (A) entrées du lemme local H2 utilisé pour les pentes (table § III.11), (B) chaîne ALG.0060 → GC.1.0105 → HypV / LinkN_at → divinN_at, en certifiant chaque flèche et en distinguant les deux entrées de G2. La flèche GC.1.0105 vers le paquet HypV n'a pas été auditée dans cette note. Localiser ensuite où les relations du modèle D096 fournissent, ou ne fournissent pas, la finitude du degré zéro et la comparaison intégrale dans le vrai code. Ne pas refaire des tests de monômes ni viser une amélioration de √b simplement pour la conversion G2. Aucune nouvelle compilation Lean ni résolution de H9, de la comparaison cristalline ou de la finitude arithmétique n'est revendiquée.
https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/zeta-paper_v2.pdf#page=197
