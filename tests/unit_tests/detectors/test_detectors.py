from unittest import TestCase

from src.anomaly_detection.detecto import get_detector
from src.anomaly_detection.models.detectors.autoencoder import AutoencoderAnomalyDetector
from src.anomaly_detection.models.detectors.block_maxima import BlockMaximaAnomalyDetector
from src.anomaly_detection.models.detectors.dbscan import DBSCANAnomalyDetector
from src.anomaly_detection.models.detectors.interface import AnomalyDetector
from src.anomaly_detection.models.detectors.isolation_forest import IsoForestAnomalyDetector
from src.anomaly_detection.models.detectors.mad import MADAnomalyDetector
from src.anomaly_detection.models.detectors.one_class_svm import OneClassSVMAnomalyDetector
from src.anomaly_detection.models.detectors.pot import POTAnomalyDetector
from src.anomaly_detection.models.detectors.zscore import ZScoreAnomalyDetector


class TestAnomalyDetectors(TestCase):
    def setUp(self) -> None:
        super().setUp()

    def test_construct_autoencoder_anomaly_detector_from_detector_factory(self):
        autoencoder_anomaly_detector = get_detector("autoencoder")

        assert issubclass(type(autoencoder_anomaly_detector), AnomalyDetector)
        assert isinstance(autoencoder_anomaly_detector, AutoencoderAnomalyDetector)
        assert str(autoencoder_anomaly_detector) == "Autoencoder Anomaly Detector"

    def test_construct_blockmaxima_anomaly_detector_from_detector_factory(self):
        blockmaxima_anomaly_detector = get_detector("block_maxima")

        assert issubclass(type(blockmaxima_anomaly_detector), AnomalyDetector)
        assert isinstance(blockmaxima_anomaly_detector, BlockMaximaAnomalyDetector)
        assert str(blockmaxima_anomaly_detector) == "Block-Maxima Anomaly Detector"

    def test_construct_dbscan_anomaly_detector_from_detector_factory(self):
        dbscan_anomaly_detector = get_detector("dbscan")

        assert issubclass(type(dbscan_anomaly_detector), AnomalyDetector)
        assert isinstance(dbscan_anomaly_detector, DBSCANAnomalyDetector)
        assert str(dbscan_anomaly_detector) == "DBSCAN Anomaly Detector"

    def test_construct_isoforest_anomaly_detector_from_detector_factory(self):
        iso_forest_anomaly_detector = get_detector("iso_forest")

        assert issubclass(type(iso_forest_anomaly_detector), AnomalyDetector)
        assert isinstance(iso_forest_anomaly_detector, IsoForestAnomalyDetector)
        assert str(iso_forest_anomaly_detector) == "Isolation Forest Anomaly Detector"

    def test_construct_mad_anomaly_detector_from_detector_factory(self):
        mad_anomaly_detector = get_detector("mad")

        assert issubclass(type(mad_anomaly_detector), AnomalyDetector)
        assert isinstance(mad_anomaly_detector, MADAnomalyDetector)
        assert str(mad_anomaly_detector) == "MAD Anomaly Detector"

    def test_construct_1_class_svm_anomaly_detector_from_detector_factory(self):
        one_class_svm_anomaly_detector = get_detector("1_class_svm")

        assert issubclass(type(one_class_svm_anomaly_detector), AnomalyDetector)
        assert isinstance(one_class_svm_anomaly_detector, OneClassSVMAnomalyDetector)
        assert str(one_class_svm_anomaly_detector) == "One Class SVM Anomaly Detector"

    def test_construct_pot_anomaly_detector_from_detector_factory(self):
        pot_anomaly_detector = get_detector("pot")

        assert issubclass(type(pot_anomaly_detector), AnomalyDetector)
        assert isinstance(pot_anomaly_detector, POTAnomalyDetector)
        assert str(pot_anomaly_detector) == "POT Anomaly Detector"

    def test_construct_zscore_anomaly_detector_from_detector_factory(self):
        z_score_anomaly_detector = get_detector("z_score")

        assert issubclass(type(z_score_anomaly_detector), AnomalyDetector)
        assert isinstance(z_score_anomaly_detector, ZScoreAnomalyDetector)
        assert str(z_score_anomaly_detector) == "Z-Score Anomaly Detector"

    def tearDown(self) -> None:
        return super().tearDown()
