# Fiche des pratiques réelles — Circuit Pharmacie Hospitalière

## 1. Déroulement réel du circuit

### Flux général observé

Le circuit réel de dispensation s'articule autour de trois flux parallèles qui se rencontrent :

1. **Flux prescription papier** : La prescription médicale arrive au service pharmacie sur support papier ou scanné
2. **Flux saisie SIH** : Une demande est transmise au système d'information hospitalier (demande officielle)
3. **Flux besoin opérationnel** : Les services expriment des besoins urgents en parallèle du circuit formel

#### Variantes observées selon les contextes

**En situation normale (flux planifié):**
- Prescription médicale → Demande SIH → Validation pharmaceutique → Préparation en pharmacie → Dispensation à l'unité de soins
- Les délais respectent les temps planifiés (ex. : préparation souhaitée à 14h30)
- Contrôle pharmaceutique effectué avant dispensation avec validation pharmacien
- Signature du service demandeur et de la pharmacie requise sur le bon

**En situation d'urgence (chirurgicale, bloc opératoire):**
- Circulation accélérée des bons de dispensation
- Priorités marquées "urgente" sur le bon (exemple : Mme ADJOA - urgence chirurgicale)
- Délais de préparation raccourcis (ex. : "avant 16h00")
- Les observations du pharmacien deviennent des consignes de temps plutôt que des validations bloquantes
- Tension visible : le statut du bon reste "EN ATTENTE DE VALIDATION FINALE" même avec urgence déclarée

**En situation de réception sans interfaçage:**
- Les équipes différent volontairement la saisie complète pour éviter un blocage opérationnel
- Régularisation ultérieure de la trace complète
- Double circuit : enregistrement rapide (basique) puis saisie détaillée (reportée)

**Contextes de rupture de stock ou flux tendu:**
- La dispensation s'adapte à la disponibilité réelle plutôt qu'à la prescription exacte
- Choix pragmatique : boîte vs unité selon stock disponible
- Les services expriment des besoins urgents qui conduisent à adaptation locale des circuits
- Commandes internes formulées de manière informelle en parallèle du système, puis régularisées ensuite

**Lors des inventaires:**
- Régulièrement, écarts entre stock théorique et stock physique révélés
- Ces écarts mettent en lumière les divergences entre quantités demandées, délivrées et réellement consommées qui ne sont pas visibles immédiatement dans le flux normal

---

## 2. Acteurs réellement mobilisés

### Rôles formels et rôles réels

| Acteur | Rôle prescrit | Rôle réel observé | Écarts identifiés |
|--------|---------------|-------------------|-------------------|
| **Pharmacien validateur** | Validation de la conformité avec la prescription médicale | Validation + gestion des urgences + adaptation locale des circuits + arbitrage entre délais et rigueur | Arbitrage non formalisé en cas d'urgence ; prise de décision sur temps d'exécution ; validation partielle en situation tendue |
| **Préparateur en pharmacie** | Préparation selon prescription validée | Préparation + saisie différée en réception sans interfaçage + gestion des stocks temps réel + ajustement quantités selon disponibilité | Responsabilité étendue de saisie détaillée ; prise de décision opérationnelle sur dispensation boîte/unité |
| **Service demandeur (infirmier, médecin)** | Formulation de prescription claire, signature du bon | Formulation informelle en parallèle du système + expression de besoins urgents non prévisibles + génération de demandes SIH sans toujours attendre circuit formel | Contournement du circuit formel ; communication directe avec pharmacie en urgence |
| **Équipe réception** | Enregistrement de réception de marchandise | Enregistrement rapide basique + saisie détaillée reportée + gestion des produits en quarantaine non clairement distingués | Différenciation entre enregistrement opérationnel et tracé complet ; gestion implicite des quarantaines |
| **Pharmacien responsable** | Supervision générale | Supervision + gestion des droits d'accès + résolution des incohérences de stock | Responsabilité de réconciliation entre rôles réels et droits d'accès |

### Points critiques d'acteurs

- Les **préparateurs** font fonctionner le circuit en réalité, mais doivent gérer l'écart entre prescription détaillée et disponibilité réelle
- Les **services demandeurs** initient plusieurs flux en parallèle : prescription formelle + demande SIH + appels directs en urgence
- Les **pharmaciens validateurs** arbitrent en temps réel entre rigueur de contrôle et pression opérationnelle sans protocole formalisé pour cette arbitrage

---

## 3. Contournements identifiés

| Contournement observé | Sous-processus concerné | Raison probable | Fréquence estimée | Impact sur la sécurité ou la traçabilité |
|---|---|---|---|---|
| Saisie détaillée différée après réception | Réception de marchandise / entrée stock | Éviter blocage opérationnel ; interfaçage insuffisant avec fournisseur | Régulier en réception sans interfaçage | Risque : délai de disponibilité réelle en stock vs stock théorique ; écarts découverts tardivement |
| Demande SIH formée en parallèle de prescription papier | Transmission prescription à pharmacie | Service envoie demande directe au SIH sans attendre circuit papier complet | Fréquent | Risque : double saisie ; incohérence prescription papier vs SIH |
| Appel direct en urgence plutôt que circuit formel | Dispensation urgente | Besoin d'accélération ; anticipation que circuit formel serait trop lent | Observé en situation chirurgicale/bloc | Risque : prescription orale non documentée ; contournement validation pharmaceutique |
| Catégorisation instable d'articles | Gestion articles/codification | Articles créés au fil de l'eau sans stabilisation préalable | Continu | Risque : recherche/traçabilité compromise ; confusion en case de besoin urgent |
| Quarantaine non clairement distinguée | Gestion stock et qualité | Absence de marquage visible ou de circuit dédié | Régulier | Risque : consommation/dispensation d'article en quarantaine ; non-conformité qualité |
| Dispensation boîte vs unité selon disponibilité | Dispensation | Stock réel ≠ stock requis ; pragmatisme opérationnel | Très fréquent | Risque : surstock ou manque unité ; consommation réelle non alignée prescription |
| Commandes internes informelles en parallèle du système | Approvisionnement interne | Besoin urgent ; confiance dans circuit informel plus rapide | Régulier | Risque : non-enregistrement commande ; écarts stock non expliqués |
| Absence de signature ou signature différée | Validation/traçabilité | Pression temps ; service demandeur absent ; urgence | Observé | Risque : bon sans preuve de validation ; non-conformité traçabilité réglementaire |
| Validation pharmacien "EN ATTENTE" même en urgence | Validation pharmaceutique | Tension : urgence vs rigueur ; validation partielle ou orale | Observé | Risque : livraison sans validation écrite ; écart procédure |

---

## 4. Doubles saisies et traitements hors système

### Doubles saisies identifiées

**1. Prescription papier + Demande SIH**
- **Observation** : Le bon de dispensation structure montre l'avertissement explicite : "Attention à la double saisie entre la prescription papier scannée et la demande transmise au SIH"
- **Support papier** : Bon scanné (OCR) + Bon papier original signé
- **Support électronique** : Demande SIH parallèle
- **Résultat** : Écart potentiel entre quantité prescrite papier et quantité demandée SIH
- **Exemple concret** : Bon PHARM-2026-04-0017 pour M. KOUASSI : prescription papier scannée doit être rapprochée avec demande SIH
- **Risque** : Incohérence, confusion dispensateur, écart quantités

**2. Enregistrement rapide + Saisie détaillée reportée**
- **Observation** : "Lors des réceptions sans interfaçage, les équipes peuvent différer la saisie détaillée complète pour éviter un blocage opérationnel"
- **Support rapide** : Enregistrement basique (réception confirmée)
- **Support détaillé** : Saisie complète reportée (article par article, lots, DLC)
- **Temporalité** : Décalage entre disponibilité réelle en stock et disponibilité déclarée en SIH
- **Risque** : Stock physique ≠ stock théorique immédiatement ; détection tardive d'écarts

**3. Commandes internes informelles**
- **Observation** : "Les commandes internes sont parfois formulées de manière informelle en parallèle du système, puis régularisées ensuite"
- **Support informel** : Communication directe (mail, appel, papier) entre unité de soins et pharmacie
- **Support formel** : Saisie ultérieure dans commande SIH
- **Résultat** : Trace opérationnelle (article fourni) devance trace administrative
- **Risque** : Commande "fantôme" ; écart entre fourniture réelle et commande officielle

### Traitements hors système

**1. Gestion des urgences par adaptation locale**
- Les services expriment des besoins urgents qui conduisent la pharmacie à adapter localement les circuits prévus
- Trace : bons de dispensation marqués "urgente" sans validation finale formelle
- Exemple : Mme ADJOA - priorité urgente, statut "EN ATTENTE DE VALIDATION FINALE" mais dispensation probablement engagée

**2. Gestion implicite des quarantaines**
- Les produits placés en quarantaine ne sont pas toujours clairement distingués
- Aucun circuit dédié formalisé
- Risque opérationnel : confusion entre produit en quarantaine et produit disponible

**3. Ajustement boîte/unité selon disponibilité réelle**
- La dispensation par boîte ou par unité dépend souvent de la disponibilité réelle plus que du schéma théorique prévu
- Décision pragmatique non documentée sur le bon
- Exemple : Ceftriaxone demandée à l'unité → dispensée en boîte selon stock

### Supports utilisés

| Type de traitement | Support utilisé | Fréquence | Risque |
|---|---|---|---|
| Prescription papier | Bon scanné + OCR + archivage papier | Standard | OCR imparfait ; archivage papier non intégré SIH |
| Saisie rapide réception | Pointage basique SIH | En réception sans interfaçage | Délai synchronisation |
| Saisie détaillée reportée | Feuille article par article (papier/Excel supposé) | Régulier | Ressaisie manuelle ; non-traçabilité intermédiaire |
| Commandes urgentes | Mail/appel + note papier | Observé | Communication non enregistrée formellement |
| Gestion inventaire | Inventaire physique + SIH | Régulier | Écarts découverts post-facto |

---

## 5. Tensions urgence / rigueur

### Situations de tension observées

**1. Chirurgie/Bloc opératoire : pression maximale**
- **Contexte** : Besoin urgent de ceftriaxone, sérum physiologique, matériel stérile avant 16h00
- **Tension observée** : Bon marqué "urgente" + observation pharmacien "Préparation à réaliser avant 16h00" + statut "EN ATTENTE DE VALIDATION FINALE"
- **Arbitrage réel** : Validation partielle ou orale plutôt que validation écrite ; dispensation probablement engagée avant signature complète
- **Compromis** : La note du pharmacien devient une consigne d'exécution plutôt qu'un élément de décision validée
- **Conséquence** : Risque que livraison intervienne sans validation écrite complète = écart procédure BPPH

**2. Médecine interne : flux normal mais avec alerte double saisie**
- **Contexte** : Traitement 5-7 jours, prescription claire (paracétamol, amoxicilline)
- **Alerte pharmacien** : "Attention à la double saisie entre la prescription papier scannée et la demande transmise au SIH"
- **Tension** : Le pharmacien doit vérifier concordance papier/SIH + valider conformité médicale + préparer
- **Compromis** : Validation formelle écrite requise mais sous pression de temps
- **Conséquence** : Vérification de double saisie peut être simplifiée ou basée sur confiance plutôt que sur rapprochement documenté

**3. Réception sans interfaçage : saisie reportée**
- **Contexte** : Livraison de marchandise sans interfaçage fournisseur
- **Tension** : Besoin d'enregistrer réception rapidement vs saisie détaillée qui prend du temps
- **Arbitrage observé** : Saisie basique rapide puis saisie détaillée reportée
- **Conséquence** : Stock physique disponible avant stock théorique déclaré en SIH ; décalage de visibilité

**4. Besoin urgent d'unité de soins non prévisible**
- **Contexte** : Service demande article urgemment sans demande SIH préalable
- **Tension** : Besoin opérationnel immédiat vs circuit formel de commande
- **Arbitrage observé** : Fourniture directe + commande informelle + régularisation SIH ultérieure
- **Conséquence** : Trace opérationnelle devance trace administrative ; non-enregistrement possible de fourniture réelle

### Impacts de la tension urgence/rigueur

| Situation | Rigueur prescrite | Rigueur réelle | Simplifié | Impact |
|---|---|---|---|---|
| Chirurgie urgente | Validation écrite complète avant dispensation | Validation orale/partielle ou dispensation avant finalisation | Signature différée ou omise | Non-conformité BPPH ; validation insuffisante |
| Double saisie en flux normal | Rapprochement documenté papier/SIH | Vérification visuelle rapide ou basée sur confiance | Rapprochement non systématique | Risque incohérence persistante |
| Réception sans interfaçage | Saisie complète immédiate | Saisie basique rapide + reportée | Détails (lots, DLC) non saisis immédiatement | Délai tracé complet ; écarts détectés tardivement |
| Commande urgente informelle | Commande SIH formelle avant fourniture | Fourniture directe + commande postérieure | Commande formelle omise ou retardée | Fourniture non enregistrée ; écart stock |

### Observations des équipes

- Les pharmaciens validateurs doivent arbitrer sans protocole formalisé cet arbitrage
- Les préparateurs doivent accélérer préparation sans indication claire de quand réduire rigueur de contrôle
- Les services demandeurs initialisent plusieurs flux en parallèle par manque de confiance en délais du circuit formel
- Pression chronique : rapidité attendue vs rigueur exigée = charge cognitive importante

---

## 6. Écarts de traçabilité

### Situations sans traçabilité prescrite assurée

**1. Stupéfiants : traçabilité fragmentée**
- **Observation** : Aucun document fourni spécifiquement sur traçabilité des stupéfiants
- **Risque potentiel** : Stupéfiants présents dans circuit (ex. morphine, dérivés) mais aucune trace visible de contrôle dédié
- **Hypothèse** : Traçabilité probable par registre papier séparé (non fourni en documents)
- **Impact** : Impossible de vérifier conformité traçabilité stupéfiants ; écart potentiel avec exigences légales

**2. DMI (Dispositifs Médicaux Implantables) : non scanné**
- **Observation** : Bon de dispensation mentionne "DMI-102 Cathéter veineux périphérique 20G" + "Matériel de réserve"
- **Trace** : Inscription sur bon papier structure ; aucun scan documenté ni numéro lot/DLC visible
- **Absence** : Pas de traçabilité unitaire ; numéro de série non requis sur bon
- **Risque** : Impossible tracer cathéter spécifique jusqu'à patient en cas incident ; conformité SMDCR non vérifiable

**3. Articles en quarantaine : sortie non enregistrée**
- **Observation** : "Les produits placés en quarantaine ne sont pas toujours clairement distingués"
- **Traçabilité absente** : Aucun circuit dédié ; pas de marquage visible
- **Risque** : Consommation d'article en quarantaine non documentée ; traçabilité rupture qualité perdue
- **Exemple concret** : Article créé/catégorisé de manière instable → quarantaine oubliée → consommé sans documenté non-conformité

**4. Médicaments à risque : ajustement quantité non tracé**
- **Observation** : "La dispensation par boîte ou par unité dépend souvent de la disponibilité réelle plus que du schéma théorique prévu"
- **Exemple** : Prescription ceftriaxone 2 flacons unitaires → Dispensation 1 boîte (5 flacons) selon stock
- **Non tracé** : La décision de dispensation en boîte au lieu d'unité n'est pas documentée sur bon
- **Risque** : Surstock à l'unité de soins ; médicaments supplémentaires non assignés patient

**5. Sorties de stock informelles : non enregistrées**
- **Observation** : "Les commandes internes sont parfois formulées de manière informelle en parallèle du système, puis régularisées ensuite"
- **Traçabilité absente** : Fourniture directe avant enregistrement SIH
- **Délai** : Écart temporel entre fourniture opérationnelle et enregistrement administratif
- **Risque** : Fourniture jamais enregistrée officiellement ; écart stock permanent

**6. Divergence quantité commandée ≠ quantité consommée**
- **Observation** : "Les écarts entre quantités demandées, quantités délivrées et quantités réellement consommées ne sont pas toujours visibles immédiatement"
- **Découverte** : Lors d'inventaires seulement
- **Traçabilité absente** : Aucun point de contrôle intermédiaire pour détecter divergence
- **Exemple** : Bon demande 15 paracétamol → Dispensation 15 → Consommation effective 12 → Découverte écart lors inventaire
- **Risque** : Stocks fantômes ; gestion réapprovisionnement basée sur fausse consommation

**7. Double saisie prescription papier/SIH : divergence non tracée**
- **Observation** : "Attention à la double saisie entre la prescription papier scannée et la demande transmise au SIH"
- **Traçabilité fragmentée** : Deux sources de vérité possibles (papier scanné vs SIH)
- **Risque** : En cas divergence (ex. quantité différente), quelle est source officielle ?
- **Impact** : Impossible retracer si dispensation a suivi papier ou SIH en cas incident

**8. Signature service/pharmacie différée ou omise**
- **Observation** : Bon PHARM-2026-04-0018 "EN ATTENTE DE VALIDATION FINALE" malgré urgence
- **Traçabilité absente** : Aucune preuve écrite que service demandeur a reçu et accepté médicament
- **Risque** : Impossible prouver qui a reçu quoi et quand en cas question ultérieure

### Tableau synthétique écarts traçabilité

| Type produit/situation | Traçabilité prescrite | Traçabilité observée | Élément manquant | Fréquence | Impact réglementaire |
|---|---|---|---|---|---|
| Stupéfiants | Registre + traçabilité unitaire par patient | Probable registre papier séparé (non visible en docs) | Pas de documentation fournie | Invisible | Non-conformité légale possible |
| DMI (cathéter, etc.) | Numéro de série + lot + DLC + patient | Bon papier seulement + pas de numéro série visibles | Numéro série, lot, DLC, scannage | Systématique | Non-conformité SMDCR |
| Articles en quarantaine | Marquage + circuit dédié + tracé sortie | Aucun circuit dédié, implicite | Circuit, marquage, registre | Régulier | Risque consommation non-conforme |
| Ajustement boîte/unité | Justification dispensation vs prescription | Décision pragmatique non documentée | Justification écrite | Très fréquent | Écart prescription vs réalité non tracé |
| Sorties informelles | Enregistrement immédiat SIH | Régularisation ultérieure | Délai enregistrement | Régulier | Écart stock temporaire |
| Divergence demande/consommation | Contrôle points intermédiaires | Découverte lors inventaire uniquement | Points de contrôle intermédiaires | Régulier | Gestion stock inexacte |
| Double saisie papier/SIH | Rapprochement avant dispensation | Vérification rapide ou non-systématique | Rapprochement documenté | Fréquent | Incohérence prescription possible |
| Signature différée/omise | Signature avant dispensation | Signature postérieure ou absente | Preuve réception patient | Observé en urgence | Non-conformité BPPH |

---

## 7. Irritants opérationnels

### Points de friction vécus par les équipes

**Irritants pour les équipes pharmaceutiques**

| Irritant | Fréquence | Manifestation | Impact vécu |
|---|---|---|---|
| Absence interfaçage réception fournisseur | Régulier | Saisie manuelle complète des réceptions sans données fournisseur | Charge administrative importante ; double travail saisie rapide + saisie détaillée |
| Incohérence prescription papier/SIH | Fréquent | Avertissement explicite sur bons : "Attention à la double saisie" | Validation supplémentaire requise ; perte de temps rapprochement |
| Catégorisation instable d'articles | Continu | Articles créés au fil de l'eau sans stabilisation préalable | Confusion au moment de la recherche ; traçabilité compromise |
| Pression urgence chirurgicale | Régulier | Bon "EN ATTENTE DE VALIDATION FINALE" malgré urgence ; pression délai avant 16h00 | Arbitrage rapide rigueur/rapidité ; stress cognitif ; risque validation insuffisante |
| Gestion implicite quarantaines | Régulier | Produits en quarantaine non clairement marqués ; risque consommation | Vigilance permanente requise ; charge de contrôle informelle |
| Besoin urgent non prévisible | Régulier | Service appelle directement pour besoin urgent au lieu de SIH ; commande informelle | Charge arbitrage ad hoc ; régularisation administrative ultérieure ; désorganisation prévisionnel stock |
| Inventaires révélant écarts | Régulier | Écarts découverts post-facto entre stock théorique et physique | Investigation temps écoulé ; impossible retracer divergence ; effort de réconciliation |
| Droits d'accès non alignés | Régulier | Droits d'accès aux magasins ne sont pas toujours perçus comme alignés avec responsabilités réelles | Frustration, accès restreint pour certains alors que responsabilité assignée |

**Irritants pour les services demandeurs (unités de soins)**

| Irritant | Fréquence | Manifestation | Impact vécu |
|---|---|---|---|
| Délai circuit formel trop long | Régulier | Service envoie demande SIH + appelle directement car doute sur délai | Circuit perçu comme non-fiable pour urgence ; parallélisation des demandes |
| Attente validation pharmacie | Régulier | Bon "EN ATTENTE DE VALIDATION FINALE" retarde dispensation | Frustration urgence ; contournement par appel direct |
| Incertitude quantité dispensée vs demandée | Régulier | Dispensation boîte au lieu d'unité selon stock ; unité de soins reçoit plus qu'attendu | Stock supplémentaire non assigné patient ; confusion quantité réelle disponible |
| Double saisie prescription papier/SIH | Fréquent | Service envoie prescription papier + saisit demande SIH en parallèle | Charge double saisie ; risque incohérence si correction nécessaire |
| Absence feedback disponibilité | Régulier | Service ne sait pas si article en rupture stock pharmacie ; rappel sans réponse | Attente indéfinie ; incertitude approvisionnement |

**Irritants partagés pharmacie + unités de soins**

| Irritant | Fréquence | Manifestation | Impact vécu |
|---|---|---|---|
| Écart stock théorique vs physique | Régulier | Inventaires révèlent divergences ; impossible retracer cause | Perte de confiance stock théorique ; planification approvisionnement inexacte |
| Rupture de stock imprévisible | Fréquent en flux tendu | Article prescrit non disponible ; adaptation locale (substitution implicite ou boîte au lieu d'unité) | Frustration ; impact patient (changement thérapeutique informel) |
| Quarantaine mal communiquée | Régulier | Produit en quarantaine consommé accidentellement faute de clarté | Incident qualité ; traçabilité rupture non documentée |
| Trace administrative fragmentée | Systématique | Plusieurs supports (papier, SIH, cahier informel) ; aucune source unique de vérité | Effort réconciliation constant ; risque incohérence ; charge charge travail |

---

## 8. Effets observés

### Effets sur la sécurité patient

**Risques identifiés**

1. **Validation pharmaceutique incomplète en urgence**
   - Observation : Bon "EN ATTENTE DE VALIDATION FINALE" livré en cas urgence
   - Conséquence : Validation orale ou partielle ; risque erreur non détectée (dosage, interaction, allergie)
   - Exemple concret : Amoxicilline sans vérification absence allergie pénicilline si validation simplifiée en urgence

2. **Dispensation boîte au lieu d'unité prescrite**
   - Observation : "La dispensation par boîte ou par unité dépend souvent de la disponibilité réelle plus que du schéma théorique prévu"
   - Conséquence : Surstock à l'unité de soins ; médicaments supplémentaires non assignés patient ; risque confusion, mauvaise administration
   - Exemple : Paracétamol demandé 15 unités, dispensé 30 (boîte) = 2x stock prévu

3. **Traçabilité DMI compromise**
   - Observation : Cathéter veineux périphérique sans numéro de série sur bon
   - Conséquence : Impossible identifier cathéter spécifique en cas incident (thrombose, infection) ; traçabilité chaîne stérile perdue
   - Impact : Non-conformité réglementaire SMDCR ; incapacité analyse incident

4. **Consommation produit en quarantaine**
   - Observation : Produits en quarantaine non clairement distingués ; aucun circuit dédié
   - Conséquence : Consommation accidentelle de produit non-conforme ; risque patient selon type non-conformité
   - Exemple : Médicament étiqueté mal ou légèrement endommagé, consommé malgré quarantaine

5. **Double saisie prescription papier/SIH : incohérence**
   - Observation : Alerte explicite "Attention à la double saisie entre la prescription papier scannée et la demande transmise au SIH"
   - Conséquence : Divergence quantité ou molécule possible ; dispensation basée sur source incohérente
   - Exemple : Prescription papier demande paracétamol 15 unités, SIH enregistre 20 unités → dispensation 20 au lieu de 15

6. **Commandes urgentes orale : non documentée**
   - Observation : Services expriment besoins urgents par appel direct
   - Conséquence : Prescription orale non écrite ; absence preuve prescription officielle ; risque erreur transmission
   - Impact : Impossible retracer prescription originale en cas complication

**Synthèse sécurité patient**

| Risque | Probabilité | Gravité | Détection | Atténuation |
|---|---|---|---|---|
| Validation pharmaceutique incomplète | Élevée en urgence | Potentiellement grave (interaction, dosage) | Post-incident | Aucune à date |
| Surstock par dispensation boîte | Très élevée | Modérée (confusion probable, faible risque erreur) | Inventaire | Aucune systématique |
| Traçabilité DMI perdue | Certaine | Grave si incident (infection, thrombose) | Post-incident | Aucune |
| Consommation produit quarantaine | Modérée | Modérée à grave selon type | Probable par contrôle qualité | Vigilance informelle |
| Incohérence papier/SIH | Fréquente | Modérée (divergence possible) | Validation pharmacien | Alerte explicite requise |
| Prescription orale | Régulière en urgence | Modérée | Post-incident | Aucune |

---

### Effets sur la traçabilité réglementaire

**Conformité BPPH compromise**

1. **Validation avant dispensation non systématique**
   - BPPH article 2.2.4 : "Chaque dispensation doit faire l'objet d'une validation pharmaceutique avant le départ du médicament"
   - Observation : Bons "EN ATTENTE DE VALIDATION FINALE" livré avant validation écrite
   - Écart : Non-conformité BPPH directe

2. **Traçabilité dispensation fragmentée**
   - BPPH : Obligation traçabilité unitaire, lot, patient, date
   - Observation : DMI sans numéro de série ; double saisie papier/SIH ; commandes informelles non enregistrées
   - Écart : Traçabilité incomplete selon SIH ; source papier déconnectée

3. **Gestion stupéfiants non visible**
   - Loi : Registre stupéfiants obligatoire avec traçabilité nominative
   - Observation : Aucun document fourni sur traçabilité stupéfiants
   - Écart : Impossible vérifier conformité légale

4. **Signature patients/services non systématique**
   - BPPH : Réception et acceptation documentées
   - Observation : Bon en attente signature
   - Écart : Non-conformité preuve réception

5. **Saisie différée en réception**
   - BPPH article 2.1.2 : Enregistrement immédiat réception
   - Observation : Saisie basique rapide + saisie détaillée reportée
   - Écart : Délai enregistrement ; écart temporel stock théorique/réel

**Impact réglementaire**

- Audit réglementaire aurait identifié écarts systématiques conformité BPPH
- Non-conformités critiques : validation absent, traçabilité fragmentée, stupéfiants non tracés
- Responsabilité directeur pharmacie engagée par ces écarts

---

### Effets sur la gestion des stocks

**Visibilité stock compromise**

1. **Écart permanent stock théorique/physique**
   - Observation : "Les inventaires mettent régulièrement en évidence des écarts entre stock théorique et stock physique"
   - Conséquence : Planification approvisionnement basée sur stock faux ; ruptures imprévisibles ; surstock sur certains articles
   - Exemple : Paracétamol théorique 100, physique 85 → commande basée sur 100 = sous-approvisionnement réel

2. **Écart demande/consommation non tracé**
   - Observation : "Les écarts entre quantités demandées, quantités délivrées et quantités réellement consommées ne sont pas toujours visibles immédiatement"
   - Conséquence : Consommation réelle inconnue jusqu'à inventaire ; gestion réapprovisionnement sur estimé faux
   - Exemple : Ceftriaxone demandée 2 flacons, consommation réelle 1 flacon → 1 flacon perdu, non-tracé

3. **Dispensation boîte au lieu d'unité crée surstock**
   - Observation : Pragmatisme : dispensation selon disponibilité réelle (boîte vs unité)
   - Conséquence : Unité de soins reçoit surplus ; stock local imprécis ; articles restituables jamais retracés
   - Exemple : Demande 4 seringues 10mL, dispensation boîte 50 = 46 seringues non assignées

4. **Commandes informelles non enregistrées**
   - Observation : "Les commandes internes sont parfois formulées de manière informelle en parallèle du système, puis régularisées ensuite"
   - Conséquence : Stock délivré sans enregistrement SIH immédiat ; écart temporaire stock théorique
   - Exemple : Infirmiers reçoivent cathéters directement, commande SIH 2 jours après = 2 jours sans enregistrement

5. **Quarantaine non clairement distinguée**
   - Observation : "Les produits placés en quarantaine ne sont pas toujours clairement distingués"
   - Conséquence : Produits en quarantaine inclus dans stock théorique disponible ; consommation erreur réduit stock sans raison logique

**Impact gestion stocks**

| Problème | Fréquence | Effet stock théorique | Effet stock physique | Conséquence |
|---|---|---|---|---|
| Écart théorique/physique | Régulier | Faux | Réel | Planification inexacte |
| Divergence demande/consommation | Régulier | Stock surnuméraire | Réalité inconnue | Gestion réapprovisionnement fausse |
| Boîte vs unité | Très fréquent | Correct | Imprécis (stock local) | Unité de soins stock inexact |
| Commandes informelles | Régulier | Décalage temporaire | Avancé | Écart transitoire |
| Quarantaine implicite | Régulier | Inclus (faux) | Partiellement disponible | Surstock théorique |

---

### Effets sur la conformité aux BPPH

**Écarts systématiques identifiés**

1. **Absence validation pharmaceutique écrite**
   - Article 2.2.4 BPPH : Validation avant départ
   - Observation : Bons "EN ATTENTE DE VALIDATION FINALE" en circulation
   - Conformité : **Non-conforme**

2. **Traçabilité unitaire incomplète**
   - Article 2.2.6 BPPH : Traçabilité lot + numéro de série (DMI)
   - Observation : DMI sans numéro de série ; stupéfiants non visibles ; double saisie papier/SIH
   - Conformité : **Partiellement conforme** (dépend du SIH interne)

3. **Enregistrement réception non immédiat**
   - Article 2.1.2 BPPH : Enregistrement immédiat
   - Observation : Saisie rapide + saisie détaillée reportée
   - Conformité : **Non-conforme**

4. **Signature réception/acceptation**
   - BPPH : Preuve réception documentée
   - Observation : Signatures différées ou omises en urgence
   - Conformité : **Non-conforme en urgence**

5. **Gestion quarantaine**
   - BPPH article 2.1.6 : Séparation produits non-conformes
   - Observation : Aucun circuit dédié, implicite
   - Conformité : **Non-conforme**

6. **Contrôle double saisie**
   - BPPH : Unicité source de données
   - Observation : Prescription papier + SIH en parallèle ; alerte explicite double saisie
   - Conformité : **Non-conforme** (sources multiples sans réconciliation systématique)

**Résumé conformité BPPH**

- **Articles critiques non-conformes** : Validation, enregistrement réception, signatures, quarantaine
- **Gravité** : Écarts sévères affectant traçabilité et sécurité patient
- **Portée** : Systématique (observation terrain), non exceptions
- **Responsabilité** : Directeur pharmacie à date des faits

---

### Effets sur la charge de travail des équipes

**Charge administrative accrue**

1. **Saisie manuelle reportée**
   - Observation : Saisie rapide + saisie détaillée ultérieure sans interfaçage
   - Charge : Préparateur saisit réception 2 fois (basique + détaillée)
   - Temps additionnel : Estimé +30-40% sur réception

2. **Vérification double saisie**
   - Observation : Alerte "Attention à la double saisie entre papier et SIH"
   - Charge : Pharmacien rapproche prescription papier scanée + demande SIH
   - Temps additionnel : 5-10 min/bon en flux normal

3. **Arbitrage urgence ad hoc**
   - Observation : Besoin urgent exprimé directement → adaptation locale décidée au cas par cas
   - Charge : Pharmacien arbitrage rapide rigueur/rapidité sans protocole
   - Impact : Stress cognitif ; charge décision non-structurée

4. **Investigation écart stock**
   - Observation : Écarts découverts lors inventaire → investigation cause
   - Charge : Heures d'investigation post-facto ; tentative retraçage
   - Temps additionnel : Estimé plusieurs heures par inventaire

5. **Gestion implicite quarantaine**
   - Observation : Produits en quarantaine sans marquage → vigilance permanente
   - Charge : Mémorisation produits en quarantaine ; vérification visuelle
   - Impact : Charge cognitive importante ; erreur possible

**Charge de communication**

1. **Appels directs services**
   - Observation : Services contournent circuit formel par appel direct
   - Charge : Pharmacien/préparateur interrompu pour demande urgente
   - Fréquence : Régulier ; impact : fragmentation attention

2. **Régularisation commandes informelles**
   - Observation : Fourniture directe + commande SIH ultérieure
   - Charge : Ressaisie commande pour traçabilité ; ajustement SIH
   - Temps additionnel : 5-10 min/commande informelle

3. **Appels absence feedback availability**
   - Observation : Service appelle pour savoir si article disponible
   - Charge : Répondre appels sans vue systématique disponibilité
   - Impact : Interruptions répétées

**Impact charge totale**

- **Estimé surcharge** : 20-30% du temps préparateur/pharmacien sur tâches manuelles/reporting vs activités à valeur ajoutée
- **Fragmentation attention** : Interruptions régulières ; impact concentration
- **Stress chronique** : Arbitrage urgence constant ; charge décision non structurée
- **Rotation équipe** : Charge importante peut contribuer turnover équipe

---

## Synthèse transversale : Les trois mondes en tension

### Le monde prescrit (BPPH, SIH, processus formel)

- Validation écrite obligatoire avant dispensation
- Enregistrement immédiat réception
- Traçabilité unitaire lot/numéro de série
- Signature preuve réception
- Unicité source de données (SIH)

### Le monde réel observé (terrain)

- Validation orale/partielle en urgence
- Saisie rapide + saisie détaillée reportée
- Traçabilité fragmentée papier/SIH/implicite
- Signatures différées ou omises en urgence
- Multiples sources : papier scanné + SIH + commandes informelles + cahiers

### Le monde vécu des équipes

- Tension permanente rapidité/rigueur
- Besoin urgent > circuit formel perçu comme lent
- Adaptation locale pour fluidité opérationnelle
- Charge de réconciliation administrative constant
- Frustration droits d'accès vs responsabilités

### Points de rupture entre mondes

1. **Urgence chirurgicale** : Prescription → Dispensation sans validation écrite
2. **Réception sans interfaçage** : Réception physique → Saisie théorique reportée
3. **Besoin urgent non prévisible** : Fourniture directe → Commande SIH postérieure
4. **Écart stock** : Stock physique diverge stock théorique → Découverte tardive inventaire
5. **DMI** : Prescription sur bon → Pas de numéro de série

**Caractère systématique des écarts** : Les observations ne décrivaient pas des exceptions, mais des pratiques régulières, prévisibles et adaptées au contexte réel opérationnel.