# Final Project Proposal

## Project Overview

**Group Members:**  
- Mengxing Wang
- Jiacheng He
- Xiao Luo
- Renwei Li

**Project Title:** **City of Boston: Building & Housing Violations Analysis [BU SPARKS]**

**Brief Description:**  
The City of Boston is interested in housing violations, possible causes, and structural remedies. Using data on housing violations, the City of Boston is interested in a comprehensive report about systemic issues in the state of housing around the city.

---

## 1. Project Description & Timeline

### Project Description
This project works with available housing and building violation data from the City of Boston in public. These records are created when residential buildings do not meet required housing or safety standards, such as problems with heating, building conditions, sanitation, and fire safety.

The project aims to look at housing violations from a data perspective in order to understand what kinds of problems appear most often and how they vary across different neighborhoods over time. In addition to descriptive analysis, the project will also consider potential reporting and inspection bias in the data and aim to provide more meaningful comparisons across regions.

The analysis mainly focuses on describing violation types, where violations are more common, and how violation activity changes across different time periods. To improve the robustness of the analysis, normalized measures (such as violation rates) will be used when possible to better reflect underlying patterns.

The goal of this project is to provide an organized summary of housing violation patterns, supported by data analysis and visualization, while offering additional insights into spatial differences and potential systemic issues in housing conditions.

---

### Project Timeline

### Background Research and Problem Definition (Week 1)
- Review Boston housing codes and violation categories  
- Study dataset documentation and metadata  
- Identify key variables (e.g., violation type, date, location)  
- Define refined research questions (spatial patterns, temporal trends, bias considerations)  
- Identify additional datasets (e.g., population, neighborhood boundaries)  

**Deliverables:**
- Problem definition document  
- Research questions list  
- Data inventory summary  


---

### Data Collection and Initial Exploration (Week 2)
- Download datasets from Boston Open Data Portal and Harvard Dataverse  
- Inspect dataset structure (columns, data types, size)  
- Perform initial data profiling (summary statistics, distributions)  
- Generate quick visualizations (histograms, counts)  
- Identify data quality issues (missing values, duplicates, inconsistencies)  

**Deliverables:**
- Organized raw datasets  
- Initial EDA notebook  
- Data quality report  


---

### Data Cleaning and Preprocessing (Week 3–4)
- Handle missing values (removal or imputation)  
- Remove duplicates and invalid records  
- Standardize date/time formats  
- Clean and normalize address/location fields  
- Map addresses to neighborhoods or regions  
- Merge datasets if needed  
- Validate cleaned dataset consistency  

**Deliverables:**
- Cleaned dataset  
- Data cleaning scripts (reproducible)  
- Documentation of preprocessing steps  


---

### Exploratory Analysis and Visualization (Week 5–6)
- Analyze frequency distribution of violation types  
- Identify top violation categories  
- Examine temporal trends (monthly/yearly patterns)  
- Compare violations across neighborhoods  
- Create visualizations (bar charts, time-series plots)  
- Perform spatial analysis (maps, heatmaps, choropleth)  

**Deliverables:**
- EDA notebook with visualizations  
- Core plots (types, trends, spatial distribution)  
- Initial geographic maps  


---

### Normalization, Bias Analysis, and Modeling (Week 7)
- Compute normalized metrics (violations per population / per area)  
- Compare raw counts vs normalized results  
- Analyze potential reporting or inspection bias  
- Discuss assumptions and data limitations  
- Perform basic modeling (regression or clustering)  
- Interpret model outputs  

**Deliverables:**
- Normalized dataset  
- Modeling notebook  
- Bias analysis summary  


---

### Evaluation, Interpretation, and Insights (Week 8)
- Synthesize results across all analyses  
- Identify high-risk neighborhoods (based on normalized metrics)  
- Compare spatial and temporal patterns  
- Extract key insights  
- Discuss limitations and implications  

**Deliverables:**
- Insight summary document  
- Key findings list  
- Draft report sections  


---

### Final Report and Presentation (Week 9)
- Organize full report structure (introduction, methods, results, discussion)  
- Refine visualizations for clarity and consistency  
- Complete final report writing  
- Prepare presentation slides  
- Final review and revisions  

**Deliverables:**
- Final report  
- Presentation slides

---

## 2. Project Goals

### Primary Goals

- Identify the most frequent types of housing violations in Boston and how they vary by neighborhood, using normalized measures when applicable.

- Analyze spatial patterns of housing violations to determine whether certain areas experience disproportionately high violation rates.

- Examine temporal trends to understand how housing violations change over time, while considering potential reporting or inspection bias.

### Measurable Outcomes

- Frequency distributions of violation types.
- Visualizations such as bar charts, geographic maps, and time-series plots.
- Quantitative comparisons of violation density across neighborhoods.

---

## 3. Data Collection Plan

### Data Sources

- **Boston.gov（City of Boston Open Data Portal – Housing / Building Violations Dataset)** [https://data.boston.gov/](https://data.boston.gov/dataset/building-and-property-violations1) Provides detailed records of reported housing and building violations, including violation type, location, neighborhood, and date.

- **Harvard Dataverse – Code, Building and Property Violations in Boston, MA** [Harvard](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/TD9YOY) A published dataset hosted on the Harvard Dataverse repository containing building and property violations in Boston, available with a DOI. This dataset is based on official city records and may be used along with data from the City of Boston Open Data Portal for analysis.

- **BU Library**

### Data Collection Method

- Download publicly available datasets from the provided sources.
- Use provided APIs.
- Clean and process data using Python libraries such as `pandas`, `NumPy`.

**Technical Stack:**  
Python, pandas, NumPy, matplotlib, seaborn, scikit-learn, Jupyter Notebook

---

## Challenges

- The project uses only publicly available, non-personal data.
- Potential problems such as missing values, inconsistent address formats might appear.
- Analysis will focus on systemic patterns rather than individual properties.

---

## Summary

This project plans to use housing and building violation data from the City of Boston to explore common housing issues in the city. The analysis mainly looks at how different types of violations appear across neighborhoods and how these patterns change over time.

The project goals focus on exploratory analysis and visualization, with clear and measurable outcomes based on the data. A two-month timeline is planned so that each step of the project, including data collection, analysis, and reporting, can be completed in an organized way.

Overall, the project uses publicly available data and standard Python tools to summarize housing violation patterns in Boston. The scope is kept flexible to allow adjustments during the project if needed.
