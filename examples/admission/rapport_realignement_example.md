# Note de réalignement — Circuit Admission-Facturation

## 1. Synthèse du désalignement

### Diagnostic d'ensemble

Le circuit admission-facturation présente un **désalignement critique** entre le processus formel prescrit (22 fonctionnalités F1-F22) et les pratiques réelles observées. Les observations terrain révèlent une **fragmentation dans l'exécution** des fonctionnalités : certaines sont systématiquement contournées (régularisations informelles), d'autres s'exécutent partiellement ou tardivement (contrôles avant facturation), créant une **cascade de dysfonctionnements** qui accumulent les retards, erreurs et surcharges administratives.

### Caractéristiques principales du désalignement

Le désalignement se manifeste selon quatre dimensions entrecroisées :

**Dimension fonctionnelle** : Les étapes prescrites (F1-F22) ne s'exécutent pas dans un flux séquentiel cohérent. Exemple : F11 (Créer admission) s'exécute sans validation des champs obligatoires ; F16 (Compléter admission incomplète) devrait s'activer automatiquement mais reste invisible/inactive ; F17/F18 (imputation) se font avant que F11 soit consolidée. Cela crée des imputations sur admissions partielles, impossibles à auditer.

**Dimension organisationnelle** : Le circuit est fragmenté en 5 domaines (accueil, arrière-office, pharmacie, contrôle qualité, facturation) sans propriétaire clair du flux bout-en-bout. Chaque équipe optimise son critère local (accueil : vitesse ; arrière-office : précision) sans arbitrage sur les tensions (urgent vs. administratif complet). Résultat : régularisations informelles qui contournent les processus formels.

**Dimension technique** : L'absence d'intégration SIH entre modules (admission, pharmacie, facturation) force des traitements manuels parallèles (doubles saisies papier→SIH, imputation pharmacie manuelle/retroactive, synchronisations par email). Aucun checkpoint de validation continu ; les contrôles (F20, F21) surviennent juste avant facturation, révélant les erreurs trop tard pour correction.

**Dimension humaine** : Les acteurs ont accepté implicitement que les admissions incomplètes, les modifications non-tracées et les délais de facturation longs sont "normaux". Ce n'est pas par incompétence, mais par rationalité locale : créer admission rapide (acceptée incomplète) permet de soigner le patient sans délai. L'arrière-office "arrange" a posteriori. Cette culture de l'imparfait, cumulée, produit le chaos observé.

### Niveau global de désalignement : **CRITIQUE**

Le désalignement est qualifié **critique** car il :
- **Bloque la chaîne de valeur** : admissions incomplètes → imputation impossible/partielle → contrôles tardifs → facturation retardée
- **Produit des erreurs systématiques** : doubles saisies → erreurs d'identité → rejets facturation
- **Expose à des risques légaux/réglementaires** : consentements non-tracés, dossiers non-auditables, violations RGPD
- **Consomme massivement des ressources** : 220-430 k€/an de surcharge opérationnelle (arrière-office, doubles saisies, corrections post-facturation, délai trésorerie)
- **Dégrade la satisfaction interne** : tensions interpersonnelles accueil↔arrière-office ; stress équipe facturation ; friction urgence vs. administratif

### Conséquences principales observées

| Conséquence | Impact | Symptôme observable |
|-----------|--------|-------------------|
| **Retard facturation** | Très élevé | Délai moyen 5-15 jours vs. objectif 1-3 jours |
| **Taux rejet facturation** | Élevé | 5-10% factures rejetées (données manquantes, erreurs identité) |
| **Erreurs identité patient** | Critique | Transcriptions doubles saisies → doublons IPP, divergences papier/SIH |
| **Dossiers incomplets** | Systématique | 70-80% admissions urgences sans champs obligatoires à J+0 |
| **Dispensations non-imputées** | Fréquent | Pharmacie dispense, imputation retardée/manquante → sous-facturation |
| **Données contact inexactes** | Fréquent | Numéros non-vérifiés à l'accueil → impossible joindre patient ultérieurement |
| **Surcharge arrière-office** | Majeur | 2-4 h/jour régularisations, complétude, corrections → burn-out |
| **Consentements manquants** | Critique (légal) | 100% urgences sans consentement signé/tracé → RGPD violation |
| **Traçabilité défaillante** | Fort | Modifications dossier informelles → non-auditables, violations obligation légale |
| **Délai recouvrement** | Majeur (trésorerie) | Facturation tardive = recouvrement tardif = BFR dégradé |

---

## 2. Tableau des écarts majeurs identifiés

| # | Désalignement constaté | Étape(s) formelle(s) | Nature de l'écart | Cause probable | Impact opérationnel | Criticité |
|---|---|---|---|---|---|---|
| **1** | Doubles saisies papier→SIH systématiques | F2, F1, F3, F11 | **Technique + Organisationnel** | Absence terminal SIH accueil ; dépendance papier comme buffer sécurité ; SIH indisponible/lent | Erreurs transcription ; perte données ; retard saisie 15-30 min/admission | **CRITIQUE** |
| **2** | Admissions créées incomplètes (champs obligatoires non remplis) | F11, F16, F15 | **Fonctionnel + Humain** | F11 sans validation obligatoire ; pression volumétrique urgences ; absence enforcement SIH ; priorité clinique sur administratif | Blocage imputation ; contrôles incomplets ; retard facturation en cascade | **CRITIQUE** |
| **3** | Régularisations a posteriori informelles (non-tracées) | F3, F13, F8 | **Organisationnel + Humain** | F3/F13 probablement trop rigides/lentes ; culture acceptation "arrière-office arrangera" ; pas de propriétaire transverse | Perte traçabilité ; dossiers non-auditables ; risque légal (RGPD) ; surcharge arrière-office | **FORT** |
| **4** | Pharmacie dispense avant imputation administrative finalisée | F17, F18, F20, F21 | **Technique + Organisationnel** | Absence intégration SIH-Pharmacie ; flux "pull" (rétroactif) au lieu "push" (temps réel) ; deux systèmes parallèles | Imputation retardée J+3-7 vs. J+0 ; dispensations orphelines ; sous-facturation | **CRITIQUE** |
| **5** | Contrôles avant facturation réalisés tardivement | F20, F21, F19, F22 | **Fonctionnel** | F20/F21 conçues comme "pré-facturation" final au lieu checkpoints continus ; pas de validation progressive ; pas d'alerte intermédiaire | Anomalies découvertes trop tard ; course correction urgente ; erreurs factures potentielles | **CRITIQUE** |
| **6** | Vérification droits/mutuelle repoussée à posteriori | F11 (champs droits) | **Organisationnel + Contexte** | Impossible vérifier urgence (mutuelle fermée) ; pas flux pré-admission urgences ; données vieilles dossier antérieur | Factures pré-édition incorrectes ; ajustements post-émission ; délai recouvrement allongé | **FORT** |
| **7** | Consentement absent ou retardé en urgences | F11 (champ consentement) | **Réglementaire + Contexte** | Tension urgence vitale (soigner vite) vs. consentement préalable (légal) ; pas d'arbitrage formel ; F11 ne force pas tracé | Dossiers légalement incomplets ; RGPD violation ; risque responsabilité établissement | **CRITIQUE** |
| **8** | Délais facturation longs (5-15 jours vs. 1-3 jours cible) | F19, F22 | **Fonctionnel + Organisationnel** | Cascade écarts antérieurs (#1-7) bloque facturation ; pas SLA clair ; pas de "gate" intermédiaires | Impact trésorerie ; délai recouvrement ; insatisfaction patient | **CRITIQUE** |

---

## 3. Analyse des causes probables

### 3.1 Causes organisationnelles

#### **Fragmentation responsabilités, absence propriétaire circuit complet**

Le circuit admission-facturation est segmenté en 5 domaines (accueil, arrière-office administratif, pharmacie, contrôle qualité, facturation) sans gouvernance transverse. Chaque équipe possède sa responsabilité fonctionnelle (ex : accueil = F1-F2-F11 ; pharmacie = F18) mais **aucune n'est accountable du flux bout-en-bout** (F11 → F19).

Conséquence : chaque acteur optimise son critère local. L'accueil maximise rapidité (patient enregistré vite, lit occupé) → créé admissions incomplètes. L'arrière-office maximise précision (corrections lentes mais sûres) → surcharge accumule. Pharmacie dispense en temps réel (clinique prime) → décalage imputation administrative. Aucun arbitrage : problèmes inter-étapes (ex : "admission incomplète bloque imputation") restent orphelins.

Impact : dysfonctionnements s'accumulent sans résolution. Chacun "fait son job", ensemble c'est chaos.

#### **Priorisation implicit urgent vs. administratif (jamais formalisée)**

Observation : admissions incomplètes (#2), consentement absent (#7), droits repoussés (#6) = tous symptômes d'une même tension non-résolue : "urgence clinique vs. complétude administrative".

Réalité acceptée (mais non-formalisée) : en urgence, soigner prime sur remplir dossier complet. Processus formel F11-F16 supposé séquentiel (admission complète → imputation) ; réalité parallèle (admission clinique vite, administratif en arrière).

Problème : cette tension n'a **jamais été arbitrée formellement**. Pas de "protocole urgence" qui dit : "en urgence, complétude minimale = identité + IPP ; droits/consentement en J+1 OK". Résultat : chacun interprète → incohérence SIH → contournements acceptés.

#### **Surcharge accueil vs. absence équipe dédiée "complétude"**

Observation directe : doubles saisies (#1) = papier utilisé en accueil car buffer face au SIH (indisponibilité, charge). Admissions incomplètes (#2) = créées rapidement, "quelqu'un d'autre complètera".

Cause : effectifs accueil insuffisants pour gérer volume + qualité complètement simultanément. Pas d'équipe tampon "complétude post-admission" (F16 n'est jamais activée systématiquement). Ressaisie manuelle papier-SIH retardée J+1/J+2 (si faite du tout).

Implication : arrière-office absorbe lacunes = surcharge 2-4 h/jour régularisations (observation documentée). Escalade : urgences créent admission incomplète → arrière-office débordée → corrections informelles → perte traçabilité.

#### **Absence gouvernance processus vs. pression opérationnelle**

Observation : régularisations informelles (#3) = personne n'a le pouvoir/responsabilité de forcer F3/F13 formelles. Pharmacie dispense avant imputation (#4) = pas de gate entre dispensation et admissibilité imputation. Contrôles tardifs (#5) = pas de KPI "facturation J+3" assorti conséquences.

Cause : pas de tableau de bord/reporting circuit (complétude admission %, délai F11→F16, délai F20→F19, etc.). Pas d'incident formalisé si écart SLA. Management par défaut = statu quo accepté.

Impact : problèmes identifiés *après coup* (rejet facturation, patient mécontent, auditeur inquiet) pas *avant* (détection proactive, intervention rapide).

### 3.2 Causes fonctionnelles et techniques

#### **F11 accepte création sans validation champs obligatoires**

Observation : admissions créées avec adresse vide, contact vide, droits vides, consentement absent. IPP provisoire = raccourci technique reproduisant le problème.

Cause : spécification F11 probablement pensée "créer IPP d'abord, détails après" (design pragmatique pour urgence). Pas de validation SIH au niveau insertion (NOT NULL constraints sur champs obligatoires). F16 (Compléter) existe mais n'est jamais activée automatiquement.

Impact : admissions incomplètes deviennent statut intermédiaire indéfini (jamais vraiment "clos"). Imputation impossible ou partielle. Contrôles incomplets.

#### **Architecture SIH fragmentée : pharmacie non-intégrée temps réel**

Observation : pharmacie dispense (système pharmacie) en temps réel. F18 imputation (SIH) s'exécute manuellement/retroactivement J+3-7. Découverte décalages lors contrôles F20/F21.

Cause : deux systèmes parallèles (Pharmacie + SIH admission-facturation) non synchronisés. Pas d'interface formalisée (F18 = action manuelle, pas flux automatisé). Pas d'événement métier "dispensation" qui trigger "imputation dossier" automatiquement.

Impact : imputation retardée massivement. Erreurs appareillage (articles imputés mauvais patient/séjour). Sous-facturation possible.

#### **Absence terminal/accès SIH accueil (dépendance papier)**

Observation : doubles saisies papier-SIH systématiques = symptôme direct : papier utilisé en accueil car SIH indisponible/pas accessible.

Cause : pas de terminal physique à l'accueil OU SIH trop lent contexte urgence OU manque investissement infra. Papier = buffer sécurité (si SIH crash, au moins on a papier).

Impact : ressaisie manuelle ultérieure = perte information, erreurs transcription, charge accueil doublée.

#### **Pas de checkpoints contrôle continu (F20/F21 seulement pré-facturation)**

Observation : F20/F21 existent mais s'exécutent juste avant F19/F22 = trop tard corriger. Anomalies identifiées jours après imputations.

Cause : spécification F20/F21 pensée "validation pré-facturation" (point unique) au lieu "contrôles progressifs/continus". Pas de règles BRMS automatisées (ex : "diagnostic manquant après J+1 séjour → alerte"). Pas d'événements entre F17/F18 et F20 pour valider incrémentalement.

Impact : anomalies détectées J+5-6 au lieu J+1-2. Corrections disséminées vs. bum pré-facturation.

#### **Absence traçabilité modifications (F3/F13 non-tracées ou contournées)**

Observation : régularisations informelles = modifications dossier patient sans traçabilité. Appels téléphoniques, emails, notes adhérentes, pas de journal audit.

Cause : F3/F13 probablement trop rigides/lentes (approbation requise ?) ou juste peu intégrées workflow. Plus rapide appeler que utiliser processus. Absence obligation légale formalisée dans SIH (modification = traçabilité obligatoire).

Impact : dossiers non-auditables. Violations RGPD (modifications non-tracées). Impossible reconstituer historique si litige.

### 3.3 Causes humaines et comportementales

#### **Culture acceptation de l'imparfait — contournements normalisés**

Observation : admissions incomplètes acceptées comme "normal" ; régularisations informelles acceptées ; chacun sait que certaine étape sera "bâclée" et quelqu'un d'autre compensera.

Mécanisme : absence "culture défaut zero" du circuit. Pas de feedback : acteur amont ignore impact imparfait sur aval (ex : accueil qui crée admission incomplète ignore qu'arrière-office passe 30 min corriger). Contournements = réponse rationnelle locale à ressources limitées, acceptés parce que "c'est comme ça qu'on fait depuis toujours".

Implication : normalisation dysfonctionnement. Pas perçu comme "problème à résoudre", juste "réalité opérationnelle".

#### **Rationalité locale vs. optimum global**

Observation : accueil maximise rapidité (SLA : "admission < 5 min") ; arrière-office maximise précision (SLA : "dossier complètement exact avant imputation") ; ces critères sont en tension.

Mécanisme : KPI par fonction (ex : "temps moyen admission < 5 min" ; "% rejet facturation < 2%") ne sont pas liés aux mêmes incentives. Personne ne décide "pour urgence, on accepte admission incomplète par design" → chacun improvise localement.

Implication : chaîne de valeur sous-optimisée. Accueil rapide + arrière-office lent = délai total pire que if accueil légèrement plus lent mais arrière-office supprimé.

#### **Coping par contournement face à outils inadaptés**

Observation : doubles saisies papier (#1) = coping face à SIH indisponible/lent ; régularisations informelles (#3) = coping face à F3/F13 trop rigides ; absence consentement (#7) = coping face à conflit urgent/administratif.

Mécanisme : chaque contournement est rationnellement justifié localement ("je dois aller vite pour soigner le patient" ; "je dois finaliser le dossier, appel plus rapide que procédure"). Acteurs ne sont **pas blâmables** : ils font choix sensés avec ressources/outils disponibles.

Implication : l'amélioration nécessite changer outils/processus, pas changer "mentalité" (mentalité est appropriate pour problème donné).

#### **Absence feedback : invisible impact dysfonctionnement en aval**

Observation : accueil ne sait pas que ses admissions incomplètes causent 30 min arrière-office/patient. Arrière-office ne sait pas que ses corrections tardives causent rejet facturation. Aucun dashboard visible de cause-effet.

Mécanisme : chaîne manquante entre action locale (créer admission rapide/incomplète) et résultat global (délai facturation, rejet). Causé par fragmentation information + pas de tableau bord transverse.

Implication : acteurs ne peuvent pas apprendre/améliorer. Cycle de dysfonctionnement s'auto-entretient.

### 3.4 Causes réglementaires et contextuelles

#### **Tension urgent vitale vs. obligation administrative/légale (jamais arbitrée)**

Observation : consentement absent en urgences (#7) ; admissions incomplètes (#2) ; vérification droits repoussée (#6).

Cause : Code déontologie/éthique stipule "urgence vitale prime sur formalités" ; Codes légaux stipulent "consentement obligatoire". Absence d'arbitrage formel = chacun interprète.

Implication : dossiers légalement incomplets (consentement absent) acceptés comme "normal urgence". Risque latent RGPD/responsabilité.

#### **Obligation NOEMIE vs. délai réaliste dossier complet**

Observation : NOEMIE = obligation facturation rapide post-séjour. Dossier ne peut pas être complet si admission incomplète, pharmacie non-rapprochée, droits non-vérifiés.

Cause : pas de "SLA réglementaire clair" : faut facturer combien de jours ? dossier peut être incomplet à l'émission ? Pratiques acceptées mais non-formalisées (ex : "facture préliminaire J+3, régularisation possible J+10").

Implication : facturation retardée (#8) = symptôme d'impossibilité réglementaire (urgent = facture vite ; urgent ≠ dossier complet).

#### **Obligation audit/traçabilité vs. culture information-locale**

Observation : RGPD, responsabilité civile = obligation dossier tracé, modifiable, auditables. Régularisations informelles (#3) = violation. Consentement absent (#7) = violation.

Cause : obligations légales connues mais pas "embodied" dans processus. Pas d'audit régulier qui détecterait non-conformité.

Implication : risque légal latent. Établissement vulnérable si contrôle/litige.

### 3.5 Synthèse causes par écart (cross-dimensionnelle)

| Écart | Cause organisationnelle | Cause fonctionnelle/tech | Cause humaine | Cause réglementaire/contexte |
|-------|------------------------|------------------------|--------------|-----------------------------|
| #1 Doubles saisies | Pas d'infra prioritaire accueil | Pas terminal accueil ; SIH trop lent | Coping papier = sécurité perçue | N/A |
| #2 Admissions incomplètes | Surcharge accueil ; pas SLA F16 | F11 sans validation ; pas workflow F16 | Culture acceptation imparfait | Tension urgent/complet non-arbitrée |
| #3 Régularisations informelles | Pas propriétaire processus | F3/F13 trop rigides ou absentes | Culture contournement acceptée | Obligation traçabilité non-enforced |
| #4 Pharmacie non-rapprochée | Pharmacie/admission parallèles | Pas intégration SIH-Pharmacie temps réel | N/A | N/A |
| #5 Contrôles tardifs | Pas checkpoint intermédiaires | F20/F21 pré-facturation seulement | N/A | N/A |
| #6 Droits repoussés | Impossible vérifier urgence | Pas flux pré-admission | Coping "appel plus tard" | Urgence vs. vérification |
| #7 Consentement absent | Pas arbitrage urgent/adminstratif | F11 sans tracé consentement | Priorité clinique implicite | Urgence vitale vs. consentement légal |
| #8 Délais facturation longs | Cascade écarts antérieurs | Pas SLA bout-en-bout | Pas de KPI facturation | NOEMIE vs. dossier incomplet |

---

## 4. Impacts opérationnels consolidés

### 4.1 Impacts par fonction

#### **Accueil/Admission**
- **Charge augmentée** : doubles saisies papier-SIH = 15-30 min supplémentaire par patient
- **Frustration patient** : relances ultérieures pour infos manquantes
- **Retard flux** : file d'attente allongée (attente ressaisie, clarifications)

#### **Arrière-office administratif**
- **Surcharge majeure** : régularisations, complétude dossier, corrections = 2-4 h/jour (observation documentée)
- **Improvisation** : pas de processus formel, arrangements au cas par cas → burn-out
- **Stress chronique** : dossiers jamais vraiment "clos", demandes/rappels constants, insécurité travail

#### **Équipe clinique (médecin, infirmier)**
- **Débordement administratif** : parfois doivent clarifier données administratives avec patients (pas leur rôle)
- **Détournement temps** : capacité soins réduite
- **Frustration** : perception "accueil n'a pas bien fait son job"

#### **Pharmacie**
- **Décalage imputation** : dispensations non-imputées dans SIH, découvertes tardives
- **Réconciliation manuelle** : effort vérifier "ce dispensé = ce imputé"
- **Litige inter-services** : responsabilité floue si dispensation manquante/mal imputée

#### **Contrôle qualité/Conformité**
- **Corrections tardives** : anomalies découvertes jours avant facturation
- **Stress** : course contre la montre avant émission facture
- **Risque non-détection** : anomalies passent à côté si délai court

#### **Facturation/Trésorerie**
- **Retard majeur** : délai moyen 5-15 jours au lieu objectif 1-3 jours
- **Erreurs** : rejets NOEMIE, litiges mutuelles, recouvrement compliqué
- **Ressources gaspillées** : gestion ajustements post-facture (courriers, rééditions, appels)

### 4.2 Impacts consolidés par métrique

| Métrique | Baseline observée | Cible prescrite | Écart | Impact |
|----------|-----------------|-----------------|-------|--------|
| **Délai admission (saisie)** | 30-60 min (papier+ressaisie) vs. 5 min direct SIH | 5-10 min | +300-500% | Retard file accueil, surcharge |
| **Complétude admission à J+0** | <20% dossiers complets | 90%+ (urgent: 80%) | -60-70pp | Blocage imputation/contrôle |
| **Délai F11→F16 (complétude)** | 1-3 jours après admission | J+0 (urgent) ou J+1 | +24-72 h | Régularisations tardives |
| **Délai F17/F18 imputation** | J+3-7 (pharmacie), J+2-4 (prestations) | J+0-1 | +48-168 h | Valorisation retardée |
| **Délai F20/F21 contrôles** | 6-24 h avant facturation | Continu/J+0-1 | -5 jours détection | Anomalies découvertes tard |
| **Délai F19/F22 facturation** | 5-15 jours post-séjour | 1-3 jours max | +200-400% | Impact trésorerie majeur |
| **Taux rejet facturation** | 5-10% (erreurs identité, données) | <2% | +3-5x taux | Rédaction/retraitement coûteux |
| **Dossiers non-auditables** | 30-50% (régularisations informelles) | 0% | 30-50pp | Risque légal/audit |
| **Consentements manquants** | 100% urgences | 100% tracés | 100pp | RGPD violation |
| **Heures arrière-office** | 2-4 h/jour régularisations | Quasi-0 (processus correct) | +2-4 h/jour | Coût 80-150 k€/an |
| **Heures doubles saisies** | 15-30 min × 2000 admissions/an = 400-800 h/an | 0 | 400-800 h/an | Coût 20-40 k€/an |

### 4.3 Impacts financiers et légaux

**Coût annuel opérationnel (quantifié)**
- Surcharge arrière-office (complétude + régularisations) : 80-150 k€
- Surcharge accueil (doubles saisies) : 20-40 k€
- Retard recouvrement (5-15 j × taux intérêt BFR) : 100-200 k€
- Rejets facturation (rédaction/retraitement) : 20-40 k€
- **Total annuel : 220-430 k€**

**Risques légaux/réglementaires (latents, non-quantifiés)**
- Consentements non-tracés = RGPD violation (ex : CNIL amende jusqu'à 50 M€ pour violations graves)
- Dossiers non-auditables = violations obligation traçabilité
- Modifications non-tracées = responsabilité civile aggravée en cas litige
- NOEMIE non-conforme (facturation tardive) = retard recouvrements

### 4.4 Impact consolidé sur la chaîne de valeur

```
Flux valeur : Patient admission → Soins → Imputation valorisation → Contrôle → Facturation → Recouvrement

Dysfonctionnement cascade :
  Admission incomplète (F11)
    ↓
  Imputation partiellement possible (F17/F18) ; pharmacie non-rapprochée
    ↓
  Contrôles tardifs découvrent anomalies (F20/F21)
    ↓
  Corrections d'urgence
    ↓
  Facturation retardée (F19/F22)
    ↓
  Recouvrement allongé = trésorerie impactée

Effet : chaque écart amont dégrade étape aval → accumulation non-linéaire
```

---

## 5. Quick Wins recommandés (< 3 mois, sans investissement technique majeur)

### Tableau synthétique

| # | Action recommandée | Désalignement(s) ciblé(s) | Effet attendu | Responsable pressenti | Délai indicatif | Difficulté estimée |
|---|---|---|---|---|---|---|
| **QW#1** | Activer F16 workflow automatisé : F11 incomplète → créer tâche F16 assignée "complétude" queue avec SLA J+1 | #2, #6, #7 | Admissions incomplètes visibles ; complétude obligatoire J+1 vs. repoussée indéfiniment | DIM + IT | 2-3 sem | Basse |
| **QW#2** | Centraliser vérif droits en pré-admission : urgences programmées (24-48h avant) = appel mutuelle auto + SIH ; urgences = accepter "à vérifier J+1" | #6 | Programmés : 100% droits vérifiés avant admission ; urgences : facturation sans ajustement post-hoc | Gestionnaire admission + IT | 4-6 sem | Basse-Modérée |
| **QW#3** | Tracer consentement électroniquement en F11 : case "consentement" (oui/rattrapage J+1) + timestamp + rapport mensuel % manquants | #7 | Conformité RGPD ; traçabilité consentement ; urgences formalisées ("rattrapage" = pas risque légal latent) | Compliance + Accueil | 3-4 sem | Basse |
| **QW#4** | Dédier 1 FTE "gestionnaire complétude" post-admission : action F16 quotidienne, relances contact patient, vérif droits rattrapage, obtention consentement | #2, #3 | Dossiers 100% complets J+1 ; arrière-office "improvisation" supprimée ; accueil peut créer rapide sans culpabilité | Direction admission + RH | Immédiat/2-3 sem | Modérée |
| **QW#5** | Interface Pharmacie↔SIH : import quotidien dispensations pharmacie (fichier) + matching automatisé (IPP → F18 imputation) ; rapport articles non-appareillés | #4 | F18 imputation se déclenche auto ; délai J+3-7 → J+0-1 ; erreurs matching baissent | DIM + IT | 2-4 sem | Basse-Modérée |
| **QW#6** | Mapping papier→SIH zéro papier : court-term = scanner formulaires admission (ref IPP+timestamp), détruire copies ; moyen-term = terminal SIH accueil | #1 | Élimination doubles saisies normales ; erreurs transcription → 0 ; charge accueil réduite | IT + Accueil | 2-3 sem (court) ; 4-8 sem (moyen) | Modérée |
| **QW#7** | Implémenter F20/F21 checkpoints continus : règles validation continu (ex: "diagnostic obligatoire après J+1") + alertes quotidiennes dossiers anomalies | #5 | Anomalies détectées J+1-2 vs. J+5-6 ; corrections disséminées vs. bum pré-facturation ; stress équipe facturation réduit | DIM + IT | 4-6 sem | Basse-Modérée |
| **QW#8** | SLA bout-en-bout + tableau bord visibilité : F11→F16 = J+1 ; F17/F18 = continu ; F20/F21 = continu ; F19 = J+0 si complet ; NOEMIE = J+3 max. Dashboard quotidien + réunion 10 min quotidienne alertes | Tous | Accountability clair ; visibilité équipes ; Direction peut décider arbitrage si conflit ; problèmes identifiables rapidement | Manager Circuit (création semaine 1) + IT | 2-3 sem | Basse |

### Détails Quick Wins prioritaires

#### **QW#1 : Workflow F16 automatisé (TRÈS HIGH-IMPACT)**

**Spécification** : Configurer SIH pour que dès qu'une F11 est créée avec champs obligatoires vides (adresse, contact, droits, consentement), une tâche F16 (Compléter admission) soit créée automatiquement et assignée à queue "Complétude" avec SLA J+1. Rappel quotidien si non-actionnée.

**Effet** : Admissions incomplètes deviennent **visibles et traçables**. Complétude = obligation explicite (not "quelqu'un arrangera"). Baseline <20% complétude J+0 → cible 80-90% J+1.

**Dépendance** : Accord DIM sur quels champs = "obligatoires à J+0" vs. "obligatoires à J+1" (urgence exception possible).

**Effort** : Configuration SIH 2-3 semaines (no développement).

---

#### **QW#4 : FTE dédié "complétude" (TRANSFORMATION RAPIDE)**

**Spécification** : Créer/redéployer 1 FTE titulaire "Gestionnaire Complétude Dossier". Rôle : chaque jour, traiter tous dossiers de veille en état "complétude requise" (F16 créée). Actions : 1) relances contact patient (appel pour adresse/contact/consentement manquants), 2) vérification droits (appel mutuelle), 3) obtention consentement (rattrapage urgence), 4) update SIH F16. Objectif : 100% dossiers "complétude J+1" (ou J+0 si programmé).

**Effet** : Arête de cascade. Arrière-office "improvisation régularisations informelles" est remplacée par processus formel tracé. Accueil peut créer rapide (même incomplète) sans culpabilité.

**Coût** : 1 FTE = 50-70 k€/an (redéploiement if possible, recruitment if needed). **ROI** : supprime 2-4 h/jour arrière-office chaos = économise 80-150 k€/an → break-even immédiat.

**Effort** : Redéploiement/recrutement 2-3 semaines.

---

#### **QW#8 : SLA + tableau bord (VISIBILITY = POWER)**

**Spécification** : Définir SLA précis : F11 création → F16 complétude = J+1 max ; F17/F18 imputation = continu après complétude ; F20/F21 contrôles = continu/J+0-1 avant F19 ; F19 facturation = J+0 si aucune anomalie sinon corriger+retry. Créer dashboard visuel : % dossiers à chaque étape chaque jour, délai moyen, anomalies détectées, déviation SLA (rouge si dépassement). Réunion quotidienne 10 min : alertes SLA, incident escalation.

**Effet** : Accountability clair. Équipes conscientes blocages. Direction peut décider arbitrage (ex : urgent/complet tension → qui prime ?). Problèmes identifiables **avant** cascade.

**Dépendance** : Manager Circuit rôle (création semaine 1, il/elle anime réunion quotidienne, escalade).

**Effort** : Design SLA 1 semaine, config BI 2 semaines.

---

### Séquençage Quick Wins

**Semaine 1-3** : QW#1 (F16 workflow) + QW#3 (consentement tracé) + QW#8 (SLA/dashboard) = 3 quick wins simultanés, basse difficulté, très high-impact.

**Semaine 2-4** : QW#4 (FTE complétude) redéploiement si possible, recruitment sinon.

**Semaine 4-8** : QW#2 (vérif droits pré-admission), QW#5 (Pharmacie sync), QW#6 (SIH accueil).

**Semaine 4-12** : QW#7 (checkpoints continus F20/F21), dépend QW#8 (dashboard exist).

**Cumul impact 8 Quick Wins** : 
- Complétude admission → 80% J+1
- Imputation pharmacie → J+0-1
- Facturation → 3-5 jours (vs. 5-15 actuellement)
- Erreurs identité → réduction 50%+
- Rejets facturation → réduction 30-50%
- Arrière-office surcharge → réduction 30-40%
- **Total économie année 1 : 100-150 k€** (sans investissement IT majeur)

---

## 6. Actions structurantes recommandées (3-18 mois, transformatives)

### Tableau synthétique

| # | Action recommandée | Désalignement(s) ciblé(s) | Effet attendu | Responsable pressenti | Horizon | Prérequis/Dépendances |
|---|---|---|---|---|---|---|
| **AS#1** | Refonte architecture SIH : intégration admission-pharmacie-facturation temps réel (bus événementiel ou API) ; F11 création → événement → abonnements pharmacie/facturation pré-remplissent | #1, #4, #5, #8 | Doubles saisies élimées ; imputation pharmacie auto J+0 ; facturation J+1-2 vs. J+5-15 ; données unifiées | DSI (architecture) + DIM (métier) | 12-18 mois | Budget 200-300 k€ ; accord direction shutdown workarounds papier-email |
| **AS#2** | Créer rôle transverse "Manager Circuit Admission-Facturation" : propriétaire F11→F19 SLA, incident escalation, gouvernance changements, tableau bord quotidien, arbitrage urgent/administratif | #2, #3, #6, #8 + tous | Accountability claire ; coordination inter-fonctions ; problèmes inter-étapes résolvables sans CODIR ; décisions arbitrage formalisées | Direction Générale (création + sponsor) | 2-4 sem création ; 6-8 sem montée en puissance | Budget 150-180 k€/an ; profil : leadership transverse, processus hospitalier |
| **AS#3** | Documenter formel détaillé "Golden Process" : cartographie BPMN flux normal + variations urgence ; spécification F1-F22 (entrée/sortie, champs obligatoires, responsable, validation) ; matrice RACI ; règles de gestion (ex: "urgence = admit sans droits/consentement, max J+1 rattrapage") ; délais SLA ; protocoles exception | #1-8 (clarté universelle) | 100% acteurs clarifiés ; règles implicites → explicites ; contournements formellement justifiés vs. tolérés ; audit/conformité possible | DIM (pilotage) + Documentation + inter-fonctions | 12-18 sem | Ateliers 5-6 avec chaque fonction ; engagement DIM ; training massif 2-3 jours |
| **AS#4** | Réformer rôles/responsabilités : Accueil = créer F11 "complétude minimale" (identité+IPP+contexte) ; Arrière-office = actionner F16 formelle endéans J+1 (droits/consentement rattrapage) ; toute correction = F3/F13 tracée | #2, #3 | Accueil soulagée (crée vite) ; arrière-office claire (son job = compléter) ; régularisations informelles → traçables ; transitions fluides inter-équipes | Direction admission (conception) + RH (job descriptions, training) | 10-14 sem | Accord sur "complétude minimale J+0" définition (ex: urgence accepte identité+IPP) |
| **AS#5** | Redesigner accueil infra : installer 2-3 terminaux SIH accueil + badge/login ; former accueil saisie directe SIH (F1/F2/F11) ; protocole papier = backup si SIH down, ressaisie < 2h | #1 | Zéro doubles saisies cas normal ; erreurs transcription → 0 ; charge accueil (ressaisie) supprimée ; temps admission → 5 min cible | IT (infra) + Accueil (training, adoption) | 12-18 sem phased | Budget 10-15 k€ infra + formation ; SIH robustesse avérée sinon papier backup risqué |
| **AS#6** | Formaliser arbitrages urgent/administratif : commission mensuelle (DG, médecins, admin, urgences, DIM, facturation) ; décider protocoles urgence (ex: "urgence = admit sans consentement, consentement rattrapage J+1 OK" oui/non ?) ; résultats → intégrés Golden Process | #2, #6, #7 | Urgences peuvent fonctionner ; admin peut fonctionner ; contentions ritualisées (commission) vs. conflits ad-hoc ; règles claires pour tous | Direction Générale (sponsorship) + Manager Circuit (secrétariat) | Immédiat (réunion sem 1) ; cadence mensuelle | Engagement DG ; slots calendrier direction |
| **AS#7** | Audit légal + rétrofitter conformité dans F1-F22 : expert légal revoit fonctionnalités vs. RGPD/droit patient/traçabilité ; identifie champs/validations manquantes ; déployer corrections SIH (ex: F11 force consentement tracé ; F3/F13 log modifications obligatoire) | #3, #7 | Conformité légale assurée ; dossiers traçables ; audit possible ; risque consentement/RGPD éliminé | Direction + Compliance/Légal (audit) + DIM (implémentation) | 4-6 sem audit + 6-12 sem implémentation | Budget 15-25 k€ audit ; engagement DIM corrections (peut nécessiter SIH changes) |
| **AS#8** | Programme change management : calculer/communiquer coût actuel admission incomplète (ex: 25 €/admission × 2000 = 50 k€/an gaspillé) ; rapport mensuel "coût défaut" ; inclure "complétude dossier" en job evaluation ; valoriser amélioration (bonus équipe) ; sessions bi-mensuels : data + histoires ; inclure équipes co-design solutions | Tous (culture transformation) | Acceptation imparfait → perception "inacceptable" ; culture qualité émerge ; amélioration auto-entretenue | Manager Circuit (mesure/comm) + RH (incentives) + Direction (sponsorship) | Continu (démarrage immédiat ; visible 3-6 mois) | Data robustesse (tableau bord) ; leadership conviction + participation équipes |

### Détails Actions Structurantes clés

#### **AS#2 : Créer Manager Circuit (GOUVERNANCE FONDATRICE)**

**Description** : Poste nouveau, reporte directement Direction Générale. Responsabilités :
1. **Propriétaire SLA bout-en-bout** : F11 création → F19 facturation délai prescrit ; monitor quotidiennement ; alert si écart.
2. **Incident escalation** : admission incomplète > J+1 → investigate → résoudre (ex : imputation bloquée → faire débloquer) → escalade DG si non-résolvable.
3. **Coordination inter-fonctions** : réunion quotidienne alertes (10 min) ; réunion hebdo "issues" (1h) ; commission mensuelle gouvernance.
4. **Tableau de bord** : KPI admission, complétude, imputation, facturation ; trends ; anomalies détectées.
5. **Gouvernance changements** : si règle NOEMIE change → analyse impact, roll-out plan.

**Hiérarchie** : Direct DG (crucial : pas peut pas être "subordonné" direction admission, sinon conflit intérêts).

**Profil** : Expérience processus hospitalier, change management, leadership transverse.

**Budget** : Manager (150-180 k€/an) + 1-2 analystes support (80-100 k€/an).

**Effet** : Accountability clair. Problèmes inter-étapes résolvables. Décisions arbitrage (urgent/administratif) formalisées. Visibilité Direction.

---

#### **AS#3 : Golden Process Documentation (CLARTÉ UNIVERSELLE)**

**Description** : Créer documentation formel complète circuit :

1. **Cartographie BPMN** : flux normal (patient admission programmée → soins → imputation → facturation) + variations urgence (admission rapide, complétude J+1).

2. **Spécification F1-F22** : pour chaque fonction :
   - Condition entrée (exemple : F11 entrée = patient identifié + type admission défini)
   - Action (exemple : F11 action = créer IPP, remplir champs obligatoires J+0, champs rattrapage J+1)
   - Condition sortie (exemple : F11 sortie = admission créée, complétude level XX)
   - Champs obligatoires (ex : adresse = J+0 programmé, J+1 urgence)
   - Validations (ex : contact format numéro phone reconnu)
   - Outils SIH (ex : "utiliser écran F11_ADMISSION")
   - Responsable (ex : "Accueil pour programmé, Urgences pour urgence")

3. **Matrice RACI** : qui Responsible, Accountable, Consulted, Informed pour chaque étape.

4. **Règles de gestion** : formelles (ex : "admission bloquée si type = programmé ET droits = vide" vs. "admission créée même si droits = vide si type = urgence").

5. **Protocoles exception** : ex : "Urgence vitale (ex: arrêt cardiaque) = admission sans ID dossier, ID dossier créée a posteriori J+1", responsable escalade.

6. **Délais SLA** : ex : "F11→F16 complétude = J+1 max", "F19 facturation = J+0 si complet sinon = correction+retry J+1".

**Ownership** : DIM (métier) + Documentation (rédaction). **Validation** : comité inter-fonctions. **Déploiement** : training 2-3 jours équipes.

**Maintenance** : revision annuelle + amendments urgents si règles réglementaires changent.

**Effet** : Zéro ambiguïté. Admissions incomplètes "par erreur" vs. "par design" = distingué. Contournements formellement justifiés vs. tolérés. Audit possible.

---

#### **AS#6 : Commission Urgence/Administratif (ARBITRAGE FORMALISÉ)**

**Description** : Réunion mensuelle (1-2h) : DG, direction médicale, direction administratif, direction urgences, DIM, facturation, RH.

**Agenda** :
1. Conflits urgent/administratif survenus ce mois (ex : "urgence vital sans consentement écrit, solution ?" → décide protocole formel) ;
2. Données manquantes impact (ex : droits impossible vérifier urgence → créer "droits rattrapage J+1" officiel) ;
3. Metriques impact (ex : "X% admissions incomplètes bloquent facturation" → décide investissements pour fixer).

**Résultat** : "Golden Rules" formalisées (ex : "Urgence = acceptable sans droits/consentement, max J+1 rattrapage"), intégrées documentation Golden Process.

**Cadence** : première réunion semaine 1, puis mensuelle.

**Prérequis** : engagement DG (sponsorship visible) ; slots calendrier direction.

**Effet** : Urgences peuvent fonctionner (admissions rapides sans admin complète) ; admin peut fonctionner (cible J+1 rattrapage). Contentions ritualisées vs. conflits ad-hoc.

---

### Séquençage Actions Structurantes

**Semaine 1-2 (URGENCE GOUVERNANCE)**
- AS#2 : Créer Manager Circuit (intérim ou permanent pour quelques semaines)
- AS#6 : Commission urgence/administratif première réunion

**Semaine 2-4 (AUDIT LÉGAL)**
- AS#7 : Lancer audit légal (découvrir violations, prioriser corrections)

**Semaine 4-12 (DOCUMENTATION FORMEL)**
- AS#3 : Golden Process (ateliers conception avec chaque fonction)

**Semaine 10-24 (CHANGE ORGANISATION)**
- AS#4 : Réformer rôles (design + job descriptions + training)
- AS#8 : Change management program (communication + incentives + culture)

**Mois 4-12 (INFRASTRUCTURE)**
- AS#5 : Redesigner accueil infra (installer terminaux, training)

**Mois 6-18 (ARCHITECTURE SIH MAJEURE)**
- AS#1 : Architecture intégrée (seulement après quick wins = ROI démontré + business case)

**Cumul impact Actions Structurantes** (mois 12-18) :
- Doubles saisies → 0
- Admissions complétude → 100% J+1
- Imputation pharmacie → J+0 auto
- Facturation → J+1-2 vs. J+5-15
- Dossiers auditables → 100%
- Conformité légale → assured
- **Total économie année 2+ : 250-400 k€/an** + compliance assured

---

## 7. Points de vigilance de gouvernance

Ces points dépassent le cadre technique ; ils requièrent arbitrage stratégique Direction Générale ou CODIR.

### 7.1 **ARBITRAGE URGENT vs. ADMINISTRATIF — Doit être FORMALISÉ**

**Enjeu** : Admissions incomplètes, consentement absent, droits non-vérifiés = tous symptômes d'une tension non-résolue et jamais arbitrée formellement.

**Décisions requises** (à valider CODIR) :

```
QUESTION 1 : En contexte URGENCE, quelle est la complétude MINIMALE acceptable à F11 ?
  Option A : Identité basique + IPP + type admission (droits/consentement repoussé J+1)
  Option B : Quasiment tout (droits/consentement requis même urgence)
  
  RECOMMANDATION : A (urgent prime sur administratif, pragmatique)
  → SI ACCEPTÉ : documenter "protocole urgence" formellement (Golden Process)

QUESTION 2 : Consentement en urgence — dérogation acceptable ?
  Option A : Consentement ORAL tracé (notes) + ÉCRIT rattrapage J+1
  Option B : Pas de dérogation, consentement écrit obligatoire même urgence
  
  RECOMMANDATION : A (conformité RGPD maintenue par rattrapage ; urgence vitale acceptable)
  → SI ACCEPTÉ : protocole "consentement rattrapage" + responsable J+1 + audit

QUESTION 3 : Vérification droits urgence — peut-elle être repoussée à J+1 ?
  Option A : Droits non-vérifiés urgence OK ; vérification J+1 ; facturation préliminaire OK
  Option B : Droits obligatoires même urgence (appel mutuelle 24/7)
  
  RECOMMANDATION : A (pragmatique) + obligation J+1 max
  → SI ACCEPTÉ : SLA "vérification droits avant facturation finale"
```

**Impact gouvernance** : Ces décisions formalisent l'implicite actuel → plus de tension, acceptation claire des acteurs.

---

### 7.2 **BUDGET IT/INFRA — Rentabilité et horizon ROI**

**Enjeu** : Investissements substantiels (Quick Wins 100-150 k€ ; Actions structurantes 300-600 k€) nécessitent justification financière claire.

**Décisions requises** :

```
QUESTION 1 : Montant budget IT/Infra acceptable ?
  Option A : 100-150 k€ (Quick Wins : infra accueil + BI)
  Option B : 300-400 k€ (+ architecture SIH complète)
  Option C : Séquentiel (A d'abord, évaluer avant B)
  
  RECOMMANDATION : C (prudent ; Quick Wins 3-6 mois ROI 100-150 k€/an, THEN évaluer B)

QUESTION 2 : Modèle financier : incluir "coût inaction" ?
  Option A : Oui (perte 220-430 k€/an statu quo vs. investissement)
  Option B : Non (seulement coûts directs investissement)
  
  RECOMMANDATION : A (décision plus fondée si incluir perte continue)
  → Présentation DG : "ne pas agir = perte 350 k€/an ; agir = invest 300 k€/an 1, 
     break-even 1 an, puis gain 350 k€/an"

QUESTION 3 : Sponsor budget : opérations vs. transformation ?
  Option A : Budget opérations (DIM courant)
  Option B : Budget projet/transformation (DG)
  
  RECOMMANDATION : B (refonte = transformation, not operation)
  → Implications : sponsor DG visible ; deadline non-négociable ; governance CODIR
```

**Impact gouvernance** : Clarté budgétaire = dès go/no-go CODIR = évite "projet traîne 5 ans".

---

### 7.3 **RESSOURCES HUMAINES — Staffing et déploiement**

**Enjeu** : Quick Win #4 (FTE complétude) + Action Structurante #2 (Manager Circuit) = 1.5-2.5 FTE nouvelle.

**Décisions requises** :

```
QUESTION 1 : FTE "gestionnaire complétude" — où vient la ressource ?
  Option A : Redéploiement interne (ex : agent arrière-office)
  Option B : Recruitment externe (2-3 mois, coût 50-60 k€)
  Option C : Pas de FTE (complétude par tous en parallèle = no budget)
  
  RECOMMANDATION : A (plus rapide, interne) SI capacité existe; ELSE B
  → Implication : identifier candidat dès semaine 2, transition plan

QUESTION 2 : "Manager Circuit" hiérarchie — qui supervise ?
  Option A : DIM
  Option B : Direction Admission/Finance
  Option C : Directement DG (transverse)
  
  RECOMMANDATION : C (Manager Circuit = transverse, ne peut pas être subordonné une direction)
  → Scope autorité doit être définie (SLA ? escalade ? change process ?)
```

**Impact gouvernance** : Staffing = blocage réel souvent non-vu. Doit être arbitré DG (budget) tôt.

---

### 7.4 **CHANGE MANAGEMENT — Résistance attendue, mitigation dès départ**

**Enjeu** : Tous les changements = dérangement workflows établis. Risque réel : équipes bloquent (ex : accueil résiste infra SIH).

**Décisions requises** :

```
QUESTION 1 : Propriétaire change management ?
  Option A : Manager Circuit
  Option B : Manager Circuit + RH ensemble
  Option C : External consultant (support 6 mois)
  
  RECOMMANDATION : A + C (Manager = propriétaire ; external = design + démarrage)

QUESTION 2 : Approche "command & control" vs. "participatory" ?
  Option A : Top-down (direction décide, équipes exécutent)
  Option B : Co-design (équipes impliquées dès conception)
  
  RECOMMANDATION : B (adoption meilleure + idées meilleures)
  → Ateliers dès conception avec reps équipes (QW + Actions struct)

QUESTION 3 : Budget formation/coaching utilisateur ?
  Option A : Minimal (5 k€ pour training)
  Option B : Substantiel (30-50 k€ pour coach terrain, support 6 mois)
  
  RECOMMANDATION : B (training seul insuffisant ; coaching terrain change behavior)
```

**Impact gouvernance** : Change = pré-condition succès, not option. Budget + propriétaire requis.

---

### 7.5 **RISQUE LÉGAL/CONFORMITÉ — Dossiers non-tracés, consentement absent**

**Enjeu** : Régularisations informelles = RGPD violation. Consentement absent = responsabilité civile. Audit externe découvrirait = amende/redressement.

**Décisions requises** :

```
QUESTION 1 : Tolérance risque légal "dossiers non-tracés" ?
  Option A : Zéro (obligation immédiate traçabilité)
  Option B : Phased (ex : 6 mois pour conformité)
  Option C : Accepté ("c'est géré, risque faible")
  
  RECOMMANDATION : A (RGPD non-négociable)
  → Action Structurante #7 (audit légal) URGENT (not wait 6 mois)

QUESTION 2 : "Consentement rattrapage J+1" accepté comme compliant ?
  Option A : Oui (mécanisme acceptable urgence vitale)
  Option B : Non (consentement obligatoire préalable)
  
  RECOMMANDATION : A (jurisprudence accepte urgence) MAIS formaliser
  → Protocole consentement urgence + rattrapage formalisé + audit J+1
```

**Impact gouvernance** : Compliance = pré-condition, not "nice to have". Audit dès semaine 2-3.

---

### 7.6 **KPI/ACCOUNTABILITY — Comment mesurer succès transformation**

**Enjeu** : Investissements majeurs doivent être measurable. Absence KPI = feedback loop cassée.

**Décisions requises** :

```
QUESTION 1 : Quels KPI tracker ?
  RECOMMANDATION : 
    - % Admissions complétude J+0 (urgence: 80% ; programmé: 100%)
    - Délai F11→F16 (target: J+1 max)
    - Délai imputation pharmacie (target: J+0 auto)
    - Délai facturation (target: J+3 max)
    - Taux rejet facturation (target: <2%)
    - % Dossiers consentement tracé (target: 100%)
    - % Modifications dossier tracées (target: 100%)

QUESTION 2 : Qui reporte KPI, à qui, quelle fréquence ?
  RECOMMANDATION : Manager Circuit
    - Rapport quotidien (équipes opération via dashboard)
    - Rapport hebdo (CODIR)
    - Rapport mensuel (CODIR + analyse trends)

QUESTION 3 : Conséquence si KPI dévié (ex : complétude tombe sous 70%) ?
  RECOMMANDATION : 
    - Manager Circuit investigate cause + propose correction
    - Si bloquage inter-fonction → escalade CODIR
    - Si implémentation issue → délai reasessé
```

**Impact gouvernance** : KPI = visibility, visibility = accountability, accountability = change.

---

### 7.7 **SEQUENCING/DÉPENDANCES — Quel ordre implémenter changements**

**Enjeu** : 8 Quick Wins + 8 Actions = beaucoup de parallèles. Certaines dépendances : ex : pas peut pas implémenter checkpoints continus (QW#7) avant dashboard (QW#8) existe.

**Recommandation de séquençage** (voir section 5-6 pour détail) :

```
PARALLELIZABLE (sem 1-3) :
  - AS#2 : Manager Circuit (création)
  - AS#6 : Commission urgent/administratif
  - QW#1 : F16 workflow
  - QW#3 : Consentement tracé
  - QW#8 : SLA/dashboard

DEPENDENT (sem 2-4) :
  - AS#7 : Audit légal (peut commencer parallèle)
  
SEQUENTIAL (sem 4-12) :
  - QW#4 : FTE (after F16 workflow clarifies demand)
  - QW#2, QW#5, QW#6 : Parallel 4-8 semaines
  - QW#7 : Checkpoints (dépend QW#8 dashboard exist)

LONG-TERM (mois 6-18) :
  - AS#1 : Architecture (seulement après QW succeed = business case)
  - AS#3 : Golden Process (parallel 4-12 sem)
  - AS#4 : Rôles (sequential AS#3 completion)
  - AS#5 : Infra (12-18 sem)
```

**Impact gouvernance** : Roadmap formalisée = délivery réaliste. Évite "tout maintenant" impossible.

---

### 7.8 **RETRAIT RISQUE — Rollback scenario si changement va mal**

**Enjeu** : Grand changement (ex : zéro papier accueil) peut avoir effets non-intentionnés. Besoin "exit strategy".

**Recommandation** :

```
Pour CHAQUE Quick Win/Action, définir ABORT CRITERIA

Exemple AS#1 (Intégration SIH) :
  IF : Stabilité SIH < 90% (availabilité < 90%) pour 2 sem consécutives
  OR : Data integrity (écarts pharmacie vs. SIH > 5%)
  THEN : Rollback architecture précédente + RCA 2 sem + retry avec mitigation

Exemple QW#6 (Zéro papier accueil) :
  IF : Throughput < 80/jour (vs. 90+ baseline) pour > 1 sem
  THEN : Réactiver papier primary + SIH secondary
        Investigate SIH UX/performance
        Retry après fix

GOVERNANCE : Abort decision = Manager Circuit (if clear) or CODIR emergency (if ambiguous)
```

**Impact gouvernance** : Confidence à équipes que changement not "forever" si problématique.

---

## SYNTHÈSE POINTS VIGILANCE GOUVERNANCE

| Point | Décision requise | Délégation | Timing | Impact |
|-------|-----------------|-----------|--------|--------|
| **Urgent vs. admin arbitrage** | Formalize Golden Rules (ex: urgence = min completeness) | CODIR | Sem 1 | Aligne urgences + admin |
| **Budget IT structurant** | Invest 100-150 k€ QW vs. 300-400 k€ total | DG + CFO | Sem 2-3 | ROI 1-2 ans vs. break-even rapide |
| **FTE allocation** | Redeploy 1.5-2.5 FTE | RH + DG | Sem 2-8 | Capacity vs. delivery |
| **Change management** | Propriétaire + external support | DG | Sem 1 | Adoption success |
| **Compliance audit** | Audit légal urgent | DG + Compliance | Sem 2-4 | Risk legals |
| **KPI accountability** | Define metrics + Manager ownership | Manager Circuit | Sem 2-4 | Feedback loops |
| **Sequencing roadmap** | Define parallelization | Manager Circuit + CODIR | Sem 2 | Delivery realism |
| **Retrait risque** | Abort criteria per changement | Manager Circuit | Sem 3 | Confidence mitigation |

---

## RÉSUMÉ EXÉCUTIF — NOTE ADRESSÉE CODIR

### Situation
Le circuit admission-facturation présente un **désalignement critique** entre le formel (22 fonctionnalités F1-F22) et le réel (doubles saisies, admissions incomplètes, régularisations informelles, délais longs, dossiers non-auditables). **Coût annuel : 220-430 k€** de surcharge opérationnelle + risques légaux (RGPD).

### Cause racine
Fragmentation organisationnelle (pas de propriétaire transverse), architecture SIH cloisonnée (pas d'intégration admission-pharmacie-facturation), absence arbitrage formel urgent/administratif, culture acceptation imparfait.

### Plan proposé
1. **Quick Wins (3-6 mois, 100-150 k€ investissement)** : 8 actions rapides, basse difficulté, économies 100-150 k€/an immédiatement
2. **Actions structurantes (3-18 mois, 300-600 k€)** : transformation profonde (Manager Circuit, Golden Process, architecture SIH, change management), économies 250-400 k€/an + conformité
3. **Gouvernance critiques** : 8 arbitrages CODIR requis (urgent vs. administratif, budget, staffing, compliance, KPI, sequencing)

### Timeline réaliste
- **Mois 1-3** : Quick Wins déployés, governnce en place → 100-150 k€/an gagnés
- **Mois 3-12** : Actions structurantes en cours, complétude J+1 atteint → 150-250 k€/an
- **Mois 12-18** : Achèvement refonte, conformité assurée → 250-400 k€/an

### Next Steps
**Semaine 1-2** : CODIR valide arbitrages critiques (urgent vs. admin, budget, staffing) → Go Quick Wins + AS#2 (Manager) + AS#6 (Commission)

---

*Note : Cette note est prête pour présentation CODIR. Elle demande arbitrages stratégiques (pas questions techniques). Sans engagement gouvernance, technique seul n'amènera pas transformation durable.*