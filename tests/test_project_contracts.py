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
        "notebooks/01_data_collection.ipynb",
        "notebooks/02_data_cleaning.ipynb",
        "notebooks/03_eda_visualization.ipynb",
        "notebooks/04_feature_engineering.ipynb",
        "notebooks/05_modeling.ipynb",
        "data/processed/property_model_features.csv",
        "data/processed/property_feature_columns.json",
        "data/processed/classification_model_metrics.csv",
    ]
    missing = [path for path in required_paths if not (PROJECT_ROOT / path).exists()]
    assert not missing, f"Missing required project files: {missing}"


def test_feature_metadata_uses_property_target_and_excludes_leakage():
    metadata_path = PROJECT_ROOT / "data" / "processed" / "property_feature_columns.json"
    metadata = json.loads(metadata_path.read_text(encoding="utf-8"))

    assert metadata["target"] == "had_violation"

    model_inputs = set(metadata["numeric_features"]) | set(metadata["categorical_features"])
    leakage_fields = {
        "violation_count",
        "recent_violation_count",
        "had_recent_violation",
        "last_violation_date",
        "first_violation_date",
    }

    assert model_inputs.isdisjoint(leakage_fields)
    assert leakage_fields.issubset(set(metadata["excluded_from_features_for_leakage"]))


def test_metrics_include_expected_models_and_prioritization_columns():
    metrics_path = PROJECT_ROOT / "data" / "processed" / "classification_model_metrics.csv"
    metrics = pd.read_csv(metrics_path)

    expected_models = {
        "Overall Rate Baseline",
        "Age-Based Baseline",
        "Logistic Regression",
        "Random Forest",
        "Histogram Gradient Boosting",
    }
    assert expected_models.issubset(set(metrics["model"]))

    required_columns = {
        "roc_auc",
        "average_precision",
        "top_10_pct_violation_rate",
        "top_10_pct_lift",
        "captured_violation_share",
    }
    assert required_columns.issubset(metrics.columns)
