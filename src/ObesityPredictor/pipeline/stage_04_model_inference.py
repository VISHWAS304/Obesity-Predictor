from ObesityPredictor.config.configuration import ConfigurationManager
from ObesityPredictor.components.model_inference import ModelInference
from ObesityPredictor.entity.config_entity import ModelInferenceConfig
from ObesityPredictor import logger
import pandas as pd

STAGE_NAME = "Model Inference Stage"

class ModelInferencePipeline:
    def __init__(self):
        config_manager = ConfigurationManager()
        self.model_inference_config = config_manager.get_model_inference_config()
        self.model_inference = ModelInference(config=self.model_inference_config)  # ✅ Pass config explicitly

    def run(self, input_data: pd.DataFrame):
        predictions = self.model_inference.run(input_data)
        return predictions

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        
        pipeline = ModelInferencePipeline()
        
        # Load sample input values from params.yaml
        sample_input_values = pipeline.model_inference_config.params["inference_sample"]
        sample_input = pd.DataFrame([sample_input_values["values"]], columns=sample_input_values["columns"])
        
        predictions = pipeline.run(sample_input)
        logger.info(f"Inference Results: {predictions}")
        
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
