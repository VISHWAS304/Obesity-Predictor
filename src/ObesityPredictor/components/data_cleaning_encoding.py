import pandas as pd
import os
from pathlib import Path
from ObesityPredictor import logger

class DataCleaningEncodingConfig:
    def __init__(self, input_file: Path, output_file: Path):
        self.input_file = input_file
        self.output_file = output_file

class DataCleaningEncoding:
    def __init__(self, config: DataCleaningEncodingConfig):
        self.config = config
    
    def load_data(self) -> pd.DataFrame:
        """
        Load the ingested data from the specified input file.
        """
        try:
            logger.info(f"Loading data from {self.config.input_file}")
            df = pd.read_csv(self.config.input_file)
            logger.info(f"Data loaded successfully with shape {df.shape}")
            return df
        except Exception as e:
            logger.error(f"Error loading data: {str(e)}")
            raise e

    def clean_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Perform data cleaning steps such as handling missing values and feature engineering.
        """
        try:
            logger.info("Cleaning data...")
            # Compute BMI
            df['BMI'] = df['Weight'] / (df['Height'] ** 2)
            df.drop(columns=['Height', 'Weight'], inplace=True)
            logger.info(f"Data cleaned, new shape: {df.shape}")
            return df
        except Exception as e:
            logger.error(f"Error during data cleaning: {str(e)}")
            raise e
    
    def encode_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Perform encoding of categorical variables.
        """
        try:
            logger.info("Encoding categorical features...")
            categorical_columns = ['Gender', 'family_history', 'FAVC', 'CAEC', 'SMOKE', 'SCC', 'CALC', 'MTRANS']
            df = pd.get_dummies(df, columns=categorical_columns, drop_first=True)  # One-hot encoding
            
            # Encode the target variable
            obesity_mapping = {
                "Insufficient_Weight": 0,
                "Normal_Weight": 1,
                "Overweight_Level_I": 2,
                "Overweight_Level_II": 3,
                "Obesity_Type_I": 4,
                "Obesity_Type_II": 5,
                "Obesity_Type_III": 6
            }
            df['Obesity'] = df['Obesity'].map(obesity_mapping)
            
            logger.info(f"Data encoding complete, new shape: {df.shape}")
            return df
        except Exception as e:
            logger.error(f"Error during data encoding: {str(e)}")
            raise e

    def save_data(self, df: pd.DataFrame):
        """
        Save the cleaned and encoded data to the specified output file.
        """
        try:
            os.makedirs(self.config.output_file.parent, exist_ok=True)
            df.to_csv(self.config.output_file, index=False)
            logger.info(f"Cleaned and encoded data saved to {self.config.output_file}")
        except Exception as e:
            logger.error(f"Error saving cleaned data: {str(e)}")
            raise e

    def run(self):
        """
        Execute the data cleaning and encoding pipeline.
        """
        df = self.load_data()
        df = self.clean_data(df)
        df = self.encode_data(df)
        self.save_data(df)