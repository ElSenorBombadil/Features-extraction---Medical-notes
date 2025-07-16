# 🧠 Medical NLP Feature Extractor

## 📌 Description

Avec l'explosion des données médicales non structurées et la pression croissante sur les systèmes de santé à opérer avec des ressources limitées, le besoin d'automatiser l'analyse de textes cliniques n’a jamais été aussi urgent.

Ce projet propose une **pipeline de traitement du langage naturel (NLP)** croisant les performances de **SpaCy** et **SciSpaCy**, deux bibliothèques puissantes de NLP — la seconde étant spécialisée dans le vocabulaire biomédical. Ensemble, elles permettent d’extraire automatiquement des informations critiques telles que :
- le nom du patient et du médecin,
- les pathologies mentionnées (et leur sévérité),
- les médicaments,
- la chronicité (acuteness) d’une condition médicale,
- et si la condition est **niée ou affirmée** dans le texte.

> 🎯 L’objectif à long terme est de **soulager les professionnels de santé des tâches redondantes**, en tirant parti des dernières avancées en NLP.

---

## 🚀 Fonctionnalités

- 📑 Analyse de corpus médical brut ligne par ligne
- 🧠 Extraction d'entités médicales par double-modèle (SpaCy & SciSpaCy)
- ⚖️ Fusion des résultats avec **score de confiance pondéré**
- 📊 Génération de tableaux :
  - Résultats d'extraction (`df_results`)
  - Score de confiance (`df_confidence`)
  - Provenance des entités (`df_sources`)
- ✅ Évaluation automatique via `df_true` pour mesurer la précision
- 🔍 Prêt pour extension vers **BioBERT**, **ClinicalBERT**, et **modèles génératifs type Mistral**

---

## 📂 Structure du projet

```bash
NER_Project/
│
├── data/
│   └── corpus.txt                # Corpus médical à analyser
│
├── src/
│   ├── feature_extraction.py    # Contient les classes SpaCy et SciSpaCy
│   ├── merger.py                # Fusion des résultats & calcul des scores
│   ├── pipeline.py              # Script principal d'orchestration
│   └── utils.py                 # Fonctions utilitaires
│
├── evaluation/
│   ├── df_true_generator.py     # Génère les labels vrais pour l’évaluation
│   └── evaluate.py              # Évalue l'extraction vs. df_true
│
├── setup/
│   └── INSTALL.md               # Instructions d’installation détaillées
│
├── requirements.txt             # Dépendances Python & modèles NLP
└── README.md                    # Ce fichier

```

---

## 🛠️ Installation rapide
```bash
git clone https://github.com/votre-utilisateur/NER_Project.git
```

> Voir setup/INSTALL.md pour des instructions plus détaillées ou en cas de conflit d'environnement.

--- 

### ▶️ Utilisation
Placez votre corpus ligne par ligne dans data/corpus.txt

Lancez la pipeline principale :

  ```bash
  python src/pipeline.py
```
Les résultats seront sauvegardés sous forme de DataFrame :

- df_results → Résultats principaux

- df_confidence → Score de confiance

- df_sources → Source du modèle utilisé

Pour évaluer la performance :

```bash
python evaluation/evaluate.py
```

--- 

### 📈 Roadmap
- [x] Pipeline rule-based : SpaCy + SciSpaCy

- [ ] Intégration de BioBERT / ClinicalBERT

- [ ] Détection multi-entités par phrase

- [ ] Support IA générative (Mistral, Med-GPT…)

--- 

## 📦 Contenu du fichier requirements.txt recommandé
```txt
pandas>=1.3.0
spacy==3.7.2
scispacy==0.5.3
en-core-web-sm @ https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.7.1/en_core_web_sm-3.7.1.tar.gz
en_ner_bc5cdr_md @ https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.5.3/en_ner_bc5cdr_md-0.5.3.tar.gz
```
---

## 🔍 Problèmes connus
Si vous avez une erreur avec spacy et scispacy ensemble, assurez-vous qu’ils utilisent la même version compatible (3.x).

Sur Mac M1, préférez installer via miniforge et éviter les wheels non optimisés.

--- 

## 📄 Licence
Ce projet est sous licence MIT – libre à l’usage académique ou professionnel.
