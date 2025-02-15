from ObesityPredictor import logger
from ObesityPredictor.config.configuration import ConfigurationManager
from ObesityPredictor.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from ObesityPredictor.pipeline.stage_02_data_cleaning_encoding import DataCleaningEncodingPipeline
from ObesityPredictor.pipeline.stage_03_model_training import ModelTrainingPipeline
from ObesityPredictor.pipeline.stage_05_model_evaluation import ModelEvaluationPipeline
from ObesityPredictor.pipeline.stage_04_model_inference import ModelInferencePipeline
import pandas as pd
from ObesityPredictor.utils.common import remove_pycache

# Remove cached files before running
remove_pycache()

def run_pipeline(stage_name, pipeline_class):
    """Generic function to execute a pipeline stage with logging."""
    try:
        logger.info(f">>>>>> Stage {stage_name} started <<<<<<")
        pipeline = pipeline_class()
        
        # Check if pipeline has `run()`, else use `main()`
        if hasattr(pipeline, "run"):
            pipeline.run()  # ✅ Call `run()` if it exists
        elif hasattr(pipeline, "main"):
            pipeline.main()  # ✅ Call `main()` if it exists
        else:
            raise AttributeError(f"{pipeline_class.__name__} has neither `run()` nor `main()` method.")
        
        logger.info(f">>>>>> Stage {stage_name} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e

# **Execute Data Pipeline Stages**
run_pipeline("Data Ingestion Stage", DataIngestionTrainingPipeline)
run_pipeline("Data Cleaning and Encoding Stage", DataCleaningEncodingPipeline)
run_pipeline("Model Training Stage", ModelTrainingPipeline)
run_pipeline("Model Evaluation Stage", ModelEvaluationPipeline)

# **Model Inference Stage**
STAGE_NAME = "Model Inference Stage"
try:
    logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")

    inference_pipeline = ModelInferencePipeline()

    # Retrieve parameters from ModelInferenceConfig
    config_manager = ConfigurationManager()
    params = config_manager.params  # ✅ Correctly access params.yaml
    sample_input_values = params["inference_sample"]  # ✅ Now properly loads inference sample
    sample_input = pd.DataFrame([sample_input_values["values"]], columns=sample_input_values["columns"])

    predictions = inference_pipeline.run(sample_input)  # ✅ Correct method call
    logger.info(f"Inference Results: {predictions}")

    logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e
