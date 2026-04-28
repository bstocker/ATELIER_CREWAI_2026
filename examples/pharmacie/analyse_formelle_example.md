# Fiche du processus formel — Circuit Pharmacie Hospitalière

## 1. Présentation générale

### Objectif du circuit
Le circuit pharmacie vise à assurer la gestion structurée du référentiel pharmaceutique, des mouvements de stock, des commandes internes, de la dispensation et de l'inventaire au sein de l'établissement hospitalier.

### Périmètre
Le processus couvre six domaines fonctionnels :
1. Gestion du référentiel (paramétrage des articles, fournisseurs, magasins, familles produits)
2. Gestion des mouvements de stock (réception, sortie de quarantaine, sortie en distribution)
3. Gestion des commandes internes
4. Dispensation (dotation et dispensation selon différents modes : par boîte, par unité, combiné)
5. Gestion des inventaires
6. Gestion des droits d'accès aux magasins

### Principaux acteurs impliqués
Le document formel fourni ne spécifie pas explicitement les acteurs responsables de chaque action. Les rôles attendus (pharmaciens, préparateurs, soignants) ne sont pas détaillés dans le document.

### Systèmes SIH concernés
- **Système d'information pharmaceutique principal** (non nommé explicitement, mais référencé implicitement)
- **SAGE** : système de gestion comptable/financière avec lequel un interfaçage est possible (les procédures PH13 et PH14 mentionnent explicitement « sans interfaçage SAGE »)

---

## 2. Sous-processus et étapes formelles

### 2.1. Sous-processus 1 : RÉFÉRENTIEL (Paramétrage)

| N° étape | Intitulé de l'étape | Acteur responsable | Action prescrite | Outil / écran SIH | Règle ou validation requise |
|----------|--------------------|--------------------|------------------|-------------------|-------------------------------|
| PH1 | Paramétrer un article avec la catégorie dispositif médical | Non spécifié | Créer/configurer un article en tant que dispositif médical dans le référentiel | SIH pharmacie | Classification correcte en tant que DMI |
| PH2 | Paramétrer un article avec la catégorie médicament | Non spécifié | Créer/configurer un article en tant que médicament dans le référentiel | SIH pharmacie | Classification correcte en tant que médicament |
| PH3 | Paramétrer un article DMI | Non spécifié | Créer/configurer les caractéristiques spécifiques d'un Dispositif Médical Implantable | SIH pharmacie | Conformité aux exigences de traçabilité DMI |
| PH4 | Paramétrer une DCI | Non spécifié | Enregistrer une Dénomination Commune Internationale | SIH pharmacie | Cohérence avec la nomenclature DCI officielle |
| PH5 | Paramétrer un fournisseur | Non spécifié | Enregistrer un fournisseur dans le référentiel | SIH pharmacie | Données complètes du fournisseur |
| PH6 | Paramétrer un type fournisseur | Non spécifié | Configurer les catégories/types de fournisseurs | SIH pharmacie | Classification appropriée |
| PH7 | Paramétrer une famille produit | Non spécifié | Créer une catégorie générique de produits | SIH pharmacie | Hiérarchie de classification cohérente |
| PH8 | Paramétrer une sous-famille produit | Non spécifié | Créer une sous-catégorie au sein d'une famille produit | SIH pharmacie | Hiérarchie de classification cohérente |
| PH9 | Paramétrer un magasin | Non spécifié | Configurer un emplacement/magasin de stockage de la pharmacie | SIH pharmacie | Identification unique du magasin |
| PH10 | Paramétrer un motif de retour | Non spécifié | Créer les motifs possibles pour les retours de stock | SIH pharmacie | Permet la traçabilité des retours |
| PH11 | Paramétrer une origine de livraison | Non spécifié | Configurer les origines possibles des livraisons | SIH pharmacie | Permet l'identification de la provenance |
| PH12 | Paramétrer un produit | Non spécifié | Configuration complète d'un article/produit pharmaceutique ou dispositif | SIH pharmacie | Référentiel complet et à jour |

---

### 2.2. Sous-processus 2 : MOUVEMENTS DE STOCK (Réception et sorties)

| N° étape | Intitulé de l'étape | Acteur responsable | Action prescrite | Outil / écran SIH | Règle ou validation requise |
|----------|--------------------|--------------------|------------------|-------------------|-------------------------------|
| PH13 | Ajouter une réception sans interfaçage SAGE | Préparateur ou pharmacien | Enregistrer une réception de marchandise sans synchronisation vers le système comptable SAGE | SIH pharmacie | Réception manuel, indépendant de SAGE |
| PH14 | Annuler une réception sans interfaçage SAGE | Pharmacien ou préparateur habilité | Annuler/supprimer un enregistrement de réception antérieur sans reflet sur SAGE | SIH pharmacie | Justification de l'annulation ; possibilité de suppression si la réception n'a pas généré de mouvements aval |
| PH15 | Extraire la liste des entrées | Préparateur ou pharmacien | Générer un rapport/export des mouvements d'entrée de stock sur une période donnée | SIH pharmacie | Traçabilité des mouvements d'approvisionnement |
| PH16 | Effectuer une sortie de la quarantaine | Préparateur | Transférer un article de l'état « quarantaine » (pré-réception, en attente de contrôle) vers un état disponible | SIH pharmacie | Contrôle qualité effectué ou dispensé préalablement |
| PH17 | Effectuer une sortie de la mise en distribution | Préparateur ou magasinier | Prélever un article du stock destiné à la mise en distribution vers les services ou unités de soins | SIH pharmacie | Stock disponible confirmé |
| PH18 | Annuler une sortie | Pharmacien ou préparateur autorisé | Annuler/reverser un mouvement de sortie de stock | SIH pharmacie | Justification ; article doit être disponible pour retour |
| PH19 | Extraire la liste des sorties | Préparateur ou pharmacien | Générer un rapport/export des mouvements de sortie de stock sur une période donnée | SIH pharmacie | Traçabilité des mouvements de distribution |

---

### 2.3. Sous-processus 3 : COMMANDE INTERNE (Demandes inter-services)

| N° étape | Intitulé de l'étape | Acteur responsable | Action prescrite | Outil / écran SIH | Règle ou validation requise |
|----------|--------------------|--------------------|------------------|-------------------|-------------------------------|
| PH20 | Ajouter une commande interne | Service clinique ou soignant | Créer une demande d'approvisionnement auprès de la pharmacie pour un article | SIH pharmacie | Article existant dans le référentiel ; quantité conforme aux stocks disponibles |
| PH21 | Traiter une commande interne | Pharmacien ou préparateur | Valider et exécuter la commande interne : préparation, dispensation et livraison au service demandeur | SIH pharmacie | Commande conforme ; stock suffisant ; traçabilité de la dispensation |

---

### 2.4. Sous-processus 4 : DISPENSATION (Dotation et dispensation)

| N° étape | Intitulé de l'étape | Acteur responsable | Action prescrite | Outil / écran SIH | Règle ou validation requise |
|----------|--------------------|--------------------|------------------|-------------------|-------------------------------|
| PH22 | Doter et dispenser par boîte | Préparateur | Dispenser la quantité demandée en unité de boîte complète | SIH pharmacie | Stock en boîte disponible ; traçabilité du mouvement |
| PH23 | Doter et dispenser par unité | Préparateur | Dispenser la quantité demandée en unités élémentaires (unités de prise, comprimés, ampoules, etc.) | SIH pharmacie | Stock en unités disponible ; traçabilité du mouvement |
| PH24 | Doter et dispenser par boîte et unité | Préparateur | Dispenser une combinaison de boîtes complètes et d'unités élémentaires pour satisfaire la commande | SIH pharmacie | Stock combiné disponible ; traçabilité du mouvement |
| PH25 | Doter et dispenser par boîte | Préparateur | (Redondant avec PH22 – Dispenser par boîte complète) | SIH pharmacie | Stock en boîte disponible ; traçabilité du mouvement |
| PH26 | Doter et dispenser par unité | Préparateur | (Redondant avec PH23 – Dispenser par unité élémentaire) | SIH pharmacie | Stock en unités disponible ; traçabilité du mouvement |
| PH27 | Doter et dispenser par boîte et unité | Préparateur | (Redondant avec PH24 – Dispenser par combinaison boîte + unité) | SIH pharmacie | Stock combiné disponible ; traçabilité du mouvement |
| PH28 | Doter et dispenser par boîte | Préparateur | (Redondant avec PH22 et PH25 – Dispenser par boîte complète) | SIH pharmacie | Stock en boîte disponible ; traçabilité du mouvement |
| PH29 | Doter et dispenser par unité | Préparateur | (Redondant avec PH23 et PH26 – Dispenser par unité élémentaire) | SIH pharmacie | Stock en unités disponible ; traçabilité du mouvement |
| PH30 | Doter et dispenser par boîte et unité | Préparateur | (Redondant avec PH24 et PH27 – Dispenser par combinaison boîte + unité) | SIH pharmacie | Stock combiné disponible ; traçabilité du mouvement |
| PH31 | Doter et dispenser par boîte | Préparateur | (Redondant avec PH22, PH25 et PH28 – Dispenser par boîte complète) | SIH pharmacie | Stock en boîte disponible ; traçabilité du mouvement |
| PH32 | Doter et dispenser par unité | Préparateur | (Redondant avec PH23, PH26 et PH29 – Dispenser par unité élémentaire) | SIH pharmacie | Stock en unités disponible ; traçabilité du mouvement |
| PH33 | Doter et dispenser par boîte et unité | Préparateur | (Redondant avec PH24, PH27 et PH30 – Dispenser par combinaison boîte + unité) | SIH pharmacie | Stock combiné disponible ; traçabilité du mouvement |

**Note importante** : Les étapes PH22 à PH33 présentent des redondances significatives. Les trois variantes (par boîte, par unité, par boîte et unité) sont répétées quatre fois chacune, sans différenciation explicite de contexte, d'acteur ou de règle de gestion.

---

### 2.5. Sous-processus 5 : INVENTAIRE (Décompte et contrôle de stock)

| N° étape | Intitulé de l'étape | Acteur responsable | Action prescrite | Outil / écran SIH | Règle ou validation requise |
|----------|--------------------|--------------------|------------------|-------------------|-------------------------------|
| PH34 | Ajouter un décompte | Préparateur ou magasinier | Enregistrer le résultat d'un décompte physique pour un article ou un lot d'articles | SIH pharmacie | Résultat précis du décompte physique ; articles identifiés |
| PH35 | Ajouter un inventaire global avec sélection multiple | Pharmacien | Procéder à un inventaire général de plusieurs articles/catégories via une sélection multiple ; consolider les écarts | SIH pharmacie | Tous les articles du périmètre sélectionné doivent être décomptés |
| PH36 | Ajouter un inventaire global avec sélection unique | Pharmacien | Procéder à un inventaire d'un seul article ou d'une seule catégorie ; enregistrer le résultat consolidé | SIH pharmacie | Article unique identifié de manière non ambiguë |

---

### 2.6. Sous-processus 6 : DROITS D'ACCÈS (Gouvernance des accès SIH)

| N° étape | Intitulé de l'étape | Acteur responsable | Action prescrite | Outil / écran SIH | Règle ou validation requise |
|----------|--------------------|--------------------|------------------|-------------------|-------------------------------|
| PH37 | Attribuer les droits d'accès aux magasins de la pharmacie | Administrateur système ou pharmacien superviseur | Configurer les profils d'accès utilisateur aux différents magasins/emplacements de la pharmacie | SIH pharmacie – Gestion des droits | Principe du moindre privilège ; traçabilité des attributions |

---

## 3. Obligations réglementaires

Le document formel fourni ne mentionne **explicitement** aucune obligation réglementaire détaillée. Cependant, certaines obligations sont implicitement attendues ou peuvent être inférées du contexte :

### Obligations mentionnées implicitement ou par allusion :

1. **Traçabilité des articles** :
   - Les étapes PH15, PH19 prévoient l'extraction de listes d'entrées et sorties, supposant une traçabilité des mouvements.
   - Les étapes PH34, PH35, PH36 (inventaire) suggèrent la nécessité d'une correspondance périodique entre stocks informatiques et physiques.

2. **Catégorisation réglementaire des articles** :
   - PH1 et PH2 distinguent les dispositifs médicaux des médicaments, indiquant une classification réglementaire attendue.
   - PH3 spécifie un paramétrage dédié aux Dispositifs Médicaux Implantables (DMI), qui ont des exigences de traçabilité particulières en France.

3. **Séparation des systèmes comptables** :
   - PH13 et PH14 mentionnent explicitement « sans interfaçage SAGE », suggérant que certains mouvements de stock doivent rester indépendants de la comptabilité, ce qui peut relever d'exigences de ségrégation des tâches ou de contrôle interne.

### Obligations **non précisées** dans le document :

Le document ne détaille **pas** :
- Les exigences de gestion des stupéfiants (registres, contrôles, signalement)
- Les règles de gestion des périmés (identification, destruction, documentation)
- Les critères des Bonnes Pratiques de Pharmacie Hospitalière (BPPH)
- Les conditions de stockage (température, humidité, conditions spéciales)
- Les délais légaux de traçabilité ou de conservation des enregistrements
- Les exigences de chaîne du froid
- Les règles de ségrégation entre stocks critiques et non critiques

---

## 4. Dépendances critiques

### 4.1. Dépendances séquentielles obligatoires

#### Cycle référentiel → mouvements de stock → dispensation :
1. **PH1-PH12 (Référentiel) doit précéder tout mouvement de stock** :
   - Avant d'enregistrer une réception (PH13), l'article doit être paramétré (PH2 pour médicaments, PH1 pour DMI, PH3 pour DMI spécifiques)
   - Avant d'effectuer une sortie (PH16, PH17), l'article doit exister dans le référentiel
   - Avant de dispenser (PH22-PH33), l'article doit être paramétré et le magasin configuré (PH9)

2. **Réception et sortie de quarantaine doivent précéder dispensation** :
   - PH13 (réception) crée un stock
   - PH16 (sortie de quarantaine) libère le stock pour utilisation
   - PH17 (sortie en distribution) ou PH22-PH33 (dispensation) peuvent alors intervenir
   - **L'ordre implicite est : PH13 → PH16 → PH17 ou PH22-PH33**

3. **Commande interne dépend du stock disponible** :
   - PH20 (ajouter commande) crée la demande
   - PH21 (traiter commande) valide la disponibilité du stock avant exécution
   - La dispensation (PH22-PH33) complète le traitement

#### Cycle inventaire :
4. **Inventaire dépend du décompte physique** :
   - PH34 (décompte) enregistre la réalité physique
   - PH35 ou PH36 (inventaire global) consolide et permet l'ajustement du stock informatique
   - **Condition bloquante** : les écarts doivent être expliqués ou justifiés avant validation (bien que le document ne le précise pas)

#### Cycle droits d'accès :
5. **PH37 (droits d'accès) doit précéder ou accompagner les accès aux magasins** :
   - Les utilisateurs doivent disposer des droits appropriés avant d'exécuter PH20, PH21, PH22-PH33, PH34-PH36

### 4.2. Validations bloquantes explicites

Le document formel spécifie **peu de validations bloquantes explicites**. Les validations attendues sont implicites :

- **Pour PH13 (réception)** : Article doit être référencé (PH2 ou PH1)
- **Pour PH16 (sortie quarantaine)** : Stock en quarantaine doit exister
- **Pour PH17 (sortie distribution)** : Stock en distribution doit exister
- **Pour PH20 (commande interne)** : Article doit exister dans le référentiel
- **Pour PH21 (traiter commande interne)** : Stock suffisant (implicite)
- **Pour PH22-PH33 (dispensation)** : Stock disponible (implicite)
- **Pour PH35 (inventaire multiple)** : Tous les articles du périmètre sélectionné doivent être décomptés

### 4.3. Dépendances de données

| Dépendance | Détail |
|-----------|--------|
| **Référentiel d'articles** | Tous les mouvements et dispensations reposent sur l'existence et la complétude du paramétrage (PH1-PH12) |
| **Classification réglementaire** | La distinction DMI/Médicament impacte les règles de traçabilité et de stockage |
| **Magasins paramétrés** | PH9 doit être exécuté avant d'assigner des droits (PH37) ou de faire des mouvements de stock |
| **Fournisseurs** | PH5 doit précéder le paramétrage des origines de livraison (PH11) et les réceptions |
| **Motifs de retour et origines** | PH10 et PH11 sont des préalables pour qualifier les réceptions et les retours |

---

## 5. Interfaces avec d'autres services

### 5.1. Interface avec les services cliniques (unités de soins)

**Type de flux** : Bidirectionnel asynchrone

- **Flux amont (services → pharmacie)** :
  - **PH20** : Les services cliniques créent des commandes internes (demande de médicaments, dispositifs, consommables)
  - **Nature de la demande** : Nominative (patient spécifique) ou globale (unité, stock tampon)
  - **Outil de transmission** : SIH pharmacie (écran de commande interne)
  - **Délai attendu** : Non spécifié dans le document

- **Flux aval (pharmacie → services)** :
  - **PH21, PH22-PH33** : La pharmacie prépare et dispense la commande
  - **PH17** : Sortie du stock en distribution vers les services
  - **Outil de transmission** : SIH pharmacie (confirmation de dispensation, bon de livraison implicite)
  - **Responsabilité du service** : Réception et signature (non documentée)

**Interface implicite non détaillée** :
- Le document ne précise pas comment les services formulent les demandes (formulaire papier, SIH, autre)
- Aucune mention de délai de livraison ou de traçabilité de la dispensation nominative
- Pas de spécification des critères d'acceptation/refus de commande

---

### 5.2. Interface avec la stérilisation

**Type de flux** : Non explicitement adressé dans le document

**Éléments implicites** :
- Les DMI (PH1, PH3) peuvent nécessiter une stérilisation avant distribution
- Les étapes PH16 (sortie quarantaine) pourraient correspondre à une libération post-stérilisation
- **Zone d'ombre** : Aucune procédure ne mentionne explicitement un cycle de stérilisation ou une interface avec un service de stérilisation

---

### 5.3. Interface avec la logistique/magasinage interne

**Type de flux** : Bidirectionnel intégré au SIH

- **Flux réception** :
  - **PH13** : Enregistrement de la réception de marchandise en provenance des fournisseurs
  - **Responsable implicite** : Magasinier ou préparateur
  - **Acteur logistique** : Reçoit la commande fournisseur, effectue la déchargement, transmet les documents à la pharmacie

- **Flux stockage et mouvement** :
  - **PH9** : Configuration des magasins (emplacements physiques)
  - **PH16, PH17** : Mouvements internes entre zones (quarantaine, mise en distribution)
  - **Responsable** : Magasinier ou préparateur pharmacie

- **Flux inventaire** :
  - **PH34, PH35, PH36** : Décompte physique régulier, impliquant le magasinier ou préparateur

**Interface implicite avec la logistique externe** (fournisseurs) :
- Pas de détail sur la commande fournisseur, le délai de livraison, ou la gestion des litiges de réception

---

### 5.4. Interface avec les fournisseurs externes

**Type de flux** : Sortant (commandes pharmacie → fournisseurs)

- **Étape implicite** : Commande aux fournisseurs (non documentée dans le processus formel, présente dans le référentiel via PH5, PH11)
- **Réception** : PH13 enregistre l'arrivée de la marchandise fournisseur
- **Traçabilité** : PH11 (paramétrage origine de livraison) permet l'identification du fournisseur pour chaque réception

**Absence de détail** :
- Aucune procédure de commande fournisseur n'est documentée
- Pas de critères de sélection fournisseur, délai de livraison, conditions de transport
- Pas de gestion explicite des retours fournisseur ou des litiges

---

### 5.5. Interface avec les organismes de contrôle ou d'inspection

**Éléments implicites** :
- Les étapes d'extraction (PH15, PH19) permettent de générer des preuves de traçabilité
- L'inventaire (PH34-PH36) documente la concordance stock informatique/physique
- **Zone d'ombre** : Aucune mention de rapports légaux, d'audits externes, ou d'obligations de communication aux autorités (ANSM, inspection pharmaceutique)

---

### 5.6. Interface avec le système comptable SAGE

**Type d'interface** : Conditionnel et explicitement exclu dans certains cas

- **Interfaçage désactivé** :
  - **PH13, PH14** : Réception et annulation de réception **« sans interfaçage SAGE »**
  - **Implication** : Ces mouvements de stock ne génèrent pas automatiquement d'écritures comptables
  - **Raison possible** : Séparation du contrôle d'accès (tâches séparation), ou mouvements internes non facturable

- **Interfaçage implicite ou absent** :
  - Les autres procédures (PH15-PH33, PH34-PH36) ne précisent pas si elles génèrent ou non des écritures SAGE
  - **Zone d'ombre** : Périmètre exact du synchronisation avec SAGE non clair

---

## 6. Points de vigilance formels

### 6.1. Points de vigilance réglementaires ou métier explicitement mentionnés

Le document formel fourni **ne mentionne explicitement aucun point de vigilance spécifique**.

### 6.2. Points de vigilance implicites ou inférables

Bien que non énoncés explicitement, les points de vigilance suivants peuvent être déduits de la structure du processus :

#### A. Gestion des deux modes de dispensation (boîte vs. unité)
- **Enjeu** : Les procédures PH22-PH33 prévoient trois variantes (boîte, unité, combinée)
- **Vigilance** : La dispensation par unité nécessite un contrôle de l'intégrité des unités et une traçabilité fine
- **Document formel** : Silencieux sur les critères de choix, les règles de conditionnement, ou les contrôles qualité à l'issue

#### B. Traçabilité des articles à haut risque
- **Enjeu** : Les DMI (PH3) et les médicaments (PH2) sont paramétrés différemment
- **Vigilance** : Les DMI nécessitent une traçabilité renforcée (lot, numéro de série, date limite)
- **Document formel** : Aucune règle de traçabilité DMI, de numérotage de lot, ou de gestion de rappels n'est spécifiée

#### C. Gestion de la quarantaine
- **Enjeu** : PH16 (sortie quarantaine) suggère qu'un article peut être bloqué après réception
- **Vigilance** : Le motif du blocage (contrôle qualité en cours, non-conformité) et les critères de libération ne sont pas documentés
- **Document formel** : Pas de procédure de contrôle qualité à la réception, pas de critères de conformité

#### D. Concordance stock informatique/physique
- **Enjeu** : PH34-PH36 (inventaire) permettent de détecter et corriger les écarts
- **Vigilance** : Les causes d'écart (vol, destruction, erreur saisie) et les actions correctives ne sont pas spécifiées
- **Document formel** : Pas de procédure de justification des écarts importants

#### E. Droits d'accès et séparation des tâches
- **Enjeu** : PH37 (attribution droits accès) est le seul contrôle d'accès documenté
- **Vigilance** : Absence de spécification des rôles (qui peut créer, valider, annuler des mouvements)
- **Document formel** : Aucune matrice de droits par rôle (pharmacien, préparateur, magasinier, soignant)

#### F. Absence d'interface explicite pour les stupéfiants
- **Enjeu** : La gestion des stupéfiants est une obligation légale majeure (registre, contrôles périodiques)
- **Vigilance** : Aucune procédure spécifique aux stupéfiants n'apparaît dans les étapes PH1-PH37
- **Implication** : Les stupéfiants sont traités comme des médicaments ordinaires (PH2), sans sur-contrôle documenté

#### G. Absence de gestion explicite des périmés
- **Enjeu** : La gestion des médicaments périmés est une obligation légale (destruction documentée)
- **Vigilance** : Aucune procédure d'identification des périmés, de retrait du stock, ou de destruction n'est mentionnée
- **Implication** : L'inventaire (PH34-PH36) doit permettre de détecter les périmés, mais le traitement reste flou

#### H. Absence de gestion des retours clients (services)
- **Enjeu** : Les services peuvent retourner des articles (non consommé, périmé, hors du protocole)
- **Vigilance** : PH10 paramètre un « motif de retour », mais aucune procédure de traitement de retour n'est documentée
- **Implication** : La procédure d'annulation (PH18) peut être utilisée, mais les critères ne sont pas clairs

#### I. Gestion de l'interfaçage SAGE
- **Enjeu** : PH13 et PH14 excluent explicitement l'interfaçage SAGE
- **Vigilance** : Les mouvements non interfacés peuvent entraîner une divergence entre stock informatique (SIH pharmacie) et comptabilité (SAGE)
- **Implication** : Les inventaires réguliers (PH34-PH36) doivent servir à rapprocher les deux systèmes

---

## 7. Zones d'ombre et incohérences du formel

### 7.1. Incohérences dans le document

#### **INCOHÉRENCE 1 : Redondance des procédures de dispensation (PH22-PH33)**

| Procédure | Objet déclaré |
|-----------|---------------|
| PH22, PH25, PH28, PH31 | Doter et dispenser par boîte |
| PH23, PH26, PH29, PH32 | Doter et dispenser par unité |
| PH24, PH27, PH30, PH33 | Doter et dispenser par boîte et unité |

**Constat** :
- Les trois variantes (boîte, unité, combiné) sont répétées **quatre fois** sans aucune différenciation.
- Aucune explication sur les raisons de cette répétition.
- **Hypothèse plausible non confirmée** : Peut-être correspond-il à différents contextes (dispensation nominative, dispensation globale, dispensation d'urgence, dotation de service) ?

**Implication** :
- **Impossible de savoir quelle procédure appliquer dans quel contexte**.
- Risque de confusion ou d'application incohérente par les utilisateurs.

---

#### **INCOHÉRENCE 2 : Absence de distinction entre "dotation" et "dispensation"**

Le titre commun est « Doter et dispenser », mais :
- **Dotation** généralement = dotation initiale d'un service (stock tampon, armoire de soins)
- **Dispensation** = remise nominative au soignant pour un patient spécifique

**Constat** :
- Les procédures PH22-PH33 ne précisent pas si elles couvrent dotation seule, dispensation seule, ou les deux.
- Aucune mention de différence de traçabilité (dispensation nominative nécessite une identification patient).

**Implication** :
- **Impossible de vérifier la conformité avec les bonnes pratiques de dispensation** (traçabilité nominative exigée).

---

### 7.2. Zones d'ombre — Informations manquantes, indispensables mais absentes

#### **ZONE D'OMBRE 1 : Acteurs responsables non spécifiés**

Pour presque toutes les procédures, le document indique « Non spécifié ».

**Exemples** :
- Qui crée un paramétraqe article ? (PH1-PH4) → Pharmacien ? Administrateur ? Gestionnaire référentiel ?
- Qui valide une réception ? (PH13) → Pharmacien ? Préparateur ? Contrôleur qualité ?
- Qui autorise une annulation de sortie ? (PH18) → Pharmacien seul ? Deux pharmaciens ? Chef de service ?

**Implication** :
- **Impossible de déterminer qui est responsable de quoi**.
- Risque de dysfonctionnement (personne inexistante assignée, ou responsabilité partagée non claire).

---

#### **ZONE D'OMBRE 2 : Règles de gestion des stocks non documentées**

**Absence de spécification pour** :
- **Stocks de sécurité minimum** : À partir de quel seuil un article doit-il être commandé aux fournisseurs ?
- **Niveaux d'alerte** : Quel événement doit déclencher une alerte (stock critique, périmé en approche) ?
- **Stratégie de prélèvement** : FIFO (First In, First Out) ? FEFO (First Expired, First Out) pour les périmés ? Autre ?
- **Gestion multi-lot** : Si un article existe en plusieurs lots, lequel est prélevé lors de PH17 ou PH22-PH33 ?

**Implication** :
- **Impossibilité de planifier les approvisionnements** ou de prévenir les ruptures de stock.
- **Risque de distribution accidentelle de produits périmés**.

---

#### **ZONE D'OMBRE 3 : Cycle de contrôle qualité à la réception**

**Absence de spécification pour** :
- **Quand et comment effectuer le contrôle qualité** (vérification colis, intégrité, conformité commande) ?
- **Qui l'effectue** ? Préparateur ? Pharmacien ? Tiers ?
- **Quels sont les critères d'acceptation** ?
- **Que se passe-t-il en cas de non-conformité** ? (renvoi au fournisseur ? destruction ? quarantaine définitive ?)

**Implication** :
- PH16 (« sortie de quarantaine ») suggère une quarantaine post-réception, mais **le processus de libération est flou**.

---

#### **ZONE D'OMBRE 4 : Traçabilité des mouvements et audit trail**

**Absence de spécification pour** :
- **Qui a effectué le mouvement** ? (utilisateur identiflé dans le SIH ?)
- **Quand** ? (date, heure ?)
- **Pour quel motif** ? (raison de l'annulation, par exemple ?)
- **Immuabilité des enregistrements** : Peut-on supprimer ou modifier un mouvement après validation ?

**Implication** :
- **Traçabilité incomplète, incompatible avec les exigences réglementaires** (BPPH, article L5143-8 du CSP).

---

#### **ZONE D'OMBRE 5 : Gestion des stupéfiants**

**Absence totale de procédure dédiée** pour :
- **Enregistrement spécifique des stupéfiants** (registre spécial exigé par l'arrêté du 6 avril 2011)
- **Contrôles périodiques** (réconciliation mensuelle/annuelle)
- **Destruction documentée** (PV de destruction)
- **Pertes déclarables** (notification exigée)

**Constat** :
- Les stupéfiants sont traités comme des médicaments ordinaires (PH2), sans sur-contrôle.

**Implication** :
- **Non-conformité réglementaire potentielle** aux exigences du décret 2006-922 et de l'arrêté du 6 avril 2011.

---

#### **ZONE D'OMBRE 6 : Gestion des périmés**

**Absence de procédure** pour :
- **Identification des périmés** : Qui et comment marque-t-on un article comme périmé ?
- **Retrait du stock** : Quand et comment un périmé est-il retiré de la circulation ?
- **Destruction** : Procédure de destruction, documentation, témoins ?
- **Notification légale** : Doit-on déclarer la destruction à une autorité ?

**Constat** :
- L'inventaire (PH34-PH36) peut déterminer des écarts, mais ne spécifie pas l'action pour les périmés.

**Implication** :
- **Risque de distribution accidentelle de produits périmés**.

---

#### **ZONE D'OMBRE 7 : Gestion des Dispositifs Médicaux Implantables (DMI)**

**Absence de spécification pour** :
- **Traçabilité DMI** : Numérotation de série ? Lot ? Date limite ? Qui enregistre ?
- **Implantation documentée** : Qui récupère et archive les données d'implantation (patient, acte, numéro de série) ?
- **Gestion des rappels DMI** : Procédure en cas de rappel fournisseur ?
- **Différence avec DMI simple** : PH1 (DMI) et PH3 (DMI spécifique) ne sont pas clarifiés.

**Constat** :
- PH3 mentionne « paramétrage article DMI », mais aucune procédure ne détaille les exigences de traçabilité.

**Implication** :
- **Impossibilité de respecter la traçabilité DMI** exigée par la directive 2017/745 (RGMDI) et l'arrêté du 6 avril 2011.

---

#### **ZONE D'OMBRE 8 : Interface avec les services cliniques**

**Absence de spécification pour** :
- **Format de la commande interne** (PH20) : Comment le service demande-t-il ? (écran SIH ? formulaire papier ? appel ?)
- **Traçabilité nominative** : La commande identifie-t-elle le patient ? Le prescripteur ? La pathologie ?
- **Délai de livraison** : Service d'urgence ? Standard ? Délai accepté ?
- **Circuit de livraison** : Qui livre ? Qui signe ? Traçabilité de signature ?

**Constat** :
- PH20 et PH21 traitent la commande interne, mais le flux amont (formulation) et aval (livraison) ne sont pas documentés.

**Implication** :
- **Impossibilité de garantir une traçabilité nominative de bout en bout** (exigée pour certains articles, notamment stupéfiants ou anticalculeux).

---

#### **ZONE D'OMBRE 9 : Interfaçage SAGE et rapprochement comptable**

**Constat** :
- PH13 et PH14 excluent explicitement l'interfaçage SAGE.
- Les autres procédures ne précisent pas si elles génèrent des écritures comptables ou non.

**Questions non répondues** :
- Comment rapprocher le stock informatique (SIH pharmacie) et le stock comptable (SAGE) si les réceptions ne sont pas interfacées ?
- Qui est responsable du rapprochement ?
- Quelle est la fréquence et le processus ?

**Implication** :
- **Risque de divergence permanente entre SIH et SAGE** → contrôle comptable défaillant.

---

#### **ZONE D'OMBRE 10 : Gestion des retours clients**

**Constat** :
- PH10 paramètre un « motif de retour ».
- PH18 permet « l'annulation d'une sortie ».
- Aucune procédure dédiée aux retours de services.

**Questions non répondues** :
- Un service peut-il retourner un article ? Sur quelles bases (date limite approchante, non-utilisation, rupture de protocole) ?
- Quelle est la procédure ? (PH18 ? autre ?)
- Que devient l'article retourné ? (réintégré au stock ? détruit ?)
- Comment justifier le retour (bon de retour ?) ?

**Implication** :
- **Flou sur la gestion des retours** → risque de perte de traçabilité ou de mauvais enregistrement comptable.

---

### 7.3. Autres incohérences ou points flous

#### **INCOHÉRENCE 3 : Confusion entre "mouvements de stock" et "dispensation"**

**Constat** :
- **Mouvements de stock** (PH13-PH19) : Réception, quarantaine, distribution (échanges entre zones d'entreposage)
- **Dispensation** (PH20-PH33) : Commande interne et satisfaction de la commande

**Flou** :
- PH17 (« sortie de mise en distribution ») et PH22-PH33 (« doter et dispenser ») semblent être deux étapes du même flux logistique.
- **Quelle est la différence** ? Est-ce que PH17 = mouvement interne vers zone de préparation, et PH22-PH33 = préparation et remise au service ?

**Implication** :
- **Processus peu clair pour l'utilisateur** → risque d'application incohérente.

---

#### **INCOHÉRENCE 4 : Absence de lien entre "commande interne" et "dispensation"**

**Constat** :
- PH20 : « Ajouter une commande interne » (crée la demande)
- PH21 : « Traiter une commande interne » (valide et exécute)
- PH22-PH33 : « Doter et dispenser » (détails d'exécution ?)

**Flou** :
- **PH21 appelle-t-il PH22-PH33 en sous-routine** ? Ou sont-ce des processus parallèles ?
- **La dispensation effective (PH22-PH33) est-elle obligatoire après PH21** ?

**Implication** :
- **Dépendances de processus mal formalisées** → risque de commandes ouvertes non exécutées.

---

#### **INCOHÉRENCE 5 : Paramétrage (PH1-PH12) vs. Mouvements (PH13-PH19)**

**Constat** :
- PH1-PH12 paramètrent le référentiel (article, fournisseur, magasin, etc.).
- PH13-PH19 effectuent des mouvements de stock.

**Question** :
- **Avant d'effectuer PH13 (réception), quels paramétrages (PH1-PH12) sont obligatoires** ?
- L'article doit-il être paramétré (PH2) avant la réception ? Ou peut-il être créé lors de la réception ?
- Le fournisseur doit-il être préalablement paramétré (PH5) ?

**Implication** :
- **Dépendances mal formalisées** → risque de commencer un mouvement sans pré-requis satisfait.

---

### 7.4. Résumé des zones d'ombre critiques

| Zone d'ombre | Criticité | Implication |
|-------------|-----------|------------|
| Acteurs non spécifiés | **CRITIQUE** | Responsabilités floues, risque de non-exécution |
| Stupéfiants : pas de procédure dédiée | **CRITIQUE** | Non-conformité réglementaire |
| Périmés : pas de processus documenté | **CRITIQUE** | Risque de distribution accidentelle |
| DMI : traçabilité incomplète | **HAUTE** | Non-conformité RGMDI |
| Inventaire : absence de procédure de justification écarts | **HAUTE** | Contrôle qualité défaillant |
| Interface services cliniques : flux amont/aval flou | **HAUTE** | Traçabilité nominative incertaine |
| Interfaçage SAGE : processus de rapprochement absent | **MOYENNE** | Risque divergence comptable |
| Redondances PH22-PH33 : contextes non clarifiés | **MOYENNE** | Confusion d'utilisation |
| Contrôle qualité réception : critique ou optionnel ? | **HAUTE** | Intégrité des produits incertaine |

---

## Conclusion synthétique

Le processus formel fourni décrit une **structure générale du circuit pharmacie** en 37 procédures regroupées en 6 catégories fonctionnelles (référentiel, mouvements de stock, commande interne, dispensation, inventaire, droits d'accès).

**Points forts du document** :
- Couverture des principaux domaines fonctionnels
- Identification des systèmes SIH (pharmacie, SAGE)
- Mention explicite de catégories réglementaires (DMI, médicaments)

**Points faibles majeurs** :
- **Très peu de détails sur les règles de gestion applicables** : seuils de stock, critères de conformité, motifs de blocage/libération
- **Acteurs responsables non spécifiés** : impossible de déterminer qui fait quoi
- **Obligations réglementaires majeures absentes** : stupéfiants, périmés, traçabilité DMI, BPPH
- **Procédures redondantes sans contexte** : PH22-PH33 répètent trois variantes quatre fois sans explication
- **Interfaces externes mal documentées** : fournisseurs, services cliniques, stérilisation
- **Absence de traçabilité formalisée** : audit trail, identifiant utilisateur, horodatage, motifs

**Statut de conformité réglementaire** :
Le document formel seul **ne suffit pas à garantir une conformité** aux exigences de la BPPH, de l'arrêté du 6 avril 2011, ou des directives sur traçabilité DMI et gestion des stupéfiants. Des procédures complémentaires seraient nécessaires pour couvrir ces exigences explicitement.