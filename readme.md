# Semantic Plagiarism Reducer (Non-LLM)

A **technical, non-LLM semantic text transformation system** built using embeddings and NLP.
The project performs **semantic lexical replacement** using vector similarity — not generation, not rewriting, not LLMs.

---

## Core Function

* Parse sentence structure
* Identify replaceable (meaning-carrying) tokens
* Generate semantic candidates using word embeddings
* Select best candidate using sentence-level semantic similarity
* Replace tokens safely
* Validate meaning preservation

---

## System Pipeline

```
Input Text
 → NLP Parsing (spaCy)
 → POS Filtering
 → Replaceable Token Selection
 → Word Embedding Similarity (GloVe)
 → Candidate Generation
 → Context Selection (Sentence Embeddings)
 → Token-Level Replacement
 → Semantic Validation
 → Output Text
```

---

## Tech Stack

| Layer              | Tech                                    |
| ------------------ | --------------------------------------- |
| NLP                | spaCy                                   |
| Word Semantics     | GloVe (Gensim)                          |
| Sentence Semantics | SentenceTransformers (all-MiniLM-L6-v2) |
| Similarity         | Scikit-learn                            |
| Vector Ops         | NumPy                                   |

---

## Project Structure

```
semantic-plagiarism-reducer/
│
├── nlp_preprocess.py
├── filter_replaceable.py
├── find_similar_list.py
├── replace_best_match.py
├── similarity_check.py
├── test.py
├── requirements.txt
└── README.md
```

---

## Installation

```bash
pip install spacy gensim sentence-transformers scikit-learn numpy
python -m spacy download en_core_web_sm
```

---

## Run

```bash
python test.py
```

---

## Example

**Input**

```
AI improves agriculture by predicting crop yield.
```

**Output**

```
AI enhances farming by forecasting harvest output.
```

---

## Classification

**Type:** Embedding-based semantic transformation system
**Approach:** Vector similarity + NLP + control logic
**Model Type:** Non-generative AI
**LLM Usage:** None

---

## Scope

* Semantic replacement (lexical level)
* Meaning preservation
* Embedding-based control
* Non-generative architecture

---


