from ObesityPredictor import logger
from ObesityPredictor.config.configuration import ConfigurationManager
from ObesityPredictor.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from ObesityPredictor.pipeline.stage_02_data_cleaning_encoding import DataCleaningEncodingPipeline
from ObesityPredictor.pipeline.stage_03_model_training import ModelTrainingPipeline
from ObesityPredictor.pipeline.stage_04_model_inference import ModelInferencePipeline
import pandas as pd
from ObesityPredictor.utils.common import remove_pycache

# Remove cached files before running
remove_pycache()

# **Data Ingestion Stage**
STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

# **Data Cleaning and Encoding Stage**
STAGE_NAME = "Data Cleaning and Encoding Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_cleaning = DataCleaningEncodingPipeline()
    data_cleaning.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

# **Model Training Stage**
STAGE_NAME = "Model Training Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    model_training = ModelTrainingPipeline()
    model_training.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

# **Model Inference Stage**
STAGE_NAME = "Model Inference Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    inference_pipeline = ModelInferencePipeline()

    # Retrieve parameters from ModelInferenceConfig
    config_manager = ConfigurationManager()
    params = config_manager.params  # ✅ Correctly access params.yaml
    sample_input_values = params["inference_sample"]  # ✅ Now properly loads inference sample
    sample_input = pd.DataFrame([sample_input_values["values"]], columns=sample_input_values["columns"])

    predictions = inference_pipeline.run(sample_input)  # ✅ Correct method call
    logger.info(f"Inference Results: {predictions}")

    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e
