import pickle
import pandas as pd
import os
import mlflow
import mlflow.sklearn
from ObesityPredictor.entity.config_entity import EvaluationConfig
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report

os.environ["MLFLOW_TRACKING_USERNAME"] = "VISHWAS304"
os.environ["MLFLOW_TRACKING_PASSWORD"] = "527246b2b46da61f4267ee833142b979e967cfdb"

# Mapping numeric predictions to human-readable class names
OBESITY_CLASS_MAPPING = {
    0: "Underweight",
    1: "Normal Weight",
    2: "Overweight",
    3: "Obesity Type I",
    4: "Obesity Type II"
}

class ModelEvaluation:
    def __init__(self, config: EvaluationConfig):
        self.config = config

    def load_model(self, model_path):
        """Load a model from the given path."""
        try:
            with open(model_path, "rb") as file:
                model = pickle.load(file)
            return model
        except Exception as e:
            raise FileNotFoundError(f"Model file not found: {model_path}. Error: {str(e)}")

    def evaluate(self):
        """Evaluate models on test data and log all metrics to MLflow."""
        try:
            # Load models
            logistic_model = self.load_model(self.config.path_of_logistic_model)
            decision_tree_model = self.load_model(self.config.path_of_decision_tree_model)

            # Load test data
            test_data = pd.read_csv(self.config.test_data_path)

            # Ensure `Obesity` column exists before dropping
            if "Obesity" not in test_data.columns:
                raise KeyError(f"'Obesity' column is missing in the test dataset {self.config.test_data_path}")

            # Prepare data for evaluation
            X_test = test_data.drop(columns=["Obesity"])  
            y_test = test_data["Obesity"]

            # Predictions
            log_pred = logistic_model.predict(X_test)
            dt_pred = decision_tree_model.predict(X_test)

            # Convert numeric predictions to class labels
            log_pred_mapped = [OBESITY_CLASS_MAPPING.get(pred, "Unknown") for pred in log_pred]
            dt_pred_mapped = [OBESITY_CLASS_MAPPING.get(pred, "Unknown") for pred in dt_pred]

            # Calculate Evaluation Metrics
            metrics = {
                "logistic_regression": {
                    "accuracy": accuracy_score(y_test, log_pred),
                    "precision": precision_score(y_test, log_pred, average="weighted", zero_division=0),
                    "recall": recall_score(y_test, log_pred, average="weighted", zero_division=0),
                    "f1_score": f1_score(y_test, log_pred, average="weighted", zero_division=0)
                },
                "decision_tree": {
                    "accuracy": accuracy_score(y_test, dt_pred),
                    "precision": precision_score(y_test, dt_pred, average="weighted", zero_division=0),
                    "recall": recall_score(y_test, dt_pred, average="weighted", zero_division=0),
                    "f1_score": f1_score(y_test, dt_pred, average="weighted", zero_division=0)
                }
            }

            # Logging into MLflow
            mlflow.set_tracking_uri(self.config.mlflow_tracking_uri)
            with mlflow.start_run():
                mlflow.log_params(self.config.all_params)
                
                # Log all metrics
                for model_name, model_metrics in metrics.items():
                    for metric_name, metric_value in model_metrics.items():
                        mlflow.log_metric(f"{model_name}_{metric_name}", metric_value)

                mlflow.sklearn.log_model(logistic_model, "logistic_model")
                mlflow.sklearn.log_model(decision_tree_model, "decision_tree_model")

            print(f"Evaluation Metrics for Logistic Regression: {metrics['logistic_regression']}")
            print(f"Evaluation Metrics for Decision Tree: {metrics['decision_tree']}")

            return {
                "logistic_regression": log_pred_mapped,
                "decision_tree": dt_pred_mapped
            }
        except Exception as e:
            raise RuntimeError(f"Error during model evaluation: {str(e)}")
