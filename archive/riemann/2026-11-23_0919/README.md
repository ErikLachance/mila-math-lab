# Riemann Proof Watch — checkpoint intermédiaire du 23 novembre 2026, 09 h 19 EST (America/New_York)

> **Historical research record / Archive de recherche.** Imported on 26 November 2026. Mathematical claims, source reports and test outcomes below describe the historical checkpoint. They have not all been independently audited or rerun during this import. No proof of RH is claimed.
> Private operational sections and scheduling metadata have been omitted. All embedded code, data and output blocks have been extracted byte-for-byte into linked files. Source scripts retain their historical paths and dependencies; they are not automatically executed.

**Source record:** `RIEMANN_CHECKPOINT_2026-11-23_0919_EST.md`. **Recorded time label:** 2026-11-23 09:19 EST (from the filename).

[Archive index](../../README.md) · [Manifest](../../manifest.json) · [Verification scope](../../README.md#what-was-checked-during-import)

## Continuité scientifique


Checkpoint Riemann antérieur : 2026-11-08 15:30:58 EST, positivité conditionnelle de la forme de Weil sur deux petits supports aux bords pour L=81/100, largeur 1/12, mais aucun résultat sur la totalité de l'intervalle ; borne de dimension négative au plus 14 non auditée de façon indépendante. Les derniers vrais travaux supplémentaires sont conservés dans les checkpoints `RIEMANN_CHECKPOINT_2026-11-23_0810_EST.md` et antérieurs, que cette exécution a **lus**. Ne pas recopier ni revendiquer comme nouveaux les travaux déjà présents : contrôles Mellin et xi, identités character-Fourier, tests H12 de fenêtre, prime auxiliary q/d, estimation de coût x/m+xm/k+m+k/n², somme diagonale de classes de carrés, etc.


## Sources effectivement consultées

- Michael O. Rubinstein et collaborateurs, *The Alpöge–Claude proof of the Riemann hypothesis explained for the Riemann zeta function*, v2, 22 Nov 2026, https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/zeta-paper_v2.pdf : sections III.1 (moyenne carrée, p. 63–65) et III.8 (frames, p. 136 et suivantes). Pages 61 et 136 inspectées en image du PDF. Le guide humain reconnaît que (M) et treize hypothèses de support H0–H12 n'y sont pas prouvées de façon autonome. Cela ne contredit pas les attestations de preuve formelle Lean.
- Andrew Sutherland (MIT), registre indépendant de vérification Lean, https://math.mit.edu/~drew/grh/ : auparavant consulté et réexaminé dans le contexte de cette exécution. Vérifications externes des 175 187 modules et des axiomes autorisés ; cette exécution n'a pas compilé l'archive.
- Levent Alpöge, note originelle, https://alpo.ge/remark.pdf ; déclarations du 20 Nov 2026 ; note déjà étudiée par étapes précédentes.
- Clay Mathematics Institute https://www.claymath.org/millennium/riemann-hypothesis/ : statut administratif à distinguer de la confiance dans la vérification formelle.

## Nouvelle passe A : borne générale du rang d'un frame après suppression de sous-espaces

Soient des applications linéaires complexes B_i:C^{d_i}->H=C^D, S=sum d_i, Q=sum B_i B_i*, e=(1/S)sum ||B_i*B_i-I||_HS², supposons e<1. Soient P_i les projecteurs orthogonaux des parties gardées des domaines, r=sum rank(I-P_i)<=alpha S, Q'=sum B_i P_i B_i*. Posons mu=trQ/D>0 et eta=tr(Q²)/(D mu²)-1>=0, delta=(alpha+sqrt(alpha e))/(1-sqrt e). Alors :
- tr Q>= (1-sqrt e)S par Cauchy-Schwarz ;
- tr(Q-Q')<=r+sqrt(r eS)<=S(alpha+sqrt(alpha e)) ;
- tr Q'>=(1-delta)trQ ; si delta<1, Cauchy sur valeurs propres et tr(Q'^2)<=tr Q² impliquent rank Q' >=D(1-delta)²/(1+eta).
Le caractère non commutatif ne gêne pas tr(Q'^2)<=tr Q², puisque tr((Q-Q')(Q+Q'))>=0 pour matrices positives, avec différence Q−Q' positive. Il ne faut pas interpréter rank >=... comme vérification de l'hypothèse arithmétique source LinkS/LinkR.

Script `/mnt/data/riemann_20261123_0908/deleted_frame_rank.py`, SHA256 `de0edb2013742d1b9570e561874a78fae8a26ac4b6f7eb1d6975ee0b7f22e4d6`. 1 200 matrices aléatoires, 808 delta<1, toutes PASS, écart minimal de rang moins borne ~0.287. Contre-exemple de crédulité : Q positif sur des blocs finis ne démontre pas l'existence ni la petite erreur de ces blocs dans le problème RH.

## Nouvelle passe B : renforcer par contrôle du noyau et donner un cas d'égalité

Soit K=ker Q', dim K=k et P_K son projecteur. Puisque Q' P_K=0, tr(P_K Q)=tr(P_K(Q−Q'))<=tr(Q−Q')<=delta trQ. Par Cauchy-Schwarz sur l'écart au scalaire mu I :
  tr(P_K Q) >= mu k -sqrt(k)||Q-mu I||_HS = mu[k-sqrt(eta D k)].
Avec t=k/D, on obtient `t-sqrt(eta*t)<=delta`, puis **t<=((sqrt eta +sqrt(eta+4 delta))/2)^2**. Cette borne peut améliorer la précédente quand eta est petit, **mais ne la domine pas uniformément** : utiliser le minimum des deux garanties, jamais dire 'toujours meilleure'. Elle est exactement atteinte pour eta=e=0 en prenant R copies d'une base orthonormée de C^D, supprimant les mêmes k coordonnées de chaque copie, d'où alpha=k/D et dim ker Q'=k. Ce dernier exemple prouve l'impossibilité d'une borne universelle avec un coefficient inférieur à 1 devant alpha dans ce cadre, sans hypothèses supplémentaires.

Script `/mnt/data/riemann_20261123_0908/frame_kernel_trace_bound.py`, SHA256 `32d3062a9231c80b53da8fb40bd330cb60dd97794c04a6d0b069b540d6e3192b` : 2 880 cas réels, 2 706 avec e<1, zéro échec ; dans 23 cas (sur 198 comparables) nouvelle borne plus forte, les autres non, confirmation de la non-dominance. Exact cas d'égalité par matrices entières Sympy pour D=2,3,8,17. Une attaque complémentaire vraiment complexe à sous-espaces gardés aléatoires : script `frame_complex_adversarial.py` SHA256 `3382965f01d59c37f76adb61a23d6475d4e9c57e1c936f644ffcd22e60622eac`, 1 600 cas hermitiens, tous Loewner & noyau PASS ; nouvelle borne plus forte dans 97 cas. Ces calculs en float64 sont des tests de falsification, pas les preuves des inégalités générales, fournies ci-dessus par des identités algébriques.

## Nouvelle passe C : famille de frames exactement serrées avec corrélations non nulles

Pour tout premier impair p, prendre la base canonique de C^p et les p bases de vecteurs v_{a,b}(x)=p^(-1/2) exp(2pi i (a x²+b x)/p), a,b,x modulo p. Dans chaque base a fixée, orthogonalité des caractères ; bases différentes mutuellement non biaisées avec |<v_{a,b},v_{a',b'}>|²=1/p par évaluation des sommes de Gauss (le carré de leur module se calcule en sommant l'écart h=x-y et en annulant les termes h≠0). Somme des projecteurs Q=(p+1)I ; donc eta=e=0 mais les corrélations inter-blocs sont **forcément non nulles** lorsque nombre total de vecteurs S=p(p+1)>D=p. Cas p=3,5,7,11,13, résidus flottants <1.5e-14, PASS. Script `mub_exact_frame.py` SHA256 `de66271b48c2b3a623ed547f7a0e5215cd4054ebd75a3d8e3e39421fc1c1e88c`. Ceci illustre les exigences de la condition 'general position' et invalide la stratégie naïve 'tous les vecteurs peuvent être orthogonaux'; ne prouve pas les relevés thêta.

## Nouvelle passe D : classe exceptionnelle de la moyenne quadratique des caractères

Dans Rubinstein III.1 p.64, pour des puissances de premiers n,n'<=Z et m0, prendre s la partie sans carré de nn' une fois retirés tous les premiers divisant m0. Alors s a nécessairement 0, 1 ou 2 facteurs premiers distincts : les exposants impairs viennent au plus des deux bases des deux puissances. Si s=n* est une classe exceptionnelle non triviale : soit n*=p avec une puissance impaire de p et l'autre terme 'neutre', soit n*=pr, p≠r avec deux puissances impaires ; trois facteurs distincts sont impossible. Posant sigma(p)=sum_{j:p^j<=Z} c_{p^j}, c=Lambda(n)min(1,y/n), et R=sum des termes neutres, on obtient respectivement contribution <=2 sigma(p) R<=6 log(y) R, et <=2 sigma(p)sigma(r)<=18 log(y)^2. Justification sigma(p)<=3log(y), y>=2 : pour p<=y, décomposer j jusqu'au plancher log_p y, tête <=log y et queue <=(p/(p-1))log p<=2log y ; pour p>y, somme totale <= y log p/(p-1)<=2log y. Ces bornes s'entendent pour poids **positifs** c ; pour |kappa|<=1 elles restent des majorants après triangle. Le terme s=1 (classes diagonales) avait déjà été étudié dans le backup de 08:10, ne pas prétendre le redémontrer comme découverte. Le contrôle nouveau porte seulement sur les exceptions s=n*.

Script `/mnt/data/riemann_20261123_0908/exceptional_squareclass_audit.py` SHA256 `118d4ba4bed2e8f5591270b62af8d392362ef7e61851da0616533cb64f4057b4` : 1 533 configurations finies (plus vérification structurelle de s sur chaque tableau), pour Z=25..800 et divers y,m0,s admissibles, **PASS**, ratio maximum charge/bornes ~0.3957. Aucun contrôle de la sommation non exceptionnelle par caractères, de l'existence des premiers auxiliaires, de la densité de zéros, ou de RH.

## Objections, limites, prochaines passes

- Toutes ces propositions de rang/exception restent des lemmes finis/algébriques, très éloignés des entrées analytiques, arithmétiques et cohomologiques H0–H12 nécessaires à (M). Aucune preuve personnelle globale de RH ni nouvelle vérification Lean indépendante.
- Le résultat extérieur de novembre a fait l'objet de vérifications formelles multiples ; l'exposition humaine v2 déclare ses treize hypothèses non prouvées dans CE GUIDE, ce qui n'est pas une réfutation du code Lean. L'hypothèse n'est pas à traiter comme une conjecture résolue par nos seuls tests.
- À éviter : extrapoler positivitité des compressions finies à tout l'espace, compter des essais float64 comme preuve, confondre l'erreur zéro du frame de toy avec les estimations des relevés thêta ; ne pas répéter les sept passes de 08:10.
- Prochaine piste à forte valeur : chercher une borne de concentration de frame directement sur la dimension du noyau (déjà amorcée) compatible avec le nombre de directions perdus aux niveaux premiers de la source ; déterminer exactement les paramètres eta,alpha,e0 dans (M) en vérifiant les quantificateurs. Autre piste : examiner les hypothèses (Q1–Q4) et le contrôle uniforme des caractères non exceptionnels, en priorité l'hypothèse inédite qui fait passer la classe exceptionnelle aux sommes uniformes, sans présupposer RH.


État scientifique : recherche partielle, aucun résultat global sur Riemann.
