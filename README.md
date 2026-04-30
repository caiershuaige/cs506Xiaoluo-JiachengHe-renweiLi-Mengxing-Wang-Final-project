# Boston Housing Code Violations: Pattern Analysis and Case Prioritization

**Course:** CS506 Final Project  
**Group:** Mengxing Wang, Jiacheng He, Xiao Luo, Renwei Li  
**Presentation video:** TBD

## How to Build and Run

Supported environment: Python 3.10+ on macOS, Windows, or Linux.

Install dependencies and run the lightweight test suite:

```bash
make install
make test
```

Reproduce the final classification model and generated figures:

```bash
make model
```

To reproduce the full notebook pipeline, run:

```bash
make notebooks
```

The notebooks are ordered as a forward-only pipeline:

```text
notebooks/01_data_collection.ipynb
notebooks/02_data_cleaning.ipynb
notebooks/03_eda_visualization.ipynb
notebooks/04_feature_engineering.ipynb
notebooks/05_modeling.ipynb
```

Main generated outputs:

- `data/processed/violations_clean.csv` - cleaned violation records
- `data/processed/violation_level_model_features.csv` - final modeling table
- `data/processed/violation_level_feature_columns.json` - feature metadata
- `data/processed/classification_model_metrics.csv` - model and baseline metrics
- `data/processed/classification_model_predictions.csv` - test-set risk scores
- `data/processed/classification_prioritization_summary.csv` - top-decile prioritization result
- `data/external/rentsmart_recent_case_summary.csv` - compact summary of the RentSmart current-case extract
- `data/external/rentsmart_neighborhood_context.csv` - aggregated RentSmart neighborhood features used by the model
- `figures/01_top_violation_types.png` ... `figures/11_rentsmart_recent_cases_by_type.png`

## Project Goal

Boston publishes building and housing code violation records, but the raw data are difficult to use directly for planning because they contain many codes, neighborhoods, dates, and case statuses. Our project asks:

> Can Boston housing violation records be used to understand violation patterns and prioritize cases that are more likely to remain unresolved?

We frame the modeling task as **violation-level binary classification**:

```text
is_unresolved = 1 if status == Open
is_unresolved = 0 if status == Closed
```

The model should be interpreted as a **case prioritization score**, not as a perfect prediction system. A case with a higher predicted risk is not guaranteed to remain unresolved; it is simply more similar to historical cases that were unresolved in the dataset snapshot.

This framing is more appropriate than predicting the exact number of future violations. Earlier neighborhood-level prediction ideas had too few rows and unstable evaluation. The current case-level task uses 16,759 modeled violation records and supports a real train/test evaluation.

## Data Sources

| Dataset | Role | Source |
|---|---|---|
| `data/raw/violations.csv` | Main Boston Building and Property Violations dataset | Analyze Boston |
| `data/external/boston_neighborhood_boundaries.geojson` | Spatial neighborhood assignment | Analyze Boston |
| `data/external/boston_population_estimates_2025_neighborhood_level.csv` | Neighborhood population context | Analyze Boston |
| `data/external/neighborhood_structural_features.csv` | Neighborhood housing-stock context, including building age, housing type mix, property count, and value/size summaries | Derived from external RentSmart / parcel-level property context data |
| RentSmart current-case extract, summarized in `data/external/rentsmart_recent_case_summary.csv` and related tables | External check of recent RentSmart case patterns by type, neighborhood, and property type | RentSmart |
| `data/external/rentsmart_neighborhood_context.csv` | Aggregated RentSmart property/context features used by the model | Derived from RentSmart current-case extract |
| RentSmart `2000-to-2019.csv` historical export | Reviewed as a historical property/context source; raw owner fields and complaint-history JSON are not used directly in the model to avoid leakage | RentSmart |
| `data/external/code-violations-data-dictionary.xlsx` | Official code reference | Boston ISD |

The repository includes the cleaned and processed tables needed to reproduce the final model. Large raw RentSmart/property files are not committed directly; instead, the project uses small summary tables so the analysis remains reproducible and GitHub-friendly. The local RentSmart current-case extract used for the summary contains 397,592 records from 2021-05-25 to 2026-04-28; if the original portal source is described as 2016-present, this local CSV appears to be a filtered export and is treated as a supporting external check rather than the model target.

## Data Collection

Notebook 01 verifies source files, previews the raw violation schema, parses the violation date field, summarizes available code and date coverage, and writes project-level metadata to `data/processed/dataset_summary.json`.

The raw violation data include 17,172 records, 520 unique violation codes, and dates ranging from 2009-12-01 to 2026-03-20.

RentSmart is used as an external context source. We summarize the current-case extract by case type, neighborhood, and property type, and we aggregate stable property fields to the neighborhood level. This adds RentSmart-derived features to the model without changing the main unresolved-status label.

## Data Cleaning

Notebook 02 creates `data/processed/violations_clean.csv`. The cleaning process:

- parses `status_dttm` as a datetime field;
- extracts year, month, and day-of-week fields for visualization;
- standardizes status labels;
- removes duplicate case records where appropriate;
- cleans ZIP code, ward, street suffix, latitude, and longitude fields;
- assigns neighborhoods using city labels, spatial boundaries, and ZIP fallback logic;
- creates flags such as `has_coords` and `has_neighborhood`.

Rows from partial 2026 data are excluded from the modeling table so the final target is less affected by incomplete current-year reporting.

## Feature Extraction

Notebook 04 builds the final violation-level modeling table. The target is `is_unresolved`.

Model features include:

| Feature group | Examples | Reason |
|---|---|---|
| Violation type | `code_grouped`, `description_group` | Captures the category of the cited issue |
| Location | `neighborhood`, `zip5`, `ward_clean`, `latitude`, `longitude` | Captures spatial differences across Boston |
| Data quality/context flags | `has_coords`, `has_neighborhood`, `neighborhood_assignment_method` | Keeps missingness explicit instead of silently dropping it |
| Neighborhood context | `population_2025`, `property_count`, `median_building_age`, `share_pre_1940`, `share_multifamily`, `properties_per_1000_residents` | Adds broader neighborhood housing-stock context |
| RentSmart context | `rentsmart_case_count`, `rentsmart_median_building_age`, `rentsmart_share_pre_1940`, `rentsmart_share_remodeled`, `rentsmart_share_condo`, `rentsmart_share_multifamily` | Adds aggregated property context from RentSmart without using owner names or complaint-history JSON |

To avoid leakage, the model does **not** use `status`, `status_clean`, `status_dttm`, `status_year`, `status_month`, or `case_no` as input features.

RentSmart-style raw fields such as owner names and historical complaint JSON are also not used directly. Owner names can overfit to specific landlords, and historical complaint JSON can leak future or target-related information unless a strict time split is constructed. Instead, we use aggregated neighborhood-level housing-stock features.

## Visualization

The EDA notebooks generate final-quality figures in `figures/`:

- top violation types;
- violations by neighborhood;
- yearly violation counts;
- monthly seasonality;
- neighborhood-by-year heatmap;
- spatial distribution of violations;
- model comparison;
- confusion matrix;
- top-10% prioritization lift;
- feature importance;
- RentSmart recent cases by type.

The visualizations support the main claim that housing violations are not evenly distributed by type, neighborhood, or location. This motivates testing whether a supervised model can combine these signals into a useful prioritization score.

## Modeling

Notebook 05 is the final modeling notebook. It trains and evaluates four approaches:

1. **Overall Rate Baseline** - assigns every case the training-set unresolved rate.
2. **Code-Only Baseline** - ranks cases by historical unresolved rate for their violation code group.
3. **Logistic Regression** - interpretable supervised baseline with class balancing.
4. **Random Forest** - main nonlinear model that can capture interactions between violation type, location, and neighborhood context.

We include the code-only baseline because a reasonable criticism is that inspectors could simply look at the violation code. The comparison tests whether the full model adds value beyond that simple rule.

Evaluation uses a stratified train/test split. Because unresolved cases are rare, accuracy is not the main metric. We focus on ROC-AUC, average precision, recall, F1, and especially **top-10% lift**: how much higher the unresolved rate is among the highest-risk 10% of cases compared with the overall test set.

## Results

Most recent run:

| Model | ROC-AUC | Average Precision | Recall | F1 | Top-10% unresolved rate | Top-10% lift |
|---|---:|---:|---:|---:|---:|---:|
| Logistic Regression | 0.790 | 0.134 | 0.722 | 0.199 | 15.27% | 3.23x |
| Random Forest | 0.761 | 0.134 | 0.525 | 0.203 | 14.56% | 3.08x |
| Code-Only Baseline | 0.740 | 0.098 | 0.000 | 0.000 | 11.69% | 2.47x |
| Overall Rate Baseline | 0.500 | 0.047 | 0.000 | 0.000 | 3.58% | 0.76x |

The overall unresolved rate in the held-out test set is 4.73%. Logistic Regression's highest-risk 10% of cases have an unresolved rate of 15.27%, which is about 3.23 times the overall rate.

This does not mean the model perfectly predicts unresolved cases. It means the model provides a useful ranking signal. The code-only baseline is already strong, which confirms that violation type contains important information. However, the full supervised models improve top-decile lift beyond the code-only baseline, suggesting that location and aggregated RentSmart neighborhood context add useful information. The improvement is modest, so we interpret RentSmart mainly as a contextual and interpretability enhancement rather than a dramatic accuracy boost.

## Limitations

- The target is based on observed open/closed status in the dataset snapshot, so this is not a causal claim and not a guarantee of future unresolved status.
- Open cases are rare, so individual-level precision is limited. The model is more useful for ranking and prioritization than for making hard yes/no decisions.
- Violation code carries a large share of the signal. This is why we compare against a code-only baseline instead of pretending the supervised model is the only useful method.
- Some neighborhood and structural features are aggregate context features, not parcel-level measurements for each violation address.
- The RentSmart current-case summary is used as a supporting external check, not as the unresolved-status training target.
- Raw RentSmart owner fields and historical complaint JSON were excluded from the model to reduce overfitting and leakage risk.
- The data reflect reported and cited violations, not all true housing problems. Areas with different inspection/reporting intensity may appear different for reasons outside actual housing quality.

## Repository Organization

```text
.github/workflows/   GitHub Actions test workflow
data/raw/            Raw violation data
data/external/       Supporting external datasets
data/processed/      Cleaned data, feature tables, predictions, and metrics
figures/             Final figures for the report and presentation
notebooks/           Reproducible data science pipeline
tests/               Lightweight reproducibility and contract tests
```

## Testing

Run:

```bash
make test
```

The tests check that:

- required project files exist;
- the violation-level modeling table has the expected target;
- final metrics include the overall baseline, code-only baseline, logistic regression, and random forest;
- the README matches the final violation-level unresolved-prioritization framing.

GitHub Actions runs the same test suite on every push and pull request.

## Contributing

1. Keep notebooks runnable from top to bottom.
2. Keep Notebook 05 as the canonical final modeling notebook.
3. Do not use target-derived fields such as `status`, `status_clean`, or `status_dttm` as model inputs.
4. Update tests when changing the modeling target, feature table, or output file names.
5. Keep figures and metrics reproducible from committed code and documented data files.
