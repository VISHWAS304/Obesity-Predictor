from ObesityPredictor.constants import *
import os
from ObesityPredictor.utils.common import read_yaml, create_directories,save_json
from ObesityPredictor.entity.config_entity import (DataIngestionConfig)


class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])


    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        # Ensure the data ingestion directory exists
        create_directories([config.root_dir])

        # ✅ Correctly instantiate DataIngestionConfig with `LOCAL_DOWNLOAD_FILE`
        data_ingestion_config = DataIngestionConfig(
            AWS_REGION=config.AWS_REGION,
            BUCKET_NAME=config.BUCKET_NAME,
            S3_OBJECT_KEY=config.S3_OBJECT_KEY,
            root_dir=Path(config.root_dir),
            LOCAL_DOWNLOAD_FILE=Path(config.LOCAL_DOWNLOAD_FILE)  # ✅ Added
        )

        return data_ingestion_config