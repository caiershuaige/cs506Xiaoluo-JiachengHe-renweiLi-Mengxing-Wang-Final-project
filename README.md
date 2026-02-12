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
This project works with available housing and building violation data from the City of Boston in public. These records are created when residential buildings do not meet required housing or safety standards, such as problems with heating, building conditions, sanitation, and fire safety, etc. The project aims to look at housing violations from a data perspective in order to understand what kinds of problems appear most often and how they vary across different neighborhoods through time. The analysis mainly focuses on describing violation types, where violations are more common, and how violation activity changes across different time periods. The goal of this project is to provide a organized summary of housing violation patterns based on data analysis and visualization.

### Project Timeline

| Task / Milestone | Estimated Duration |
|------------------|--------------------|
| Background research and understanding housing codes | 1 week |
| Data collection and initial exploration | 1 week |
| Data cleaning and preprocessing | 2 weeks |
| Exploratory analysis and modeling | 2 weeks |
| Evaluation, visualization, and interpretation | 1 week |
| Final report writing, presentation, and review | 1 week |

---

## 2. Project Goals

### Primary Goals

- Identify the most frequent types of housing violations in Boston and how they vary by neighborhood.
- Analyze spatial patterns of housing violations to determine whether certain areas experience disproportionately high violation rates.
- Examine temporal trends to understand how housing violations change over time.

### Measurable Outcomes

- Frequency distributions of violation types.
- Visualizations such as bar charts, geographic maps, and time-series plots.
- Quantitative comparisons of violation density across neighborhoods.

---

## 3. Data Collection Plan

### Data Sources

- **Boston.gov（City of Boston Open Data Portal – Housing / Building Violations Dataset)** [https://data.boston.gov/](https://data.boston.gov/dataset/building-and-property-violations1) Provides detailed records of reported housing and building violations, including violation type, location, neighborhood, and date.

- **Harvard Dataverse – Code, Building and Property Violations in Boston, MA** [Harvard](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/TD9YOY) A published dataset hosted on the Harvard Dataverse repository containing building and property violations in Boston, available with a DOI. This dataset is based on official city records and may be used along with data from the City of Boston Open Data Portal for analysis.

- **BU Library** 伟大无需多言

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
