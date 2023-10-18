from typing import Literal

from src.anomaly_detection.utils.types import AnomalyDetector


class FactoryAnomalyDetector:
    def __init__(
        self,
        detector: Literal[
            "autoencoder", "block_maxima", "dbscan", "iso_forest", "mad", "1_class_svm", "pot", "z_score"
        ],
    ):
        self.detector = detector

    def __call__(self) -> AnomalyDetector:
        if self.detector == "autoencoder":
            from src.anomaly_detection.models.detectors.autoencoder import AutoencoderAnomalyDetector

            return AutoencoderAnomalyDetector()
        elif self.detector == "block_maxima":
            from src.anomaly_detection.models.detectors.block_maxima import BlockMaximaAnomalyDetector

            return BlockMaximaAnomalyDetector()
        elif self.detector == "dbscan":
            from src.anomaly_detection.models.detectors.dbscan import DBSCANAnomalyDetector

            return DBSCANAnomalyDetector()
        elif self.detector == "iso_forest":
            from src.anomaly_detection.models.detectors.isolation_forest import IsoForestAnomalyDetector

            return IsoForestAnomalyDetector()
        elif self.detector == "mad":
            from src.anomaly_detection.models.detectors.mad import MADAnomalyDetector

            return MADAnomalyDetector()
        elif self.detector == "1_class_svm":
            from src.anomaly_detection.models.detectors.one_class_svm import OneClassSVMAnomalyDetector

            return OneClassSVMAnomalyDetector()
        elif self.detector == "pot":
            from src.anomaly_detection.models.detectors.pot import POTAnomalyDetector

            return POTAnomalyDetector()
        from src.anomaly_detection.models.detectors.zscore import ZScoreAnomalyDetector

        return ZScoreAnomalyDetector()
