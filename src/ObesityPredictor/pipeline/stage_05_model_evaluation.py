from ObesityPredictor.config.configuration import ConfigurationManager
from ObesityPredictor.components.model_evaluation import ModelEvaluation
from ObesityPredictor.entity.config_entity import EvaluationConfig
from ObesityPredictor import logger
import pandas as pd

STAGE_NAME = "Model Evaluation Stage"

class ModelEvaluationPipeline:
    def __init__(self):
        config_manager = ConfigurationManager()
        self.evaluation_config = config_manager.get_evaluation_config()
        self.model_evaluator = ModelEvaluation(config=self.evaluation_config)  # ✅ Explicitly passing config

    def run(self):
        self.model_evaluator.evaluate()

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")

        pipeline = ModelEvaluationPipeline()
        pipeline.run()

        logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
