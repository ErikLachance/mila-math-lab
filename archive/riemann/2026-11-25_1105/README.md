# Riemann — checkpoint du 25 novembre 2026, session 11:05 EST

> **Historical research record / Archive de recherche.** Imported on 26 November 2026. Mathematical claims, source reports and test outcomes below describe the historical checkpoint. They have not all been independently audited or rerun during this import. No proof of RH is claimed.
> Private operational sections and scheduling metadata have been omitted. All embedded code, data and output blocks have been extracted byte-for-byte into linked files. Source scripts retain their historical paths and dependencies; they are not automatically executed.

**Source record:** `RIEMANN_CHECKPOINT_2026-11-25_1105_EST.md`. **Recorded time label:** 2026-11-25 11:05 EST (from the filename).

[Archive index](../../README.md) · [Manifest](../../manifest.json) · [Verification scope](../../README.md#what-was-checked-during-import)


## 2. Sources réellement consultées
- Andrew Sutherland (MIT), https://math.mit.edu/~drew/grh/ , mise à jour 24 novembre 05:25 UTC, vérifications positives des cinq énoncés et noyaux indépendants ; Comparator 4.36 encore annoncé en cours. Michael Rubinstein (Waterloo), https://math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/ : rapport du 21 novembre, 175187 modules compilés, nanoda et replay positifs. Ces vérifications externes ne sont pas une compilation Lean personnelle. Clay https://www.claymath.org/millennium/riemann-hypothesis/ affiche Active au moment de consultation.
- Catalogue Andrew O'Desky D103 https://andrewodesky.com/rh/lean/UpperTheory.V.Aut.AutomorphyUnramifiedCoefficientsAlt/ : hypothèse d'automorphie comportant quatre propriétés, dont finitude S0 ; ne pas confondre avec la démonstration complète H9 ou RH.
- Documentation primaire PARI/GP https://pari.math.u-bordeaux1.fr/dochtml/html/General_number_fields.html et https://pari.math.u-bordeaux1.fr/dochtml/ref/General_number_fields.html : bnfinit peut dépendre de GRH, bnfcertify assure certification inconditionnelle. PARI/Sage absents du conteneur (command -v gp/sage). On utilise ici seulement unités explicites de norme exacte ±1 et rang fini, aucun recours à GRH.

## 3. Axe A : bases réduites et polynômes septiques
Les deux ordres de degré7 du checkpoint 1004 ont été relus et vérifiés exactement : changement de base de l'ordre de puissance donne les matrices fournies, discriminants respectifs -764987380787 et -1791488485843. La maximalité reste conditionnelle à la construction de corps et au discriminant théorique du checkpoint antérieur. Une première LLL à précision insuffisante (150 chiffres, échelle 10^50) pour q683 a donné de longues bases et un coefficient de multiplication de 7,524,402,554, mauvais pour une recherche efficace ; les premières exécutions ont été interrompues par le délai. Une deuxième tentative, précision 350 chiffres mais LLL directe sur la base brute degré21, a aussi dépassé le délai. Solution : réduire d'abord la base septique à précision 350 chiffres (racines n=300, échelle 10^200), construire le tensoriel de cette base avec le cubique, saturer à 7 (indices 49,2401), puis LLL degré21 à échelle 10^40. Discriminants confirmés -7^14 q^9. Coefficients des matrices de multiplication dans les bases finales bornés par 8 (683), 9 (907). Les embeddings numériques servent uniquement à sélectionner une transformation unimodulaire et des candidats : aucune certification par flottants.

Générateurs exacts nouveaux, indices relatifs premiers à 7, choisis parmi 157 et 161 candidats :
- q683 : x^7 - 9x^6 + 41x^5 - 19x^4 - 121x^3 - 374x^2 + 456x - 121, indice 1219231.
- q907 : x^7 - 10x^6 + 31x^5 - 40x^4 + 247x^3 - 298x^2 - 215x - 36, indice 425984.
Les deux polynômes sont irréductibles selon Sympy et vérifiés par charpoly et identité disc(P)=disc(O)*indice^2. Réduction mod7 : (x-2)(x²+2)^3 et (x+1)(x²+x-1)^3. Ne pas refaire les grosses résolvantes.

## 4. Axe B : recherche directe et collisions d'idéaux
Recherche directe par combinaisons ±1 dans la base réduite. q683 23793 candidats, 19 unités trouvées (rang logarithmique heuristique 4). q907 23476 candidats, 10 unités (rang heuristique 2). Les normes sont exactement vérifiées par déterminant entier ; plusieurs unités appartiennent au cubique et sont dépendantes. Premier calcul local : rang 8 pour 683, 2 pour 907, pas 20.

Nouvelle méthode rapide : énumération de vecteurs par lots de 256, calcul des déterminants modulo 1009,1013,1019 par élimination de Gauss vectorisée, CRT, filtre des petites normes <=10000, puis recalcul du déterminant entier. Deux éléments a,b non nuls avec même HNF de matrices de multiplication engendrent le même idéal principal, donc a/b et b/a sont unités. On calcule le quotient par résolution exacte, vérifie intégralité et norme ±1. L'égalité du HNF, pas celle des seules normes, est indispensable. q683 : 190208 candidats, 101 petites normes exactes, 34 collisions, 33 unités (incluant anciennes) ; rang local 14. q907 : 209408 candidats, 26 petites normes, 1 collision, toujours 10 unités, rang2. Le filtre CRT peut exclure de grandes normes, mais ne crée pas de fausses unités puisque le contrôle final est exact ; aucune exhaustivité des petites normes de tous éléments du corps n'est revendiquée.

## 5. Axe C : LLL pondérée, diversification
Dans l'espace de Minkowski, poids exp(w) commun aux deux coordonnées d'un plongement complexe, w tirés de manière déterministe dans [-3,3] puis [-6,6], réduction LLL unimodulaire. Examiner cinq premiers vecteurs et leurs sommes/différences, tester norme exacte et HNF des petits idéaux de norme <=10^7. Ces poids sont une heuristique, pas un théorème de génération du groupe des unités.
- q683 : 25 réductions, 579 candidats, 204 petites normes, 24 collisions, 70 unités ; seconde passe 12 réductions, 300 candidats, 74 petites normes, 6 collisions, 80 unités. Rang local reste 14.
- q907 : 26 réductions, 584 candidats, 104 petites normes, 7 collisions, 23 unités ; seconde passe 12 réductions, 300 candidats, 44 petites normes, 1 collision, aucune unité supplémentaire ; rang local passe de 2 à 8.
Les 103 unités finales (80+23) ont toutes été vérifiées séparément par déterminant exact. Ce n'est PAS 103 unités multiplicativement indépendantes : le rang de Dirichlet du corps degré21 signature (3,9) est 11. Les images de conjugaison dans le degré42 peuvent avoir rang jusqu'à 20. On n'a PAS déterminé le groupe complet des unités.

## 6. Axe D : images locales, vérification indépendante et structure des modules
Adapter embed107 au q variable, première exécution échouée par variable locale q masquant le discriminant, corrigée avant toute revendication. Dans R=Z_7[pi,t], pi^3=7pi²-14pi+7, t²=-q, les sept racines des deux septiques ont été construites par Hensel : une racine simple et deux paquets de trois après translation et division par pi³, résidus simples. Delta envoie pi vers 4pi-pi² et t vers -t ; racines étiquetées pour delta(i)=3i. On évalue les unités exactes dans les sept copies, log(a^48) mod 7m, m=(pi). Comme e=3, pour k>=4, v_pi(h^k/k)>=4 quand v_pi(h)>=1 (y compris k=7, v>=4), donc les trois termes suffisent. Dénominateurs de base ont valuation 7 <=1, racines levées à pi^13 puis pi^16, précision mod 7^6 puis 7^7 ; les deux tableaux finaux de vecteurs et G sont exactement identiques pour chaque q. Ce contrôle reproduit la même méthode avec précision différente, pas une deuxième construction arithmétique indépendante.

U_partial est engendré par les images des unités trouvées et leurs sept translatés S. Contrôles Sympy puis élimination mod7 NumPy indépendante, stabilité par S et G, G^6=1, G S=S^3 G, D=log S et D^7=0. Résultats :
|q|unités testées norme exacte|rang U_partial|rangs U_partial+im D^i (i=1..7)|rangs D^i U_partial (i=0..7)|dimensions poids 1..6|
|--|--:|--:|--|--|--|
|683|80|14|38,34,30,26,22,18,14|14,12,10,8,6,4,2,0|2,3,2,3,2,2|
|907|23|8|37,32,27,22,17,12,8|8,6,5,4,3,2,1,0|1,2,1,2,1,1|
Donc pour q683 le sous-module trouvé a deux blocs de Jordan de longueur7 ; q907 un bloc longueur7 et un longueur1 (différences de rang). Ce sont des structures des sous-modules trouvés, non du module global complet. Si rang complet=20 attendu par le modèle antérieur, il manque respectivement 6 et 12 dimensions. L'absence de rang maximal ne démontre pas une défaillance de Leopoldt, ni la nullité d'un coefficient. Impossible de déterminer e_loc et e8 à partir d'un sous-espace incomplet : une relation absente du sous-espace peut appartenir au vrai espace des unités. Ne pas réutiliser les assertions rank20/rank32 du script -107 sur ces données partielles.

## 7. Bilan critique et prochaine expérience
Quatre axes substantiels : réduction certifiée des bases, collisions exactes d'idéaux, recherche pondérée, plongements/rang et structure. Les deux petits générateurs et les certificats d'unités et de rang sont des acquis ; le rang 20 n'est pas atteint. Pour q683 les recherches directes supplémentaires ont produit essentiellement des unités dépendantes localement ; pour q907 les collisions à même idéal sont rares. Ne pas répéter simplement les tirages de poids ou les combinaisons ±1. Prochaine expérience distincte : collecte de relations de petits idéaux principaux à normes friables. Pour chaque a non nul de norme N, décomposer aO en composantes primaires via HNF([p^v_p(N) I,M(a)]) ; ces composantes ont produit aO par supports premiers disjoints et CRT des idéaux. Stocker les HNF exacts, former une matrice d'incidence des composants, chercher des relations entières entre plusieurs principaux (noyau), vérifier l'unité obtenue comme produit/quotient exact et recalculer rang local. Si insuffisant, passer à la vraie décomposition en idéaux premiers et à une base de facteurs (Buchmann). Ne pas présumer la saturation des unités ni utiliser GRH. La localisation non abélienne pour -107, les certificats de classes historiques et l'audit Lean restent ouverts. Aucun résultat général H9, aucune nouvelle preuve indépendante RH.

Deux commandes de réduction et une commande de vérification en lot ont atteint leur délai ; la comparaison finale des deux certificats a été relancée séparément et réussie.

## 8. Scripts et données reproductibles
Recréer /mnt/data/riemann_1105. Les fullorder*.json du checkpoint 1004 sont les entrées de units_retry.py. Les scripts principaux ci-dessous ont été exécutés : `python units_retry.py 907 12`, `python units_retry.py 683 12`, `python norm_collisions.py 683 18`, `python norm_collisions.py 907 18`, `python weighted_units.py 907 18`, `python weighted_units.py 683 18`, `python wide_units.py 683 14`, `python wide_units.py 907 14`, `PREC=6 LIFT=13 python embed_wide.py q`, `PREC=7 LIFT=16 python embed_wide.py q`, `python audit_units.py`. Les recherches à limite de temps peuvent examiner un nombre légèrement différent de candidats à la reproduction. Les certificats JSON finaux permettent de rejouer le contrôle sans relancer les heuristiques. Les données de départ volumineuses (fullorder*.json) restent dans le checkpoint 1004, pas répétées ici. Les logs des phases finales sont inclus. 

### order7.py


[Extracted file: order7.py](files/order7.py) · 3,165 bytes · Source block 1.

### units_retry.py


[Extracted file: units_retry.py](files/units_retry.py) · 5,021 bytes · Source block 2.

### norm_collisions.py


[Extracted file: norm_collisions.py](files/norm_collisions.py) · 2,698 bytes · Source block 3.

### weighted_units.py


[Extracted file: weighted_units.py](files/weighted_units.py) · 3,150 bytes · Source block 4.

### wide_units.py


[Extracted file: wide_units.py](files/wide_units.py) · 3,155 bytes · Source block 5.

### embed_wide.py


[Extracted file: embed_wide.py](files/embed_wide.py) · 5,041 bytes · Source block 6.

### audit_units.py


[Extracted file: audit_units.py](files/audit_units.py) · 1,924 bytes · Source block 7.

### units683_final.log


[Extracted file: units683_final.log](files/units683_final.log) · 1,540 bytes · Source block 8.

### units907_final.log


[Extracted file: units907_final.log](files/units907_final.log) · 1,135 bytes · Source block 9.

### coll683.log


[Extracted file: coll683.log](files/coll683.log) · 3,989 bytes · Source block 10.

### coll907.log


[Extracted file: coll907.log](files/coll907.log) · 3,812 bytes · Source block 11.

### weight683.log


[Extracted file: weight683.log](files/weight683.log) · 1,439 bytes · Source block 12.

### weight907.log


[Extracted file: weight907.log](files/weight907.log) · 745 bytes · Source block 13.

### wide683.log


[Extracted file: wide683.log](files/wide683.log) · 459 bytes · Source block 14.

### wide907.log


[Extracted file: wide907.log](files/wide907.log) · 190 bytes · Source block 15.

### embwide683_6.log


[Extracted file: embwide683_6.log](files/embwide683_6.log) · 541 bytes · Source block 16.

### embwide683_7.log


[Extracted file: embwide683_7.log](files/embwide683_7.log) · 580 bytes · Source block 17.

### embwide907_6.log


[Extracted file: embwide907_6.log](files/embwide907_6.log) · 553 bytes · Source block 18.

### embwide907_7.log


[Extracted file: embwide907_7.log](files/embwide907_7.log) · 582 bytes · Source block 19.

### audit.log


[Extracted file: audit.log](files/audit.log) · 261 bytes · Source block 20.

### smallgen683.json


[Extracted file: smallgen683.json](files/smallgen683.json) · 1,480 bytes · Source block 21.

### smallgen907.json


[Extracted file: smallgen907.json](files/smallgen907.json) · 1,052 bytes · Source block 22.

### units_wide683.json


[Extracted file: units_wide683.json](files/units_wide683.json) · 94,910 bytes · Source block 23.

### units_wide907.json


[Extracted file: units_wide907.json](files/units_wide907.json) · 76,790 bytes · Source block 24.

### partial_cert683_6.json


[Extracted file: partial_cert683_6.json](files/partial_cert683_6.json) · 10,375 bytes · Source block 25.

### partial_cert683_7.json


[Extracted file: partial_cert683_7.json](files/partial_cert683_7.json) · 10,375 bytes · Source block 26.

### partial_cert907_6.json


[Extracted file: partial_cert907_6.json](files/partial_cert907_6.json) · 3,079 bytes · Source block 27.

### partial_cert907_7.json


[Extracted file: partial_cert907_7.json](files/partial_cert907_7.json) · 3,079 bytes · Source block 28.


