from anomaly_detection.models.detectors.autoencoder import AutoencoderAnomalyDetector
from anomaly_detection.models.detectors.block_maxima import BlockMaximaAnomalyDetector
from anomaly_detection.models.detectors.dbscan import DBSCANAnomalyDetector
from anomaly_detection.models.detectors.isolation_forest import IsoForestAnomalyDetector
from anomaly_detection.models.detectors.mad import MADAnomalyDetector
from anomaly_detection.models.detectors.one_class_svm import OneClassSVMAnomalyDetector
from anomaly_detection.models.detectors.pot import POTAnomalyDetector
from anomaly_detection.models.detectors.zscore import ZScoreAnomalyDetector

AnomalyDetector = (
    AutoencoderAnomalyDetector
    | BlockMaximaAnomalyDetector
    | DBSCANAnomalyDetector
    | IsoForestAnomalyDetector
    | MADAnomalyDetector
    | OneClassSVMAnomalyDetector
    | POTAnomalyDetector
    | ZScoreAnomalyDetector
)
