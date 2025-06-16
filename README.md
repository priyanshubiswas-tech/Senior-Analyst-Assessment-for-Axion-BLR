#  AxionRay Senior-Analyst Assessment - BLR

**Company:** [AxionRay](https://axionray.com)  
**Role Context:** Evaluating proficiency in data validation, cleaning, integration, and exploratory data analysis using Python.  
**Domains:** Automotive quality, failure diagnostics, and component analytics.

---

##  Assignment Overview

AxionRay, a leading AI-driven engineering safety company, focuses on leveraging Large Language Models and Generative AI to improve data quality and operational insights for next-gen products like electric vehicles and airplanes.

This assignment consists of **three main tasks**, which were successfully completed and documented:

- **Task 1:** Data Validation & Cleaning  
- **Task 2:** Data Integration & Preparation  
- **Task 3:** Exploratory Data Analysis (Trend & Root Cause Analysis)

---

##  Problem Statement

 [View Problem Statement (PDF)](https://github.com/priyanshubiswas-tech/Senior-Analyst-Assessment-for-Axion-BLR/blob/main/PO%20Assignment.pdf)

---

##  Task 1 – Data Validation & Tag Extraction

### Goals
- Column-wise dataset profiling
- Handling missing & malformed data
- Tag extraction from free-text fields
- Exploratory visualizations

### Key Actions
- Standardized column names
- Replaced nulls and dropped critical-missing rows
- Extracted tags from `correction_verbatim` via keyword-matching
- Identified system-level causes for missing `causal_part_nm`
- Highlighted top 10 most failing components

###  Outputs
-  Bar plots of component failures
-  Tag generation for free-text diagnostics
-  Missing data insights (plant, dealer-level trends)

###  Files & Deliverables
-  [Original Dataset](https://github.com/priyanshubiswas-tech/Senior-Analyst-Assessment-for-Axion-BLR/blob/main/Data%20for%20Task%201.xlsx)
-  [Cleaned Dataset with Tags](https://github.com/priyanshubiswas-tech/Senior-Analyst-Assessment-for-Axion-BLR/blob/main/Task%201/cleaned_task1_with_tags.xlsx)
-  [Jupyter Notebook](https://github.com/priyanshubiswas-tech/Senior-Analyst-Assessment-for-Axion-BLR/blob/main/Task%201/task1_analysis.ipynb)
-  [PDF Report](https://github.com/priyanshubiswas-tech/Senior-Analyst-Assessment-for-Axion-BLR/blob/main/Task%201/task1_analysis.pdf)
-  [Python Script](https://github.com/priyanshubiswas-tech/Senior-Analyst-Assessment-for-Axion-BLR/blob/main/Task%201/task1_analysis.py)

---

### Task 2 – Data Preparation & Integration

#### Objectives:
- Identify and justify a common primary key for dataset merging
- Perform thorough data cleaning: missing values, datatype corrections, standardizations
- Merge datasets with appropriate join strategy

#### Key Steps:
- Used `"Primary Key"` column for a **left join**
- Cleaned whitespace and standardized column names
- Filled missing values:
  - `Coverage → "Unknown"`
  - `Cause`, `Correction` → "Not Mentioned"
- Converted numeric columns to float where needed
- Removed duplicates and checked null distributions

---

### Task 3 – Exploratory Data Analysis (EDA)

#### 3.1 Trend Analysis
- Transformed `Order Date` to datetime
- Grouped by month to analyze volume trends
- Visualized trends using:
  -  Line Plot (monthly order count)
  -  Heatmap (variable correlation)

#### 3.2 Root Cause Identification
- Bar chart showing **top 8 components** contributing to revenue loss
- Boxplot comparing **actual hours spent** across failure components

#### Insights:
- Identified components with highest cost/time burden
- Discovered correlations that inform resource planning
- Visualization-driven exploration enables root cause prioritization

---

###  Deliverables (Tasks 2 & 3 Combined)

-  [Problem Statement](https://github.com/priyanshubiswas-tech/Senior-Analyst-Assessment-for-Axion-BLR/blob/main/PO%20Assignment.pdf)
-  [Original Dataset](https://github.com/priyanshubiswas-tech/Senior-Analyst-Assessment-for-Axion-BLR/blob/main/Data%20for%20Task%202.xlsx)
-  [Merged Output Dataset](https://github.com/priyanshubiswas-tech/Senior-Analyst-Assessment-for-Axion-BLR/blob/main/Task%202/merged_task2_output.xlsx)
-  [Jupyter Notebook](https://github.com/priyanshubiswas-tech/Senior-Analyst-Assessment-for-Axion-BLR/blob/main/Task%202/task%202%20%26%203_analysis.ipynb)
-  [PDF Report](https://github.com/priyanshubiswas-tech/Senior-Analyst-Assessment-for-Axion-BLR/blob/main/Task%202/task%202%20%26%203_analysis.pdf)
-  [Python Script](http://github.com/priyanshubiswas-tech/Senior-Analyst-Assessment-for-Axion-BLR/blob/main/Task%202/task%202%20%26%203_analysis.py)

---


##  Conclusion

The tasks demonstrate:

- Clear identification and resolution of data quality issues
- Integration of disparate datasets using relational keys
- Visualization-driven insights into component behavior and trends
- Strategic recommendations for data validation and cost optimization

These outputs can directly support AxionRay's mission to enhance quality engineering through AI and data-driven diagnostics.



