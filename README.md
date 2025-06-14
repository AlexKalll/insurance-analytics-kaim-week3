

```markdown
# Insurance Analytics | ML

## 📘 Project Overview

This project focuses on analyzing and modeling insurance policy and claim data for risk evaluation and premium optimization. The dataset comprises over 1 million rows from an insurance portfolio with features including vehicle characteristics, policy details, and financials (claims, premiums). The goal is to explore risk drivers and build predictive models for smarter pricing and segmentation.

---

## 🏗️ Project Setup

### Repo Structure
We follow a modular and professional structure with the following main directories:

```

insurance-analytics-kaim-week3/
├── src/
├── scripts/
├── notebooks/
├── data/
│   ├── raw/
│   └── processed/
├── tests/
├── .github/workflows/
├── .vscode/
├── config/
├── readme.md
├── requirements.txt
├── .gitignore
├── .vscode


### Tech Stack
- Python 3.11+
- Pandas, NumPy, Seaborn, Matplotlib
- Scikit-learn, XGBoost, LIME
- DVC (for data versioning)
- PyTest (for testing)
- GitHub Actions (CI/CD)

---

## 📊 Exploratory Data Analysis 

The dataset contains 1,000,098 rows and 52 columns. The main steps completed include:

### 🔹 Data Structure Review
- 15 numerical columns (e.g., `TotalPremium`, `TotalClaims`, `CustomValueEstimate`)
- 36 categorical columns (e.g., `Province`, `VehicleType`, `Gender`)
- 1 boolean column

### 🔹 Missing Data
- Significant nulls found in:
  - `NumberOfVehiclesInFleet` (100%)
  - `CustomValueEstimate` (77%)
  - Vehicle metadata (`make`, `Model`, `bodytype`, etc.) — ~552 rows missing

### 🔹 Key Metrics
- Summary statistics calculated for premium and claims columns
- Loss Ratio metric to be explored in relation to Province, Gender, VehicleType
- Placeholder for visualizations:
  - ![Distribution of Total Premiums](<add_path>)
  - ![Claims by Province](<add_path>)
  - ![Loss Ratio by Vehicle Type](<add_path>)

---

## 📈 Next Steps
- Conduct EDA visualizations (histograms, boxplots, barplots)
- Calculate and visualize Loss Ratio patterns
- Analyze outliers and temporal trends in claim severity and frequency

---

## 🚧 In Progress
- EDA notebooks per domain (e.g., geography, vehicle, financials)
- DVC versioning (Task 2)
- Hypothesis testing (Task 3)
- Predictive modeling (Task 4)

---

```

