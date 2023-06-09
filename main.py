from cnnClassifier import logger

from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline

STAGE_NAME = "DATA Ingestion Stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} Started <<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} Completed <<<<<\n\nx=======x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Prepare Base Model"
try:
    logger.info(f"************************")
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<<")
    prepare_base__model = PrepareBaseModelTrainingPipeline()
    prepare_base__model.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx=======x")
except Exception as e:
    logger.exception(e)
    raise e

