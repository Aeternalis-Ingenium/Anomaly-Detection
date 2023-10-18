from unittest import TestCase

from src.anomaly_detection.utils.timeframe import calculate_timeframe


class TestTimeFrameCalculator(TestCase):
    def setUp(self) -> None:
        super().setUp()

    def test_calculate_1000days_timeframe_with_50_30_20_percentages(self):
        t0, t1, t2 = calculate_timeframe(total_rows=1000, t0_percentage=0.5, t1_percentage=0.3, t2_percentage=0.2)

        assert t0 == 500
        assert t1 == 300
        assert t2 == 200

    def test_calculate_10000days_timeframe_with_50_30_20_percentages(self):
        t0, t1, t2 = calculate_timeframe(total_rows=10000, t0_percentage=0.5, t1_percentage=0.3, t2_percentage=0.2)

        assert t0 == 5000
        assert t1 == 3000
        assert t2 == 2000

    def test_calculate_1000days_timeframe_with_60_25_15_percentages(self):
        t0, t1, t2 = calculate_timeframe(total_rows=1000, t0_percentage=0.6, t1_percentage=0.25, t2_percentage=0.15)

        assert t0 == 600
        assert t1 == 250
        assert t2 == 150

    def test_calculate_10000days_timeframe_with_60_25_15_percentages(self):
        t0, t1, t2 = calculate_timeframe(total_rows=10000, t0_percentage=0.6, t1_percentage=0.25, t2_percentage=0.15)

        assert t0 == 6000
        assert t1 == 2500
        assert t2 == 1500

    def tearDown(self) -> None:
        return super().tearDown()
