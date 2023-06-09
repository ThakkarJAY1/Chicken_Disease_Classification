from cnnClassifier import logger

from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "DATA Ingestion Stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} Started <<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} Completed <<<<<\n\nx=======x")
except Exception as e:
    logger.exception(e)
    raise e

