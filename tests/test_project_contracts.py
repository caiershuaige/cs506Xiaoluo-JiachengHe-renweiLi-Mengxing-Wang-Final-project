import json
from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def test_required_project_files_exist():
    required_paths = [
        "README.md",
        "Makefile",
        "requirements.txt",
        ".github/workflows/tests.yml",
        "data/external/rentsmart_neighborhood_context.csv",
        "data/external/rentsmart_recent_case_summary.csv",
        "notebooks/01_data_collection.ipynb",
        "notebooks/02_data_cleaning.ipynb",
        "notebooks/03_eda_visualization.ipynb",
        "notebooks/04_feature_engineering.ipynb",
        "notebooks/05_modeling.ipynb",
    ]
    missing = [path for path in required_paths if not (PROJECT_ROOT / path).exists()]
    assert not missing, f"Missing required project files: {missing}"


def test_violation_level_feature_table_has_expected_target_and_metadata_excludes_leakage():
    feature_path = PROJECT_ROOT / "data" / "processed" / "violation_level_model_features.csv"
    metadata_path = PROJECT_ROOT / "data" / "processed" / "violation_level_feature_columns.json"
    assert feature_path.exists()
    assert metadata_path.exists()

    columns = pd.read_csv(feature_path, nrows=0).columns
    assert "is_unresolved" in columns
    assert "code_grouped" in columns
    assert "neighborhood" in columns

    metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    model_inputs = set(metadata["numeric_features"]) | set(metadata["categorical_features"])
    forbidden_model_inputs = {"status", "status_clean", "status_dttm", "status_year", "status_month", "case_no"}
    assert model_inputs.isdisjoint(forbidden_model_inputs)
    assert "rentsmart_median_building_age" in model_inputs
    assert "rentsmart_share_multifamily" in model_inputs


def test_classification_metrics_include_baselines_and_models():
    metrics_path = PROJECT_ROOT / "data" / "processed" / "classification_model_metrics.csv"
    assert metrics_path.exists()

    metrics = pd.read_csv(metrics_path)
    expected_models = {
        "Overall Rate Baseline",
        "Code-Only Baseline",
        "Logistic Regression",
        "Random Forest",
    }
    assert expected_models.issubset(set(metrics["model"]))

    required_columns = {
        "roc_auc",
        "average_precision",
        "top_10_pct_lift",
        "top_10_pct_unresolved_rate",
        "overall_unresolved_rate",
    }
    assert required_columns.issubset(metrics.columns)
    assert metrics["top_10_pct_lift"].notna().all()


def test_readme_matches_violation_level_project_framing():
    readme = (PROJECT_ROOT / "README.md").read_text(encoding="utf-8").lower()
    assert "violation-level" in readme
    assert "unresolved" in readme
    assert "code-only baseline" in readme
    assert "property-level" not in readme
