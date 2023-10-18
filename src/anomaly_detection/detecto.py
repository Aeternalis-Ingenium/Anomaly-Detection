from typing import Literal

from src.anomaly_detection.models.detectors.detector import FactoryAnomalyDetector
from src.anomaly_detection.utils.types import AnomalyDetector


def get_detector(
    detector: Literal["autoencoder", "block_maxima", "dbscan", "iso_forest", "mad", "1_class_svm", "pot", "z_score"]
) -> AnomalyDetector:
    return FactoryAnomalyDetector(detector=detector)()


if __name__ == "__main__":
    pass
