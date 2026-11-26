# Riemann — checkpoint du 25 novembre 2026, session 11:51 EST

> **Historical research record / Archive de recherche.** Imported on 26 November 2026. Mathematical claims, source reports and test outcomes below describe the historical checkpoint. They have not all been independently audited or rerun during this import. No proof of RH is claimed.
> Private operational sections and scheduling metadata have been omitted. All embedded code, data and output blocks have been extracted byte-for-byte into linked files. Source scripts retain their historical paths and dependencies; they are not automatically executed.

**Source record:** `RIEMANN_CHECKPOINT_2026-11-25_1151_EST.md`. **Recorded time label:** 2026-11-25 11:51 EST (from the filename).

[Archive index](../../README.md) · [Manifest](../../manifest.json) · [Verification scope](../../README.md#what-was-checked-during-import)


## 2. Sources réellement consultées
- Andrew Sutherland, MIT https://math.mit.edu/~drew/grh/ (dernière mise à jour 24 novembre 05:25 UTC) : compilations, axiomes et vérifications indépendantes positifs ; lake comparator v4.36.0 encore indiqué en cours. Waterloo https://math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/ (résultat 21 novembre, vérifications positives). Il s'agit de vérifications externes, non d'une exécution Lean personnelle. Le travail ci-dessous est indépendant et exploratoire.
- Andrew O'Desky D103 https://andrewodesky.com/rh/lean/UpperTheory.V.Aut.AutomorphyUnramifiedCoefficientsAlt/ : quatre propriétés de l'hypothèse d'automorphie, dont S0 fini pour tout anneau pertinent à un g1 marqué. Ne pas confondre une obstruction calculée pour un datum avec H9 générale ou preuve de RH.
- Documentation PARI https://pari.math.u-bordeaux1.fr/dochtml/html/General_number_fields.html : cette tentative de consultation a échoué (timeout HTTP400). Aucun recours à PARI/Sage ni à GRH ; les matrices d'ordres exacts viennent de 1105, leur maximalité et l'identification galoisienne héritées restent conditionnelles à leur audit.

## 3. Axe A : décomposition des petits premiers par Frobenius fixe
Dans un ordre maximal O de discriminant -7^14 q^9 (q=683 ou 907), pour p ne divisant pas 7q, O/pO est une algèbre étale. Le noyau de Frobenius moins identité est le produit F_p^r. Pour chaque vecteur fixe a, les idempotents 1-(a-r)^(p-1) séparent ses valeurs r dans F_p ; raffiner les produits sur une base du noyau donne les idempotents primitifs e_i. Contrôles exacts : orthogonalité, somme 1, e_i^2=e_i, somme des degrés 21, HNF de (p,1-e_i) de déterminant p^f_i. Cette méthode ne demande pas un générateur monogène, et fonctionne même si p divise l'indice du générateur choisi mais pas le discriminant de l'ordre. Pour les premiers 7 et autres hors base, les composantes primaires HNF([p^v_p(N) I,M(a)]) sont traitées comme étiquettes entières ; ce n'est qu'une condition suffisante pour détecter une relation, non un factoriseur complet. Les ensembles de premiers préparés sont visibles dans les logs ; le dernier premier 97 de la préparation 907 n'a pas été enregistré avant timeout, donc n'est pas requis pour les résultats.

## 4. Axe B : relations de plusieurs idéaux et réduction ciblée
LLL sur le réseau de Minkowski de petits idéaux premiers (et O), pondération aléatoire déterministe, candidats à 1–3 vecteurs parmi huit premiers vecteurs réduits. Filtre de normes par CRT de quatre premiers 1009,1013,1019,1021 ; recalcul exact du déterminant pour tout candidat retenu. Seuls les éléments de norme <=10^8 et à facteurs dans la base sont gardés (heuristique non exhaustive). q683 : 10 339 candidats, 196 éléments au pool ; q907 : 21 554 candidats, 350 éléments au pool. Inclusion des trois conjugués du facteur cubique c -> c^2-2 ; la matrice de conjugaison est entière, ordre trois, respecte l'unité et chaque matrice de multiplication (21 identités par corps).
Décomposition des idéaux des éléments, recherche d'une dépendance rationnelle par élimination creuse des vecteurs de valuations, élimination des dénominateurs et réduction primitive. Une dépendance entière donne égalité des idéaux principaux produits. Calcul du quotient par matrices entières et résolution exacte ; contrôle que B*u=a, intégralité et norme ±1. Normes des produits vérifiées séparément. Pour éviter explosion, relations dont somme des valeurs absolues des coefficients >80 non exploitées. 683 : 502 éléments/conjugués traités, 410 dépendances (81 écartées par seuil), 339 unités finales contre 80. 907 : 439 éléments/conjugués traités, 345 dépendances (34 écartées), 266 unités finales contre 23. Les pools n'ont pas tous été parcourus, ce n'est pas nécessaire puisque rang maximal atteint. 605 unités testées au total par déterminants exacts indépendants dans verify_rel.py ; ce ne sont PAS 605 unités indépendantes. L'algorithme exact de relations évite la recherche de collisions entre deux seuls idéaux. Aucun recours à une estimation de rang flottante pour le résultat.
Premières tentatives de réduction avec HNF et inverses rationnels ont atteint le délai, dont une commande double. L'accélération consiste à relever l'idempotent e_i modulo p^k par e -> 3e²-2e³ (double la précision d'idempotence), puis tester e_i*a=0 mod p^k. Comme p non ramifié, c'est exactement la divisibilité par la puissance de l'idéal. Le code utilise object Python pour modulus >10^6 afin d'éviter overflow. Les sommes f_i v_i reproduisent v_p(N). Contrôle indépendant HNF vs Hensel pour 62 cas q683 et 64 q907, tous égaux. Le checksum des normes et les unités exactes sont une défense supplémentaire contre erreur de factorisation.

## 5. Axe C : rang maximal et certificat réduit
Évaluation dans Z_7[pi,t], pi³=7pi²-14pi+7, t²=-q, sept plongements étiquetés par delta(i)=3i. Les deux certificats aux précisions 7^6 (lift pi^13) et 7^7 (lift pi^16) sont exactement identiques pour chaque q. Linéarité utilisée pour accélérer l'évaluation des coordonnées entières. Vérification séparée via évaluation directe des cinq unités choisies, pas par multiplication par les valeurs précalculées de la base ; mêmes vecteurs. Sous l'identification du corps de degré42 CM et des plongements des checkpoints antérieurs, rang de Dirichlet 20, donc le sous-espace de rang20 des images locales des unités est l'image entière (aucune hypothèse de saturation requise pour ce constat de rang). Ne pas prétendre avoir une base fondamentale des unités ou vérifié Leopoldt en général. Le rang est 20 dans les deux cas, contre 14 et 8 avant ce run. Pour les deux : rangs U+D^i W pour i1..7 = 38,35,32,29,26,23,20 ; rangs D^i U pour i0..7 = 20,17,14,11,8,5,2,0 ; poids 1..6 = 3,4,3,4,3,3. Covariance G^6=1, GS=S^3G, stabilité par G et S ; deux blocs longueur7, un longueur6. Certificat minimal : cinq unités de hauteurs max [1,1,1,3,3626] pour 683, [1,1,3,6,211] pour 907, indices donnés dans minimal_certificate.json. Elles suffisent par leurs orbites à engendrer U de rang20. Ceci rend la reproduction beaucoup plus simple que les centaines de candidats.

## 6. Axe D : coefficients exacts et généralisation partielle
Calcul du quotient W/U et des expansions par l'algorithme full107 adapté sans présupposer non-nullité. Les 168 cas (2 corps x 2 précisions x 6 générateurs x 7 places) passent toutes les identités : rangs, covariance, résidus des solutions, poids. En normalisation premier générateur/place0 :
- q683 : c=5, e_loc=1, e8=0. u3=5X0+4Dy1+D²y5 ; u2=D²y1 ; u4=2D⁴y1+5Dy6+4D⁵y5. Même profil de nullité que -107, la branche j=5r reste ouverte.
- q907 : c=5, e_loc=6, e8=1. u3=5X0+3Dy1+6D⁴y6+6D²y5 ; u2=5D²y1+4D⁵y6+D³y5 ; u4=5D⁴y1+2Dy6+2D⁵y5. Même profil de nullité que -79. L'obstruction conditionnelle au degré8 peut être transportée à ce datum SI toutes les hypothèses arithmétiques et d'identification réciprocité et Frobenius sont auditées. Ne pas revendiquer la finitude complète avant cet audit.
Les quatre profils (-79,-107,-683,-907) sont donc (non nul, non nul), (non nul, zéro), (non nul, zéro), (non nul, non nul) pour (e_loc,e8). Ceci est un résultat de calcul arithmétique fini sous les identifications héritées, ni une preuve de H9, ni une réfutation. Les valeurs de coefficients dépendent du choix des bases et normalisations, leur nullité est vérifiée invariante dans les 84 configurations par corps. Dans la branche 683 le coefficient de D³y5 est nul mais celui de D⁵y5 dans u4 non nul ; au degré 10r cette direction est potentiellement pertinente, toutefois pour X=aE31+b(E12+E23), les composantes inférieures de ad_X^5(V) peuvent s'annuler et les corrections de A/B doivent être prises en compte. Ne pas assimiler coefficient non nul à obstruction sans calcul complet.

## 7. Axe E : vérification Bernoulli relative et prochaine expérience
Calcul exact du produit des trois B_{1,chi} impairs dans Q(z)/(z²+z+1), pour les quatre discriminants ; produits -140,-252,-2660,-4788, h^- possibles respectivement (35,70),(63,126),(665,1330),(1197,2394), selon indice de Hasse 1 ou 2. Dans chaque cas v_7=1. Ceci contrôle une condition arithmétique nécessaire indépendamment de la recherche d'unités, mais ne prouve pas toutes les hypothèses Kummer/Frattini, ni l'identification du corps de classe, ni p-rationalité. La priorité suivante n'est plus de chercher des unités pour 683/907. Auditer les hypothèses de classes et les isomorphismes de réciprocité, comparer les deux cas e8=0 et développer le calcul non abélien de la branche j=5r (quotient de classe 2, corrections au degré13). Étudier précisément la différence u2,u4 entre -107 et -683 et déterminer si elle produit une nouvelle obstruction avec un modèle de jets variable plutôt que fixer A à I+tX. Ne pas annoncer H9 générale, ni preuve indépendante RH. Éviter de réutiliser la même recherche LLL maintenant que le certificat maximal existe.

## 8. Reproductibilité et limites
Recréer le dossier /mnt/data/riemann_1151, extraire order7.py, norm_collisions.py, audit_units.py, units_wide{683,907}.json et smallgen{683,907}.json du checkpoint 1105. Les nouveaux scripts et données sont ci-dessous. prime_prepare.py crée des caches locaux pickle (à utiliser uniquement à partir des fichiers créés par son exécution, ne pas charger de pickle non fiable). collect.py q batch crée pool ; process.py q puis process_fast.py q calcule des relations et enregistre l'état. Les limites de temps changent les pools à une réexécution. Les vecteurs finaux certifiés sont inclus séparément avec leurs normes ; on peut reconstruire units_rel{q}.json à partir du fichier units_wide{q}.json en remplaçant la clé units par les vecteurs finaux. embed_rel.py q avec PREC=6 LIFT=13 puis PREC=7 LIFT=16, verify_rel.py, embed_direct.py, full_rel.py, class_factors.py. verify_valuation.py q compare deux algorithmes de valuation sur les pools réellement produits. Les listes complètes des relations (plus de 800 Ko) ne sont pas répétées dans ce snapshot ; les témoins sélectionnés et la vérification directe de norme suffisent à reproduire les rangs et les coefficients sans refaire la collecte. Les scripts historiques ont eu des timeouts ; seuls résultats réellement terminés revendiqués. Les calculs de ce run sont conditionnels aux ordres exacts et données arithmétiques héritées (non audit complet) ; no Lean build.


## 9. Scripts et certificats

### factor_relations.py


[Extracted file: factor_relations.py](files/factor_relations.py) · 6,929 bytes · Source block 1.

### prime_prepare.py


[Extracted file: prime_prepare.py](files/prime_prepare.py) · 6,607 bytes · Source block 2.

### collect.py


[Extracted file: collect.py](files/collect.py) · 2,088 bytes · Source block 3.

### process.py


[Extracted file: process.py](files/process.py) · 1,588 bytes · Source block 4.

### process_fast.py


[Extracted file: process_fast.py](files/process_fast.py) · 2,217 bytes · Source block 5.

### embed_rel.py


[Extracted file: embed_rel.py](files/embed_rel.py) · 5,569 bytes · Source block 6.

### verify_rel.py


[Extracted file: verify_rel.py](files/verify_rel.py) · 1,956 bytes · Source block 7.

### embed_direct.py


[Extracted file: embed_direct.py](files/embed_direct.py) · 5,571 bytes · Source block 8.

### full_rel.py


[Extracted file: full_rel.py](files/full_rel.py) · 4,009 bytes · Source block 9.

### class_factors.py


[Extracted file: class_factors.py](files/class_factors.py) · 592 bytes · Source block 10.

### verify_valuation.py


[Extracted file: verify_valuation.py](files/verify_valuation.py) · 807 bytes · Source block 11.

### minimal_certificate.json


[Extracted file: minimal_certificate.json](files/minimal_certificate.json) · 11,691 bytes · Source block 12.

### pool683.json


[Extracted file: pool683.json](files/pool683.json) · 15,585 bytes · Source block 13.

### pool907.json


[Extracted file: pool907.json](files/pool907.json) · 28,183 bytes · Source block 14.

### full_rel.log


[Extracted file: full_rel.log](files/full_rel.log) · 1,434 bytes · Source block 15.

### verify_rel.log


[Extracted file: verify_rel.log](files/verify_rel.log) · 323 bytes · Source block 16.

### val683.log


[Extracted file: val683.log](files/val683.log) · 79 bytes · Source block 17.

### val907.log


[Extracted file: val907.log](files/val907.log) · 78 bytes · Source block 18.

### class_factors.log


[Extracted file: class_factors.log](files/class_factors.log) · 221 bytes · Source block 19.

### prep683.log


[Extracted file: prep683.log](files/prep683.log) · 1,094 bytes · Source block 20.

### prep907.log


[Extracted file: prep907.log](files/prep907.log) · 1,024 bytes · Source block 21.

### collect683_0.log


[Extracted file: collect683_0.log](files/collect683_0.log) · 2,219 bytes · Source block 22.

### collect907_0.log


[Extracted file: collect907_0.log](files/collect907_0.log) · 2,274 bytes · Source block 23.

### collect907_1.log


[Extracted file: collect907_1.log](files/collect907_1.log) · 2,333 bytes · Source block 24.

### embed683_6.log


[Extracted file: embed683_6.log](files/embed683_6.log) · 542 bytes · Source block 25.

### embed683_7.log


[Extracted file: embed683_7.log](files/embed683_7.log) · 581 bytes · Source block 26.

### embed907_6.log


[Extracted file: embed907_6.log](files/embed907_6.log) · 557 bytes · Source block 27.

### embed907_7.log


[Extracted file: embed907_7.log](files/embed907_7.log) · 586 bytes · Source block 28.

### direct683.log


[Extracted file: direct683.log](files/direct683.log) · 579 bytes · Source block 29.

### direct907.log


[Extracted file: direct907.log](files/direct907.log) · 584 bytes · Source block 30.

### unit_vectors683.json


[Extracted file: unit_vectors683.json](files/unit_vectors683.json) · 55,480 bytes · Source block 31.

### selected_relations683.json


[Extracted file: selected_relations683.json](files/selected_relations683.json) · 2,261 bytes · Source block 32.

### rel_cert683_6.json


[Extracted file: rel_cert683_6.json](files/rel_cert683_6.json) · 43,527 bytes · Source block 33.

### unit_vectors907.json


[Extracted file: unit_vectors907.json](files/unit_vectors907.json) · 80,275 bytes · Source block 34.

### selected_relations907.json


[Extracted file: selected_relations907.json](files/selected_relations907.json) · 1,229 bytes · Source block 35.

### rel_cert907_6.json


[Extracted file: rel_cert907_6.json](files/rel_cert907_6.json) · 34,183 bytes · Source block 36.
