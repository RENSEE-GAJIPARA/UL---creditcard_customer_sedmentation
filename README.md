<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f2027,50:203a43,100:2c5364&height=220&section=header&text=Credit%20Card%20Customer%20Segmentation&fontSize=40&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=K-Means%20%7C%20Hierarchical%20%7C%20DBSCAN%20%7C%20Streamlit&descAlignY=58&descSize=18" width="100%"/>

<a href="https://git.io/typing-svg"><img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=20&pause=1200&color=2C9CFF&center=true&vCenter=true&width=700&lines=Unsupervised+Learning+Practical+Exam+%E2%80%94+Set+C;8%2C950+cardholders+%E2%86%92+3+actionable+segments;From+raw+usage+data+to+a+deployed+Streamlit+app" alt="Typing SVG" /></a>

<br/>

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-Clustering-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)](https://scikit-learn.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](notebook/credit_card_customer_segmention.ipynb)
[![Dataset](https://img.shields.io/badge/Dataset-Kaggle-20BEFF?style=for-the-badge&logo=kaggle&logoColor=white)](https://www.kaggle.com/datasets/arjunbhasin2013/ccdata)
[![Demo Video](https://img.shields.io/badge/Demo-Video-red?style=for-the-badge&logo=youtube&logoColor=white)](#-demo-video)

</div>

---

## 📑 Table of Contents

- [📌 Project Overview](#-project-overview)
- [🎯 Objectives](#-objectives)
- [📂 Repository Structure](#-repository-structure)
- [📊 Dataset](#-dataset)
- [🛠️ Tech Stack](#️-tech-stack)
- [🔄 Methodology](#-methodology)
- [📈 Results & Visualisations](#-results--visualisations)
- [👥 Customer Personas](#-customer-personas)
- [🚀 Streamlit App](#-streamlit-app)
- [🌐 Live Streamlit App Link](#-live-streamlit-app-link)
- [🎬 Demo Video](#-demo-video)
- [⚙️ Setup & Installation](#️-setup--installation)
- [📄 Report](#-report)
- [🔮 Future Work](#-future-work)
- [👤 Author](#-author)

---

## 📌 Project Overview

A large Indian private bank (think HDFC / ICICI) wants to move away from one-size-fits-all card upgrades, reward programmes and limit revisions. This project groups **8,950 active credit-card holders** into meaningful **behavioural segments** so Relationship Managers can offer the right product to the right customer, reducing attrition and increasing wallet share.

Behavioural features are engineered from raw usage data, then **three unsupervised algorithms** are tuned, evaluated with internal metrics and compared: **K-Means**, **Agglomerative Hierarchical Clustering** and **DBSCAN**. The best model is saved and served through a **Streamlit** app.

> 🏫 *Red & White Skill Education — Practical Exam — Unsupervised Learning (Set C)*

---

## 🎯 Objectives

- Understand how **clustering** differs from classification.
- Engineer behavioural features (monthly averages, limit usage, payment-to-minimum ratio).
- Tune **K-Means** (Elbow + Silhouette), **Hierarchical** (Dendrogram) and **DBSCAN** (k-NN distance plot + grid search).
- Evaluate with **Silhouette, Davies-Bouldin and Calinski-Harabasz** indices.
- Translate clusters into **actionable credit-card personas** for the business.
- Deploy a scoring pipeline (`.pkl` files + Streamlit app).

---

## 📂 Repository Structure

```
creditcard-segmentation-unsupervised-learning/
│
├── 📁 dataset/
│   └── CC GENERAL.csv                       # Kaggle credit card dataset
├── 📁 images/                               # Plots exported from the notebook (01–08)
├── 📁 models/
│   ├── cc_scaler.pkl                        # Fitted StandardScaler
│   └── cc_segmentation_model.pkl            # Best model + preprocessing metadata + personas
├── 📁 notebook/
│   └── credit_card_customer_segmention.ipynb  # Fully executed notebook
├── 📁 report/
│   └── summary_report.md                    # ~1-page business summary
├── 📄 app.py                                # Streamlit app
├── 📄 requirements.txt                      # Python dependencies
└── 📄 README.md
```

---

## 📊 Dataset

| Item | Details |
|---|---|
| **Name** | Credit Card Dataset for Clustering |
| **Source** | [Kaggle – arjunbhasin2013/ccdata](https://www.kaggle.com/datasets/arjunbhasin2013/ccdata) |
| **Rows** | 8,950 cardholders |
| **Columns** | 18 (17 behavioural features + `CUST_ID`) |
| **Key features** | `BALANCE`, `PURCHASES`, `CASH_ADVANCE`, `CREDIT_LIMIT`, `PAYMENTS`, `MINIMUM_PAYMENTS`, `PRC_FULL_PAYMENT`, `TENURE` |
| **Cleaning** | `CUST_ID` dropped; 1 missing `CREDIT_LIMIT` and 313 missing `MINIMUM_PAYMENTS` imputed with the median |

**Quick insights:** 22.8% of customers never made a purchase, and ~26% of customers generate 80% of total purchase volume.

---

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white&style=flat-square)
![Pandas](https://img.shields.io/badge/-Pandas-150458?logo=pandas&logoColor=white&style=flat-square)
![NumPy](https://img.shields.io/badge/-NumPy-013243?logo=numpy&logoColor=white&style=flat-square)
![Matplotlib](https://img.shields.io/badge/-Matplotlib-11557C?style=flat-square)
![Seaborn](https://img.shields.io/badge/-Seaborn-4C72B0?style=flat-square)
![scikit-learn](https://img.shields.io/badge/-scikit--learn-F7931E?logo=scikitlearn&logoColor=white&style=flat-square)
![SciPy](https://img.shields.io/badge/-SciPy-8CAAE6?logo=scipy&logoColor=white&style=flat-square)
![Joblib](https://img.shields.io/badge/-Joblib-2C5364?style=flat-square)
![Streamlit](https://img.shields.io/badge/-Streamlit-FF4B4B?logo=streamlit&logoColor=white&style=flat-square)

---

## 🔄 Methodology

```mermaid
flowchart LR
    A[Load & EDA] --> B[Feature Engineering]
    B --> C[Outlier Capping<br/>Q3 + 3×IQR]
    C --> D[log1p Transform]
    D --> E[StandardScaler]
    E --> F1[K-Means]
    E --> F2[Hierarchical]
    E --> F3[DBSCAN]
    F1 & F2 & F3 --> G[Metric Comparison]
    G --> H[Personas & Actions]
    H --> I[.pkl + Streamlit App]
```

| Step | What was done |
|---|---|
| **1. EDA** | Missing values, duplicates, histograms (log-scaled), correlation heatmap, utilisation ratio, Pareto analysis |
| **2. Features** | `Monthly_Avg_Purchase`, `Monthly_Avg_Cash_Advance`, `Limit_Usage`, `Payment_to_Minpayment_Ratio` |
| **3. Preprocessing** | Winsorise at Q3 + 3×IQR → `log1p` on skewed money columns → `StandardScaler` |
| **4. K-Means** | Elbow + Silhouette for k = 2–10 → **k = 3** |
| **5. Hierarchical** | Ward dendrogram, cut at 3 clusters; ward vs complete vs average compared |
| **6. DBSCAN** | k-NN distance elbow (ε ≈ 2.03) + grid over ε × min_samples → ε = 2.03, min_samples = 10 |
| **7. Evaluation** | Silhouette ↑, Davies-Bouldin ↓, Calinski-Harabasz ↑, noise %, seed-stability check |
| **8. Deployment** | `cc_scaler.pkl`, `cc_segmentation_model.pkl`, `predict_segment()`, Streamlit app |

---

## 📈 Results & Visualisations

### Algorithm Comparison

| Algorithm | Settings | Clusters | Silhouette ↑ | Davies-Bouldin ↓ | Calinski-Harabasz ↑ | Noise % |
|---|---|---|---|---|---|---|
| 🏆 **K-Means** | k = 3, k-means++ | 3 | **0.223** | 1.679 | **2,729** | 0.0 |
| Agglomerative | ward, 3 clusters | 3 | 0.198 | 1.728 | 2,213 | 0.0 |
| DBSCAN | ε = 2.03, min_samples = 10 | 3 | 0.122 | 0.951 | 87 | 8.3 |

**K-Means** ranks first overall and is **stable across seeds** (silhouette std ≈ 0.000), so it is the model deployed. DBSCAN's 8.3% noise points are useful as a flag for unusual accounts needing manual review. K-Means vs Hierarchical agreement (Adjusted Rand Index) = 0.33.

### 🔍 Exploratory Analysis

<table>
<tr>
<td align="center"><b>Feature Distributions</b><br/><img src="images/01.feature_distributions.png" width="480"/></td>
<td align="center"><b>Correlation Heatmap</b><br/><img src="images/02.feature_correlation_heatmap.png" width="480"/></td>
</tr>
</table>

### 🔵 K-Means

<p align="center"><img src="images/03.kmeans_cluster_selection.png" width="800"/></p>
<p align="center"><img src="images/04.kmeans_balance_vs_purchases_%26_3d_clusters.png" width="900"/></p>

### 🌳 Hierarchical Clustering

<p align="center"><img src="images/05.hierarchical_dendrogram.png" width="700"/></p>
<p align="center"><img src="images/06.hierarchical_balance_vs_purchases_%26_3d_clusters.png" width="800"/></p>

### 🔴 DBSCAN

<p align="center"><img src="images/07.dbscan_k_distance.png" width="550"/></p>
<p align="center"><img src="images/08.dbscan_balance_vs_purchases_%26_3d_clusters.png" width="800"/></p>

---

## 👥 Customer Personas

| Segment | Share | Behaviour | Recommended Action |
|---|---|---|---|
| 💎 **Premium Spenders** | 36% | High purchases (≈2.2× average), above-average credit limit | Upgrade to premium card with travel & lifestyle rewards and a higher limit |
| 💸 **Cash-Advance Reliant** | 32% | Heavy cash advances (≈2.2×), almost no purchases, rarely pay in full | Offer low-rate personal loan / cash-advance-to-EMI conversion; monitor credit risk |
| 🛒 **Low-Balance Full Payers** | 32% | Near-zero balance, pay in full, light spending | Drive usage with cashback / EMI-on-card offers and merchant tie-ups |

---

## 🚀 Streamlit App

An interactive app that scores a new cardholder using the saved scaler and model and returns the **segment**, the **recommended business action** and the **segment profile table**.

**Features**
- Enter balance, purchases, cash advance, credit limit, payments, frequencies, transaction counts and tenure
- Same preprocessing as training (feature engineering → outlier caps → log1p → scaling)
- Instant persona + recommended action
- Highlighted segment profile comparison table

**Run locally**

```bash
pip install -r requirements.txt
streamlit run app.py
```

<!-- Replace with a screenshot of the running app: save it as images/09.streamlit_app.png -->
<!-- <p align="center"><img src="images/09.streamlit_app.png" width="900"/></p> -->

---

## 🌐 Live Streamlit App Link

<div align="center">

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](PASTE_YOUR_STREAMLIT_APP_LINK_HERE)

[![Live App](https://img.shields.io/badge/🚀%20Try%20the%20Live%20App-Streamlit%20Cloud-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://creditcardcustomersedmentation.streamlit.app/)

</div>

---

## 🎬 Demo Video

[![Watch the demo](https://img.shields.io/badge/▶%20Watch%20the%20Demo-Google%20Drive%20%2F%20YouTube-red?style=for-the-badge&logo=youtube&logoColor=white)](https://drive.google.com/file/d/1VxfBUSPnYMPQsytYfJFepr_w3dJSCWjS/view?usp=sharing)

---

## ⚙️ Setup & Installation

```bash
# 1. Clone the repository
git clone https://github.com/RENSEE-GAJIPARA/creditcard-segmentation-unsupervised-learning.git
cd creditcard-segmentation-unsupervised-learning

# 2. (Optional) create a virtual environment
python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # macOS / Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the notebook
jupyter notebook notebook/credit_card_customer_segmention.ipynb

# 5. Launch the app
streamlit run app.py
```

---

## 📄 Report

The ~1-page business summary (problem, features, algorithm comparison, segments, actions, next steps) is in [`report/summary_report.md`](report/summary_report.md).

---

## 🔮 Future Work

- Add transaction-level and time-series features (spend trends, merchant categories)
- Use delinquency / churn labels for semi-supervised refinement and validation
- Real-time scoring API (FastAPI) behind the saved scaler and model
- Re-cluster periodically to detect segment drift

---

## 👤 Author

<div align="center">

**Rensee Gajipara**
B.Tech — Artificial Intelligence & Data Science, SCET, Surat

[![GitHub](https://img.shields.io/badge/GitHub-RENSEE--GAJIPARA-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/RENSEE-GAJIPARA)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Rensee%20Gajipara-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/rensee-gajipara)
[![Gmail](https://img.shields.io/badge/Gmail-renseegajipara%40gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:renseegajipara@gmail.com)

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:2c5364,100:0f2027&height=120&section=footer" width="100%"/>

⭐ *If you found this useful, consider starring the repository.*

</div>

</div>
