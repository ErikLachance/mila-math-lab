# Riemann — checkpoint du 25 novembre 2026, 06:19 EST

> **Historical research record / Archive de recherche.** Imported on 26 November 2026. Mathematical claims, source reports and test outcomes below describe the historical checkpoint. They have not all been independently audited or rerun during this import. No proof of RH is claimed.
> Private operational sections and scheduling metadata have been omitted. All embedded code, data and output blocks have been extracted byte-for-byte into linked files. Source scripts retain their historical paths and dependencies; they are not automatically executed.

**Source record:** `RIEMANN_CHECKPOINT_2026-11-25_0619_EST.md`. **Recorded time label:** 2026-11-25 06:19 EST (from the filename).

[Archive index](../../README.md) · [Manifest](../../manifest.json) · [Verification scope](../../README.md#what-was-checked-during-import)


## 2. Sources effectivement consultées
- MIT Andrew Sutherland, https://math.mit.edu/~drew/grh/ (état daté 24 novembre 05:25 UTC : acceptations indépendantes, Comparator v4.36 encore en cours sur la page). Waterloo, https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/ (résultat 21 novembre, compilation et noyau indépendant). Clay https://www.claymath.org/millennium/riemann-hypothesis/ (statut Active). Aucune nouvelle compilation Lean personnelle.
- Magma Handbook, https://docs.magma-maths.org/v2.30-1/GlobalFields/NumberFieldsAndOrders/creation.html (Round 2, p-radical et multiplicateur, exemple d'algorithme). PARI, https://pari.math.u-bordeaux.fr/dochtml/ref/General_number_fields.html (bnfinit et bnfcertify, risque GRH). Sympy documentation https://dokk.org/documentation/sympy/sympy-1.11.1/modules/polys/numberfields.html (round_two). Sarkar–Shaikh https://arxiv.org/abs/1904.09850 (résumé, logarithme principal si e<p−1). Pas de PDF ouvert/analy­sé. Les calculs propres ci-dessous ne viennent pas de ces références.

## 3. Axe A — ordre maximal sans PARI, sans GRH
Soit B défini par P=X^7−35X^5−3899X^4+54572X³−293664X²+1396416X−6760448 (irréductibilité exacte contrôlée), C=X³+X²−2X−1, R=B Q(c), C(c)=0. Les degrés 7 et 3 étant copremiers, le compositum a degré21. L'identification de B et de R avec les sous-corps de l'extension Kummer E des checkpoints précédents demeure une hypothèse de continuité (pas de nouvel audit complet de cette construction).
Algorithme autonome : pour un ordre O de rang n, calculer le noyau de Frobenius x→x^(p^k) dans O/pO avec p^k≥n, ce qui donne le nilradical, et relever à I⊂O. L'anneau multiplicateur (I:I) se trouve entre O et p^-1 O : pO⊂I, et donc a∈(I:I) implique pa∈I⊂O. Pour a/p avec a∈O, la condition est aI⊂pI, linéaire modulo p en utilisant les matrices de multiplication conjuguées dans la base de I. Calculer le noyau modulo p, HNF de pO et des relèvements du noyau, diviser par p. Vérifier fermeture entière de l'ordre obtenu et identité discriminant/index². Répéter jusqu'au point fixe; critère standard Round 2 de p-maximalité au point fixe, voir Magma. Les autres premiers restent maximaux car l'agrandissement est d'indice puissance de p. Ce calcul ne suppose pas la valeur théorique du discriminant du corps, ni GRH. En degré7, étapes d'indices 2,4,8,2,4,8 pour p=2; 7,49,7,7 pour p=7; 1 pour 79; 38737 et 13513109 chacun une étape. Les cinq nombres premiers ont été les seuls facteurs du discriminant polynomial; vérifier la factorisation avec le code/arithmétique exacte. Discriminant de B obtenu −1183786639=−7^4*79^3, coïncide avec le calcul ramification du checkpoint 04:54. En degré21, ordre tensoriel O_B⊗Z[c], discriminant d_B^3*49^7, donc seulement 7,79 à traiter. Agrandissements 49,2401, indice total 117649=7^6; aucun agrandissement en 79. Discriminant maximal exact −81286117713188259904898920831. Bases rationnelles et matrices d'ordre reproductibles par le script. Première phase 9.26s dans un appel réussi. Aucun besoin de Sympy round_two, dont ClosureFailure avait bloqué la session précédente.

## 4. Axe B — unités globales et saturation mod 7 certifiée
LLL sur plongements de Minkowski, 100 décimales et échelle 10^32, utilisé seulement pour choisir une base courte. Matrice unimodulaire vérifiée, produit de transformation exact, toutes matrices de multiplication entières. Recherche de combinaisons de 1 à 4 vecteurs avec signes; filtre sur les normes modulo 3,5,7,11,13, puis déterminant entier exact. Premier appel de recherche trop long (timeout; log partiel), corrigé par arrêt après 19 unités. Deuxième appel réussi : 9900 candidats, 135 survivants du filtre, 19 unités de norme ±1 dont 11 log-indépendantes numériquement (cette indépendance flottante n'est PAS la certification). Normes recalculées exactement dans le script suivant.
Soit I=rad(7O_R). Dimension nilradical 14 dans O_R/7, dimension résiduelle7; Frobenius49 idempotent modulo7 (degrés résiduels divisent2). I^4=7I vérifié par HNF des produits d'idéaux; ceci certifie e=3 pour chaque place au-dessus de7. Pour u unité, u^48−1∈I; log(u^48) modulo 7I = h−h²/2+h³/3 avec h=u^48−1. Tous termes n≥4 ont valuation ≥n−3v_7(n)≥4; le calcul modulo49O suffit car 49O⊂7I. Comme e=3<6, log est bijectif principal et la puissance48 est inversible sur le quotient de type F7. Calcul dans I/7I de dimension21 : rang exactement11 des 19 unités; indices indépendants [1,2,8,9,10,11,15,16,17,18,19]. 361 vérifications exactes d'additivité du logarithme sur les produits de toutes les paires. Le rang local implique indépendance dans O_R^×/(O_R^×)^7; le rang global maximal est11 (signature (3,9), pas de 7e racine de l'unité puisque 6 ne divise pas 21). Donc ces unités forment une base MODULO 7, sans certifier qu'elles sont une base intégrale de tout le groupe des unités. Cette distinction est essentielle. Pas de bnfinit ni hypothèse RH.

## 5. Axe C — modèle petit et localement monogène
LLL du degré7 suivi de recherche de combinaisons courtes, indices calculés par les puissances exactes. 152 candidats primitifs d'indice premier à7. Meilleur selon hauteur des coefficients : f=X^7−2X^6+9X^5−10X^4+10X³+5X+4, indice 64 dans O_B; irréductibilité et discriminant f=d_B*64² vérifiés. Modulo7 : (X+3)(X²+3X−1)^3. Matrice de passage des anciennes puissances de P aux nouvelles exacte, incluse dans le log et régénérée par le script. Ce modèle permet de faire le calcul local sans PARI ni Hensel à index divisible par7.

## 6. Axe D — calcul EFFECTIF du coefficient de localisation (conditionnel à l'identification arithmétique antérieure)
Notations 02:59/04:54 : K=Q(sqrt(-79)), F=K Q(c), E/F extension cyclique non ramifiée de degré7, theta=eta omega², beta=theta^-1. Hypothèses antérieures à auditer : identification E, liberté pro-7 de rang4, groupe de classes Cl(E)[7]=0, présentation locale D096. Localement F_v=Q7(pi,t) avec pi=2−c, pi³=7pi²−14pi+7, t²=−79, e=3, f=2. Le complément Delta est généré ici par delta(c)=c²−2, delta(t)=−t, theta(delta)=3 et beta(delta)=5. On fixe une place et des étiquettes des plongements du corps B en accord avec ce complément (x générateur de C7, delta x delta^-1=x³). Les racines du nouveau polynôme dans F_v sont calculées par Hensel : racine simple résiduelle4; deux racines résiduelles 2±t de multiplicité3. Pour chacune des dernières, substituer a+pi Y, diviser les coefficients par pi³; trois racines simples résiduelles distinctes (vérifiées), donc trois relèvements. Sept racines en tout, une fixe sous delta; numéroter les six autres par delta(r_i)=r_(3i). Cela repose sur l'action Galois theta déjà identifiée, pas seulement sur une permutation arbitraire des racines. Vérifier l'action et la précision : premier calcul modulo 7^5 avec relèvements à pi^10; second modulo 7^6 et pi^12, avec choix différent de racine génératrice. Les divisions par pi³ dans les coefficients restent assez précises. Les dénominateurs p-part des coordonnées des unités sont au plus 7^1 (assertion), perte de précision ≤3 en valuation; même le premier calcul conserve la précision requise pi^4. Les coefficients de passage rationnels sont exacts; résidus et rangs uniquement entiers. Pas de détermination de zéro par flottants.
Pour chacune des 19 unités, évaluer aux sept plongements (c fixé) et former le vecteur log(u^48) dans W=(m/7m)^7, dimension42. Le module engendré par les 7 translations de ces vecteurs a rang20 (deux calculs indépendants en précision et choix de générateur); il est stable sous delta. Sous les hypothèses antérieures, ceci est exactement U, noyau W→Hbar, car U de dimension20. Même sans la conclusion de p-rationalité, c'est un calcul explicite de l'espace des images des unités de E sous l'identification de corps et l'argument de génération; le lien au quotient Hbar reste conditionnel. La relation GS=S³G est vérifiée exactement, S décalage cyclique, D=log S. R3=U+D³W rang32, R4=U+D⁴W rang29, donc quotients de dimensions10,13, conformes à la théorie. K4={v : Dv∈R4} calculé via noyau du bloc [D,-R4]; son image modulo R3 est de dimension1 (ligne X0). Les classes locales u_theta, y1, y_beta sont obtenues comme vecteurs propres de la matrice 6×6 de delta, dans le seul slot0, de valeurs propres3,1,5; chaque espace propre est unidimensionnel. Vérifier indépendance des classes dans le quotient :
- rang R3 =32;
- rang (R3+K4)=33;
- rang (R3+K4+span(D y1))=34;
- rang après ajout de u_theta =35;
- rang après ajout de D² ybeta =35 (calcul séparé à partir de l'espace rang34);
- rang R3+span(D y1,D² ybeta,u_theta)=35, donc le coefficient X0 de u_theta est lui aussi non nul.
Conclusion du test de rang : e_loc NON NUL dans F7 (pas de valeur normalisée revendiquée), sous les hypothèses de la construction. Résultat répété en précision accrue et avec un autre générateur du groupe cyclique. Dans les réductions conditionnelles du checkpoint 02:59, j=2 est exclu, j=5 reste possible. Cette conclusion ne prouve ni la réalisation d'une déformation j5 ni H9. Le certificat numérique est fini et exact, pas un test matriciel synthétique : il emploie de vraies unités du corps de degré21 et leurs images locales calculées. Les preuves de Hensel et du quotient restent à relire adversarialement; ne pas effacer les hypothèses de départ. 

## 7. Reprise et limites
Quatre axes réellement réalisés : bases maximales, unités et saturation locale, petit générateur, plongements et test de rang. Obstacle technique antérieur (absence PARI/Sage) contourné par code indépendant. Première recherche trop longue, puis réussie; aucune assertion échouée dans les scripts finaux. Pas de preuve générale de RH; aucune nouvelle vérification Lean personnelle. H9 est conditionnel et j5 n'est pas résolu. Plus haut niveau de priorité pour la prochaine session : (i) audit indépendant de l'identification Kummer E et de la p-rationalité, notamment le caractère theta exact de l'action et la présentation D096; (ii) dans la branche j5 restante, utiliser le Frobenius de la place et le marquage. Le résultat non nul fournit la relation nécessaire v0=c q²/(2 e_loc a). Déterminer si la condition de Frobenius/marquage fournit une incompatibilité supplémentaire ou si une déformation admissible réelle existe à l'ordre 7. Ne pas recommencer les recherches d'unités ou de bases maximales sans nouvelle question. Un coefficient non nul n'est pas une contradiction générale. Vérifier aussi la formule de passage de l'inertie au groupe de classes local dans la convention d'Artin utilisée.

## 8. Scripts et sorties reproductibles
Les scripts utilisent Sympy, mpmath et numpy. Exécuter dans le même dossier (adapter les chemins /mnt/data au besoin); ordre : order, units, local, smallgen, embed. Le script units régénère le JSON des matrices/unités, smallgen régénère le JSON de passage. Le dernier script produit un certificat fini de 19 colonnes de dimension42. Le script embed a été relancé avec PREC=6 LIFT=12 ROOT_CHOICE=4; le premier passage employait les valeurs par défaut (5,10,0) avant ajout des assertions finales.

### riemann_order_run11.py


[Extracted file: riemann_order_run11.py](files/riemann_order_run11.py) · 2,965 bytes · Source block 1.

### riemann_units_run11.py


[Extracted file: riemann_units_run11.py](files/riemann_units_run11.py) · 3,114 bytes · Source block 2.

### riemann_local_run11.py


[Extracted file: riemann_local_run11.py](files/riemann_local_run11.py) · 1,905 bytes · Source block 3.

### riemann_smallgen_run11.py


[Extracted file: riemann_smallgen_run11.py](files/riemann_smallgen_run11.py) · 1,731 bytes · Source block 4.

### riemann_embed_run11.py


[Extracted file: riemann_embed_run11.py](files/riemann_embed_run11.py) · 6,197 bytes · Source block 5.

### riemann_order_run11.log


[Extracted file: riemann_order_run11.log](files/riemann_order_run11.log) · 2,965 bytes · Source block 6.

### riemann_units_run11.log


[Extracted file: riemann_units_run11.log](files/riemann_units_run11.log) · 2,017 bytes · Source block 7.

### riemann_local_run11.log


[Extracted file: riemann_local_run11.log](files/riemann_local_run11.log) · 1,965 bytes · Source block 8.

### riemann_smallgen_run11.log


[Extracted file: riemann_smallgen_run11.log](files/riemann_smallgen_run11.log) · 2,714 bytes · Source block 9.

### riemann_embed_run11.log


[Extracted file: riemann_embed_run11.log](files/riemann_embed_run11.log) · 581 bytes · Source block 10.

### riemann_embed_run11_verify.log


[Extracted file: riemann_embed_run11_verify.log](files/riemann_embed_run11_verify.log) · 670 bytes · Source block 11.

### Certificat F7 (second passage)


[Extracted file: block-012.json](files/block-012.json) · 2,975 bytes · Source block 12.


