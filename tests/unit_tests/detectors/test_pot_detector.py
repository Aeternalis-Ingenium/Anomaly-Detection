from unittest import TestCase

from pandas import DataFrame

from src.anomaly_detection.detecto import get_detector
from src.anomaly_detection.models.detectors.interface import AnomalyDetector
from src.anomaly_detection.models.detectors.pot import POTAnomalyDetector


class TestPOTAnomalyDetectors(TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.pot_anomaly_detector = get_detector("pot")
        self.test_df = DataFrame(
            data={
                "col_1": [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
                "col_2": [15, 25, 35, 45, 55, 65, 75, 85, 95, 105],
                "col_3": [12, 22, 32, 42, 52, 62, 72, 82, 92, 102],
            }
        )

    def test_construct_pot_anomaly_detector(self):
        assert issubclass(type(self.pot_anomaly_detector), AnomalyDetector)
        assert isinstance(self.pot_anomaly_detector, POTAnomalyDetector)
        assert str(self.pot_anomaly_detector) == "POT Anomaly Detector"

    def test_default_value_for_t1_threshold_attribute(self):
        assert type(self.pot_anomaly_detector.t1_th) == float  # type: ignore
        assert self.pot_anomaly_detector.t1_th == 0.97  # type: ignore

    def test_default_value_for_pot_threshold_attribute(self):
        assert type(self.pot_anomaly_detector.pot_th) == float  # type: ignore
        assert self.pot_anomaly_detector.pot_th == 0.97  # type: ignore

    def test_default_value_for_t0_t1_t2_attributes(self):
        assert self.pot_anomaly_detector.t0 == None  # type: ignore
        assert self.pot_anomaly_detector.t1 == None  # type: ignore
        assert self.pot_anomaly_detector.t2 == None  # type: ignore

    def test_set_default_interval_value_for_t0_t1_t2_attributes(self):
        assert self.pot_anomaly_detector.t0 == None  # type: ignore
        assert self.pot_anomaly_detector.t1 == None  # type: ignore
        assert self.pot_anomaly_detector.t2 == None  # type: ignore

        self.pot_anomaly_detector.set_timeframe(total_rows=1000)  # type: ignore
        assert self.pot_anomaly_detector.t0 == 600  # type: ignore
        assert self.pot_anomaly_detector.t1 == 250  # type: ignore
        assert self.pot_anomaly_detector.t2 == 150  # type: ignore

    def test_set_conservative_interval_value_for_t0_t1_t2_attributes(self):
        assert self.pot_anomaly_detector.t0 == None  # type: ignore
        assert self.pot_anomaly_detector.t1 == None  # type: ignore
        assert self.pot_anomaly_detector.t2 == None  # type: ignore

        self.pot_anomaly_detector.set_timeframe(  # type: ignore
            total_rows=1000, t0_percentage=0.6, t1_percentage=0.3, t2_percentage=0.1
        )
        assert self.pot_anomaly_detector.t0 == 600  # type: ignore
        assert self.pot_anomaly_detector.t1 == 300  # type: ignore
        assert self.pot_anomaly_detector.t2 == 100  # type: ignore

    def test_get_pot_data_from_097_quantile_pot_th(self):
        expected_pot_data_df = DataFrame(
            data={
                "pot_data_col_1": [0.0, 0.0, 0.0, 0.0, 0.0, 1.5, 11.5, 11.8, 12.1, 12.4],
                "pot_data_col_2": [0.0, 0.0, 0.0, 0.0, 0.0, 1.5, 11.5, 11.8, 12.1, 12.4],
                "pot_data_col_3": [0.0, 0.0, 0.0, 0.0, 0.0, 1.5, 11.5, 11.8, 12.1, 12.4],
            }
        )
        expected_pot_th_df = DataFrame(
            data={
                "pot_th_col_1": [58.5, 58.5, 58.5, 58.5, 58.5, 58.5, 58.5, 68.2, 77.9, 87.6],
                "pot_th_col_2": [63.5, 63.5, 63.5, 63.5, 63.5, 63.5, 63.5, 73.2, 82.9, 92.6],
                "pot_th_col_3": [60.5, 60.5, 60.5, 60.5, 60.5, 60.5, 60.5, 70.2, 79.9, 89.6],
            }
        )

        assert self.pot_anomaly_detector.t0 == None  # type: ignore
        assert self.pot_anomaly_detector.t1 == None  # type: ignore
        assert self.pot_anomaly_detector.t2 == None  # type: ignore

        self.pot_anomaly_detector.set_timeframe(total_rows=self.test_df.shape[0])  # type: ignore

        assert self.pot_anomaly_detector.t0 == 6  # type: ignore
        assert self.pot_anomaly_detector.t1 == 3  # type: ignore
        assert self.pot_anomaly_detector.t2 == 1  # type: ignore

        pot_df = self.pot_anomaly_detector.compute_pot_data(df=self.test_df)  # type: ignore
        for feature in pot_df.columns:
            if "pot" in feature:
                pot_df[feature] = round(pot_df[feature], 2)

        assert self.pot_anomaly_detector.pot_th == 0.97  # type: ignore
        assert pot_df["pot_th_col_1"].equals(expected_pot_th_df["pot_th_col_1"])
        assert pot_df["pot_th_col_2"].equals(expected_pot_th_df["pot_th_col_2"])
        assert pot_df["pot_th_col_3"].equals(expected_pot_th_df["pot_th_col_3"])
        assert pot_df["pot_data_col_1"].equals(expected_pot_data_df["pot_data_col_1"])
        assert pot_df["pot_data_col_2"].equals(expected_pot_data_df["pot_data_col_2"])
        assert pot_df["pot_data_col_3"].equals(expected_pot_data_df["pot_data_col_3"])

    def tearDown(self) -> None:
        return super().tearDown()
