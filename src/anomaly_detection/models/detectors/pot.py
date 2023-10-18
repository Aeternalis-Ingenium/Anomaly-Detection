from pandas import DataFrame

from src.anomaly_detection.models.detectors.interface import AnomalyDetector
from src.anomaly_detection.utils.math import calculate_peak_over_threshold, get_data_over_threshold
from src.anomaly_detection.utils.timeframe import calculate_timeframe


class POTAnomalyDetector(AnomalyDetector):
    def __init__(self):
        self.t0: int | None = None
        self.t1: int | None = None
        self.t2: int | None = None
        self.__pot_th = 0.97
        self.__t1_th = 0.97

    @property
    def pot_th(self) -> float:
        return self.__pot_th

    @pot_th.setter
    def pot_th(self, th: float) -> None:
        if th < 0.0:
            raise ValueError("Threshold value can only be between 0. and 1.0")
        elif th > 1.0:
            raise ValueError("Threshold value can only be between 0. and 1.0")
        self.__pot_th = th

    @property
    def t1_th(self) -> float:
        return self.__t1_th

    @t1_th.setter
    def t1_th(self, th: float) -> None:
        if th < 0.0:
            raise ValueError("Threshold value can only be between 0. and 1.0")
        elif th > 1.0:
            raise ValueError("Threshold value can only be between 0. and 1.0")
        self.__t1_th = th

    def set_timeframe(
        self, total_rows: int, t0_percentage: float = 0.6, t1_percentage: float = 0.25, t2_percentage: float = 0.15
    ) -> None:
        self.t0, self.t1, self.t2 = calculate_timeframe(
            total_rows=total_rows,
            t0_percentage=t0_percentage,
            t1_percentage=t1_percentage,
            t2_percentage=t2_percentage,
        )

    def compute_pot_data(self, df: DataFrame) -> DataFrame:
        features = [feature for feature in df.columns if df[feature].dtype != object]
        pot_th_df = calculate_peak_over_threshold(df=df, features=features, min_period=self.t0, quantile=self.pot_th)  # type: ignore
        pot_data_df = get_data_over_threshold(df=pot_th_df, features=features)
        return pot_data_df

    def compute_anomaly_score(self, df: DataFrame) -> DataFrame:
        t1t2_df = df.iloc[self.t0 :]
        pot_t1t2_df = t1t2_df[[feature for feature in t1t2_df.columns[1:] if "pot_data" in feature]]

    def detect_anomaly(self, df: DataFrame) -> DataFrame:
        pass

    def __str__(self) -> str:
        return "POT Anomaly Detector"
