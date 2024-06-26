from cnnClassifier import logger
#from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
#from cnnClassifier.pipeline.stage_03_model_training import ModelTrainingPipeline
#from cnnClassifier.pipeline.stage_04_model_evaluation import EvaluationPipeline

from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f'>>>>>> stage {STAGE_NAME} started <<<<<<')
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f'>>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x')
except Exception as e:
    logger.exception(e)
    raise e