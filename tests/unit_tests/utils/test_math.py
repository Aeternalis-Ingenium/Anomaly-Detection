from unittest import TestCase

from numpy import allclose
from pandas import DataFrame

from src.anomaly_detection.utils.math import calculate_peak_over_threshold, get_data_over_threshold


class TestPOTCalculation(TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.test_df = DataFrame(
            data={
                "col_1": [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
                "col_2": [15, 25, 35, 45, 55, 65, 75, 85, 95, 105],
                "col_3": [12, 22, 32, 42, 52, 62, 72, 82, 92, 102],
            }
        )
        self.features = ["col_1", "col_2", "col_3"]

    def test_calculate_peak_over_threshold_050_quantile(self):
        expected_pot_th_df = DataFrame(
            data={
                "pot_th_col_1": [35.0, 35.0, 35.0, 35.0, 35.0, 35.0, 35.0, 40.0, 45.0, 50.0],
                "pot_th_col_2": [40.0, 40.0, 40.0, 40.0, 40.0, 40.0, 40.0, 45.0, 50.0, 55.0],
                "pot_th_col_3": [37.0, 37.0, 37.0, 37.0, 37.0, 37.0, 37.0, 42.0, 47.0, 52.0],
            }
        )
        pot_th_df = calculate_peak_over_threshold(df=self.test_df, features=self.features, min_period=6, quantile=0.5)
        assert pot_th_df["pot_th_col_1"].equals(expected_pot_th_df["pot_th_col_1"])
        assert pot_th_df["pot_th_col_2"].equals(expected_pot_th_df["pot_th_col_2"])
        assert pot_th_df["pot_th_col_3"].equals(expected_pot_th_df["pot_th_col_3"])

    def test_calculate_peak_over_threshold_097_quantile(self):
        expected_pot_th_df = DataFrame(
            data={
                "pot_th_col_1": [58.5, 58.5, 58.5, 58.5, 58.5, 58.5, 58.5, 68.2, 77.9, 87.6],
                "pot_th_col_2": [63.5, 63.5, 63.5, 63.5, 63.5, 63.5, 63.5, 73.2, 82.9, 92.6],
                "pot_th_col_3": [60.5, 60.5, 60.5, 60.5, 60.5, 60.5, 60.5, 70.2, 79.9, 89.6],
            }
        )
        pot_th_df = calculate_peak_over_threshold(df=self.test_df, features=self.features, min_period=6, quantile=0.97)
        assert pot_th_df["pot_th_col_1"].equals(expected_pot_th_df["pot_th_col_1"])
        assert pot_th_df["pot_th_col_2"].equals(expected_pot_th_df["pot_th_col_2"])
        assert pot_th_df["pot_th_col_3"].equals(expected_pot_th_df["pot_th_col_3"])

    def test_get_data_over_threshold_050_quantile(self):
        expected_pot_data_df = DataFrame(
            data={
                "pot_data_col_1": [0.0, 0.0, 0.0, 5.0, 15.0, 25.0, 35.0, 40.0, 45.0, 50.0],
                "pot_data_col_2": [0.0, 0.0, 0.0, 5.0, 15.0, 25.0, 35.0, 40.0, 45.0, 50.0],
                "pot_data_col_3": [0.0, 0.0, 0.0, 5.0, 15.0, 25.0, 35.0, 40.0, 45.0, 50.0],
            }
        )
        pot_th_df = calculate_peak_over_threshold(df=self.test_df, features=self.features, min_period=6, quantile=0.5)
        pot_data_df = get_data_over_threshold(df=pot_th_df, features=self.features)
        assert pot_data_df["pot_data_col_1"].equals(expected_pot_data_df["pot_data_col_1"])
        assert pot_data_df["pot_data_col_2"].equals(expected_pot_data_df["pot_data_col_2"])
        assert pot_data_df["pot_data_col_3"].equals(expected_pot_data_df["pot_data_col_3"])

    def test_get_data_over_threshold_097_quantile(self):
        expected_pot_data_df = DataFrame(
            data={
                "pot_data_col_1": [0.0, 0.0, 0.0, 0.0, 0.0, 1.5, 11.5, 11.8, 12.1, 12.4],
                "pot_data_col_2": [0.0, 0.0, 0.0, 0.0, 0.0, 1.5, 11.5, 11.8, 12.1, 12.4],
                "pot_data_col_3": [0.0, 0.0, 0.0, 0.0, 0.0, 1.5, 11.5, 11.8, 12.1, 12.4],
            }
        )
        pot_th_df = calculate_peak_over_threshold(df=self.test_df, features=self.features, min_period=6, quantile=0.97)
        pot_data_df = get_data_over_threshold(df=pot_th_df, features=self.features)

        assert allclose(pot_data_df["pot_data_col_1"].values, expected_pot_data_df["pot_data_col_1"].values)
        assert allclose(pot_data_df["pot_data_col_2"].values, expected_pot_data_df["pot_data_col_2"].values)
        assert allclose(pot_data_df["pot_data_col_3"].values, expected_pot_data_df["pot_data_col_3"].values)

    def test_get_data_over_threshold_050_quantile_failed_cause_by_different_expected_result(self):
        expected_pot_data_df = DataFrame(
            data={
                "pot_data_col_1": [0.0, 0.0, 0.0, 5.3, 15.3, 25.3, 35.3, 40.3, 45.3, 50.3],
                "pot_data_col_2": [0.0, 0.0, 0.0, 5.3, 15.3, 25.3, 35.3, 40.3, 45.3, 50.3],
                "pot_data_col_3": [0.0, 0.0, 0.0, 5.3, 15.3, 25.3, 35.3, 40.3, 45.3, 50.3],
            }
        )
        pot_th_df = calculate_peak_over_threshold(df=self.test_df, features=self.features, min_period=6, quantile=0.5)
        pot_data_df = get_data_over_threshold(df=pot_th_df, features=self.features)
        assert not pot_data_df["pot_data_col_1"].equals(expected_pot_data_df["pot_data_col_1"])
        assert not pot_data_df["pot_data_col_2"].equals(expected_pot_data_df["pot_data_col_2"])
        assert not pot_data_df["pot_data_col_3"].equals(expected_pot_data_df["pot_data_col_3"])

    def test_get_data_over_threshold_097_quantile_failed_caused_by_very_small_differences(self):
        expected_pot_data_df = DataFrame(
            data={
                "pot_data_col_1": [0.0, 0.0, 0.0, 0.0, 0.0, 1.5, 11.5, 11.8, 12.1, 12.4],
                "pot_data_col_2": [0.0, 0.0, 0.0, 0.0, 0.0, 1.5, 11.5, 11.8, 12.1, 12.4],
                "pot_data_col_3": [0.0, 0.0, 0.0, 0.0, 0.0, 1.5, 11.5, 11.8, 12.1, 12.4],
            }
        )
        pot_th_df = calculate_peak_over_threshold(df=self.test_df, features=self.features, min_period=6, quantile=0.97)
        pot_data_df = get_data_over_threshold(df=pot_th_df, features=self.features)

        assert not pot_data_df["pot_data_col_1"].equals(expected_pot_data_df["pot_data_col_1"])
        assert not pot_data_df["pot_data_col_2"].equals(expected_pot_data_df["pot_data_col_2"])
        assert not pot_data_df["pot_data_col_3"].equals(expected_pot_data_df["pot_data_col_3"])

    def tearDown(self) -> None:
        return super().tearDown()
