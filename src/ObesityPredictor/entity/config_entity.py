from dataclasses import dataclass
from pathlib import Path
from typing import Dict

@dataclass(frozen=True)
class DataIngestionConfig:
    AWS_REGION: str
    BUCKET_NAME: str
    S3_OBJECT_KEY: str
    root_dir: Path
    LOCAL_DOWNLOAD_FILE: Path  # ✅ Added file path

@dataclass(frozen=True)
class DataCleaningEncodingConfig:
    input_file: Path
    output_file: Path

@dataclass(frozen=True)
class ModelTrainingConfig:
    input_file: Path  # Path to the cleaned dataset
    models_dir: Path  # Directory where trained models will be saved
    params: Dict  # Parameters for train-test split and models

@dataclass(frozen=True)
class ModelInferenceConfig:
    models_dir: Path  # Directory where trained models are saved

@dataclass(frozen=True)
class EvaluationConfig:
    path_of_logistic_model: Path
    path_of_decision_tree_model: Path
    test_data_path: Path
    mlflow_tracking_uri: str
    all_params: dict


