from ObesityPredictor.constants import *
import os
from ObesityPredictor.utils.common import read_yaml, create_directories, save_json
from ObesityPredictor.entity.config_entity import (
    DataIngestionConfig, DataCleaningEncodingConfig, ModelTrainingConfig,
    ModelInferenceConfig, EvaluationConfig
)
from pathlib import Path

class ConfigurationManager:
    def __init__(
        self,
        config_filepath=CONFIG_FILE_PATH,
        params_filepath=PARAMS_FILE_PATH
    ):
        self.config = read_yaml(config_filepath)  # ✅ Read YAML as dictionary
        self.params = read_yaml(params_filepath)

        create_directories([self.config["artifacts_root"]])  # ✅ Ensure artifacts directory exists

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config["data_ingestion"]

        # Ensure the data ingestion directory exists
        create_directories([config["root_dir"]])

        data_ingestion_config = DataIngestionConfig(
            AWS_REGION=config["AWS_REGION"],
            BUCKET_NAME=config["BUCKET_NAME"],
            S3_OBJECT_KEY=config["S3_OBJECT_KEY"],
            root_dir=Path(config["root_dir"]),
            LOCAL_DOWNLOAD_FILE=Path(config["LOCAL_DOWNLOAD_FILE"])
        )

        return data_ingestion_config
    
    def get_data_cleaning_encoding_config(self) -> DataCleaningEncodingConfig:
        config = self.config["data_cleaning_encoding"]
        return DataCleaningEncodingConfig(
            input_file=Path(config["input_file"]),
            output_file=Path(config["output_file"])
        )
    
    def get_model_training_config(self) -> ModelTrainingConfig:
        config = self.config["model_training"]
        return ModelTrainingConfig(
            input_file=Path(config["input_file"]),
            models_dir=Path(config["models_dir"]),
            params=self.params
        )

    def get_model_inference_config(self) -> ModelInferenceConfig:
        config = self.config["model_inference"]
        return ModelInferenceConfig(
            models_dir=Path(config["models_dir"])
        )
    
    def get_evaluation_config(self) -> EvaluationConfig:
        config = self.config["model_evaluation"]  # ✅ Fixed reference
        model_config = self.config["model_training"]  # ✅ Correct model paths

        evaluation_config = EvaluationConfig(
            path_of_logistic_model=Path(model_config["logistic_regression_model"]),  # ✅ Fixed path
            path_of_decision_tree_model=Path(model_config["decision_tree_model"]),  # ✅ Fixed path
            test_data_path=Path(config["test_data"]),  # ✅ Corrected test data path
            mlflow_tracking_uri=config["mlflow_tracking_uri"],  # ✅ Fixed MLflow URI reference
            all_params=self.params
        )

        return evaluation_config
