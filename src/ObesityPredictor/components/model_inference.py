import pickle
import pandas as pd
import json
from pathlib import Path
from ObesityPredictor.config.configuration import ConfigurationManager
from ObesityPredictor.entity.config_entity import ModelInferenceConfig
from ObesityPredictor import logger

# Mapping numeric predictions to human-readable class names
OBESITY_CLASS_MAPPING = {
    0: "Underweight",
    1: "Normal Weight",
    2: "Overweight",
    3: "Obesity Type I",
    4: "Obesity Type II"
}

class ModelInference:
    def __init__(self, config: ModelInferenceConfig):
        self.config = config
        self.models_dir = self.config.models_dir
        self.feature_names_path = Path("artifacts/models/feature_names.json")

    def load_feature_names(self):
        """Load feature names used during training."""
        try:
            with open(self.feature_names_path, "r") as f:
                feature_names = json.load(f)
            return feature_names
        except Exception as e:
            logger.error(f"Error loading feature names: {str(e)}")
            raise e

    def align_features(self, input_data: pd.DataFrame):
        """Ensure inference data matches training feature set."""
        try:
            feature_names = self.load_feature_names()
            aligned_data = pd.DataFrame(columns=feature_names)

            for col in input_data.columns:
                if col in feature_names:
                    aligned_data[col] = input_data[col]

            aligned_data = aligned_data.fillna(0).infer_objects(copy=False)  # ✅ Fixed inplace issue
            return aligned_data
        except Exception as e:
            logger.error(f"Error aligning features: {str(e)}")
            raise e

    def load_model(self, model_name):
        """Load a trained model from the models directory."""
        try:
            model_path = self.models_dir / model_name / "model.pkl"
            with open(model_path, "rb") as f:
                model = pickle.load(f)
            logger.info(f"Loaded model from {model_path}")
            return model
        except Exception as e:
            logger.error(f"Error loading model {model_name}: {str(e)}")
            raise e

    def predict(self, model_name, input_data: pd.DataFrame):
        """Perform inference using the specified trained model."""
        try:
            model = self.load_model(model_name)
            aligned_data = self.align_features(input_data)
            predictions = model.predict(aligned_data)
            return [OBESITY_CLASS_MAPPING[pred] for pred in predictions]  # ✅ Convert numeric prediction to class names
        except Exception as e:
            logger.error(f"Error during prediction with model {model_name}: {str(e)}")
            raise e

    def run(self, input_data: pd.DataFrame):
        """Run inference for both models and return predictions."""
        try:
            logger.info("Running inference for Logistic Regression")
            log_reg_predictions = self.predict("logistic_regression", input_data)

            logger.info("Running inference for Decision Tree")
            decision_tree_predictions = self.predict("decision_tree", input_data)

            return {
                "logistic_regression": log_reg_predictions,
                "decision_tree": decision_tree_predictions
            }
        except Exception as e:
            logger.error(f"Error during model inference: {str(e)}")
            raise e
