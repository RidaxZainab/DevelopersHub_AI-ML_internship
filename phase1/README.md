# 📈 Task 2: Short-Term Stock Forecasting Engine (`task_2_stock_prediction`)

### 🎯 Strategic Goal
To forecast the subsequent market tracking cycle's dynamic closing valuation (`Next_Close`) of **Tesla (TSLA)** stock as a function of continuous historical feature sets, utilizing an automated evaluation pattern of stock performance characteristics.

### 🧠 Complete Technical Approach (What is Happening?)
* **Live Data Ingestion Pipeline:** Immediately upon execution, the script instantiates synchronous API wrappers that systematically stream and harvest historical pricing vectors from Yahoo Finance (`yfinance`) data endpoints.
* **Predictive Target Engineering:** During the data transformation phase, a temporal sequence shift logic is applied by shifting the actual closing price parameters array by exactly `-1` step backward. This generates a new structural target block named `Next_Close`, training the model to map the linear impact of today's continuous features on tomorrow's asset value.
* **Multi-Feature Array Isolation:** Autocorrelated mathematical attributes are dropped to strictly isolate fundamental, independent feature variables (`Open`, `High`, `Low`, `Volume`) via array slicing sequences.
* **Chronological Pipeline Matrix:** Because market trends carry a critical temporal sequence dependency, standard random data shuffling is bypassed (`shuffle=False` using an 80-20 train-test ratio) to ensure validation sets remain completely clean of look-ahead data leakage patterns.
* **Regression Modeling:** Isolated data segments are fed into a **Linear Regression Engine** to calculate optimal feature weights and intercept matrices, subsequently rendering an interactive graph mapping actual validation limits against AI-predicted trends.

---

# 🩺 Task 3: Heart Disease Risk Analysis Dashboard (`task_3_heart_disease`)

### 🎯 Strategic Goal
To parse patients' clinical parameters and multi-dimensional physiological mapping matrices (such as cholesterol levels, maximum heart rate index, and resting blood pressure parameters) to mathematically classify whether a subject is safe or at-risk via algorithmic boundary calculations.

### 🧠 Complete Technical Approach (What is Happening?)
* **High-Dimensional Benchmark Simulation:** To isolate the code logic from external network vulnerabilities or broken links, a `make_classification` optimization layer synthesizes a high-fidelity dataset of 303 medical profiles. This synthetic data maps exactly onto standard UCI Clinical Heart Disease benchmark constraints (e.g., Age, CP, Thalach, Ca).
* **Stratified Data Distribution:** Following feature transformation, a standard `train_test_split` controller separates the multi-dimensional arrays into designated training and testing matrices.
* **Boundary Classifier Fitting:** The feature matrices are processed via a stable **Maximum Entropy Logistic Regression Classifier**, optimizing a sigmoid decision boundary to calculate distinct mathematical probability risks.
* **Advanced Performance Analytics:**
  * **Confusion Matrix Profiler:** True Negative, False Positive, False Negative, and True Positive metrics are mapped into discrete tabular frames, visualized via a annotated `seaborn` heatmap to check true classification thresholds.
  * **ROC-AUC Diagnostics:** True Positive Rate coordinates are plotted against False Positive Rate scales across changing probability boundaries to determine the model's absolute discriminatory capacity via the Area Under the Curve (AUC).
  * **Absolute Feature Importance Matrix:** Mathematical parameters are extracted from the learned model coefficients to chart an explicit feature impact profile, visualizing precisely which clinical biomarkers influence the model's classification boundaries the most.

---

# 🤖 Task 4: Rule-Aligned AI Medical Chatbot (`task_4_health_chatbot`)

### 🎯 Strategic Goal
To establish a zero-dependency, automated terminal stream interface that maps natural language queries against localized health contexts, providing explicit, safety-vetted conversational guidelines while strictly avoiding hazardous medical diagnostic claims or prescription liabilities.

### 🧠 Complete Technical Approach (What is Happening?)
* **Prompt Engineering Isolation Protocol:** At the foundation of the conversational flow, a highly customized `SYSTEM_PROMPT` wrapper architecture is injected. This structural persona forces the assistant's responses to remain empathetic and clear while rigidly restricting unauthorized diagnostic declarations or drug dosage variables.
* **Zero-Dependency Array Engineering:** To fully bypass unpredictable external web response latency or expired bearer API network tokens, the chatbot implements an independent, localized application routing strategy.
* **Intent Parsing Module:** An active, continuous input evaluation loop sweeps the console string tokens. A parsing algorithm scans user queries against a curated local dictionary covering distinct informational keys (such as *fever, cough, sore throat, or paracetamol safety metrics*).
* **Hardcoded Disclaimer Injection:** To guarantee operational compliance and mitigate automation risks, the execution logic automatically appends deterministic regulatory warning text blocks at the base of every generated assistant string.
* **Interface Loop Processing:** The runtime state begins by generating pre-configured example test scripts to demonstrate behavioral alignment, then transitions into a live user query evaluation loop that remains active until terminated via the targeted command keyword `exit`.
