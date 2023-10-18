from abc import ABCMeta, abstractmethod

from pandas import DataFrame


class AnomalyDetector(metaclass=ABCMeta):
    @abstractmethod
    def compute_anomaly_score(self, dataset: DataFrame) -> DataFrame:
        """A function to prepare the dataset by calculating the anomaly score for a chosen time interval.

        Args:
            :dataset (
                dict | pd.DataFrame
            ): A Pandas DataFrame in which the data is used for the anomaly score calculation.

        Returns:
            :AnomalyScoreDataset (pd.DataFrame): The processed dataset with anomaly score for each data point.
        """

    @abstractmethod
    def detect_anomaly(self, dataset: DataFrame) -> DataFrame:
        """A function to detect the anomalous data.

        Args:
            :dataset (dict | pd.DataFrame): A Pandas DataFrame of anomaly scores with a certain time interval e.g. daily.

        Returns:
            :AnomalyDataset (pd.DataFrame): The processed dataset that reveals the anomalous data.
        """
