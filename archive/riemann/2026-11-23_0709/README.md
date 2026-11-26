# Riemann Proof Watch — checkpoint de secours — 2026-11-23 07:08:59 EST (America/New_York)

> **Historical research record / Archive de recherche.** Imported on 26 November 2026. Mathematical claims, source reports and test outcomes below describe the historical checkpoint. They have not all been independently audited or rerun during this import. No proof of RH is claimed.
> Private operational sections and scheduling metadata have been omitted. All embedded code, data and output blocks have been extracted byte-for-byte into linked files. Source scripts retain their historical paths and dependencies; they are not automatically executed.

**Source record:** `RIEMANN_CHECKPOINT_2026-11-23_0709_EST.md`. **Recorded time label:** 2026-11-23 07:09 EST (from the filename).

[Archive index](../../README.md) · [Manifest](../../manifest.json) · [Verification scope](../../README.md#what-was-checked-during-import)

## Continuité scientifique


Checkpoint Riemann antérieur : **2026-11-08 15:30:58 EST**, borne conditionnelle de positivité de la forme de Weil seulement sur deux petites collerettes de largeur 1/12 dans `L=0.81`, indice négatif borné séparément à 14; le couplage avec le complément central n'est PAS contrôlé; aucune nouvelle preuve globale.

Le checkpoint `RIEMANN_CHECKPOINT_2026-11-23_0613_EST.md` a également été lu, avec tests Lemniscate jusqu'à n=5833 et audits de l'inégalité (M). On évite de présenter ses résultats comme nouveaux dans le présent run.


## Sources examinées dans ce run

1. Michael O. Rubinstein, *The Alpöge–Claude proof of the Riemann hypothesis explained for the Riemann zeta function*, brouillon V2 du **22 novembre 2026**: https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/zeta-paper_v2.pdf . PDF ouvert, texte §§I,II,III.10,III.11 lu, captures visuelles des p. 185 et 194 inspectées. L'introduction et §III.11 déclarent explicitement que **les treize hypothèses H0–H12 ne sont pas toutes démontrées dans le GUIDE humain**, notamment la fourniture uniforme sur les intervalles. Le guide cite (M) de l'archive Lean: **ce n'est pas un contre-exemple à la preuve formelle**.
2. Andrew Sutherland, MIT, log actualisé **22 novembre 2026 à 16:20 UTC**: https://math.mit.edu/~drew/grh/ ; **175 187** modules Lean compilés, seulement trois axiomes standards, revérifications indépendantes acceptées; certains replays monolithiques redondants encore en cours lors de l'actualisation.
3. Déclaration Lean/Mathlib du **21 novembre 2026**: https://leanprover-community.github.io/blog/posts/riemann-hypothesis/ ; certifie l'énoncé Mathlib et la preuve Lean. Vérifié via le résultat de recherche de cette séance; la présente séance n'a **pas** compilé localement les 17 millions de lignes.
4. Recherche complémentaire de la borne classique de Chebyshev `psi(x)=O(x)`, notes d'enseignement Harvard de Noam Elkies identifiées par recherche https://people.math.harvard.edu/~elkies/M229.09/chebi.pdf (résultat de recherche uniquement, PDF non ouvert ici). Une dérivation élémentaire indépendante, sans besoin de citation, est fournie ci-dessous.

## Passe nouvelle A — l'écart logique «unbounded scales» contre couverture uniforme

Hypothèse O23 de Rubinstein §III.10, p.176: pour ε fixé, ensemble **non borné** des échelles admissibles x, avec les objets/contraintes à ces x. En revanche H12 §III.11, p.194+: `pour tout seuil y, il existe Z≥y tel que pour tout x∈[Z,Z^(3/2)] des données satisfaisant H0–H11 existent`, et avec les constantes requises **uniformes en x** et des premiers auxiliaires appropriés. Une suite non bornée de points admissibles **ne fournit pas** une telle couverture; H12 est donc une obligation **supplémentaire** dans le guide. Les validateurs Lean vérifient une autre construction formalisée; on n'a découvert **aucune faille** de cette preuve.

Contremodèle analytique exact: fixer β=3/4, θ=3/5 et `f(x)=x^β sin(log x)` pour x≥1. Les points `Y_n=exp((3/2+2n)π)` satisfont `f(Y_n)=−Y_n^β ≤Y_n^θ` et sont non bornés. Mais `X_n=e^π Y_n` appartient à `[Y_n,Y_n^(3/2)]` pour n≥1 et `f(X_n)=X_n^β > X_n^θ`. De plus sa transformée de Mellin vaut exactement `1/((s−β)^2+1)` pour Re s>β; elle a des pôles en β±i avec β>θ. Cette analogie montre rigoureusement pourquoi un contrôle en points isolés ne suffit PAS au lemme de Landau; **f n'est pas G, pas d'infirmation de RH**. Script `interval_quantifier_audit.py` et rapport JSON exécutés: 5 échelles de plus en plus grandes et 4 comparaisons Mellin d'erreur numérique jusqu'à environ 1e−33 à 1e−38.

## Passe nouvelle B — renforcement précis du «maillage de bonnes échelles»

Définition réellement utilisée dans le guide: `G(x)=Σ_{n≤x} Λ(n)(x/n−1)−x log x+(1+γ)x`. G est continue, y compris aux puissances de nombres premiers puisque le nouveau terme vaut zéro au point où il apparaît, et est différentiable presque partout. On a

`G'(x)=A(x)−log x+γ`, avec `A(x)=Σ_{n≤x} Λ(n)/n`.

**Borne élémentaire explicite sans RH**: pour m≥2, la valuation p-adique du coefficient binomial central assure `ψ(m)−ψ(ceil(m/2))≤log C(m,floor(m/2))≤m log 2` (chaque puissance p^k strictement dans (ceil(m/2),m] contribue). En itérant `m_j=ceil(m/2^j)` jusqu'à 1, `ψ(m)≤2m log 2+log m+log2`. D'autre part `log(N!)=Σ_{n≤N} Λ(n)floor(N/n)` exactement, d'où

`log N−1+1/N ≤ A(N) ≤ log N−1+2log2+[1+2log N+log2]/N`,

via bornes intégrales sur `log(N!)`. Pour x∈[N,N+1), A(x)=A(N). Puis `γ−1≤G'(x)≤γ−1+2log2+[1+2log3+log2]/3 = 2.2603006... <3` pour tout x≥3 non entier/point de discontinuité de A. **Conclusion prouvée**: `|G(b)−G(a)|≤3|b−a|` pour tout b≥a≥3, car G est continue et par morceaux C1. Cette borne simple est très conservative; aucun résultat nouveau sur les zéros.

**Critère conditionnel de maillage qui suffit à RH**: pour tout θ>1/2, supposer qu'il existe des Z arbitrairement grands et un maillage de `[Z,Z^(3/2)]` ancré à Z, dont les écarts successifs (y compris le dernier) sont ≤`Z^θ`, et que `G(y)≤y^θ` en **tous** ses points. Le Lipschitz ci-dessus donne pour chaque x de l'intervalle `G(x)≤x^θ+3Z^θ≤4x^θ`, donc pour tout η>0 fixé et Z assez grand, `G(x)≤x^(θ+η)` partout. Le lemme de Landau sur les longues fenêtres, prouvé dans Rubinstein Part II §1, exclut alors les zéros avec `Re s>θ+η`; en faisant θ,η↓1/2, on obtient RH. C'est **une réduction conditionnelle et NON une preuve**: ni O23 ni nos calculs n'établissent les maillages requis ou les bornes G aux points. Un maillage espacé de `Z^θ` serait donc une cible plus faible et précise que la propriété H12 partout, mais reste une obligation majeure.

Vérifications locales: `mesh_to_window_lemma.py` évalué sur 1 999 998 entiers jusqu'à 2 millions. Une première version oubliait le terme Λ(2)/2, produisant des dérivées systématiquement décalées de −log2/2; bug identifié puis corrigé et script relancé. Après correction, dérivée dans l'échantillon environ [−0.0493,0.1914] et borne 2 log²x vérifiée; script `explicit_uniform_lipschitz.py` a contrôlé **exactement 1 023** inégalités de divisibilité par binomiaux centraux pour m=2..1024 et majorant explicite <3. `chebyshev_lipschitz_mesh.py`: identité exacte log N! pour N=2..500 en nombres entiers arbitrairement longs; résultat conforme. **Ce sont des vérifications de régression, non nécessaires à la démonstration élémentaire**.

## Passe nouvelle C — tests d'entrées H12 non responsables de la difficulté de couverture

Les contraintes de discrétisation en §III.10 `n=2^e` avec `x^(2+8ε)≤n≤2x^(2+8ε)` et `m,k` pairs dans des intervalles [A,2A] sont individuellement satisfaisables **pour tout x suffisamment grand** par arrondi `n=2^ceil(log2 A)`, `m=2ceil(A/2)`, `k=2ceil(B/2)`. Le choix de n puissance de deux n'est donc PAS en lui-même source d'absence d'échelles. Les véritables obligations difficiles restent les nombres premiers auxiliaires, les espaces automorphes et lattices, les ponts entre translates et les estimations uniformes H0–H11. Test entier EXACT à ε=1/100, x=10^1600: n dans [x^(52/25),2x^(52/25)), m pair 10^799, k pair 10^7360, k≥m+3, m≤2n≤k et `k≤n²x^(49/100)` tous vérifiés. Un premier essai du rapport a échoué sur la limite Python de conversion des entiers de plus de 4300 chiffres; correction `sys.set_int_max_str_digits(0)`, rerun PASS. `h12_discrete_parameter_rounding.py`/JSON.

## Passe nouvelle D — récurrence lemniscatique et obstruction exacte à une induction trop naïve

Le précédent backup vérifiait des valuations p=3 de la dérivée de `sl''=−2sl³` jusqu'à n=5833, sans preuve tous indices. Ici examen d'une tentative distincte de **preuve d'induction terme par terme** avec les degrés n=4k+1 et les bornes inférieures proposées α_k=floor(3(4k+1)/8), β_k=floor(3(4k+2)/8) pour les dérivées de sl et sl². Les valuations exactes de coefficients binomiaux de Kummer ont été testées sur k=1..1800, environ 3.2 millions de combinaisons. Cette induction terme à terme **ÉCHOUE**: pire déficits dans les termes de A de −2, dans ceux de B de −1, plus de 157 000 termes A et 81 000 termes B sous la puissance ciblée. Falsification de la méthode, pas de la borne finale.

Petit témoin EXACT pour `B3=(sl²)^(14)(0)`: quatre termes de valuation 3-adique **4** et somme totale de valuation **5**. Pour `A6=sl^(25)(0)`: les six termes de la récurrence ont valuations **8,7,8,7,9,7**, leur somme a valuation **10** alors que α6=9. Des annulations 3-adiques entre termes sont indispensables; ne pas présenter la borne globale comme conséquence immédiate de la divisibilité de chaque terme. Scripts `padic_binomial_induction_probe.py` et `padic_cancellation_counterexample.py` exécutés; rapports JSON. **Prochaine vraie piste**: exploiter la symétrie/mod 3 et les identités de fonctions elliptiques pour capturer ces annulations, ou inspecter la preuve formelle originale avant toute revendication.

## Passe nouvelle E — terme des zéros triviaux et contrôles de régression indépendants

En déplaçant formellement la transformée Mellin `F(s)=−ζ'(s)/(ζ(s)s(s−1))−1/(s−1)^2+(1+γ)/(s−1)` (explication de Rubinstein II.1), le résidu au zéro trivial s=−2k contribue `−x^(−2k)/[2k(2k+1)]`. Pour r=x^(−2), x>1, série élémentaire positive:

`B(x)=Σ_{k≥1} r^k/[2k(2k+1)] = 1−(1/2)log(1−r)−atanh(sqrt(r))/sqrt(r) = 1−(1/2)log(1−x^(−2))−x·atanh(1/x)`.

Le développement en série prouve `r/6 < B(x) < r/[6(1−r)]`. Tests 100 chiffres pour x=1.01,1.1,2,10,10000 d'accord avec la somme à mieux que 1e−80; à x=1.0001 l'algorithme `mpmath.nsum` converge trop lentement et un premier test strict a échoué: acceptation correcte seulement à 1e−9 (erreur observée ~6e−14). Cela précise un reste O(x^-2) de la formule explicite, sans établir la convergence des contributions des zéros non triviaux ni RH. `trivial_zero_tail_closed_form.py`/JSON.

Régressions également exécutées en début de run avant découverte des tests plus anciens: scripts `reconstruct_checks.py` (G(10^4,10^5,10^6,2·10^6), Mellin 6 cas, 80 zéros), `lemniscate_exact.py` (dérivées exactes n≤201, première intégrale et inert p), `character_formula.py` (pour q=11,d=1319,x=1000, identité `(1+χq)(1−χd)=1+χq−χd−χqχd` sur 193 puissances premières, erreur flottante ~1e−12). Ces calculs **RÉPLIQUENT** surtout la séance de secours précédente et ne sont pas affichés comme découvertes. La combinaison des caractères n'est pas la formule (M) centrée, dont les constantes L'/L n'ont pas été évaluées.

## Bilan critique, lacunes et recommandations

- L'archive Lean d'Alpöge–Claude a été **vérifiée par les groupes externes**, pas recompilée ici. Les 13 hypothèses de la prose Rubinstein sont laissées ouvertes **dans son brouillon**, ceci ne met pas en cause les preuves du noyau Lean. La reconnaissance éditoriale est une question séparée.
- Aucun calcul ci-dessus n'est une preuve indépendante de RH. Le projet doit pivoter du développement aveugle de matrices Weil vers l'analyse du pont H12/quantificateurs, du texte humain vers les lemmes Lean qui fournissent la couverture uniforme. Le théorème élémentaire «3-Lipschitz + maillage de taille Z^θ» réduit la couverture nécessaire mais les maillages ne sont PAS démontrés.
- Éviter de répéter les 200 valeurs lemniscatiques ou les 2 millions de G sans nouvelle question; ne pas tenter d'induction p-adique simplement terme par terme (contre-exemple exact), ne pas traiter O23 comme H12 et ne pas réutiliser une minuscule plage de nombres premiers comme preuve d'une estimation uniforme à grande échelle.
- Travail prochain prioritaire: identifier le lemme formel précis qui instancie H12 sur les fenêtres et ses constantes indépendantes de x; si possible source textuelle et contrôle direct des quantificateurs, puis audit de la possibilité de l'affaiblir en maillage `Z^θ`. Deuxième priorité: traiter les annulations 3-adiques par groupements exacts/Kummer, non par bornes terme à terme.

Aucun résultat global RH original.
