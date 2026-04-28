# Fiche du processus formel — Bloc Opératoire

## 1. Présentation générale

### Objectif et périmètre
Le processus formel bloc opératoire couvre l'ensemble du parcours patient de la pré-hospitalisation à la clôture administrative post-intervention. Il englobe 28 étapes formelles couvrant :
- **Pré-hospitalisation** : consultation chirurgicale, création de préadmission
- **Admission** : accueil, identification, vérification du rendez-vous, transformation préadmission/admission, vérifications administratives, édition des documents d'identification
- **Hospitalisation** : orientation, vérification identité en unité, affectation lit, évaluation clinique, constitution dossier, prescriptions, examens complémentaires, dispensation médicaments
- **Bloc opératoire** : entrée en bloc, anesthésie, intervention, sortie du patient
- **Sortie et clôture** : validation des actes, rendez-vous de contrôle, ordonnances de sortie, sortie médicale, facturation, encaissement, sortie administrative

### Principaux acteurs impliqués
- **Médecins/Chirurgiens** : consultation, indication opératoire, prescriptions, validation des actes, sortie médicale
- **Anesthésiste** : anesthésie, validation protocole anesthésique
- **Personnel hospitalisation/infirmiers** : orientation, affectation lit, évaluation initiale, traçabilité administrations
- **Administration/secrétariat** : création préadmission, admission, vérifications administratives et comptables, orientation, facturation
- **Bloc opératoire (IBODE, IADE, cadre)** : accueil en bloc, participation à l'intervention, traçabilité peropératoire
- **Brancardage** : transfert patient
- **Pharmacie** : dispensation médicaments
- **Services supports** : biologie, imagerie, anatpath

### Systèmes SIH concernés
- **DHE** (Dossier Hospitalier Électronique) / SIH : gestion globale de l'admission et du séjour
- **SIH admissions** : gestion des flux d'arrivée, identité, vérification RDV
- **SIH bloc/agenda bloc** : planification opératoire, gestion du flux bloc
- **SIH soins/dossier patient** : prescriptions, observations, traçabilité des actes
- **SIH prescription/pharmacie** : gestion des ordonnances et dispensations
- **SIH facturation** : enregistrement des actes et facturation
- **SIH lits/hospitalisation** : gestion des affectations et disponibilités

---

## 2. Étapes formelles du parcours patient

| N° étape | Phase | Intitulé de l'étape | Acteur responsable | Action prescrite | Outil / écran SIH | Règle ou validation requise | Dépendances antérieures |
|---|---|---|---|---|---|---|---|
| BO-F-001 | Pré-hospitalisation | Consultation chirurgicale réalisée | Médecin | Confirmer l'indication opératoire et orienter vers préadmission | DHE / SIH | Intervention programmée uniquement après décision médicale validée | Disponibilité médecin, dossier initial du patient |
| BO-F-002 | Pré-hospitalisation | Création d'une préadmission automatique | Administration | Créer la préadmission à partir des données de consultation validées | DHE / SIH | Création à partir des données validées avec contrôle de cohérence identité | Consultation chirurgicale validée (BO-F-001) |
| BO-F-003 | Admission | Arrivée patient jour J | Accueil | Déclencher le parcours de prise en charge | SIH admissions | Présence au rendez-vous programmé | Préadmission créée (BO-F-002) |
| BO-F-004 | Admission | Identification du patient | Administration | Sécuriser l'identitovigilance par contrôle de concordance pièce d'identité / dossier | SIH admissions | Contrôle d'identité obligatoire, concordance stricte identité / dossier | Arrivée patient (BO-F-003) |
| BO-F-005 | Admission | Vérification du rendez-vous | Administration | Confirmer que le patient correspond à une séquence planifiée | SIH / agenda bloc | Validation agenda : le patient doit figurer dans le planning opératoire | Identification confirmée (BO-F-004) |
| BO-F-006 | Admission | Transformation préadmission en admission | Administration | Ouvrir le séjour hospitalier à partir de la préadmission valide | SIH admissions | Pas d'admission sans dossier minimal | RDV vérifié (BO-F-005) |
| BO-F-007 | Admission | Vérification des formalités administratives et comptables | Administration | Sécuriser couverture sociale et conformité financière (pièces assurance, garanties, avance) | SIH facturation | Formalités complètes avant prise en charge sauf exception | Admission active (BO-F-006) |
| BO-F-008 | Admission | Création étiquettes et bracelet patient | Administration | Matérialiser l'identification du patient (bracelet obligatoire) | SIH admissions | Bracelet obligatoire avant hospitalisation, contrôle identité posé | Formalités vérifiées (BO-F-007) |
| BO-F-009 | Hospitalisation | Orientation vers l'hospitalisation | Administration | Diriger le patient vers l'unité correcte selon spécialité et disponibilité | SIH lits | Orientation selon spécialité et disponibilité validée | Bracelet créé (BO-F-008) |
| BO-F-010 | Hospitalisation | Vérification de l'identité du patient dans l'unité | Infirmier | Sécuriser la continuité d'identité à chaque point clé | SIH soins | Contrôle à chaque point clé : vérification bracelet et dossier | Patient orienté (BO-F-009) |
| BO-F-011 | Hospitalisation | Affectation du lit | Hospitalisation | Installer le patient au lit disponible et conforme | SIH hospitalisation | Un lit disponible et conforme est requis | Identité reconfirmée (BO-F-010) |
| BO-F-012 | Hospitalisation | Évaluation initiale | Infirmier | Évaluer l'état du patient à l'entrée (constantes, antécédents, signes cliniques) | SIH soins | Évaluation préalable à tout soin programmé | Lit affecté (BO-F-011) |
| BO-F-013 | Hospitalisation | Constitution / alimentation du dossier d'hospitalisation | Médecin | Centraliser les informations du séjour (évaluation, prescriptions, observations) | SIH dossier patient | Toute action doit être tracée ; toute information centralisée | Évaluation initiale (BO-F-012) |
| BO-F-014 | Hospitalisation | Prescriptions médicales | Médecin | Définir les actes et médicaments selon protocole et examens | SIH prescription | Prescription nécessaire avant administration ; validation médicale | Dossier d'hospitalisation alimenté (BO-F-013) |
| BO-F-015 | Hospitalisation | Passation de consignes et traçabilité des administrations | Infirmier | Assurer continuité des soins par tracée des administrations et transmissions | SIH soins | Toute administration doit être tracée | Prescriptions actives (BO-F-014) |
| BO-F-016 | Support | Examens biologie / imagerie / anatpath si nécessaire | Médecin | Obtenir les éléments de décision selon prescription et délai requis | SIH + systèmes tiers | Examens selon prescription et délai requis ; résultats examinés avant décision | Prescriptions définies (BO-F-014) |
| BO-F-017 | Pharmacie | Ordonnance médicaments puis dispensation | Médecin | Mettre à disposition les traitements sur prescription validée | SIH pharmacie | Dispensation sur prescription validée ; contrôle stock | Prescriptions médicales (BO-F-014) |
| BO-F-018 | Bloc opératoire | Entrée en bloc opératoire | Bloc opératoire | Prendre en charge le patient au bloc après vérification programmation et identité | SIH bloc | Entrée conditionnée à programmation et identité vérifiée ; check pré-bloc | Patient préparé, identité vérifiée (dépend parcours hospitalisation) |
| BO-F-019 | Bloc opératoire | Anesthésie | Anesthésiste | Préparer l'intervention selon protocole validé d'anesthésie | SIH bloc / anesthésie | Procédure selon protocole validé ; validation anesthésiste | Entrée en bloc (BO-F-018) |
| BO-F-020 | Bloc opératoire | Incision / intervention | Chirurgien | Réaliser l'acte opératoire selon indication validée avec équipe bloc (anesthésiste, IBODE, IADE) | SIH bloc | Intervention selon indication validée ; check-list peropératoire | Patient anesthésié (BO-F-019) |
| BO-F-021 | Bloc opératoire | Sortie patient / fin intervention | Bloc opératoire | Clore la séquence opératoire et transférer le patient hors bloc | SIH bloc | Fin intervention tracée avant transfert ; disponibilité unité/SSPI | Acte réalisé (BO-F-020) |
| BO-F-022 | Sortie | Validation des relevés des actes et du CRH | Médecin | Fiabiliser dossier et facturation en validant les actes réalisés et compte rendu | SIH dossier / facturation | Pas de clôture sans validation des actes | Sortie patient du bloc (BO-F-021) |
| BO-F-023 | Sortie | Attribution du rendez-vous de contrôle | Hospitalisation | Organiser le suivi post-opératoire | SIH agenda | RDV si requis par protocole ; validation médicale | Validation actes (BO-F-022) |
| BO-F-024 | Sortie | Ordonnances de sortie | Médecin | Sécuriser la sortie et la continuité des soins | SIH prescription | Ordonnance conforme à la prise en charge validée | Validation actes (BO-F-022) |
| BO-F-025 | Sortie | Sortie médicale du patient | Médecin | Autoriser la fin de prise en charge clinique après évaluation clinique finale | SIH dossier | Sortie après décision médicale ; dossier à jour | Ordonnances de sortie (BO-F-024) |
| BO-F-026 | Clôture administrative | Facturation | Administration | Produire la facture du séjour fondée sur actes validés | SIH facturation | Facture fondée sur actes validés et séjour clôturé | Sortie médicale (BO-F-025) |
| BO-F-027 | Clôture administrative | Encaissement | Comptabilité | Encaisser le reste à charge ou avance selon règles comptables | SIH comptable | Encaissement selon règles comptables | Facturation (BO-F-026) |
| BO-F-028 | Clôture administrative | Sortie patient | Administration | Clôturer administrativement le parcours | SIH admissions / facturation | Séjour clos après validations nécessaires ; dossier complet | Encaissement (BO-F-027) |

---

## 3. Obligations réglementaires

### Obligations explicitement mentionnées dans les documents

| Obligation réglementaire | Étape(s) concernée(s) | Exigence prescrite | Acteur responsable | Outil SIH / Traçabilité |
|---|---|---|---|---|
| **Identitovigilance** | BO-F-004, BO-F-008, BO-F-010, BO-F-018 | Contrôle stricte concordance identité/dossier ; bracelet obligatoire avant hospitalisation ; vérification identité à chaque point clé ; check pré-bloc | Administration, Infirmier, Bloc opératoire | SIH admissions, SIH soins, SIH bloc ; Bracelet patient ; Dossier |
| **Consentement et indication opératoire** | BO-F-001 | Intervention programmée uniquement après décision médicale validée | Médecin | DHE / SIH ; Compte rendu de consultation |
| **Check-list HAS (sécurité du patient)** | BO-F-018 | Check pré-bloc obligatoire à l'entrée du bloc opératoire | Bloc opératoire | SIH bloc ; Traçabilité heure entrée bloc |
| **Traçabilité peropératoire** | BO-F-020, BO-F-021 | Acte réalisé selon indication validée ; fin intervention tracée avant transfert ; compte rendu opératoire | Chirurgien, Bloc opératoire | SIH bloc ; Compte rendu opératoire (CRH) ; Heure fin intervention |
| **Compte rendu opératoire (CRH)** | BO-F-022 | Validation des relevés des actes et du CRH obligatoire avant clôture | Médecin | SIH dossier / facturation ; Actes validés, CRH |
| **Codage CCAM** | BO-F-022 | Relevés des actes réalisés (implicite dans validation des actes) | Médecin | SIH dossier / facturation |
| **Dossier complet et traçabilité** | BO-F-013, BO-F-015, BO-F-025, BO-F-028 | Toute action doit être tracée ; dossier centralisé ; toute administration tracée ; dossier à jour avant sortie médicale ; dossier complet avant clôture administrative | Médecin, Infirmier, Administration | SIH dossier patient ; SIH soins ; Prescriptions, observations, CR actes |
| **Prescriptions médicales** | BO-F-014 | Prescription nécessaire avant administration ; validation médicale obligatoire | Médecin | SIH prescription ; Ordonnances / prescriptions |
| **Continuité des soins post-opératoires** | BO-F-023, BO-F-024 | RDV de contrôle si requis par protocole ; ordonnances de sortie conformes à la prise en charge | Médecin, Hospitalisation | SIH agenda, SIH prescription ; RDV de contrôle, Ordonnances éditées |
| **Formalités administratives et comptables** | BO-F-007 | Formalités complètes (couverture sociale, garanties financières) avant prise en charge sauf exception | Administration | SIH facturation ; Statut dossier conforme |

### Obligations implicites mais fortement présentes

- **Délai de validation** : Les étapes de validation (actes, sortie médicale) doivent être réalisées sans délai excessif, bien qu'aucun délai précis ne soit spécifié dans le formel fourni.
- **Disponibilité et accessibilité du dossier** : Le dossier d'hospitalisation électronique doit être disponible en temps réel pour l'ensemble des professionnels.
- **Sécurité des données** : Les informations (identité, actes, administrations) doivent être enregistrées avec horodatage.

---

## 4. Dépendances critiques

### Dépendances séquentielles obligatoires

#### Phase Pré-hospitalisation et Admission
1. **BO-F-001 → BO-F-002** : La consultation chirurgicale (BO-F-001) doit être validée avant création de la préadmission (BO-F-002). La préadmission ne peut être créée que si l'indication opératoire est confirmée.

2. **BO-F-002 → BO-F-003** : La préadmission (BO-F-002) doit exister avant l'arrivée du patient jour J (BO-F-003).

3. **BO-F-003 → BO-F-004** : L'arrivée (BO-F-003) doit précéder l'identification (BO-F-004).

4. **BO-F-004 → BO-F-005** : L'identité doit être confirmée (BO-F-004) avant vérification du rendez-vous (BO-F-005).

5. **BO-F-005 → BO-F-006** : Le rendez-vous doit être vérifié dans le planning (BO-F-005) avant la transformation de préadmission en admission (BO-F-006). **BLOC CRITIQUE** : Si le patient ne figure pas au planning opératoire, pas d'admission.

6. **BO-F-006 → BO-F-007** : L'admission doit être ouverte (BO-F-006) avant vérification des formalités administratives (BO-F-007).

7. **BO-F-007 → BO-F-008** : Les formalités doivent être vérifiées (BO-F-007) avant édition du bracelet (BO-F-008). **Exception mentionnée** : "sauf exception" pour les formalités complètes, mais aucune exception détaillée n'est spécifiée.

#### Phase Hospitalisation
8. **BO-F-008 → BO-F-009** : Le bracelet doit être créé (BO-F-008) avant orientation vers l'unité (BO-F-009).

9. **BO-F-009 → BO-F-010** : Orientation (BO-F-009) précède vérification identité en unité (BO-F-010).

10. **BO-F-010 → BO-F-011** : Identité reconfirmée (BO-F-010) avant affectation du lit (BO-F-011).

11. **BO-F-011 → BO-F-012** : Lit affecté (BO-F-011) avant évaluation initiale (BO-F-012).

12. **BO-F-012 → BO-F-013** : Évaluation initiale (BO-F-012) doit précéder constitution du dossier (BO-F-013).

13. **BO-F-013 → BO-F-014** : Dossier alimenté (BO-F-013) avant prescriptions médicales (BO-F-014).

14. **BO-F-014 → BO-F-015** : Prescriptions actives (BO-F-014) avant administrations tracées (BO-F-015).

15. **BO-F-014 → BO-F-016** : Prescriptions (BO-F-014) déclenchent examens complémentaires (BO-F-016).

16. **BO-F-014 → BO-F-017** : Prescriptions médicales (BO-F-014) conditionnent dispensation pharmacie (BO-F-017).

#### Phase Bloc Opératoire
17. **BO-F-012 à BO-F-017 → BO-F-018** : L'entrée en bloc (BO-F-018) suppose patient préparé et identité vérifiée. Les étapes d'hospitalisation doivent être suffisamment avancées.

18. **BO-F-018 → BO-F-019** : Entrée en bloc (BO-F-018) avec check pré-bloc doit précéder anesthésie (BO-F-019).

19. **BO-F-019 → BO-F-020** : Patient anesthésié (BO-F-019) avant incision/intervention (BO-F-020).

20. **BO-F-020 → BO-F-021** : Acte réalisé (BO-F-020) avant sortie patient du bloc (BO-F-021).

#### Phase Sortie et Clôture
21. **BO-F-021 → BO-F-022** : Sortie patient du bloc (BO-F-021) précède validation des actes et CRH (BO-F-022). **BLOC CRITIQUE** : "Pas de clôture sans validation des actes".

22. **BO-F-022 → BO-F-023** : Validation des actes (BO-F-022) avant attribution RDV contrôle (BO-F-023).

23. **BO-F-022 → BO-F-024** : Validation des actes (BO-F-022) avant ordonnances de sortie (BO-F-024).

24. **BO-F-024 → BO-F-025** : Ordonnances de sortie (BO-F-024) avant sortie médicale (BO-F-025).

25. **BO-F-025 → BO-F-026** : Sortie médicale (BO-F-025) avant facturation (BO-F-026). **BLOC CRITIQUE** : "Facture fondée sur actes validés et séjour clôturé".

26. **BO-F-026 → BO-F-027** : Facturation (BO-F-026) avant encaissement (BO-F-027).

27. **BO-F-027 → BO-F-028** : Encaissement (BO-F-027) avant sortie administrative (BO-F-028).

### Validations et blocages explicites

| Étape | Validation critique | Si absente → Bloc |
|---|---|---|
| BO-F-001 | Décision médicale validée | Impossible de programmer l'intervention |
| BO-F-002 | Cohérence identité | Erreur dossier à l'arrivée |
| BO-F-005 | Patient figure dans le planning opératoire | Impossible transformer préadmission en admission ; désorganisation du flux |
| BO-F-007 | Formalités administratives et comptables complètes | Blocage facturation ou litige ; exception possible mais non précisée |
| BO-F-008 | Bracelet obligatoire édité | Erreur d'identification au soin ; entrée bloc impossible |
| BO-F-022 | Validation des actes et CRH obligatoire | Impossible clôturer le séjour ; facturation incomplète |
| BO-F-025 | Sortie médicale prononcée | Impossible de facturer et clôturer administrativement |
| BO-F-026 | Facture émise fondée sur actes validés | Sortie administrative impossible ; perte de recette |

---

## 5. Interfaces avec d'autres services

### 5.1 Interface avec la Réanimation / SSPI (Soins de Suite Post-Interventionnelle)

| Interface | Étape(s) concernée(s) | Ce qui est attendu | Responsable côté bloc | Responsable côté SSPI/réanimation |
|---|---|---|---|---|
| **Transfert post-intervention** | BO-F-021 | Disponibilité unité/SSPI selon organisation ; patient transféré hors bloc avec fin intervention tracée | Bloc opératoire | Réanimation/SSPI/Hospitalisation |
| **Continuité des soins** | BO-F-021 → BO-F-025 | Transmission des informations (actes réalisés, recommandations anesthésie, protocoles) | Bloc opératoire | Réanimation/SSPI |

**Implicite** : Aucun détail ne précise le format de transmission ni les délais de réception. Le document mentionne "disponibilité unité/SSPI selon organisation" mais ne spécifie pas les responsabilités de chacun en cas d'indisponibilité.

---

### 5.2 Interface avec la Stérilisation

**Observation** : La stérilisation n'est pas explicitement mentionnée dans le document formel fourni. Aucune étape ne décrit :
- La demande de matériel stérilisé
- La traçabilité des charges de stérilisation
- Les délais de disponibilité du matériel stérilisé pour l'intervention
- Les responsabilités en cas de matériel non stérilisé

**Zone d'ombre** : Il existe une dépendance implicite mais non formalisée entre la préparation du matériel stérilisé et l'étape BO-F-020 (incision/intervention).

---

### 5.3 Interface avec le Brancardage

| Interface | Étape(s) concernée(s) | Ce qui est attendu | Responsable |
|---|---|---|---|
| **Transfert vers l'hospitalisation** | BO-F-009 | Transfert du patient vers l'unité correcte ; disponibilité brancardage | Administration (orientation), Brancardage (transfert) |
| **Transfert vers le bloc opératoire** | BO-F-018 | Patient présenté au bloc ; identité vérifiée | Brancardage (transfert), Bloc opératoire (accueil) |
| **Transfert post-opératoire** | BO-F-021 | Patient transféré vers SSPI/réanimation selon disponibilité | Bloc opératoire, Brancardage, SSPI/Réanimation |

**Implicite** : Le brancardage n'a pas de validation spécifique formalisée. Aucune traçabilité du délai de transfert n'est mentionnée (entre heure d'orientation et heure d'arrivée en unité, entre heure de sortie bloc et heure d'arrivée en SSPI).

---

### 5.4 Interface avec le DIM (Département d'Information Médicale)

| Interface | Étape(s) concernée(s) | Ce qui est attendu | Responsable côté bloc | Responsable côté DIM |
|---|---|---|---|---|
| **Codage des actes CCAM** | BO-F-022 | Relevés des actes validés et codés pour facturation | Médecin (validation) | DIM (codage optimal) |
| **Traçabilité des actes** | BO-F-020 → BO-F-022 | Compte rendu opératoire conforme, actes énumérés pour validation médicale | Chirurgien (rédaction CRH) | DIM (exploitation pour requête, qualité codage) |

**Implicite** : Aucun délai de retour vers le bloc pour validation/correction du codage n'est spécifié. Le document ne précise pas qui est responsable de la correspondance entre actes réalisés et codes CCAM.

---

### 5.5 Interface avec la Pharmacie

| Interface | Étape(s) concernée(s) | Ce qui est attendu | Responsable côté hospitalisation | Responsable côté pharmacie |
|---|---|---|---|---|
| **Dispensation des médicaments** | BO-F-017 | Prescriptions médicales validées → Médicaments dispensés sur ordonnance | Médecin (prescription) | Pharmacie (validation, dispensation, trace) |
| **Gestion des stupéfiants bloc** | BO-F-014, implicite BO-F-020 | Prescriptions médicales ; administrations tracées | Médecin, Équipe bloc | Pharmacie (fourniture, contrôle consommation) |

**Zone d'ombre** : Bien que la traçabilité des administrations soit mentionnée (BO-F-015), aucune procédure spécifique n'est détaillée pour :
- La gestion des stupéfiants utilisés au bloc
- La traçabilité peropératoire des stupéfiants
- La procédure de destruction ou retour en pharmacie des stupéfiants non utilisés

---

### 5.6 Interface avec les Services d'Hospitalisation

| Interface | Étape(s) concernée(s) | Ce qui est attendu | Responsable bloc opératoire | Responsable hospitalisation |
|---|---|---|---|---|
| **Orientation et affectation** | BO-F-009, BO-F-011 | Disponibilité lit, affectation selon spécialité | Administration (orientation) | Hospitalisation (gestion lits, affectation) |
| **Vérification identité continuité** | BO-F-010 | Identité reconfirmée à chaque point clé | Infirmier en unité | Infirmier en unité |
| **Évaluation initiale et dossier** | BO-F-012, BO-F-013 | Évaluation préalable à tout soin ; dossier centralisé | Infirmier en unité | Infirmier + Médecin en unité |
| **Transmission d'information post-opératoire** | BO-F-021 → Unité | Information peropératoire, recommandations, observations | Bloc opératoire | Réanimation/SSPI/Hospitalisation |

---

### 5.7 Interface avec l'Imagerie Peropératoire

| Interface | Étape(s) concernée(s) | Ce qui est attendu | Responsable |
|---|---|---|---|
| **Examens complémentaires préopératoires** | BO-F-016 | Imagerie demandée par prescription médicale ; résultats disponibles avant intervention | Médecin (prescription), Imagerie (réalisation) |
| **Imagerie peropératoire** | BO-F-020, implicite | Imagerie possible selon protocole chirurgical (C-arm, échographie peropératoire) | Chirurgien (demande), Imagerie/bloc (réalisation) |

**Zone d'ombre** : Aucune étape spécifique ne mentionne l'imagerie peropératoire. Celle-ci est implicite dans l'étape BO-F-020 (incision/intervention) mais sans formalisation explicite.

---

### 5.8 Interface avec la Biologie et l'Anatpathologie

| Interface | Étape(s) concernée(s) | Ce qui est attendu | Responsable |
|---|---|---|---|
| **Examens biologie préopératoires** | BO-F-016 | NFS, TP, créatinine selon protocole ; résultats examinés avant intervention | Médecin (prescription), Biologie (réalisation) |
| **Prélèvements peropératoires et traçabilité** | BO-F-020, implicite | Prélèvements pathologiques si nécessaire (biopsies, pièces opératoires) | Chirurgien (prélèvement), IBODE (traçabilité), Anatpathologie (réception, traçabilité) |

**Zone d'ombre** : La traçabilité des prélèvements anatpathologiques n'est pas détaillée. Aucune obligation de traçabilité de la pièce opératoire n'est mentionnée explicitement, bien que cela soit une exigence réglementaire implicite.

---

## 6. Points de vigilance formels

### 6.1 Points d'attention explicitement mentionnés dans les documents

| Point de vigilance | Étape(s) concernée(s) | Nature du risque | Conséquence si non respecté |
|---|---|---|---|
| **Erreur d'identité** | BO-F-004, BO-F-008, BO-F-010, BO-F-018 | Identitovigilance : concordance stricte identité/dossier ; bracelet obligatoire | Erreur d'identification au soin ; intervention sur mauvais patient |
| **Désorganisation du flux** | BO-F-003, BO-F-005, BO-F-009 | Patient non programmé au bloc ; arrivée sans préadmission ; orientation impossible | Retard ou annulation ; errance du patient |
| **Retard ou programmation inadaptée** | BO-F-001, BO-F-003 | Absence de validation médicale ; patient absent au rendez-vous | Retard programmation ; intervention non réalisée |
| **Perte de suivi post-opératoire** | BO-F-023 | RDV de contrôle non fixé ou non respecté | Discontinuité des soins ; complications non détectées |
| **Perte d'information** | BO-F-013, BO-F-021 | Dossier incomplet ; fin intervention non tracée | Rupture de traçabilité ; complication non documentée |
| **Erreur thérapeutique** | BO-F-014, BO-F-017 | Prescription manquante ; médicament non prescrit ou non dispensé | Mauvaise continuité post-hospitalisation ; retard traitement |
| **Facturation incomplète** | BO-F-022, BO-F-026 | Actes non validés ; dossier incomplet avant facturation | Perte de recette ; litige comptable |
| **Complication ou non-conformité peropératoire** | BO-F-020, BO-F-021 | Acte réalisé hors protocole ; fin intervention non tracée | Complication non documentée ; responsabilité mal établie |
| **Rupture de continuité des soins** | BO-F-015, BO-F-021 | Administrations non tracées ; transmission post-bloc insuffisante | Erreur de prise en charge ; événement adverse non détecté |
| **Risque clinique non détecté** | BO-F-012 | Évaluation initiale insuffisante ou non documentée | Complication précoce non préventée ; contre-indication opératoire non détectée |
| **Retard de prise en charge** | BO-F-009, BO-F-011 | Lit non disponible ; affectation retardée | Surcharge urgences ; insatisfaction patient |
| **Blocage facturation/litige** | BO-F-007 | Formalités administratives non complètes | Fonds non collectés ; recours juridique |
| **Impayé** | BO-F-027 | Encaissement non réalisé | Perte financière ; impact budget |

### 6.2 Délais critiques non spécifiés

Le document formel ne précise aucun délai pour les étapes suivantes :

| Étape | Délai prescrit | Impact de l'absence de délai |
|---|---|---|
| BO-F-001 → BO-F-002 | Non spécifié | Délai de programmation imprévisible |
| BO-F-003 → BO-F-008 | Non spécifié | Durée d'arrivée/admission variable |
| BO-F-016 (examens complémentaires) | "Selon délai requis" (imprécis) | Retard possible si délai non défini |
| BO-F-022 (validation des actes) | Non spécifié | Clôture du séjour retardée |
| BO-F-025 → BO-F-028 | Non spécifié | Sortie administrative retardée |

### 6.3 Points d'attention spécifiques au bloc opératoire

| Point critique | Détail | Formulation dans le document |
|---|---|---|
| **Check-list HAS** | Obligatoire à l'entrée du bloc | "Check pré-bloc" mentionné comme validation requise pour BO-F-018 |
| **Traçabilité peropératoire** | Acte et fin intervention doivent être tracés | "Fin intervention tracée avant transfert" ; "Compte rendu opératoire" |
| **Indication opératoire validée** | L'acte doit correspondre à l'indication initiale | "Intervention selon indication validée" pour BO-F-020 |
| **Équipe bloc complète** | Anesthésiste, IBODE, IADE présents | Mentionnés dans BO-F-020 mais sans formalisation de validation de présence |
| **Disponibilité salle et matériel** | Critique pour démarrage anesthésie et intervention | Mentionnée comme "Disponibilité salle, équipe, matériel" pour BO-F-020 |

---

## 7. Zones d'ombre et incohérences du formel

### 7.1 Zones d'ombre majeures

#### 7.1.1 Gestion des Dispositifs Médicaux Implantables (DMI)
- **Mention explicite** : AUCUNE
- **Impact** : Bien que la traçabilité des DMI soit une obligation réglementaire majeure (traçabilité de l'implant, numéro de série, fabricant, lot), aucune étape ne décrit :
  - La validation de la disponibilité de l'implant avant intervention
  - La traçabilité du numéro de série et du lot
  - L'enregistrement du DMI dans le dossier patient
  - Les responsabilités de l'IBODE ou du médecin dans cette traçabilité
  - La communication avec la matériovigilance en cas de problème

#### 7.1.2 Gestion des Stupéfiants au Bloc
- **Mention explicite** : Implicite dans BO-F-014 (prescriptions) et BO-F-015 (administrations tracées), mais AUCUNE procédure spécifique
- **Imprécisions** :
  - Qui valide les stupéfiants dispensés avant intervention ?
  - Quelle est la traçabilité peropératoire des stupéfiants utilisés ?
  - Comment sont gérés les résidus ou les stupéfiants non utilisés ?
  - Qui remplit le registre des stupéfiants au bloc ?
  - Aucune étape ne mentionne l'archivage des ordonnances stupéfiants

#### 7.1.3 Prélèvements Anatpathologiques et Traçabilité de la Pièce Opératoire
- **Mention explicite** : BO-F-016 (examens anatpath si nécessaire) mais SANS détail
- **Manques** :
  - Qui remplit le bon de prélèvement ?
  - Qui s'assure que le prélèvement est correctement identifié au patient ?
  - Quel est le délai d'envoi à l'anatpathologie ?
  - Qui valide la réception en anatpathologie ?
  - Aucune responsabilité attribuée (IBODE, Médecin, ?)

#### 7.1.4 Imagerie Peropératoire
- **Mention explicite** : BO-F-016 (examens préopératoires) mais AUCUNE mention d'imagerie peropératoire
- **Zone grise** : Bien que l'imagerie peropératoire soit courante au bloc (C-arm, échographie), aucune étape ne formalise :
  - La demande d'imagerie peropératoire
  - La disponibilité du matériel
  - La stérilité des équipements
  - Qui en est responsable
  - La traçabilité des clichés

#### 7.1.5 Incident Peropératoire ou Complication Intraopératoire
- **Mention explicite** : AUCUNE
- **Imprécisions** : 
  - Comment est documentée une complication peropératoire ?
  - Qui remplit la déclaration d'incident/événement adverse ?
  - Comment cela affecte-t-il le compte rendu opératoire ?
  - Quel est le rôle du bloc opératoire vs. celui du médecin vs. celui du gestionnaire de risque ?

#### 7.1.6 Stérilisation et Tracabilité du Matériel
- **Mention explicite** : AUCUNE
- **Dépendances implicites** : 
  - Avant BO-F-020 (incision/intervention), le matériel doit être stérilisé
  - Mais aucune étape ne décrit :
    - La demande de stérilisation
    - La validation de la stérilité
    - La traçabilité de la charge
    - La responsabilité en cas d'incident de stérilisation (matériel non stérilisé)

#### 7.1.7 Check-list HAS : Détail du Contenu
- **Mention explicite** : "Check pré-bloc" (BO-F-018) comme validation requise
- **Imprécisions** :
  - Quels éléments spécifiques doivent être vérifiés selon la HAS ?
  - Qui remplit la check-list (anesthésiste, chirurgien, IBODE, cadre) ?
  - En cas de non-conformité, peut-on reporter l'intervention ?
  - Aucune trace formelle de cette check-list dans le SIH n'est mentionnée

#### 7.1.8 Traçabilité Peropératoire Détaillée
- **Mention explicite** : Compte rendu opératoire (BO-F-022) et "Acte réalisé" (BO-F-020)
- **Imprécisions** :
  - Qui rédige le compte rendu opératoire (chirurgien seul, avec l'IBODE) ?
  - Quel est le délai de rédaction après intervention ?
  - Quels éléments minimaux doivent figurer dans le CRH (durée acte, geste peropératoire, incident, temps d'ischémie si applicable) ?
  - Qui valide ce compte rendu ?

#### 7.1.9 Données Manquantes / Absence de Patient
- **Mention explicite** : "Retard ou annulation" (BO-F-003)
- **Imprécisions** :
  - Si le patient ne se présente pas, qui annule la programmation au bloc ?
  - Quel est le délai de notification aux équipes du bloc ?
  - Qui repositionne le patient dans le planning ?
  - Aucune procédure de déprogrammation n'est décrite

#### 7.1.10 Anesthésie : Dossier et Validation
- **Mention explicite** : BO-F-019 (Anesthésie - "Préparer l'intervention selon protocole validé")
- **Imprécisions** :
  - Qui valide que le protocole anesthésique est conforme (anesthésiste seul, commission, protocole standard) ?
  - Quel est le dossier anesthésie minimal (antécédents, contre-indications, allergie, classification ASA) ?
  - Aucune mention du dialogue anesthésiste-chirurgien avant incision
  - Aucune traçabilité détaillée des gestes anesthésiques (sonde trachéale, voie veineuse, monitoring)

#### 7.1.11 Réanimation / SSPI : Critères de Transfert
- **Mention explicite** : "Disponibilité unité/SSPI selon organisation" (BO-F-021)
- **Imprécisions** :
  - Qui décide si le patient va en SSPI ou directement en hospitalisation (anesthésiste, chirurgien, SSPI) ?
  - Quel est le critère de décision (ASA, durée d'intervention, comorbidités) ?
  - Aucune dépendance critique ne lie le transfert à une validation SSPI préalable
  - Le document ne mentionne pas le rôle de la réanimation dans la décision de transfert

#### 7.1.12 Formalités Administratives "Sauf Exception"
- **Mention explicite** : BO-F-007 "Formalités complètes avant prise en charge sauf exception"
- **Imprécisions** :
  - Quelles sont les exceptions autorisant l'admission sans formalités complètes ?
  - Qui valide l'exception (direction, médecin, administration) ?
  - Aucun exemple donné (urgence, absence d'assurance, patient vulnérable, etc.)
  - Qui est responsable de la facturation ultérieure en cas d'exception ?

#### 7.1.13 Ordonnances de Sortie : Niveau de Détail
- **Mention explicite** : BO-F-024 "Ordonnances de sortie" et "conforme à la prise en charge"
- **Imprécisions** :
  - Qui rédige les ordonnances (chirurgien, médecin généraliste, praticien du bloc) ?
  - Doit-elle inclure les prescriptions peropératoires, les analgésiques post-opératoires, les consignes de rééducation ?
  - Aucune traçabilité détaillée mentionnée dans le SIH

#### 7.1.14 Rendez-vous de Contrôle : Protocole et Responsabilité
- **Mention explicite** : BO-F-023 "RDV si requis par protocole"
- **Imprécisions** :
  - Quel protocole spécifie si un RDV est requis (protocole chirurgical, protocole par spécialité) ?
  - Qui fixe le RDV (secrétariat, chirurgien, hospitalisation) ?
  - Quel est le délai attendu (J1, J15, J30 post-op) ?
  - Que faire si le patient ne se présente pas au RDV ?

#### 7.1.15 Consentement Éclairé / Document d'Accord
- **Mention explicite** : BO-F-001 mentionne "Décision opératoire" mais AUCUNE mention du formulaire de consentement
- **Manque** :
  - Quand le consentement doit-il être signé (avant admission, en hospitalisation, avant entrée bloc) ?
  - Qui s'assure que le document est présent au dossier ?
  - Aucune validation explicite mentionnée avant BO-F-018 (entrée bloc)

#### 7.1.16 Identification du Chirurgien et de l'Équipe
- **Mention explicite** : Chirurgien mentionné dans BO-F-020 mais AUCUNE validation de l'identité du chirurgien avant intervention
- **Imprécisions** :
  - Qui valide que le chirurgien prévu est effectivement présent ?
  - Que faire en cas de changement de chirurgien (remplacement) ?
  - Aucune traçabilité du chirurgien réel dans le SIH bloc n'est mentionnée

#### 7.1.17 Compte Rendu Opératoire : Format et Validation
- **Mention explicite** : BO-F-022 mentionne "Compte rendu opératoire" comme élément de validation
- **Imprécisions** :
  - Format du CRH (texte libre, template structuré, code CCAM) ?
  - Quels éléments minimaux (indicateurs de la HAS : patient, chirurgien, acte exact, durée, incidents) ?
  - Qui valide le CRH (chirurgien seul, DIM, médecin responsable du séjour) ?
  - Délai de validation après intervention

#### 7.1.18 Données Biométriques et Latéralité
- **Mention explicite** : AUCUNE
- **Imprécision** : Bien que la vérification de la latéralité soit une exigence HAS majeure (intervention sur le bon côté), aucune étape ne spécifie :
  - Qui valide la latéralité avant intervention
  - Comment cela est documenté (marquage cutané, check-list HAS)
  - Trace dans le dossier peropératoire

#### 7.1.19 Iatrogénie Peropératoire
- **Mention explicite** : "Complication ou non-conformité" (BO-F-020) mais SANS procédure spécifique
- **Imprécisions** :
  - Comment documente-t-on une iatrogénie peropératoire ?
  - Notification à la matériovigilance, pharmacovigilance, ou signalement interne ?
  - Qui décide si l'intervention peut continuer ou doit être arrêtée ?

#### 7.1.20 Dossier Peropératoire Minimal : Contenu Prescrit
- **Mention explicite** : Aucun détail spécifique sur le contenu du "dossier anesthésie" ou du "dossier opératoire"
- **Imprécisions** :
  - Qui remplit quoi exactement (anesthésiste, chirurgien, IBODE, IADE) ?
  - Quels éléments minimaux (allergies, antécédents, ASA, durée anesthésie, durée acte) ?
  - Format papier, électronique, hybride ?

---

### 7.2 Incohérences et contradictions

#### 7.2.1 "Dossier minimal" pour admission
- **BO-F-006** : "Pas d'admission sans dossier minimal"
- **Incohérence** : Le contenu du "dossier minimal" n'est nulle part défini dans le formel fourni. Qu'est-ce qui constitue ce dossier minimal ? Pièce d'identité, assurance, justificatif de domicile, dossier médical initial ?

#### 7.2.2 Check pré-bloc vs. Check-list HAS
- **BO-F-018** : Validation requise = "Check pré-bloc"
- **Imprécision** : "Check pré-bloc" est-il l'équivalent de la "check-list HAS de sécurité du patient au bloc" ? Le document ne clarifie pas cette correspondance.

#### 7.2.3 Prescription médicale vs. protocole
- **BO-F-014** : "Définir les actes et médicaments selon protocole et examens"
- **Imprécision** : Prescription "selon protocole" : le protocole vient-il du chirurgien, de l'hôpital, ou est-il standard de spécialité ? Qui valide sa conformité avec la pratique locale ?

#### 7.2.4 Transformation préadmission en admission : Timing implicite
- **BO-F-005 vs. BO-F-006** : 
  - BO-F-005 : "Vérification du rendez-vous" → validation agenda
  - BO-F-006 : "Transformation préadmission en admission"
  - **Imprécision** : Peut-on transformer la préadmission en admission SANS vérification du rendez-vous ? Le document le stipule comme dépendance, mais cela crée une dépendance implicite non explicitement formalisée dans le tableau des validations.

#### 7.2.5 Validation des actes réalisés vs. compte rendu opératoire
- **BO-F-020** : "Acte réalisé" (simple affirmation)
- **BO-F-022** : "Validation des relevés des actes et du CRH"
- **Incohérence** : 
  - Y a-t-il une différence entre "acte réalisé" (BO-F-020) et "actes validés" (BO-F-022) ?
  - Qui valide les actes ? Le chirurgien ? Un médecin coordinateur ? Une commission ?
  - Aucune trace SIH précise n'est mentionnée pour cette validation

#### 7.2.6 Responsabilité du médecin dans BO-F-001 vs. Chirurgien dans BO-F-020
- **BO-F-001** : Acteur responsable = "Médecin" (imprécis : interniste, cardiologue ?)
- **BO-F-020** : Acteur responsable = "Chirurgien"
- **Imprécision** : Sont-ce la même personne ? Y a-t-il un circuit de vérification que le chirurgien de BO-F-020 est bien celui qui a validé l'indication en BO-F-001 ?

#### 7.2.7 Sortie médicale vs. Sortie administrative
- **BO-F-025** : "Sortie médicale du patient" = fin de prise en charge clinique
- **BO-F-028** : "Sortie patient" = clôture administrative
- **Imprécision** : Peut-on avoir une sortie administrative sans sortie médicale ? Aucune étape ne précise le rapport entre les deux ni le rôle de chacune.

#### 7.2.8 Encaissement avant sortie administrative ?
- **BO-F-027 → BO-F-028** : Encaissement (BO-F-027) précède sortie administrative (BO-F-028)
- **Imprécision** : Que se passe-t-il si l'encaissement n'est pas complet (impayé partiel, reste à charge non recouvrable) ? La sortie administrative est-elle bloquée ou peut-elle se faire quand même ?

#### 7.2.9 Acteurs secondaires vs. Acteurs responsables imprécis
Le tableau CSV distingue "primary_actor" et "secondary_actors" mais cette distinction n'est pas toujours claire :
- **BO-F-002** : Primary = Administration, Secondary = Médecin, SIH. Qui valide vraiment la création de préadmission ?
- **BO-F-014** : Primary = Médecin, Secondary = Pharmacie, Infirmier. Le médecin seul prescrit-il ou en concertation avec la pharmacie/infirmier ?

#### 7.2.10 "Disponibilité" vs. "Validation"
Plusieurs étapes mentionnent "Disponibilité X" comme dépendance critique (ex. : "Disponibilité salle et équipe" pour BO-F-020), mais cela n'est pas une validation réelle - cela ne peut pas être validé avant une certaine heure.
- **Imprécision** : Doit-on considérer que la salle/équipe est toujours disponible (par organisation), ou faut-il une validation préalable ?

---

### 7.3 Éléments implicites non formalisés

#### 7.3.1 Dialogue Anesthésiste - Chirurgien
- Le document ne mentionne AUCUN dialogue ou validation croisée entre l'anesthésiste (BO-F-019) et le chirurgien (BO-F-020) avant incision.
- **Pratique commune** : Cette validation est obligatoire (même avant la check-list HAS) mais elle n'apparaît pas formellement.

#### 7.3.2 Accord de Bloc Opératoire pour Entrée du Patient
- Le document ne précise pas qui valide que le patient peut entrer en bloc :
  - Cadre de bloc opératoire ?
  - Anesthésiste ?
  - Planificateur du bloc ?
- **Seule mention** : "Check pré-bloc" comme validation requise pour BO-F-018.

#### 7.3.3 Responsable Médical du Séjour
- Aucun rôle explicite n'est assigné au "praticien responsable du séjour", bien que cela soit une exigence réglementaire implicite.
- **Impact** : Qui valide la conformité du séjour avec la prise en charge initiale ? Qui arbitre en cas de complication ?

#### 7.3.4 Traçabilité des Décisions Thérapeutiques post-opératoires
- Les étapes BO-F-023 (RDV contrôle), BO-F-024 (ordonnances sortie) ne formalisent pas qui prend les décisions (chirurgien, médecin hospitalisé, praticien généraliste).

#### 7.3.5 Critères d'Admission en SSPI vs. Hospitalisation Classique
- Aucun critère n'est spécifié. Le document dit simplement "Disponibilité unité/SSPI selon organisation" (BO-F-021).
- **Imprécision** : Y a-t-il des patients qui sortent directement du bloc sans SSPI ? Qui décide ?

---

### 7.4 Manques de traçabilité SIH spécifique

| Élément critique | Étape | Trace SIH mentionnée | Trace attendue mais absente |
|---|---|---|---|
| Check-list HAS | BO-F-018 | "Heure entrée bloc" | Présence/validation check-list HAS dans SIH bloc |
| Anesthésie (gestes, durée, incident) | BO-F-019 | "Trace anesthésie" (imprécis) | Détail : durée anesthésie, gestes, incidents, durée ischémie si applicable |
| Incident peropératoire | BO-F-020 | "Compte rendu opératoire" | Déclaration d'incident formelle, notification gestionnaire risque |
| Stupéfiants utilisés | BO-F-015, BO-F-020 | Aucune | Trace peropératoire des stupéfiants, registre bloc, reste-quantités |
| Matériel stérilisé utilisé | BO-F-020 | Aucune | Traçabilité charge stérilisation, lot matériel, incident stérilisation |
| DMI implanté | BO-F-020 | Aucune | Numéro série, fabricant, lot, date implantation |
| Prélèvements anatpath | BO-F-016 | Aucune | Bon de prélèvement identifié, traçabilité envoi/réception anatpathologie |
| Latéralité vérifiée | BO-F-020 | Aucune | Validation latéralité (marquage cutané, check-list) |
| Équipe bloc présente | BO-F-020 | Aucune | Noms anesthésiste, chirurgien, IBODE, IADE enregistrés |
| Consentement signé | BO-F-001 → BO-F-018 | Aucune | Présence document consentement validé au dossier avant entrée bloc |

---

### 7.5 Réglementations applicables mais non détaillées

| Réglementation | Mention dans le document | Détail spécifié |
|---|---|---|
| **HAS - Audit de Sécurité du Bloc** | Check-list pré-bloc (BO-F-018) | Aucun détail de contenu HAS |
| **Traçabilité DMI (ordonnance 2008-1350)** | AUCUNE | Complètement absent du formel |
| **Traçabilité stupéfiants (code santé publique)** | Implicite dans prescriptions (BO-F-014) | Aucune procédure spécifique bloc |
| **Traçabilité anatpath (décret 2005-1161)** | BO-F-016 minimal | Aucun détail responsabilités |
| **Dossier patient complet (ISO 27002)** | BO-F-013 "Constitution dossier" | Contenu minimal non spécifié |
| **Codage CCAM (décret 2005-1160)** | BO-F-022 implicite | Responsabilité DIM vs. bloc non clarifié |
| **Compte rendu opératoire (HAS)** | BO-F-022 | Format et éléments minimaux non détaillés |
| **Matériovigilance (décret 2008-1350)** | AUCUNE | Aucune procédure d'incident matériel |
| **Incidents peropératoires (HAS/ANSM)** | AUCUNE | Aucune procédure de déclaration |

---

## Synthèse des zones d'ombre critiques

### Domaines complètement absent du formel fourni :
1. **Gestion des DMI** (traçabilité série, lot, implantation)
2. **Gestion des stupéfiants au bloc** (traçabilité peropératoire, registre)
3. **Imagerie peropératoire** (demande, stérilité, traçabilité)
4. **Stérilisation** (demande, charge, incident stérilisation)
5. **Incidents peropératoires** (documentation, notification, gestion)
6. **Matériovigilance** (signalement, procédure)
7. **Prélèvements anatpath** (bon, traçabilité, responsabilités)
8. **Check-list HAS détaillée** (contenu, qui la remplit, signature)
9. **Consentement éclairé** (quand, qui valide, trace SIH)
10. **Identification du chirurgien réel** (validation avant intervention)

### Domaines partiellement formalisés :
1. **Anesthésie** : Existence validée (BO-F-019) mais détail pratique absent
2. **Compte rendu opératoire** : Obligation mentionnée (BO-F-022) mais format/contenu non spécifié
3. **Traçabilité peropératoire** : Horodatage mentionné mais détail observations absent
4. **SSPI/Réanimation** : Transfert mentionné mais critères décision absent
5. **Formalités administratives** : "Sauf exception" mais exceptions non définies

---

## Synthèse générale

Le document formel fourni (EALIGNIS_bloc_operatoire_jeu_formel.csv) décrit un flux de 28 étapes couvrant le parcours complet patient de la pré-hospitalisation à la sortie administrative. 

**Points de clarté** :
- Sequencing clair et dépendances majoritairement logiques
- Acteurs principaux identifiés pour la plupart des étapes
- Systèmes SIH globalement documentés
- Validations critiques explicitement nommées (identité, programmation, actes, sortie)

**Points de faiblesse majeurs** :
- Nombreuses zones d'ombre sur les processus bloc opératoire spécifiques (DMI, stupéfiants, imagerie peropératoire, incidents)
- Réglementations critiques (HAS, matériovigilance) non détaillées
- Check-list HAS mentionnée mais non formalisée
- Absence de timing et délais pour les étapes critiques
- Imprécision sur les rôles (qui valide vraiment ? qui décide ?)
- Traçabilité SIH incomplète pour les actes peropératoires critiques

Cette fiche reflète **exclusivement** ce que le document formel prescrit, sans interprétation ni correction des incohérences identifiées.