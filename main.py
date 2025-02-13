from ObesityPredictor import logger
from ObesityPredictor.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from ObesityPredictor.utils.common import remove_pycache
remove_pycache()

STAGE_NAME = "Data Ingestion stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e