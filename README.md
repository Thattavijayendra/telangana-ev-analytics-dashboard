# Telangana EV Charging Electricity Consumption Analysis

### Real-World Data Collection, EDA & Power BI Dashboard

An end-to-end data analytics project analyzing **EV charging electricity consumption in Telangana, India**, using real-world data scraped and collected from the **Telangana Open Data Portal**. 

Unlike pre-cleaned datasets, this project covers the entire data lifecycle — from automated web scraping using Playwright to data cleaning, exploratory data analysis (EDA), statistical modeling, and an interactive executive Power BI dashboard.

---

## 📌 Table of Contents
- [Project Overview](#-project-overview)
- [Key Business Insights & Findings](#-key-business-insights--findings)
- [Project Workflow](#-project-workflow)
- [Tools & Technologies](#-tools--technologies)
- [Data Cleaning & Validation](#-data-cleaning--validation)
- [Exploratory Data Analysis](#-exploratory-data-analysis)
- [Power BI Dashboard Overview](#-power-bi-dashboard-overview)
- [Repository Structure](#-repository-structure)
- [Data Source](#-data-source)
- [Future Roadmap](#-future-roadmap)
- [Author](#-author)

---

## 📊 Project Overview

This project analyzes monthly EV charging electricity consumption data across two primary DISCOMs (Distribution Companies) in Telangana:
- **TGNPDCL** (Northern Power Distribution Company of Telangana)
- **TGSPDCL** (Southern Power Distribution Company of Telangana)

* **Analysis Period:** January 2023 – August 2026
* **Scope:** Electricity consumption trends, recorded service growth, reported load capacities, circle-level distribution, and infrastructure demand-load screening.

---

## 💡 Key Business Insights & Findings

1. **Massive Growth Trajectory:** Recorded EV charging consumption in Telangana experienced sustained exponential growth from Jan 2023 through Aug 2026.
2. **Heavy Regional Concentration:**
   * **TGSPDCL** accounts for **33.80M units**, compared to **2.59M units** in **TGNPDCL**.
   * Top 5 circles in TGSPDCL contribute **~61.4%** of its consumption (*Cybercity* leading).
   * Top 5 circles in TGNPDCL contribute **~71.6%** of its consumption (*Hanumakonda* leading).
3. **Usage Intensity:**
   * **TGSPDCL Average:** 1,642.59 Units / Recorded Service / Month
   * **TGNPDCL Average:** 513.95 Units / Recorded Service / Month
4. **Reported Load vs. Actual Consumption:** Correlation analysis proved that reported load alone is a poor predictor of actual energy draw, highlighting the need for dynamic demand-load screening rather than static capacity planning.

---

## ⚙️ Project Workflow

```text
Telangana Open Data Portal
           │
           ▼
   Automated Web Scraping (Playwright)
           │
           ▼
     Raw CSV Datasets
           │
           ▼
   Data Cleaning & Validation (Python, Pandas)
           │
           ▼
   Exploratory Data Analysis (Pandas, NumPy, Seaborn)
           │
           ▼
   Statistical Analysis & Screening (SciPy)
           │
           ▼
   Interactive Power BI Dashboard (DAX, Data Modeling)
```

---

## 🛠️ Tools & Technologies

| Domain | Tools & Libraries |
| :--- | :--- |
| **Data Collection** | Playwright (Python) |
| **Data Manipulation** | Python, Pandas, NumPy |
| **Exploratory Analysis** | Matplotlib, Seaborn, SciPy |
| **Business Intelligence** | Power BI, DAX |
| **Documentation & Versioning** | Git, GitHub, Markdown |

---

## 🧹 Data Cleaning & Validation

Raw data from government portals often contains inconsistencies. Key data quality checks and interventions included:
* **Missing Value Handling:** Identified 554 record gaps in `billedservices` for TGSPDCL and applied context-aware imputation.
* **Deduplication:** Detected and purged 64 identical duplicate records.
* **Anomaly Flagging:** Flagged 13 instances of negative consumption records as domain anomalies while retaining original records for audit trails.
* **Outlier Correction:** Investigated a high reported load spike of `30,030 kW` for *TGNPDCL Nizamabad - SN PURAM* (Jan 2023) against historical benchmarks and corrected it to `30 kW`.

---

## 📈 Exploratory Data Analysis

### 1. DISCOM Performance & Growth
```text
Total Consumption Breakdown:
├── TGSPDCL: 33.80 Million Units
└── TGNPDCL:  2.59 Million Units
```

### 2. Services vs. Consumption Correlation
Strong positive linear associations were verified between active EV service connections and total consumption:
* **TGNPDCL Pearson Correlation ($r$):** `0.897`
* **TGSPDCL Pearson Correlation ($r$):** `0.791`

### 3. Demand–Load Gap Screening
To identify grid stress or expansion opportunities, a **Demand–Load Index** was created by evaluating:
$$	ext{Demand-Load Gap} = 	ext{Percentile}(	ext{Consumption}) - 	ext{Percentile}(	ext{Reported Load})$$
Areas with positive gaps indicate high consumption relative to allocated capacity, signaling candidates for prioritized infrastructure reviews.

---

## 🖥️ Power BI Dashboard Overview

The project features a **3-page interactive Power BI dashboard**:

* **Page 1: Executive Overview** — Global KPIs (36M Units, 20K Services, 830K Load), monthly consumption trends, and top-performing circles.
* **Page 2: Geographic & Load Analysis** — Year-over-Year (Jan–Aug '25 vs Jan–Aug '26) area growth, load percentile comparisons, and circle-wise heatmaps.
* **Page 3: Business Opportunities & Priority Areas** — Multi-factor matrix combining growth, current demand, and capacity limits to identify priority candidate sites for EV station expansion.

---

## 📁 Repository Structure

```text
Telangana-EV-Analytics/
│
├── data/
│   ├── raw/                  # Scraped datasets from Open Data Portal
│   └── processed/            # Cleaned master CSV datasets
│
├── scraping/
│   └── playwright/           # Automated web scraping scripts
│
├── notebooks/
│   └── EDA.ipynb             # Jupyter Notebook for EDA & Statistical Tests
│
├── powerbi/
│   └── EV_Dashboard.pbix     # Power BI Dashboard file
│
├── outputs/
│   ├── tg_ev_monthly_master.csv
│   └── tg_ev_priority_areas.csv
│
└── README.md                 # Project Documentation
```

---

## 🌐 Data Source

* **Portal:** [Telangana Open Data Portal](https://data.telangana.gov.in/)
* **Dataset:** TG NPDCL & TG SPDCL EV Charging Stations Consumption Data

---

## 🚀 Future Roadmap

- [x] **Part 1:** Web Scraping → Data Cleaning → EDA → Statistical Analysis → Power BI Dashboard
- [ ] **Part 2:** Predictive Machine Learning models (Prophet / XGBoost) for EV electricity demand forecasting across DISCOM circles.

---

## 👤 Author

**Thatta Vijayendra**  
*Data Analytics | Python | Playwright | Pandas | Power BI*  

---
*Disclaimer: Priority areas derived in this study serve as analytical screening candidates. Engineering feasibility, transformer capacities, and traffic studies are required before physical site deployments.*
