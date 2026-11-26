# Riemann — checkpoint 25 novembre 2026, session 08:46 EST

> **Historical research record / Archive de recherche.** Imported on 26 November 2026. Mathematical claims, source reports and test outcomes below describe the historical checkpoint. They have not all been independently audited or rerun during this import. No proof of RH is claimed.
> Private operational sections and scheduling metadata have been omitted. All embedded code, data and output blocks have been extracted byte-for-byte into linked files. Source scripts retain their historical paths and dependencies; they are not automatically executed.

**Source record:** `RIEMANN_CHECKPOINT_2026-11-25_0846_EST.md`. **Recorded time label:** 2026-11-25 08:46 EST (from the filename).

[Archive index](../../README.md) · [Manifest](../../manifest.json) · [Verification scope](../../README.md#what-was-checked-during-import)


## 2. Sources effectivement consultées
- MIT, Andrew Sutherland, https://math.mit.edu/~drew/grh/ : état daté du 24 novembre 05:25 UTC, les vérifications par plusieurs noyaux et Comparator v4.33 positives; Comparator v4.36 en cours selon le rapport. Waterloo, Michael Rubinstein, https://math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/ : vérifications du 21 novembre réussies; le texte explicatif v2 est un brouillon réduisant (M) à treize hypothèses, pas leur preuve intégrale. Clay https://www.claymath.org/millennium/riemann-hypothesis/ affiche Active. Pas de compilation Lean personnelle ni de nouvelle preuve complète revendiquée.
- Andrew O'Desky, AGR.D103 https://andrewodesky.com/rh/lean/UpperTheory.V.Aut.AutomorphyUnramifiedCoefficientsAlt/ (conditions 1–4, finitude S0 et deux conditions d'automorphie), D096 https://andrewodesky.com/rh/lean/UpperTheory.V.U3.GG/ (accès direct échoué, accès via lien D103 réussi; définitions du groupe signé, idéal saturé et marquage, lignes18–67), AGR.1123 https://andrewodesky.com/rh/lean/UpperTheory.V.Z.J.oneCharU_of_katoTwoW_rig_admI_automorphy/ (conditions 1–4 du datum, rôle de H9 et distinction liste D). Catalogue non substitut à l'audit Lean brut; D096 en attente de revue. N=2 avec psi trivial, e=2, p=7 et K=Q(sqrt(-107)) satisfont les quatre conditions affichées, en utilisant h_K=3 du checkpoint 0815 et la disjonction K de Q(zeta7).
- Georges Gras https://arxiv.org/html/1709.06388v2, section1, p-rationalité et unités locales; référence du passage pro-p libre. Les calculs spécifiques ci-dessous sont nos dérivations conditionnelles, pas des théorèmes attribués à Gras ou aux vérificateurs.

## 3. Axe A — résolvante de degré 7 pour q=107 et réduction exacte
Entrées arithmétiques de 0815 : F=K Q(zeta7)^+, L=K(zeta7), Cl(L)[7^inf]=C7(theta), theta=eta omega², Cl(E)[7]=0 pour l'extension non ramifiée E/F de degré7, F 7-rationnel, G libre pro-7 rang4, la place à7 scindée. Ces assertions restent à auditer intégralement, sans GRH; les calculs suivants ne les présument pas pour les déterminants exacts mais en dépendent pour interprétation galoisienne.

N=749 dans le script cyclotomique (à distinguer du conducteur N=2 du datum), g=12, six cosets du groupe fixant L^+. Normaliser les exponents [4,1,0,2,5,6] de 0815 en [1,-2,-3,-1,2,3] puisque produit u_j=1. R_j=3^j mod7. Appliquer la construction de traces de b, b^7=alpha, du 0454 et LLL sur 243 vecteurs de traces de b prod(u_l^k_l) (k_l dans {-1,0,1}, dernier nul), utilisant LLL seulement pour sélectionner un élément entier explicite. Candidat retenu: -2 Tr(b u0^-1 u1^-1 u2 u3^-1 u4^-1)+Tr(b u0^-1 u2 u3^-1). Trace ici somme sur six conjugués. La borne entière des plongements, par trace exacte des puissances septièmes positives, est 1062. Borne coefficients 1523602291672735694208. CRT exact sur premiers 1499,68909,98869,107857,193243, puis contrôle indépendant 202231. Résolvante irréductible:

P = x^7 -819 x^5 -132370 x^4 +7939358 x^3 -67624354 x^2 +4300177441 x +57532485313.

Discriminant polynomial = -7^14 *107^3 *373599001^2 *47447980890086283233^2. Saturation par multiplicateurs du radical nilpotent mod p (algorithme 0619) : indices locaux à7 7,49,7,7; aux deux grands facteurs une division chacun; disc de l'ordre final = -2941328243 = -7^4*107^3, cohérent avec la ramification tame et le degré7 prévu. La primalité des deux grands facteurs a été testée par Sympy; pas de certificat indépendant pour le second >64 bits. Pour les unités il suffit d'un ordre entier et d'un norm ±1; on ne fonde pas le certificat des unités sur la seule maximalité annoncée. Changement de base exact et fermeture vérifiés par structure de multiplication. Pour compositum avec le cubique x³+x²−2x−1, saturation supplémentaire indice 117649=7^6 et discriminant -1246885456355149615796896680443, cohérent avec discriminant attendu. Temps mesuré du calcul des ordres 9.40 s.

Nouveau petit générateur choisi parmi 159 candidats primitifs 7-maximaux, polynôme de degré7 :

Psmall = x^7 -4 x^6 -3 x^5 -12 x^4 +8 x^3 -10 x^2 -7 x -8.

Indice dans l'ordre calculé 1016=8*127, premier à7; factorisation mod7 (x-1)(x²-x-3)^3. Changement de générateur exact donné dans riemann_smallgen_run11.json. Coefficients max 57532485313 → 12. Pas une affirmation d'optimalité de hauteur.

## 4. Axe B — unités et plongements locaux; e_loc non nul MAIS e8 nul
Dans le sous-corps de degré21, utiliser une base entière réduite par LLL. 442 candidats examinés, 29 passent les tests de norme modulo3,5,7,11,13, 19 éléments de norme ±1 certifiés exactement. Rang logarithmique archimédien heuristique 10, non 11; ce n'est pas une preuve de base fondamentale. Ce qui importe: rang EXACT 20 des orbites de leurs images locales dans W=F7^42. Les deux précisions 7^5 (10 chiffres uniformisants) et 7^7 (14 chiffres, autre choix de racine/générateur) donnent ce même rang. Les deux triples de racines multiples se séparent par translation et division par pi³. Localement pi=2-(zeta7+zeta7^-1), pi³=7pi²−14pi+7, t²=-107, e=3,f=2, résidu F49. Pour unités, log(u^48) modulo pi^4 se réduit aux trois premiers termes (les termes de degré >=4 ont valuation >=4, y compris h^7/7 de valuation >=4). Dénominateurs rationnels du changement de base contrôlés avec au plus un facteur7; précision suffisante vérifiée par deuxième calcul. Choix de signe de Frobenius ou de réciprocité ne modifie pas dichotomie.

Sous l'identification de la réciprocité globale 0815, U=image des unités, Hbar=W/U dimension22. Rangs exacts de U+D^i W = 38,35,32,29,26,23,20 pour i=1..7, D=log(S), S décalage des sept places. Deux certificats bruts V,G; Gauss-Jordan mod7 et covariance, six choix de générateur et sept places chacun, donc 84 configurations. Les 84 donnent c non nul et e_loc non nul; les 84 donnent e8=0. Une première assertion héritée du cas -79 imposant e8 non nul a ÉCHOUÉ; elle a été remplacée par la vérification de l'équation exacte et de la valeur, pas par une autre hypothèse. Dans la normalisation cert1, k=1, place0:

u3 = 3 X0 + 3 D y1 + 2 D² y5 + 6 D⁴ y6,
u2 = 2 D² y1 + D⁵ y6,
u4 = 4 D⁴ y1 + 2 D y6 + 3 D⁵ y5,
u1=y1, u5=y5, u6=y6.

Ici les indices 1..6 sont les valeurs des caractères sur delta, theta=3, eta=6, beta=5. Dans M3: c=3, e_loc=2. Dans M4: e8=0. Les expansions complètes des six lignes vérifiées exactement dans les 84 cas, avec le poids de chaque coefficient. Cette expérience est un VRAI contre-exemple arithmétique à l'extrapolation de la non-nullité de e8 de -79 vers -107, sous l'identification Kummer/reciprocity, pas un contre-exemple à H9. Le coefficient e_loc exclut la ramification précoce j<5r sous l'argument précédent, mais l'obstruction ordre8 n'exclut PAS j=5r pour -107. Ne pas annoncer finitude de S0 pour -107.

Contrôle indépendant du h_F pour q107: Bernoulli impairs exacts -321/107, (1498z-5992)/749, (-1498z-7490)/749 avec z²+z+1=0; produit -252. h_F=63 ou126 selon indice de Hasse 1 ou2; v7=1 dans les deux cas. Le même argument de valuation à107 que pour -79 donne indice1, donc h_F=63. La classe miroir et la partie réelle s'appuient sur 0815, non revérifiées complètement ici.

## 5. Axe C — la donnée abélienne complète ne ferme pas j5: modèle de jets
X=a E31+b(E12+E23), V=E13, a,b non nuls. Dans branche j=5r, les y1,y6 ont image triviale selon argument de relèvement fixe C3 du 0259. Alors seule relation active u3 est c log(A^7)+e_loc D² log B; u2=0 dans l'image abélienne, u4=3D^5 log B dans la normalisation ci-dessus. Pour le test r=1,a=b=1, choisir c=3,e_loc=2 et v=6=c/(2 e_loc) dans F7. Test exact sur k[t]/t^11 et k[t]/t^12. A=I+tX avec B supérieur, coefficients libres de degrés6 et suivants: système LINÉAIRE pour log B, inconsistent dans ces deux jets, mais ce n'est qu'un A fixé, pas exclusion générale. Avec A= sum_{i=0}^6 (tX)^i/i!, B=I+6t^5 V, le système est consistant, aucune correction de B requise. Rangs9 puis12, vérification directe des contraintes et inverses. Résultats non nuls:

u3 -> t^7(E12+E23), u4 -> t^10(E12-E23), u2 -> 0, y5 -> 6t^5 V.

Ces images sont supérieures strictes; à ordre10 tous les générateurs de H commutent et sont d'exposant divisant7. À ordre11 les commutateurs se trouvent dans la droite supérieure centrale t^11 V; après quotient par cette droite le même modèle reste valide pour la donnée abélienne. Le modèle ne prétend PAS respecter le marquage, les relations de Delta, ni les relèvements non abéliens réels de l'inertie. Il prouve uniquement que les contraintes linéaires abéliennes utilisées ici ne suffisent pas pour exclure ce jet, même avec tous les coefficients. Identités exactes ad_X^j(V): j=2 -> ab(E12+E23)-2a² E31; j=3 ->3a²b(E32-E21); j=5 ->9a²b³(E12-E23). Donc le nouveau coefficient de u4 est non nul mais mène à des entrées SUPÉRIEURES, pas à une contradiction d'ordre10. Ne pas appeler le modèle une représentation du groupe de Galois local/global.

## 6. Axe D — véritable classe de Frobenius dans Hbar
Chercher élément de norme pure puissance de7 du petit corps (degré7), dont réduction au premier simple de Psmall est nulle mais non aux deux autres racines dans F49. 23 candidats filtrés examinés; trouvé alpha_small = (-94 -219 x -327 x² -505 x³ -266 x⁴ -75 x⁵ +30 x⁶)/254. Résultant exact avec Psmall = -7; valuations locales 3 au slot fixe et 0 aux six autres, certifiées par les évaluations. Aucun besoin de supposer une principalisation via GRH. Premier export JSON échoué (entier Sympy non sérialisable), corrigé en int et calcul refait. Le premier simple du corps de degré7 est de complétion Q7; 7 a valuation3 dans le corps local de degré6, donc classe de 7 représente 3 fois un Frobenius normalisé, éventuellement inverse selon réciprocité. Réciprocité globale: classe du 7 au slot0 = moins la somme des classes unitaires alpha_small/7 au slot0 et alpha_small ailleurs. Les 2401 quadruplets de coefficients dans la base y1,D^6y1,D³y6,Dy5 testés exactement par projection duale annihilant U. Une solution unique. Pour cert1 (PREC5, LIFT10, ROOT_CHOICE0) coefficients (0,2,6,4); pour cert2 (PREC7, LIFT14, ROOT_CHOICE2), (0,2,6,2). La non-nullité du coefficient Dy5 est reproduite. Dans la branche j5, la classe de 7 induirait donc une diagonale non nulle au degré6r, proportionnelle à ad_X V=diag(-a,0,a). Ceci est compatible avec un Frobenius supérieur diagonal; ce n'est PAS une exclusion de j5. Donnée arithmétique utile pour tester les commutateurs locaux à l'ordre suivant. Les valeurs normalisées dépendent des choix de générateur.

## 7. Axe E — limite précise du passage par le quotient de Frattini
Dans le modèle exponentiel, poser U1=[X,V], U2=[X,U1]. Identités symboliques exactes: [V,U1]=2a V; [V,U2]=2a U1; [X^7,V]=(ab²)^2 U1. Premier essai avait un a de trop dans la deuxième identité, assertion échouée, corrigée. Les conjugués B_i ont logarithmes t^5 vV+i t^6 vU1+i²/2 t^7 vU2+...; le commutateur [B_i,B_j] a aux degrés11,12 dans ce modèle (j-i)v²[V,U1], (j²-i²)v²/2 [V,U2]. Le choix des paires (0,1),(0,2) donne deux coefficients linéairement indépendants dans les directions t^11 V et t^12 U1; vérification exacte 216 triples a,b,v non nuls, déterminant non nul. À degré12, [A^7,B] donne aussi une diagonale non nulle. Donc le quotient par les commutateurs, qui suffisait aux ordres précédents, peut perdre une information DIAGONALE à degré12. Le coefficient abélien ne contrôle pas les corrections de relèvement des unités locales dans H. Une contradiction déduite uniquement d'un calcul abélien à cet ordre serait non justifiée. Priorité : calculer la localisation dans un quotient de classe 2 de H, en particulier les coefficients de [B_i,B_j] et [x^7,B] des relèvements locaux de u2,u3,u4 et du Frobenius, puis imposer la triangularité et les caractères. Les matrices modèles et leurs commutateurs sont des diagnostics, non des relèvements galoisiens réels. À défaut de données non abéliennes, basculer vers les discriminants -683 et -907 pour tester les non-nullités sans prétendre généraliser.

## 8. Bilan, limites, prochaines expériences
Six axes substantifs: résolvante et ordre; unités/plongements; expansions complètes et contre-exemple à généralisation e8; jets; classe de Frobenius; premières directions non abéliennes. Nouveau résultat le plus important: q107 donne e_loc non nul et e8 nul, contrairement à q79; le calcul complet de rang a été effectué, pas supposé. La généralisation de la finitude à -107 ne peut donc PAS être annoncée. Il reste le quotient non abélien, l'audit des hypothèses de classe, de la présentation et du Lean brut. Aucune nouvelle preuve de RH, aucune réfutation de H9. Le travail reproductible et les erreurs corrigées sont reproduits ci-dessous.

## 9. Scripts, résultats et données reproductibles
Recréer /mnt/data/riemann_0846, y placer les scripts ci-dessous; exécuter degree7.py, order107.py, units107.py, smallgen107.py, embed107.py (PREC5 LIFT10 ROOT_CHOICE0; sauvegarder cert1), puis PREC=7 LIFT=14 ROOT_CHOICE=2 embed107.py (cert2), full107.py, frob107.py, frob_embed107.py aux deux précisions. Les scripts utilisent Sympy, Numpy, mpmath. order107.py contient P explicite; les fichiers JSON bruts sont donnés pour vérification de rang indépendante sans refaire LLL. Le script jet107.py contient un assert redondant d'égalité à soi-même, non compté comme vérification; jet107_order11.py l'enlève. La preuve de commutativité/exposant et de contraintes est ailleurs dans ces scripts. Le script full107.py contient le contrôle indépendant des expansions complètes; son rapport peut être reproduit au lieu d'inclure 72Ko redondants. Les sorties order et smallgen volumineuses sont reproductibles, seules les lignes principales sont répliquées ici.

### degree7.py


[Extracted file: degree7.py](files/degree7.py) · 4,301 bytes · Source block 1.

### order107.py


[Extracted file: order107.py](files/order107.py) · 3,007 bytes · Source block 2.

### units107.py


[Extracted file: units107.py](files/units107.py) · 3,132 bytes · Source block 3.

### smallgen107.py


[Extracted file: smallgen107.py](files/smallgen107.py) · 1,748 bytes · Source block 4.

### embed107.py


[Extracted file: embed107.py](files/embed107.py) · 6,227 bytes · Source block 5.

### full107.py


[Extracted file: full107.py](files/full107.py) · 5,179 bytes · Source block 6.

### jet107.py


[Extracted file: jet107.py](files/jet107.py) · 3,064 bytes · Source block 7.

### jet107_order11.py


[Extracted file: jet107_order11.py](files/jet107_order11.py) · 3,067 bytes · Source block 8.

### frob107.py


[Extracted file: frob107.py](files/frob107.py) · 2,078 bytes · Source block 9.

### frob_embed107.py


[Extracted file: frob_embed107.py](files/frob_embed107.py) · 1,358 bytes · Source block 10.

### brackets107.py


[Extracted file: brackets107.py](files/brackets107.py) · 769 bytes · Source block 11.

### degree7.log


[Extracted file: degree7.log](files/degree7.log) · 1,078 bytes · Source block 12.

### units107.log


[Extracted file: units107.log](files/units107.log) · 1,788 bytes · Source block 13.

### embed107.log


[Extracted file: embed107.log](files/embed107.log) · 644 bytes · Source block 14.

### embed107_verify.log


[Extracted file: embed107_verify.log](files/embed107_verify.log) · 704 bytes · Source block 15.

### full107.log


[Extracted file: full107.log](files/full107.log) · 359 bytes · Source block 16.

### jet107.log


[Extracted file: jet107.log](files/jet107.log) · 183 bytes · Source block 17.

### jet107_order11.log


[Extracted file: jet107_order11.log](files/jet107_order11.log) · 185 bytes · Source block 18.

### frob107.log


[Extracted file: frob107.log](files/frob107.log) · 797 bytes · Source block 19.

### frob_embed107.log


[Extracted file: frob_embed107.log](files/frob_embed107.log) · 904 bytes · Source block 20.

### frob_embed107_low.log


[Extracted file: frob_embed107_low.log](files/frob_embed107_low.log) · 844 bytes · Source block 21.

### brackets107.log


[Extracted file: brackets107.log](files/brackets107.log) · 241 bytes · Source block 22.

### cert1.json


[Extracted file: cert1.json](files/cert1.json) · 2,975 bytes · Source block 23.

### cert2.json


[Extracted file: cert2.json](files/cert2.json) · 2,975 bytes · Source block 24.

### riemann_smallgen_run11.json


[Extracted file: riemann_smallgen_run11.json](files/riemann_smallgen_run11.json) · 806 bytes · Source block 25.

### frob_element.json


[Extracted file: frob_element.json](files/frob_element.json) · 110 bytes · Source block 26.

### frob_cert_low.json


[Extracted file: frob_cert_low.json](files/frob_cert_low.json) · 171 bytes · Source block 27.

### frob_cert_high.json


[Extracted file: frob_cert_high.json](files/frob_cert_high.json) · 171 bytes · Source block 28.

### Données unités (matrices de multiplication régénérables)


[Extracted file: block-029.json](files/block-029.json) · 26,722 bytes · Source block 29.

### Expansions normalisées, place fixe, deux précisions (les 84 sont reproductibles)


[Extracted file: block-030.json](files/block-030.json) · 6,975 bytes · Source block 30.


