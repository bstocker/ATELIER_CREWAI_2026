# Fiche des pratiques réelles — Admission-Facturation

## 1. Déroulement réel du circuit

### Flux standard observé (cas nominal)
1. **Arrivée et accueil initial** : Le patient arrive avec ou sans dossier papier. L'agent d'accueil procède à l'identification et crée une admission avec un IPP provisoire (ex. ADM-2026-0042).
2. **Collecte d'informations** : Les données administratives et cliniques sont recueillies partiellement à l'accueil, souvent sur papier (formulaire d'admission partiel, registre manuel).
3. **Création de l'admission** : Une admission est créée dans le SIH même si tous les champs requis ne sont pas renseignés, pour ne pas bloquer la prise en charge clinique.
4. **Régularisation a posteriori** : Les informations manquantes sont complétées ultérieurement par des agents en arrière-plan.
5. **Dispense pharmaceutique** : La pharmacie dispense des produits sans attendre le rapprochement immédiat avec le dossier administratif.
6. **Imputation des prestations** : Les actes et prestations sont imputés au dossier patient, parfois avec retard.
7. **Contrôles avant facturation** : Des contrôles de complétude et de conformité sont effectués, mais souvent tardivement dans le processus.
8. **Facturation** : Génération de la facture sur la base du dossier administratif et clinique consolidé.

### Variations observées selon le contexte

**En période de forte affluence (urgences, pics d'admission)** :
- L'accueil privilégie la **fluidité** au détriment de la complétude immédiate.
- Les champs obligatoires ne sont remplis que partiellement.
- Les numéros de téléphone et contacts ne sont pas toujours vérifiés à l'accueil.
- L'admission est créée rapidement avec l'IPP provisoire, et la régularisation administrative est repoussée.

**Cas patient sans droits déclarés ou couverture administrative manquante** :
- L'admission n'est pas bloquée malgré l'absence de mutuelle ou d'information de droits.
- La vérification des droits est repoussée à une phase ultérieure.
- Un ajustement facturation est réalisé une fois la couverture clarifiée.

**Cas patient avec dossier papier complet vs partiel** :
- Dossier complet : ressaisie directe dans le SIH, création admission rapide.
- Dossier partiel : double vérification et recherche d'information par appel ou mail à posteriori.

---

## 2. Acteurs réellement mobilisés

| Acteur | Rôle prescrit | Rôle réel observé | Écarts notables |
|--------|---------------|-------------------|-----------------|
| **Agent d'accueil / Accueil** | Collecter les infos administratives, créer l'admission, saisir dans le SIH | Crée l'admission rapidement avec infos partielles. Privilégie la fluidité. Recueille infos sur papier en parallèle. Ne vérifie pas systématiquement les numéros de contact. | Création d'admissions incomplètes. Pas de validation immédiate. Double support (papier + SIH). |
| **Équipe clinique (médecin, infirmier)** | Assurer la prise en charge clinique | Acceptent l'admission incomplète pour commencer les soins. Signalent parfois les informations manquantes. | Pas de blocage de la prise en charge en attente de complétude administrative. |
| **Pharmacie** | Dispenser les produits prescrits | Dispense sans attendre le rapprochement administratif du dossier. Enregistre les dispensations en parallèle. | Dispensations effectuées avant consolidation du dossier administratif. |
| **Équipe de régularisation / Arrière-office administratif** | Non explicitement défini dans le formel | Procèdent à la complétude du dossier a posteriori : vérification des droits, corrections numéros, recherche d'informations manquantes. | **Acteur "implicite"** qui absorbe les lacunes de l'accueil. Travail informel. |
| **Contrôle qualité / Facturation** | Vérifier la complétude avant facturation | Effectuent les contrôles, mais **tardivement** dans le processus. Détectent les erreurs peu de temps avant la facturation. | Risque de rejet ou de refacturation élevé. Peu de temps pour correction. |

---

## 3. Contournements identifiés

| Contournement observé | Étape concernée | Raison probable | Fréquence estimée | Impact observé |
|----------------------|-----------------|-----------------|-------------------|-----------------|
| Création d'admission avec champs obligatoires non remplis | Création de l'admission (étape 3) | Urgence de commencer les soins. Fluidité du flux en période affluente. Éviter de bloquer le patient en accueil. | **Fréquent en urgences, pics d'admission** ; moins fréquent en consultations externes | Dossier incomplet au moment de l'admission. Régularisation ultérieure nécessaire. Risque d'erreur ou d'oubli. |
| Vérification des droits/mutuelle repoussée à posteriori | Collecte d'informations administratives (étape 2) | Manque de données au moment de l'admission. Patient ne dispose pas de sa carte vitale. Processus de vérification lent. | **Fréquent** (observé dans cas MARTIN Claire) | Retard dans la facturation. Ajustements facturation ultérieurs. Imputation provisoire puis correction. |
| Double saisie : papier → SIH réalisée manuellement et ultérieurement | Saisie des admissions (étape 2-3) | Accueil recueille sur papier, puis ressaisie dans le SIH en arrière-office. Absence d'intégration directe papier-SIH. | **Très fréquent** (explicitement noté dans le formulaire OCR) | Temps supplémentaire. Risque d'erreurs de transcription. Données divergentes papier vs SIH. |
| Non-rapprochement immédiat pharmacie-dossier administratif | Dispense pharmaceutique (étape 5) | Pharmacie opère indépendamment. Pas de synchronisation temps réel avec le dossier administratif. | **Systématique** | Traçabilité affaiblie. Risque de dispensations non imputées ou imputées à mauvais dossier. |
| Report des contrôles avant facturation | Contrôle de complétude (étape 7) | Contrôles effectués trop tard. Pas de contrôle en temps réel lors de la création. | **Systématique** | Détection tardive des anomalies. Peu de temps pour correction. Refacturations fréquentes. |
| Vérification des contacts/numéros repoussée après admission | Collecte d'info administratives (étape 2) | Surcharge en accueil. Pas de temps pour vérification. | **Fréquent** (noté dans dossier MARTIN : "numéro doit être vérifié à l'accueil") | Données de contact inexactes. Difficultés pour joindre le patient. Courriers non reçus. |
| Admission créée sans consentement signé | Formalités administratives (étape 1-2) | Urgence clinique. Patient en incapacité de signer. Processus de consentement considéré non-critique pour accueil. | **Fréquent en urgences** ; moins en secteur programmé | Consentement recueilli ultérieurement ou pas du tout. Risque légal faible mais présent. |

---

## 4. Doubles saisies et traitements hors système

### Doubles saisies identifiées

| Opération | Support primaire | Support secondaire | Moment de ressaisie | Raison |
|-----------|------------------|-------------------|---------------------|--------|
| **Données d'admission patient** | Formulaire papier | SIH (ressaisie manuelle) | Ultérieurement (arrière-office) | Accueil recueille sur papier, pas de capture directe numérique. |
| **Registre d'admission** | Registre manuel (cahier/feuille) | SIH | Fin de journée ou lendemain | Tenue manuelle parallèle au SIH. |
| **Informations de contact** | Formulaire papier / verbal | SIH | Vérification ultérieure | Vérification des numéros après admission, correction si nécessaire. |

### Traitements hors système

| Opération | Support utilisé | Raison | Fréquence |
|-----------|-----------------|--------|-----------|
| **Collecte initiale données administratives** | Papier (formulaire d'admission, dossier patient papier) | Processus d'accueil "hérité". Pas d'outil de capture numérique direct. | **Systématique** |
| **Tenue de registre d'admission** | Cahier / registre manuel (papier) | Traçabilité locale, statut de chaque admission en temps réel. | **Systématique** |
| **Régularisation et corrections a posteriori** | Notes manuscrites, corrective mails internes, commentaires dans le dossier SIH | Correction des données avant facturation. | **Fréquent** |
| **Coordination avec pharmacie** | Messages informels (mail, appel, passage physique) | Pharmacie et admission ne sont pas intégrées informatiquement. Coordination manuelle. | **Systématique** |
| **Vérification des droits** | Appels téléphoniques aux organismes de prise en charge, consultation externe de bases de données (Ameli, etc.) | Vérification différée, en arrière-office. | **Fréquent** |
| **Archivage documents papier** | Dossier patient papier, classeur d'admission | Conservation locale de preuves (pièce d'identité, consentement, dossier médical papier). | **Systématique** |

---

## 5. Coordinations informelles

### Modes de coordination observés

| Mode | Entre qui | Contenu / Raison | Fréquence | Support |
|------|-----------|-----------------|-----------|---------|
| **Appel téléphonique ou passage physique** | Accueil ↔ Arrière-office administratif | Clarification d'une donnée manquante, correction avant saisie SIH. | **Fréquent** en cas d'admission incomplète | Téléphone direct, visite à la zone administrative |
| **Mail interne** | Arrière-office ↔ Pharmacie | Confirmation dispensation patient, liaison assiette facturation pharmaceutique. | **Régulier** | Email interne, pas de flux systématisé |
| **Passage physique / verbal direct** | Accueil ↔ Médecin/Infirmier | Confirmation patient admis, justification de l'admission incomplète ("patient arrivé par urgence, ne pouvait pas attendre"). | **Fréquent** en urgences | Face-à-face, discussions informelles |
| **Appel de clarification** | Arrière-office ↔ Patient ou tiers | Vérification numéro contact, confirmation couverture sociale, demande doc manquant. | **Fréquent** | Appel téléphonique direct au patient ou à la mutuelle |
| **Note / Commentaire** | Accueil → Dossier SIH (champ libre ou historique) | Signalisation des anomalies ("dossier papier incomplet", "à vérifier", "patient sans droits"). | **Fréquent** | Champs libres du SIH, commentaires texte |
| **Validation informelle par-dessus l'épaule** | Contrôle qualité ↔ Agent saisie | Avant facturation, vérification rapide des données saisies, feedback direct. | **Régulier** | Conversation face-à-face, relecture physique du dossier |

---

## 6. Irritants opérationnels

### Principaux points de friction

| Irritant | Description / Manifestation | Fréquence | Impact sur l'agent / la qualité |
|----------|---------------------------|-----------|-------------------------------|
| **Surcharge accueil en pics d'affluence** | Impossibilité de collecter complètement l'info administrative lors de pics (urgences, matin). Agents pressés, priorité au flux de patients. | **Très fréquent** (remarqué en urgences) | Frustration : agents savent que données sont incomplètes mais ne peuvent pas ralentir le flux. Stress de créer des dossiers qu'on sait imparfaits. |
| **Absence de données au moment de l'admission** | Patients sans carte vitale, sans droits déclarés, dossier papier incomplet. Impossible de vérifier les droits immédiatement. | **Fréquent** | Retard de facturation. Réadaptation ultérieure du dossier. Charge de travail repoussée à l'arrière-office. |
| **Double saisie manuelle papier → SIH** | Obligation de transcrire à la main les données du formulaire papier dans le SIH. Consomme du temps, génère erreurs. | **Très fréquent** (explicitement noté) | Frustration majeure : travail répétitif, perte de temps. Risque d'erreur élevé (transposition, oubli, lecture manuscrite difficile). Agents découragés. |
| **Vérification des numéros repoussée** | Numéros de contact saisis à l'accueil sans vérification. Découverte d'erreurs tardivement. | **Fréquent** | Impossibilité de joindre le patient pour confirmation ultérieure. Courriers retournés. Frustration au moment de l'utilisation du contact. |
| **Manque de synchronisation pharmacie-dossier** | Pharmacie dispense sans vérifier que le dossier administratif est à jour. Risque de dispensations imputées à mauvais dossier ou non imputées. | **Systématique** | Tension entre services. Rejet de factures. Recherche manuelle de concordance. |
| **Contrôles tardifs avant facturation** | Anomalies découvertes trop tard. Peu de temps pour corriger. Facturation repoussée. | **Systématique** | Stress avant clôture de période. Refacturations. Délai facturation allongé. |
| **Absence de consentement signé en urgences** | Patient arrive en urgence, consentement non signé à l'accueil. Récupération ultérieure difficile. | **Fréquent en urgences** | Risque légal latent. Tracabilité imparfaite. Insécurité juridique. |
| **Flux d'information lent entre services** | Accueil, pharmacie, clinique, facturation ne communiquent pas en temps réel. Information parcellaire, aller-retour fréquents. | **Systématique** | Délais allongés. Itérations multiples. Agent remet en question plusieurs fois les mêmes points. Frustration cumulée. |
| **Impossibilité de passer à l'étape suivante sans attendre** | Contrôle en attente, régularisation suspendue. Agent bloqué, ne peut pas avancer si info manquante. | **Fréquent** | Sensation d'impuissance. Dossiers stagnent en cours de traitement. Sentiment de débordement. |
| **Charge administrative pour équipe clinique réduite** | Médecins/infirmiers doivent parfois clarifier des données administratives avec patients. Déborde sur temps clinique. | **Régulier** | Frustration équipe clinique : n'est pas leur rôle. Détournement de temps. Mauvaise qualité de prise en charge ou retard. |

---

## 7. Cas non couverts par le formel

### Situations hors du processus prescrit

| Situation | Fréquence | Comment l'équipe la gère en pratique | Efficacité / Risques |
|-----------|-----------|---------------------------------------|----------------------|
| **Patient arrive en urgence sans aucune documentation** | **Fréquent** | Création admission avec données verbales, données minimales. Collecte exhaustive repoussée. Pièce d'identité reçue sur place ou vérifiée ultérieurement. | Risque : mauvaise identité. Charge de régularisation importante. |
| **Couverture sociale inconnue ou refusée** | **Fréquent** | Admission créée quand même (pas de blocage). Vérification des droits déléguée à l'arrière-office. Patient peut être imputé en tiers payant ou en tiers restant selon hypothèse. | Risque : facturation incorrecte jusqu'à clarification. Ajustements répétés. |
| **Patient mineur sans représentant légal présent** | **Occasionnel** | Admission créée. Consentement reçu verbalement. Recherche du représentant a posteriori. | Risque légal. Soin prodigué avant formalités complètes. |
| **Dossier papier reçu en pièces détachées (complété par tranches)** | **Régulier** | Admission créée sur base de pièces disponibles. Complément reçu jours après. Ressaisie piecemeal dans SIH. | Risque : données incohérentes. Dossier fragmenté. Délai de consolidation long. |
| **Pharmacie dispense avant imputation administratif finalisée** | **Systématique** | Dispense effectuée sur base de prescription clinique. Imputation à dossier patient repoussée après consolidation administrative. | Risque : dispensations orphelines. Rejet facturation. Recherche manuelle de concordance. |
| **Contact patient erroné (numéro faux, adresse incomplète)** | **Fréquent** | Découverte lors de tentative de contact ultérieure. Correction manuelle. Parfois impossible de joindre le patient après. | Risque : courriers non livrés, suivi patient compromis. |
| **Absence de vérification consentement en urgences** | **Fréquent** | Patient soigné d'abord. Consentement recherché tardivement. Parfois jamais obtenu formellement. | Risque légal. Absence de traçabilité formelle. |
| **Changement couverture sociale pendant séjour (ex. nouvelle affiliation)** | **Occasionnel** | Dossier reçoit info en cours de séjour. Ajustement facturation réalisé ultérieurement. Rétroactif imputé différemment. | Risque : facture incohérente. Demande d'ajustement ultérieure. |
| **Patient refuse de fournir infos (sans droits, situation administrative flou)** | **Occasionnel** | Admission créée avec données minima. Traitement "au cas par cas" par l'arrière-office. Recours à des tiers (assistant social, travailleurs sociants) si besoin. | Risque : dossier restera incomplet. Facturation provisoire longtemps. |
| **Flux tendu : admission doublée par erreur (IPP différent pour même patient)** | **Occasionnel mais grave** | Découvert lors de contrôle tardif. Fusion manuelle de dossiers. Ajustement facturation long. | Risque : facturation dupliquée. Double imputations. Dossier patient fragmenté. |

---

## 8. Effets observés

### Conséquences du fonctionnement réel

| Effet | Description / Manifestation | Fréquence | Gravité / Impact |
|------|---------------------------|-----------|-----------------|
| **Retard de facturation** | Factures générées tardivement après fin de séjour. Non facturation immédiate. Délai entre sortie et facturation : **plusieurs jours à plusieurs semaines**. | **Très fréquent** | **Majeur** : Délai de trésorerie. Imputation comptable repoussée. Recours clients tardifs. |
| **Taux de rejet facturation élevé** | Factures rejetées pour données manquantes ou incoherentes (mauvaise identité, couverture inconnue, dispensations non imputées). Nécessite refacturation. | **Fréquent** (chiffre non spécifié dans obs) | **Majeur** : Charge administrative importante. Délai allongé. Client doit retraiter. |
| **Erreurs d'identité patient** | Double saisie manuelle → transcription d'erreurs de nom, prénom, date de naissance. Patient identifié de manière inexacte. | **Régulier** (risque accru par double saisie) | **Majeur** : Dossier patient fragmenté. Risque clinique (médicaments à mauvais patient). Facturation inexacte. |
| **Dossiers administratifs incomplets** | Admissions créées sans tous les champs requis. Manque pièces d'identité, consentement, info couverture. Dossier jamais vraiment "clos". | **Très fréquent** | **Modéré à majeur** : Traçabilité faible. Risque légal. Qualité information patient dégradée. |
| **Dispensations pharmacie non imputées ou imputées tardive** | Pharmacie dispense, mais imputation administrative retardée. Risque de perte d'imputation ou doublon. | **Fréquent** | **Majeur** : Facturation incomplète. Manque à gagner. Litige avec pharmacie. |
| **Données de contact obsolètes ou fausses** | Numéros non vérifiés à l'accueil. Découverts faux trop tard. Impossible de joindre le patient. Courriers retournés. | **Fréquent** | **Modéré** : Difficultés relance ultérieure. Suivi patient compromis. |
| **Surcharge agents arrière-office** | Flux continu de "régularisations a posteriori" pour absorber lacunes accueil. Volume non prévisible, pics d'activité. | **Très fréquent** | **Modéré à majeur** : Burn-out agents. Qualité du travail variable. Irritation interpersonnelle. |
| **Dégradation lien service accueil ↔ arrière-office** | Accueil savait que dossiers incomplets → tension. Arrière-office surchargé de corrections → tension inverse. Coordination difficile. | **Systématique** | **Modéré** : Climat de travail tendu. Perception de manque de reconnaissance. Silos opérationnels. |
| **Perte temps double saisie** | Ressaisie manuelle papier → SIH. Estimé : **15-30 min par admission**. Accumulation sur volume annuel = **centaines d'heures**. | **Très fréquent** (systématique) | **Majeur** (mesure du temps) : Inefficacité opérationnelle flagrante. Argent dépensé en travail non-valeur ajoutée. |
| **Itérations multiples avant clôture dossier** | Dossier passe plusieurs fois par "boucle" avant clôture : 1ère vérif → correction → 2e vérif → correction → facturation. | **Systématique** | **Majeur** : Flux de travail non linéaire. Difficulté à projeter délai facturation. Imprédictibilité. |
| **Sentiment "d'usure" équipe clinique** | Médecins/infirmiers contactés pour clarifier données administratives. Déborder sur rôle. Frustration. | **Régulier** | **Modéré** : Qualité relation clinique dégradée. Détournement capacité soins. Insatisfaction professionnelle. |
| **Risque légal latent (consentement, données manquantes)** | Admissions sans consentement signé, pièces manquantes, dossier incomplet. Pas de problème tant que pas de litige. Si problème : vulnérable. | **Fréquent** | **Modéré (latent)** : Exposé à risque. Si audit/contrôle externe : observations. Si litige patient : vulnérable juridiquement. |
| **Absence de traçabilité claire du statut dossier** | Pas de "workflow" informatisé visible. Dossier en cours de régularisation : personne ne sait où il en est. Stagnation possible. | **Systématique** | **Modéré** : Difficulté pilotage. Invisible aux managers. Dossiers "oubliés" possibles. |

---

## Résumé synthétique des dysfonctionnements

**Schéma du problème central** : 
- **Accueil** : Privilégie fluidité clinique → création admissions incomplètes en cas d'urgence/affluence.
- **Chaîne administrative** : Faute d'informations complètes en temps réel, doit procéder à régularisation a posteriori.
- **Pharmacie & services** : Opèrent en parallèle (non intégrés), créant décalages imputation/dispensation.
- **Contrôle tardif** : Anomalies détectées trop tard → peu de temps correction → rejet/refacturation.
- **Support papier-manuel prédominant** : Double saisie, traçabilité fragmentée, erreurs transcription.

**Boucle perverse** : Incompletude → charge arrière-office → délai facturation → rejet → itération.