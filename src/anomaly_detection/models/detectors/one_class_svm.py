from pandas import DataFrame

from src.anomaly_detection.models.detectors.interface import AnomalyDetector


class OneClassSVMAnomalyDetector(AnomalyDetector):
    def compute_anomaly_score(self, dataset: DataFrame) -> DataFrame:
        pass

    def detect_anomaly(self, dataset: DataFrame) -> DataFrame:
        pass

    def __str__(self) -> str:
        return "One Class SVM Anomaly Detector"
