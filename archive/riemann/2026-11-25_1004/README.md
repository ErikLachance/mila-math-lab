# Riemann — checkpoint 25 novembre 2026, session 10:04 EST

> **Historical research record / Archive de recherche.** Imported on 26 November 2026. Mathematical claims, source reports and test outcomes below describe the historical checkpoint. They have not all been independently audited or rerun during this import. No proof of RH is claimed.
> Private operational sections and scheduling metadata have been omitted. All embedded code, data and output blocks have been extracted byte-for-byte into linked files. Source scripts retain their historical paths and dependencies; they are not automatically executed.

**Source record:** `RIEMANN_CHECKPOINT_2026-11-25_1004_EST.md`. **Recorded time label:** 2026-11-25 10:04 EST (from the filename).

[Archive index](../../README.md) · [Manifest](../../manifest.json) · [Verification scope](../../README.md#what-was-checked-during-import)


## 2. Sources consultées
- Andrew Sutherland, MIT, https://math.mit.edu/~drew/grh/ (page mise à jour 24 novembre 05:25 UTC; plusieurs noyaux indépendants et Comparator v4.33 positifs, v4.36 encore annoncé en cours). Clay https://www.claymath.org/millennium/riemann-hypothesis/ (Active). Pas de nouvelle compilation Lean personnelle.
- Andrew O'Desky AGR.D103 https://andrewodesky.com/rh/lean/UpperTheory.V.Aut.AutomorphyUnramifiedCoefficientsAlt/ et D096 https://andrewodesky.com/rh/lean/UpperTheory.V.U3.GG/ (accès direct échoué puis via lien D103 réussi; lignes 18–67 lues). D103 a quatre propriétés; finitude S0 n'est qu'une partie. Catalogue en attente de revue, non le code Lean brut.
- Georges Gras https://arxiv.org/html/1709.06388v2 (p-rationalité, programme ray class, section introductive), Mizusawa https://doi.org/10.1090/TRAN/7787 (résumé sur présentations de Koch et nombres de Milnor), Mizusawa–Okano https://arxiv.org/abs/2610.31965 (résumé récent sur nombres de liaison arithmétiques). Ces deux derniers ne fournissent pas la localisation de notre groupe libre: ne pas importer leurs théorèmes hors hypothèses.

## 3. Axe A — q=107 : première correction potentiellement inférieure du quotient de classe 2
Reprendre X=aE31+b(E12+E23), V=E13, a,b,v non nuls; A=I+tX+O(t²), B=I+t^5 vV+O(t^6), B supérieur unipotent (hypothèse du drapeau local). H image engendrée par A^7 et B_i=A^i B A^-i (i=0..6) après avoir tué y1,y6 dans le modèle conditionnel des checkpoints précédents. Noter U1=[X,V], U2=[X,U1]. Les premiers termes de B_i-I sont t^5 vV et t^6(B6+i v U1). Pour [B_i,B_j], le terme degré10 s'annule; degré11 est supérieur. Au degré12 les contributions sont [V,matrice arbitraire] et [B6+i v U1,B6+j v U1]. La première est supérieure triangulaire (E13 ne produit que la ligne1 ou colonne3); la seconde l'est car B6 strictement supérieur et U1 diagonal. Les autres termes de commutateur multiplicatif commencent au degré15. [A^7,B_i] commence au degré12 par v[X^7,V], diagonal. Donc TOUT le sous-groupe commutateur de cette image de H est triangulaire modulo t^13, y compris conjugaisons par H, puisque H commence au degré5. Attention diagonales possiblement non nulles: triangulaire ne veut pas dire strictement unipotent.

NOUVEAU : C1=B1 B0^-1 et C2=B2 B1^-2 B0 ont premiers termes t^6 vU1 et t^7 vU2, respectivement, par différences finies (les produits croisés n'interviennent pas avant degré10). Leur commutateur commence exactement à t^13, avec coefficient v²[U1,U2]. Identité symbolique [U1,U2]=-a²b(E12+E23)-4a³E31. Le coefficient inférieur est non nul pour tous a,v non nuls en F7, sans restriction sur les corrections supérieures d'A et de B. Cela localise le premier degré où le sous-groupe commutateur peut affecter la coordonnée inférieure, au degré13r pour le changement d'échelle t→t^r (sous hypothèses de filtration correspondantes, les calculs exécutés r=1). Les classes D ybeta et D² ybeta ont poids 1 et theta=3; leur bracket de poids theta peut donc entrer dans la correction du relèvement d'u_theta. Le quotient abélien seul ne peut plus contrôler cette coordonnée, et aucune exclusion de la branche j=5 pour q107 n'en découle. Tests exacts: 216 triples a,b,v non nuls avec échantillons déterministes de corrections supérieures arbitraires, 1296 contrôles de paires, identité symbolique vérifiée. Ce n'est pas une réalisation arithmétique non abélienne. Priorité: calculer la vraie localisation dans le quotient de classe2, pas décréter que ce commutateur est un relèvement d'inertie.

## 4. Axe B — constructions de deux nouveaux corps et certificat de scission à7
q=683,907; N=7q, K=Q(sqrt(-q)), F=K Q(zeta7)^+, L=K(zeta7). u_j normes de 1-zeta_N vers L^+, g=2 (eta(g)=-1), lambda(g)=eta(g) omega(g)^5=3. Six groupes de q-1 facteurs, exponents signés e=[1,-2,-3,-1,2,3], e_j+e_{j+3}=0 et e_{j-1}=3e_j mod7. Le radical alpha=produit u_j^e_j est une unité (Phi_N(1)=1). Non-septième-puissance certifiée directement dans F_ell: q683 ell57373, alpha^((ell-1)/7)=52898; q907 ell152377, valeur95713. Pas besoin de supposer les calculs de classes pour cette non-trivialité. Gal(L(alpha^(1/7))/L)=C7, caractère theta=eta omega². Hors7, non-ramification par Kummer et unité. À7, ord_q(7)=q-1=682,906, premiers à7. Calcul modulo49 dans Z[C_N], réduction dans la base zeta_q^i pi^j, pi=zeta7-1. Utiliser exposants [4,1,0,2,5,6], égaux aux signés grâce à produit u_j=1. Pour chacun, v_pi(alpha^48-1)=7, c=(alpha^48-1)/pi^7 mod pi satisfait c^7=-c. Choisir a=-c/2, y=1+a*pi. Vérification exacte v_pi(alpha^48-y^7)>=8 (borne tronquée modulo pi^12). Comme U2^7=U8 (log/exp, e=6), alpha^48 et donc alpha sont septièmes puissances localement. Descente par norme, degré local premier à7. L'involution de L/F se relève en b→b^-1, zeta7→zeta7^-1, centralise C7 et est centrale (unique involution au-dessus d'elle); quotient donne E/F cyclique d'ordre7 partout non ramifiée et scindée à7, indépendamment de GRH. L'unicité comme Hilbert 7-primaire dépend encore du certificat de classes de 0815.

Gal(E/Q)=C7⋊C6, theta fidèle. Corps septique P fixé par un complément C6, signature (1,3); la ramification tame à q (inertie ordre2, trois transpositions) donne exposant3, à7 (inertie ordre3, deux triples) donne exposant4. Aucune ramification ailleurs. Discriminant D_P=-7^4 q^3. Le compositum P Q(zeta7)^+ a degré21, signature (3,9), est fixe par conjugaison complexe dans E, discriminant -7^14 q^9 (sur 21 lettres, inertie ordre3 à7 sans point fixe car agit régulièrement sur le cubique, inertie ordre2 à q donne neuf transpositions). Ce calcul de discriminant théorique sera utilisé comme cible de certification d'ordre; il ne vient pas d'une factorisation de polynôme.

## 5. Axe C — résolvantes, échec de LLL et réparation par rang exact
Pour b^7=alpha, choisir plongement b positif. Le relèvement positif du générateur g envoie b vers b^3 fois un monôme unitaire, avec exposants d_l=(e_{l-1}-3e_l)/7; pour g^j, r_j=3^j mod7, d_{jl}=(e_{l-j}-r_j e_l)/7. Son ordre6 suit de la positivité et de g^6=1 sur L. Traces sur le complément (b fois monômes unitaires) sont entières dans le corps septique, et leurs 7 conjugués s'obtiennent en multipliant les termes par zeta7^(i r_j). La conjugaison complexe fixe les termes réels; la combinaison de g³ avec conjugaison donne l'involution L/F, donc ces traces appartiennent à E. Les candidats non rationnels ont degré7.

Premier essai, adaptation directe du script 0846: échec assertion Sympy LLL pour q683, délai pour q907. Deuxième essai, LLL rationnel: q683 sélectionne une relation exacte nulle à cause du faux rang numérique (poly x^7); q907 délai dans la borne par fractions géantes. Ces échecs ne sont PAS des résultats sur les corps. Réparation: choisir un monôme unique parmi 243 candidats heuristiques par corps; borne rigoureuse des unités via formule de Machin pour pi, 80 termes atan, 18 termes sinus avec alternance et arrondi rationnel extérieur à 2^-64, produits entiers. Pour chaque plongement, borner la septième puissance du monôme par le produit des intervalles selon signe de chaque exposant, prendre racine septième entière majorante. Le CRT (module>2 fois borne maximale des coefficients) et un premier supplémentaire indépendant donnent les polynômes moniques irréductibles sans dépendre de la précision des logs.

Ensuite sélectionner sept vecteurs réellement indépendants via réduction dans F_ell aux 7 racines (ell28687/342847, rang7), éliminer les relations algébriques avant LLL. LLL rationnel avec transformation unimodulaire contrôlée choisit un générateur plus petit. Nouveau CRT avec mêmes bornes sûres (ne pas utiliser la petite norme numérique pour certifier), 12 et 20 premiers plus contrôle indépendant. Polynômes réduits :

q683: x^7 -1908487*x^5 -9138565393412*x^4 -320523474497361086*x^3 -3063577916116214319914*x^2 -9647224574538804441430599*x -9694675432499093990708718703.
q907: x^7 -13055350*x^5 +45763622296*x^4 -135390003353486*x^3 +247303112325041017*x^2 -275954967556491451963*x +232291079984812324672404.

Coefficients max en chiffres: q683 48→28, q907 37→24 (comparaison des polynômes monômes uniques aux réduits, pas optimum absolu). Les polynômes sont irréductibles selon Sympy et le degré7 du corps construit. Aucun calcul de GRH. Fichiers et logs ci-dessous.

## 6. Axe D — anneaux d'entiers sans factoriser les grands indices
Calcul des structures de multiplication dans les ordres Z[x]/P, saturation classique au premier7 avec étapes d'indices 7,49,7,7 pour les deux, total 7^5=16807. Le discriminant théorique permet d'obtenir exactement l'indice de l'ordre initial comme racine carrée de D_pol/D_corps. Factorisation partielle (limit=10000) laisse des COMPOSITES de 68 chiffres (q683) et 61 chiffres (q907). Les premiers connus supplémentaires sont 41,181,633877 et 293, respectivement, chacun avec indice1 en valuation. Ne pas perdre une session à factoriser intégralement ces composites.

NOUVELLE méthode de calcul utilisée et vérifiée ici: pour le module composite m restant, prendre noyau de la matrice trace T modulo m par pivots inversibles; si pivot non inversible, pgcd peut scinder le module (non requis dans ces deux calculs). Préimage I du noyau dans l'ordre, HNF de [mI,K]. Vérifier exactement que I est idéal (matrices de multiplication dans base I entières). Pour l'idealizer, calculer noyau modulo m du système empilé de toutes les matrices de multiplication sur I, puis HNF et division par m. L'ordre candidat est vérifié par calcul EXACT de changement de base, fermeture de multiplication et présence de 1. Le noyau trace et celui de l'idealizer ont chacun dimension1 (base libre calculée par pivots unités) dans les deux cas. L'élargissement intégral a indice exactement m, sans factorisation du composite. Le discriminant atteint la cible théorique -764987380787 (q683) et -1791488485843 (q907), donc ordre maximal si la construction de corps et son discriminant théorique sont corrects. En outre les deux identités disc_pol*det(B)^2=disc_ord et 98 identités exactes de composition des matrices de multiplication (49 par corps) ont été contrôlées séparément. La généralité de la méthode pour composites arbitraires n'est PAS démontrée: le certificat final par discriminant et intégralité est ce qui assure la conclusion pour ces cas. Temps composite_order.py y compris étapes aux premiers connus : 0,54s et 0,25s.

Puis produit tensoriel avec le cubique x^3+x^2-2x-1, saturation à7 (étapes indice49,2401; total117649=7^6). Disc exact des ordres de degré21:
q683 -21936073536305340936530059074278066747;
q907 -281733275000784905869346976586964233243.
Ils égalent -7^14 q^9, donc anneaux d'entiers obtenus sous le certificat théorique ci-dessus. Temps 6,97 et 7,23s. Certificats JSON des bases et de la multiplication joints dans ce Markdown. Cela enlève l'obstacle pratique de factorisation des indices des deux nouveaux corps. Pas de calcul des unités ou des images locales e_loc/e8 pour ces deux cas dans cette exécution.

## 7. Bilan, limites, reprise
Cinq axes: obstruction de classe2 au degré13; constructions Kummer et scission locale; CRT rigoureux et réduction; saturation par composite sans factorisation; anneaux de degré21. Blocages corrigés: LLL flottant/rang fictif, borne lente, factorisation partielle. Blocage restant: localisation NON ABÉLIENNE de q107, et unités/images locales des deux nouveaux corps; le lien exact au code Lean intégral et les certificats historiques de classes restent à auditer. Aucun résultat général H9, aucune nouvelle preuve indépendante de RH. Ne pas recommencer les mêmes calculs de polynômes ou factoriser les deux grands indices. Prochaine expérience: adapter units107.py, smallgen107.py et embed107.py du checkpoint 0846 aux nouveaux ordres de degré21, sélectionner unités par norme exacte, vérifier rang20 des plongements, calculer e_loc et e8 aux deux précisions. En parallèle, pour q107 calculer les images de classe2 des relèvements de u_theta; le degré13 est désormais la limite inférieure précise du premier effet sur les entrées inférieures. Si aucun vrai calcul arithmétique non abélien disponible, ne pas inventer les coefficients et poursuivre l'audit.

## 8. Code et certificats reproductibles
Recréer /mnt/data/riemann_1004 et les scripts ci-dessous; exécuter local_split.py 683 907, degree7_single.py puis degree7_reduced.py 683 et 907 séparément; order7.py et index_factor.py pour diagnostics; composite_order.py 683 907; order21.py 683 907; class2_filtration.py. Les premières tentatives échouées ne sont pas des preuves; leurs logs sont inclus pour ne pas les répéter. Les polynômes écrits par degree7_reduced.py sont ceux utilisés dans les ordres.

### class2_filtration.py


[Extracted file: class2_filtration.py](files/class2_filtration.py) · 2,143 bytes · Source block 1.

### local_split.py


[Extracted file: local_split.py](files/local_split.py) · 2,445 bytes · Source block 2.

### degree7_single.py


[Extracted file: degree7_single.py](files/degree7_single.py) · 4,502 bytes · Source block 3.

### degree7_reduced.py


[Extracted file: degree7_reduced.py](files/degree7_reduced.py) · 6,932 bytes · Source block 4.

### order7.py


[Extracted file: order7.py](files/order7.py) · 3,129 bytes · Source block 5.

### index_factor.py


[Extracted file: index_factor.py](files/index_factor.py) · 463 bytes · Source block 6.

### composite_order.py


[Extracted file: composite_order.py](files/composite_order.py) · 2,993 bytes · Source block 7.

### order21.py


[Extracted file: order21.py](files/order21.py) · 969 bytes · Source block 8.

### class2.log


[Extracted file: class2.log](files/class2.log) · 204 bytes · Source block 9.

### local_split.log


[Extracted file: local_split.log](files/local_split.log) · 371 bytes · Source block 10.

### single683.log


[Extracted file: single683.log](files/single683.log) · 1,078 bytes · Source block 11.

### single907.log


[Extracted file: single907.log](files/single907.log) · 959 bytes · Source block 12.

### reduced683.log


[Extracted file: reduced683.log](files/reduced683.log) · 1,245 bytes · Source block 13.

### reduced907.log


[Extracted file: reduced907.log](files/reduced907.log) · 1,369 bytes · Source block 14.

### order7.log


[Extracted file: order7.log](files/order7.log) · 1,886 bytes · Source block 15.

### index_factor.log


[Extracted file: index_factor.log](files/index_factor.log) · 363 bytes · Source block 16.

### composite_order.log


[Extracted file: composite_order.log](files/composite_order.log) · 1,975 bytes · Source block 17.

### order21.log


[Extracted file: order21.log](files/order21.log) · 682 bytes · Source block 18.

### degree683.log


[Extracted file: degree683.log](files/degree683.log) · 2,011 bytes · Source block 19.

### rigorous683.log


[Extracted file: rigorous683.log](files/rigorous683.log) · 2,300 bytes · Source block 20.

### fullorder683.json


[Extracted file: fullorder683.json](files/fullorder683.json) · 17,970 bytes · Source block 21.

### fullorder907.json


[Extracted file: fullorder907.json](files/fullorder907.json) · 14,920 bytes · Source block 22.

### fullorder21_683.json


[Extracted file: fullorder21_683.json](files/fullorder21_683.json) · 339,097 bytes · Source block 23.

### fullorder21_907.json


[Extracted file: fullorder21_907.json](files/fullorder21_907.json) · 280,854 bytes · Source block 24.


