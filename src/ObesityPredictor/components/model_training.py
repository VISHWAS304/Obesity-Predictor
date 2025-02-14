import pandas as pd
import os
import pickle
import json
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from ObesityPredictor import logger
from ObesityPredictor.utils.common import read_yaml
from ObesityPredictor.config.configuration import ModelTrainingConfig

class ModelTraining:
    def __init__(self, config: ModelTrainingConfig):
        self.config = config

    def load_data(self):
        """Load cleaned and encoded dataset."""
        try:
            logger.info(f"Loading data from {self.config.input_file}")
            df = pd.read_csv(self.config.input_file)
            X = df.drop(columns=["Obesity"])
            y = df["Obesity"]
            return X, y
        except Exception as e:
            logger.error(f"Error loading data: {str(e)}")
            raise e

    def split_data(self, X, y):
        """Split dataset into train and test sets."""
        try:
            test_size = self.config.params["train_test_split"]["test_size"]
            random_state = self.config.params["train_test_split"]["random_state"]
            stratify = y if self.config.params["train_test_split"]["stratify"] else None

            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=test_size, random_state=random_state, stratify=stratify
            )
            logger.info(f"Data split complete: Train size={X_train.shape}, Test size={X_test.shape}")
            return X_train, X_test, y_train, y_test
        except Exception as e:
            logger.error(f"Error during data splitting: {str(e)}")
            raise e

    def save_feature_names(self, feature_names, file_path="artifacts/models/feature_names.json"):
        """Save feature names used during training."""
        try:
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path, "w") as f:
                json.dump(feature_names, f)
            logger.info(f"Feature names saved at {file_path}")
        except Exception as e:
            logger.error(f"Error saving feature names: {str(e)}")
            raise e

    def train_and_save_model(self, X_train, y_train, model, model_name):
        """Train a given model and save it."""
        try:
            logger.info(f"Training {model_name}...")
            model.fit(X_train, y_train)
            os.makedirs(self.config.models_dir / model_name, exist_ok=True)
            model_path = self.config.models_dir / model_name / "model.pkl"
            with open(model_path, "wb") as f:
                pickle.dump(model, f)
            logger.info(f"{model_name} saved at {model_path}")
        except Exception as e:
            logger.error(f"Error training {model_name}: {str(e)}")
            raise e

    def run(self):
        """Execute the model training pipeline."""
        X, y = self.load_data()
        X_train, X_test, y_train, y_test = self.split_data(X, y)

        # Save feature names for inference alignment
        feature_names = list(X_train.columns)
        self.save_feature_names(feature_names)

        # Train Logistic Regression
        log_reg_params = self.config.params["models"]["logistic_regression"]
        log_reg = LogisticRegression(**log_reg_params)
        self.train_and_save_model(X_train, y_train, log_reg, "logistic_regression")

        # Train Decision Tree
        dt_params = self.config.params["models"]["decision_tree"]
        decision_tree = DecisionTreeClassifier(**dt_params)
        self.train_and_save_model(X_train, y_train, decision_tree, "decision_tree")
