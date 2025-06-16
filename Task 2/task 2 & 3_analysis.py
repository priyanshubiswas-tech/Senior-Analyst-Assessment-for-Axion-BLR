#!/usr/bin/env python
# coding: utf-8

# # TASK 2: Data Preparation and Integration

# In[1]:


import pandas as pd


# In[6]:


file_path = r"C:\Users\91952\Documents\ACADEMICS\Programming 1x\Projects\Axion Assessment\Data for Task 2.xlsx"


df1 = pd.read_excel(file_path, sheet_name=0)
df2 = pd.read_excel(file_path, sheet_name=1)


# In[9]:


df1.info()


# In[10]:


df2.info()


# In[11]:


df1.head(2)


# In[13]:


df2.head(3)


# Both df1 and df2 have the column `"Primary Key"`. We'll use `"Primary Key"` as the join key.

# ### Check for Nulls:

# - df1:

# In[14]:


print("Nulls in df1:")
print(df1.isnull().sum(), "\n")


# - df2:

# In[15]:


print("Nulls in df2:")
print(df2.isnull().sum(), "\n")


# ### Drop duplicates if any

# In[16]:


df1.drop_duplicates(subset="Primary Key", inplace=True)
df2.drop_duplicates(subset="Primary Key", inplace=True)


# ### Standardize column names (strip whitespace)

# In[17]:


df1.columns = df1.columns.str.strip()
df2.columns = df2.columns.str.strip()


# In[18]:


print("\nData types:")
print(df1.dtypes, "\n")
print(df2.dtypes)


# ### Convert cost and segment total to float

# In[19]:


df2['Cost'] = pd.to_numeric(df2['Cost'], errors='coerce')
df2['Segment Total $'] = pd.to_numeric(df2['Segment Total $'], errors='coerce')


# ### Replace null 'Coverage' with 'Unknown'

# In[21]:


df2['Coverage'] = df2['Coverage'].fillna('Unknown')


# In[28]:


df2[['Coverage']].isnull().sum()


# ### Fill 'Cause' and 'Correction' in df1 with 'Not Mentioned'

# In[24]:


df1['Cause'] = df1['Cause'].fillna('Not Mentioned')
df1['Correction'] = df1['Correction'].fillna('Not Mentioned')


# In[25]:


df1[['Cause', 'Correction']].isnull().sum()


# ### Merge on Primary Key using LEFT JOIN to preserve all rows from df1

# In[29]:


merged_df = pd.merge(df1, df2, on="Primary Key", how="left")


# In[30]:


merged_df.head(3)


# In[31]:


merged_df.isnull().sum()


# # TASK 3.1 – Trend Analysis (Visual + Insights)

# In[32]:


import matplotlib.pyplot as plt
import seaborn as sns


# ### Make sure Order Date is datetime

# In[34]:


merged_df['Order Date'] = pd.to_datetime(merged_df['Order Date'])


# ### Count by Month

# In[35]:


trend = merged_df.groupby(merged_df['Order Date'].dt.to_period('M')).size()


# ### Plot

# In[36]:


trend.plot(kind='line', marker='o', title="Failures Over Time", figsize=(10,5))
plt.xlabel("Month")
plt.ylabel("Number of Failures")
plt.grid()
plt.show()


# ### Heatmap for numeric columns

# In[ ]:


plt.figure(figsize=(10,6))
sns.heatmap(merged_df.corr(numeric_only=True), annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()


# ### **Breakdown**:
# 
# - ***Correlation Coefficient:*** The numbers within each cell (e.g., 1.00, -0.05, 0.13) are the Pearson correlation coefficients, ranging from -1 to +1.
#     - +1.00: Perfect positive correlation (as one variable increases, the other increases proportionally).
#     - -1.00: Perfect negative correlation (as one variable increases, the other decreases proportionally).
#     - 0.00: No linear correlation.
#     - Values closer to +1 or -1: Stronger correlation.
#     - Values closer to 0: Weaker correlation.
# - ***Color Scale (Coolwarm):*** The color bar on the right indicates the range of correlation values.
#     - Red (warm colors): Indicate positive correlations. Darker red means stronger positive correlation.
#     - Blue (cool colors): Indicate negative correlations. Darker blue means stronger negative correlation.
#     - White/Light colors: Indicate correlations close to zero (weak or no linear correlation).

# # TASK 3.2 – Root Cause Identification

# In[47]:


merged_df['Failure Condition - Failure Component'].unique()


# In[48]:


merged_df['Failure Condition - Failure Component'] = merged_df['Failure Condition - Failure Component'].str.strip()


# In[49]:


# Strip and simplify failure labels to the first condition
merged_df['Primary Failure Component'] = merged_df['Failure Condition - Failure Component'].str.split(',').str[0].str.strip()


# In[50]:


top_primary_failures = merged_df['Primary Failure Component'].value_counts().nlargest(8).index
filtered_df = merged_df[merged_df['Primary Failure Component'].isin(top_primary_failures)]


# In[52]:


merged_df['Primary Failure Component'].value_counts(dropna=False).head(10)


# In[53]:


merged_df[['Primary Failure Component', 'Cost']].dropna().shape


# ### Plot: Avg Revenue by Failure Component (Top 8)

# In[57]:


plt.figure(figsize=(12,6))
sns.barplot(data=filtered_df, 
            x='Primary Failure Component', 
            y='Revenue', 
            estimator='mean',
            errorbar=None)
plt.title("Avg Revenue by Top 8 Failure Components")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()


# ### Plot: Actual Hours by Failure Component (Boxplot)

# In[58]:


plt.figure(figsize=(12,6))
sns.boxplot(data=filtered_df, 
            x='Primary Failure Component', 
            y='Actual Hours')
plt.title("Actual Hours by Top 8 Failure Components")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()


# In[61]:


merged_df.to_excel("merged_task2_output.xlsx", index=False)


# ##  Executive Summary: Task 2 & Task 3
# 
# ---
# 
# ###  Task 2: Data Preparation and Integration
# 
# This task focused on cleaning, formatting, and joining two datasets for further analysis.
# 
# #### Steps Performed:
# 
# - **Loading Data**: Two Excel sheets were loaded into `df1` and `df2`.
# - **Join Strategy**: Both datasets contained a common column `"Primary Key"`, which was used to perform a **left join**, keeping all records from `df1`.
# - **Data Cleaning**:
#   - Checked for and noted any `null` values.
#   - Dropped duplicate records if present.
#   - Stripped whitespace from column names to standardize naming.
#   - Converted columns like `Cost` and `Segment Total` to float data types.
#   - Filled missing values:
#     - `Coverage` → replaced with `"Unknown"`.
#     - `Cause`, `Correction` in `df1` → filled with `"Not Mentioned"`.
# 
# ---
# 
# ###  Task 3.1 – Trend Analysis
# 
# This analysis involved identifying temporal patterns and data relationships through visual exploration.
# 
# #### Steps Performed:
# 
# - **Date Handling**: Ensured `Order Date` was converted to proper datetime format.
# - **Monthly Trends**: Grouped data by month and counted records to assess trends.
# - **Visualizations**:
#   - Line plot to show monthly record count.
#   - Heatmap showing **correlation between numeric variables**, with interpretation of:
#     - Pearson Correlation Coefficient scale (from -1 to 1).
#     - Use of Coolwarm color map to distinguish strength and direction of relationships.
# 
# ---
# 
# ###  Task 3.2 – Root Cause Identification
# 
# This sub-task explored how component failures contribute to revenue and resource consumption.
# 
# #### Steps Performed:
# 
# - **Average Revenue by Failure Component**:
#   - Bar chart showing the top 8 failure components contributing the most revenue loss.
# - **Actual Hours by Failure Component**:
#   - Boxplot showing variation in actual hours spent across different failure components.
# 
# ---
# 
# ###  Summary of Key Actions
# 
# - Standardized and merged two datasets via primary key.
# - Cleaned and preprocessed text, numeric, and date fields.
# - Used visual tools (line plot, heatmap, bar chart, boxplot) to explore:
#   - Monthly trends
#   - Variable relationships
#   - Revenue and time distribution by failure component
# 
# 
