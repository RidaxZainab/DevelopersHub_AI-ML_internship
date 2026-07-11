# Advanced AI & Machine Learning Task Set

This repository contains a comprehensive suite of advanced Artificial Intelligence and Machine Learning solutions. The projects span across Deep Learning fine-tuning, Retrieval-Augmented Generation (RAG) architecture, and Large Language Model (LLM) prompt engineering frameworks.

---

## 🎯 Overall Repository Objective

The core objective of this repository is to demonstrate production-ready implementations of modern Natural Language Processing (NLP) techniques. It showcases how to move from traditional **fine-tuning of open-source transformer models** to **orchestrator frameworks like LangChain** and **structured LLM prompt engineering** for real-world automation tasks.

### Core Goals:
* **Domain Adaptation:** Fine-tune pre-trained language models on domain-specific datasets (AG News) to achieve high-accuracy classification.
* **Knowledge Isolation & Memory:** Implement context-aware RAG systems that accurately reference custom external corporate/technical documents while maintaining stateful conversation history.
* **Structured LLM Output:** Build deterministic automated categorization pipelines using cloud-based/local LLMs, comparing zero-shot and few-shot inference properties while enforcing strict JSON output structures.
* **Production Prototyping:** Deploy user-facing interactive interfaces for every backend engine using Streamlit and Gradio.

---

## 🛠️ Detailed Implementation Breakdown

### 📰 Task 3: News Topic Classifier Using BERT

#### Implementation Workflow:
1. **Data Ingestion & Tokenization:** The script loads the raw **AG News Dataset** from Hugging Face. The text is passed through the `bert-base-uncased` tokenizer, which applies WordPiece tokenization, adds special tokens (`[CLS]`, `[SEP]`), handles truncation at a maximum length of 128 tokens, and dynamically pads the inputs into uniform tensors.
2. **Model Graph Setup:** We initialize `AutoModelForSequenceClassification` with a sequence classification head configured with 4 target class output nodes mapping to the dataset categories: *World (0), Sports (1), Business (2), and Sci/Tech (3)*.
3. **Hyperparameter Optimization & Training Loop:** Using the Hugging Face `Trainer` API, the model undergoes supervised fine-tuning across 3 epochs with a learning rate of $2 \times 10^{-5}$ managed by an AdamW optimizer, incorporating a weight decay of $0.01$ to mitigate overfitting. 
4. **Metric Evaluation Strategy:** At the conclusion of each epoch, the system runs validation text arrays through the model to track loss curves and extract performance characteristics using $F_1$-macro scores and standard accuracy calculations via `scikit-learn`.
5. **Deployment:** The optimized runtime model weight checkpoints are serialized locally. `app.py` loads these weights, builds a feature extraction pipeline, and binds it to a clean **Gradio** web application for real-time inference testing.

---

### 🤖 Task 4: Context-Aware Chatbot Using LangChain & RAG

#### Implementation Workflow:
1. **Document Processing Pipeline:** The unindexed custom corpus (`knowledge_base.txt`) is read via LangChain's `TextLoader` and broken down using `RecursiveCharacterTextSplitter` into overlapping text chunks (size: 300 characters, overlap: 50 characters) to ensure zero context loss across chunk boundaries.
2. **Dense Vector Space Mapping:** Each text chunk is processed using the local open-source `all-MiniLM-L6-v2` SentenceTransformer embedding model, converting chunks into dense 384-dimensional mathematical vector spaces.
3. **Vector DB Storage & Search Indexing:** These generated embeddings are indexed into an in-memory `FAISS` vector database. The database is exposed as a retriever component configured to perform similarity searches matching the top 2 highest-scoring localized vectors ($k=2$).
4. **History-Aware Contextualization:** When a user submits a follow-up query containing pronouns or dependent shorthand, a specialized `history_aware_retriever` chain passes the active query combined with the array list of `chat_history` to the LLM. The LLM reformulates the request into a fully qualified standalone query.
5. **RAG Compilation & Memory Loop:** The standalone query performs a similarity lookup inside the FAISS database. The retrieved context documents and the original conversation logs are compiled into a strict engineering prompt structure and routed to `gpt-4o-mini`. The session state memory appends the runtime transaction logs (`HumanMessage` and `AIMessage`) inside the persistent **Streamlit** UI window loop.

---

### 🎫 Task 5: Auto-Tagging Support Tickets Using LLM

#### Implementation Workflow:
1. **System Prompt & Tag Constraints:** The system prompt explicitly isolates the allowed classification classes, bounding the operational logic to a fixed list: `["Billing", "Technical Support", "Account Access", "Feature Request", "Bug Report", "Security"]`.
2. **Strict Structure Enforcement:** To prevent parsing exceptions, we enforce deterministic schema generation by setting the API parameters to `response_format={"type": "json_object"}`. The system prompt contains a precise JSON prototype template that requires the output to return an array containing exactly the **top 3 most probable tags** sorted by descending confidence scores.
3. **Technique A Implementation (Zero-Shot):** The raw input support ticket is framed directly into the standard context prompt instructions without context history clues or pattern examples, forcing the model to infer classification purely from internal pre-trained semantic understanding.
4. **Technique B Implementation (Few-Shot):** The ticket prompt is prepended with highly specific domain examples showcasing complex multi-label classification tickets (e.g., tickets containing overlapping billing bugs or credential access issues). This explicitly calibrates the model's confidence ranking outputs.
5. **Execution Loop & Analysis:** The final script runs an isolated pipeline loops over the target data arrays, feeding the inputs through both architectures simultaneously, and displays a side-by-side terminal performance ranking grid to analyze prediction confidence variance.

---

