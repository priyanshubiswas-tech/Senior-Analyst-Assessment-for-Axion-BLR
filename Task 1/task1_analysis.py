#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install pandas openpyxl matplotlib seaborn numpy


# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

print("Libraries loaded successfully.")


# In[3]:


df = pd.read_excel(r"C:\Users\91952\Documents\ACADEMICS\Programming 1x\Projects\Axion Assessment\Data for Task 1.xlsx")


# ### Basic overview of the data 

# In[4]:


df.head()


# ### Shape, Column Names and Types

# In[5]:


print("Shape of the dataset:", df.shape)
print("\nColumn names:")
print(df.columns.tolist())

df.info()


# In[6]:


df.describe()


# ### Check Missing Values and Unique Entries

# In[7]:


for col in df.columns:
    print(f"--- {col} ---")
    print(f"Missing: {df[col].isnull().sum()}")
    print(f"Unique: {df[col].nunique()}")
    print()


# ### View all column names with nulls only

# In[8]:


null_cols = df.columns[df.isnull().any()]
df[null_cols].isnull().sum()


# ### Drop rows where Transaction ID values (key identifier) is missing

# In[9]:


df = df.dropna(subset=['TRANSACTION_ID'])


# ### Convert All Columns to Lowercase

# In[14]:


df.columns = df.columns.str.strip().str.lower()


# ### Fill Nulls Only for Columns That Exist

# In[16]:


df.columns.tolist()


# In[15]:


minor_null_cols = [
    'causal_part_nm', 'plant', 'state', 'repair_dlr_postal_cd',
    'veh_test_grp', 'optn_famly_certification',
    'optf_famly_emissiof_system', 'engine_source_plant',
    'engine_trace_nbr', 'transmission_source_plant',
    'transmission_trace_nbr', 'line_series', 'last_known_delvry_type_cd'
]

# Fill "unknown" only if column exists
for col in minor_null_cols:
    if col in df.columns:
        df[col] = df[col].fillna("unknown")
    else:
        print(f" Column not found: {col}")


# In[19]:


df.rename(columns={'causal_part_nm': 'component'}, inplace=True)


# ### Identify Critical Columns & Create Visualizations

# | Column                          | Reason                                         |
# | ------------------------------- | ---------------------------------------------- |
# | `component`                     | Which part/component is failing                |
# | `repair_date`                   | Timeline of repairs                            |
# | `totalcost` or `reporting_cost` | Cost of failure (financial impact)             |
# | `actual_hrs` or `repair_age`    | Time impact of the failure                     |
# | `correction_verbatim`           | Root cause or fix summary (for tag extraction) |
# 

# In[17]:


import seaborn as sns
import matplotlib.pyplot as plt


# ### Top 10 failing components

# In[21]:


plt.figure(figsize=(10, 5))
sns.countplot(
    data=df[df['component'] != 'unknown'], 
    y='component', 
    order=df[df['component'] != 'unknown']['component'].value_counts().head(10).index
)
plt.title("Top 10 Failing Components (Excluding 'unknown')")
plt.xlabel("Count")
plt.ylabel("Component")
plt.tight_layout()
plt.show()


# Records labeled as 'unknown' represent missing or unrecorded component data and were excluded from core visual analysis to maintain the accuracy and actionability of insights.

# ### Investigate 'unknown' Root Causes

# In[22]:


df[df['component'] == 'unknown'][['vin', 'repair_date', 'correction_verbatim']].head(10)


# Group by Key Identifiers ('plant', 'dealer_name')

# In[24]:


df[df['component'] == 'unknown'].groupby('plant').size().sort_values(ascending=False)


# In[26]:


df[df['component'] == 'unknown'].groupby('dealer_name').size().sort_values(ascending=False)


# ###  Missing Component Analysis:
# 
# A small portion of records 6% had missing values in the `component` field, labeled as `'unknown'`. Further investigation revealed the following:
# 
# ####  Key Findings:
# - All missing entries originated from just **three plants**: `FLT`, `FTW`, and `SIL` (2 records each).
# - Only **five dealers** were associated with these cases — each contributing just **1 record**.
# - The free-text field `correction_verbatim` still provided clues about the actual component involved (e.g., "steering wheel", "horn").
# 
# ####  Possible Reasons:
# - System-level data mapping failure at the plant level.
# - Repair submission forms allowing component fields to be skipped.
# - Lack of validation in structured data capture.
# 
# ####  Suggestions:
# - Add mandatory field validation for `component` during data entry.
# - Implement simple keyword-based auto-tagging from `correction_verbatim`.
# - Review repair workflows or systems at plants `FLT`, `FTW`, and `SIL` to close the data gap.
# 
# These steps will help reduce data quality issues and improve insight reliability for future analyses.
