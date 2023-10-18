from random import randint, uniform
from typing import Callable

from pandas import DataFrame


class DataGenerator:
    def __init__(
        self,
        total_cols: int = 2,
        total_rows: int = 1000,
        max_value: int = 1000,
        total_pos_inf: int | None = None,
        total_neg_inf: int | None = None,
        is_float: bool = False,
        is_pos: bool = True,
        anomaly_percentage: float | None = 0.03,
    ):
        self.total_cols: int = total_cols
        self.total_rows: int = total_rows
        self.max_value = max_value
        self.total_pos_inf: int | None = total_pos_inf
        self.total_neg_inf: int | None = total_neg_inf
        self.is_float: bool = is_float
        self.is_pos: bool = is_pos
        self.total_anomalies = int(anomaly_percentage * max_value) if anomaly_percentage else None

    def __gen_data(self) -> list[int | float]:
        if self.total_rows <= 0:
            raise ValueError("Parameter `total_rows` must be a positive integer.")
        if not self.is_float:
            data_gen: Callable[[], int] = lambda: randint(0, self.max_value)  # type: ignore
        elif self.is_float:
            data_gen: Callable[[], float] = lambda: uniform(0, self.max_value)  # type: ignore
        rows: list[int | float] = [data_gen() for _ in range(self.total_rows)]
        return rows

    def __convert_to_neg(self, rows: list[int | float]) -> list[int | float]:
        converted_rows = []
        if not self.is_pos:
            for data in rows:
                converted_rows.append((data * -1) - 1)
        else:
            converted_rows = rows
        return converted_rows

    def __gen_anomaly(self, rows: list[int | float]) -> list[int | float]:
        new_rows = rows
        if self.total_anomalies:
            new_rows = new_rows[: -self.total_anomalies]
            if self.total_pos_inf or self.total_neg_inf:
                for _ in range(0, self.total_anomalies):
                    new_rows.append(float("inf") if self.total_pos_inf else float("-inf"))
            else:
                max_value = self.max_value**2
                if not self.is_float:
                    data_gen: Callable[[], int] = lambda: randint(0, max_value)  # type: ignore
                elif self.is_float:
                    data_gen: Callable[[], float] = lambda: uniform(0, max_value)  # type: ignore
                anomaly_rows = [data_gen() for _ in range(0, self.total_anomalies)]
                for anomaly_row in anomaly_rows:
                    new_rows.append(anomaly_row)
        return new_rows

    def __gen_rows(self) -> list[int | float]:
        print("Start random data generation. . .")
        rows = self.__gen_data()
        print(f"{len(rows)} rows are successfully generated!")
        print("Positive-Negative data convertion. . .")
        converted_rows = self.__convert_to_neg(rows=rows)
        if converted_rows[0] < 0:
            print("Data values are negative!")
        else:
            print("Data values stay positive!")
        print(f"Generating {self.total_anomalies} anomalous data. . .")
        print(f"{self.total_anomalies} anomalous data are successfully generated!")
        return self.__gen_anomaly(rows=converted_rows)

    def __call__(self):
        data = {}
        for i in range(0, self.total_cols):
            data[f"col_{i+1}"] = self.__gen_rows()
        df = DataFrame(data=data)
        print(f"Total DF rows: {df.shape[0]}")
        return df


def gen_data(
    total_cols: int = 2,
    total_rows: int = 1000,
    max_value: int = 1000,
    anomaly_percentage: float | None = 0.03,
    total_pos_inf: int | None = None,
    total_neg_inf: int | None = None,
    is_float: bool = False,
    is_pos: bool = True,
) -> DataFrame:
    return DataGenerator(
        total_cols=total_cols,
        total_rows=total_rows,
        max_value=max_value,
        anomaly_percentage=anomaly_percentage,
        total_pos_inf=total_pos_inf,
        total_neg_inf=total_neg_inf,
        is_float=is_float,
        is_pos=is_pos,
    )()


df1_pos_int_1000_003 = gen_data(
    total_cols=2,
    total_rows=1000,
    max_value=1000,
    anomaly_percentage=0.03,
    total_pos_inf=None,
    total_neg_inf=None,
    is_float=False,
    is_pos=True,
)
df2_pos_int_1000_003 = gen_data(
    total_cols=2,
    total_rows=10000,
    max_value=1000,
    anomaly_percentage=0.03,
    total_pos_inf=None,
    total_neg_inf=None,
    is_float=False,
    is_pos=True,
)
df3_pos_int_1000_003 = gen_data(
    total_cols=2,
    total_rows=100000,
    max_value=1000,
    anomaly_percentage=0.03,
    total_pos_inf=None,
    total_neg_inf=None,
    is_float=False,
    is_pos=True,
)
df4_pos_int_1000_003 = gen_data(
    total_cols=2,
    total_rows=1000000,
    max_value=1000,
    anomaly_percentage=0.03,
    total_pos_inf=None,
    total_neg_inf=None,
    is_float=False,
    is_pos=True,
)
df5_pos_int_1000_003 = gen_data(
    total_cols=2,
    total_rows=10000000,
    max_value=1000,
    anomaly_percentage=0.03,
    total_pos_inf=None,
    total_neg_inf=None,
    is_float=False,
    is_pos=True,
)
df1_pos_int_10000_003 = gen_data(
    total_cols=2,
    total_rows=1000,
    max_value=10000,
    anomaly_percentage=0.03,
    total_pos_inf=None,
    total_neg_inf=None,
    is_float=False,
    is_pos=True,
)
df2_pos_int_10000_003 = gen_data(
    total_cols=2,
    total_rows=10000,
    max_value=10000,
    anomaly_percentage=0.03,
    total_pos_inf=None,
    total_neg_inf=None,
    is_float=False,
    is_pos=True,
)
df3_pos_int_10000_003 = gen_data(
    total_cols=2,
    total_rows=100000,
    max_value=10000,
    anomaly_percentage=0.03,
    total_pos_inf=None,
    total_neg_inf=None,
    is_float=False,
    is_pos=True,
)
df4_pos_int_10000_003 = gen_data(
    total_cols=2,
    total_rows=1000000,
    max_value=10000,
    anomaly_percentage=0.03,
    total_pos_inf=None,
    total_neg_inf=None,
    is_float=False,
    is_pos=True,
)
df5_pos_int_10000_003 = gen_data(
    total_cols=2,
    total_rows=10000000,
    max_value=10000,
    anomaly_percentage=0.03,
    total_pos_inf=None,
    total_neg_inf=None,
    is_float=False,
    is_pos=True,
)

df1_neg_int_1000_003 = gen_data(
    total_cols=2,
    total_rows=1000,
    max_value=1000,
    anomaly_percentage=0.03,
    total_pos_inf=None,
    total_neg_inf=None,
    is_float=False,
    is_pos=False,
)
df2_neg_int_1000_003 = gen_data(
    total_cols=2,
    total_rows=10000,
    max_value=1000,
    anomaly_percentage=0.03,
    total_pos_inf=None,
    total_neg_inf=None,
    is_float=False,
    is_pos=False,
)
df3_neg_int_1000_003 = gen_data(
    total_cols=2,
    total_rows=100000,
    max_value=1000,
    anomaly_percentage=0.03,
    total_pos_inf=None,
    total_neg_inf=None,
    is_float=False,
    is_pos=False,
)
df4_neg_int_1000_003 = gen_data(
    total_cols=2,
    total_rows=1000000,
    max_value=1000,
    anomaly_percentage=0.03,
    total_pos_inf=None,
    total_neg_inf=None,
    is_float=False,
    is_pos=False,
)
df5_neg_int_1000_003 = gen_data(
    total_cols=2,
    total_rows=10000000,
    max_value=1000,
    anomaly_percentage=0.03,
    total_pos_inf=None,
    total_neg_inf=None,
    is_float=False,
    is_pos=False,
)
df1_neg_int_10000_003 = gen_data(
    total_cols=2,
    total_rows=1000,
    max_value=10000,
    anomaly_percentage=0.03,
    total_pos_inf=None,
    total_neg_inf=None,
    is_float=False,
    is_pos=False,
)
df2_neg_int_10000_003 = gen_data(
    total_cols=2,
    total_rows=10000,
    max_value=10000,
    anomaly_percentage=0.03,
    total_pos_inf=None,
    total_neg_inf=None,
    is_float=False,
    is_pos=False,
)
df3_neg_int_10000_003 = gen_data(
    total_cols=2,
    total_rows=100000,
    max_value=10000,
    anomaly_percentage=0.03,
    total_pos_inf=None,
    total_neg_inf=None,
    is_float=False,
    is_pos=False,
)
df4_neg_int_10000_003 = gen_data(
    total_cols=2,
    total_rows=1000000,
    max_value=10000,
    anomaly_percentage=0.03,
    total_pos_inf=None,
    total_neg_inf=None,
    is_float=False,
    is_pos=False,
)
df5_neg_int_10000_003 = gen_data(
    total_cols=2,
    total_rows=10000000,
    max_value=10000,
    anomaly_percentage=0.03,
    total_pos_inf=None,
    total_neg_inf=None,
    is_float=False,
    is_pos=False,
)

df1_pos_float_1000_003 = gen_data(
    total_cols=2,
    total_rows=1000,
    max_value=1000,
    anomaly_percentage=0.03,
    total_pos_inf=None,
    total_neg_inf=None,
    is_float=True,
    is_pos=True,
)
df2_pos_float_1000_003 = gen_data(
    total_cols=2,
    total_rows=10000,
    max_value=1000,
    anomaly_percentage=0.03,
    total_pos_inf=None,
    total_neg_inf=None,
    is_float=True,
    is_pos=True,
)
df3_pos_float_1000_003 = gen_data(
    total_cols=2,
    total_rows=100000,
    max_value=1000,
    anomaly_percentage=0.03,
    total_pos_inf=None,
    total_neg_inf=None,
    is_float=True,
    is_pos=True,
)
df4_pos_float_1000_003 = gen_data(
    total_cols=2,
    total_rows=1000000,
    max_value=1000,
    anomaly_percentage=0.03,
    total_pos_inf=None,
    total_neg_inf=None,
    is_float=True,
    is_pos=True,
)
df5_pos_float_1000_003 = gen_data(
    total_cols=2,
    total_rows=10000000,
    max_value=1000,
    anomaly_percentage=0.03,
    total_pos_inf=None,
    total_neg_inf=None,
    is_float=True,
    is_pos=True,
)
df1_pos_float_10000_003 = gen_data(
    total_cols=2,
    total_rows=1000,
    max_value=10000,
    anomaly_percentage=0.03,
    total_pos_inf=None,
    total_neg_inf=None,
    is_float=True,
    is_pos=True,
)
df2_pos_float_10000_003 = gen_data(
    total_cols=2,
    total_rows=10000,
    max_value=10000,
    anomaly_percentage=0.03,
    total_pos_inf=None,
    total_neg_inf=None,
    is_float=True,
    is_pos=True,
)
df3_pos_float_10000_003 = gen_data(
    total_cols=2,
    total_rows=100000,
    max_value=10000,
    anomaly_percentage=0.03,
    total_pos_inf=None,
    total_neg_inf=None,
    is_float=True,
    is_pos=True,
)
df4_pos_float_10000_003 = gen_data(
    total_cols=2,
    total_rows=1000000,
    max_value=10000,
    anomaly_percentage=0.03,
    total_pos_inf=None,
    total_neg_inf=None,
    is_float=True,
    is_pos=True,
)
df5_pos_float_10000_003 = gen_data(
    total_cols=2,
    total_rows=10000000,
    max_value=10000,
    anomaly_percentage=0.03,
    total_pos_inf=None,
    total_neg_inf=None,
    is_float=True,
    is_pos=True,
)

df1_neg_float_1000_003 = gen_data(
    total_cols=2,
    total_rows=1000,
    max_value=1000,
    anomaly_percentage=0.03,
    total_pos_inf=None,
    total_neg_inf=None,
    is_float=True,
    is_pos=False,
)
df2_neg_float_1000_003 = gen_data(
    total_cols=2,
    total_rows=10000,
    max_value=1000,
    anomaly_percentage=0.03,
    total_pos_inf=None,
    total_neg_inf=None,
    is_float=True,
    is_pos=False,
)
df3_neg_float_1000_003 = gen_data(
    total_cols=2,
    total_rows=100000,
    max_value=1000,
    anomaly_percentage=0.03,
    total_pos_inf=None,
    total_neg_inf=None,
    is_float=True,
    is_pos=False,
)
df4_neg_float_1000_003 = gen_data(
    total_cols=2,
    total_rows=10000000,
    max_value=1000,
    anomaly_percentage=0.03,
    total_pos_inf=None,
    total_neg_inf=None,
    is_float=True,
    is_pos=False,
)
df5_neg_float_1000_003 = gen_data(
    total_cols=2,
    total_rows=10000000,
    max_value=1000,
    anomaly_percentage=0.03,
    total_pos_inf=None,
    total_neg_inf=None,
    is_float=True,
    is_pos=False,
)
df1_neg_float_10000_003 = gen_data(
    total_cols=2,
    total_rows=1000,
    max_value=10000,
    anomaly_percentage=0.03,
    total_pos_inf=None,
    total_neg_inf=None,
    is_float=True,
    is_pos=False,
)
df2_neg_float_10000_003 = gen_data(
    total_cols=2,
    total_rows=10000,
    max_value=10000,
    anomaly_percentage=0.03,
    total_pos_inf=None,
    total_neg_inf=None,
    is_float=True,
    is_pos=False,
)
df3_neg_float_10000_003 = gen_data(
    total_cols=2,
    total_rows=100000,
    max_value=10000,
    anomaly_percentage=0.03,
    total_pos_inf=None,
    total_neg_inf=None,
    is_float=True,
    is_pos=False,
)
df4_neg_float_10000_003 = gen_data(
    total_cols=2,
    total_rows=10000000,
    max_value=10000,
    anomaly_percentage=0.03,
    total_pos_inf=None,
    total_neg_inf=None,
    is_float=True,
    is_pos=False,
)
df5_neg_float_10000_003 = gen_data(
    total_cols=2,
    total_rows=10000000,
    max_value=10000,
    anomaly_percentage=0.03,
    total_pos_inf=None,
    total_neg_inf=None,
    is_float=True,
    is_pos=False,
)

df1_pos_int_1000_003.to_csv(
    path_or_buf="./tests/datasets/test_dataset1_col_2_row_1000_dtype_int_max_1000_anomaly_003.csv", index=False
)
df2_pos_int_1000_003.to_csv(
    path_or_buf="./tests/datasets/test_dataset2_col_2_row_10000_dtype_int_max_1000_anomaly_003.csv", index=False
)
df3_pos_int_1000_003.to_csv(
    path_or_buf="./tests/datasets/test_dataset3_col_2_row_100000_dtype_int_max_1000_anomaly_003.csv", index=False
)
df4_pos_int_1000_003.to_csv(
    path_or_buf="./tests/datasets/test_dataset4_col_2_row_1000000_dtype_int_max_1000_anomaly_003.csv", index=False
)
df5_pos_int_1000_003.to_csv(
    path_or_buf="./tests/datasets/test_dataset5_col_2_row_10000000_dtype_int_max_1000_anomaly_003.csv", index=False
)
df1_neg_int_1000_003.to_csv(
    path_or_buf="./tests/datasets/test_dataset6_col_2_row_1000_dtype_int_min_1000_anomaly_003.csv", index=False
)
df2_neg_int_1000_003.to_csv(
    path_or_buf="./tests/datasets/test_dataset7_col_2_row_10000_dtype_int_min_1000_anomaly_003.csv", index=False
)
df3_neg_int_1000_003.to_csv(
    path_or_buf="./tests/datasets/test_dataset8_col_2_row_100000_dtype_int_min_1000_anomaly_003.csv", index=False
)
df4_neg_int_1000_003.to_csv(
    path_or_buf="./tests/datasets/test_dataset9_col_2_row_1000000_dtype_int_min_1000_anomaly_003.csv", index=False
)
df5_neg_int_1000_003.to_csv(
    path_or_buf="./tests/datasets/test_dataset10_col_2_row_1000000_dtype_int_min_1000_anomaly_003.csv", index=False
)
df1_pos_float_1000_003.to_csv(
    path_or_buf="./tests/datasets/test_dataset11_row_2_col_1000_dtype_float_max_1000_anomaly_003.csv", index=False
)
df2_pos_float_1000_003.to_csv(
    path_or_buf="./tests/datasets/test_dataset12_row_2_col_10000_dtypefloatt_max_1000_anomaly_003.csv", index=False
)
df3_pos_float_1000_003.to_csv(
    path_or_buf="./tests/datasets/test_dataset13_row_2_col_100000_dtype_float_max_1000_anomaly_003.csv", index=False
)
df4_pos_float_1000_003.to_csv(
    path_or_buf="./tests/datasets/test_dataset14_row_2_row_1000000_dtype_float_max_1000_anomaly_003.csv", index=False
)
df5_pos_float_1000_003.to_csv(
    path_or_buf="./tests/datasets/test_dataset15_col_2_row_10000000_dtype_float_max_1000_anomaly_003.csv", index=False
)
df1_neg_float_1000_003.to_csv(
    path_or_buf="./tests/datasets/test_dataset16_row_2_col_1000_dtype_float_min_1000_anomaly_003.csv", index=False
)
df2_neg_float_1000_003.to_csv(
    path_or_buf="./tests/datasets/test_dataset17_row_2_col_10000_dtype_float_min_1000_anomaly_003.csv", index=False
)
df3_neg_float_1000_003.to_csv(
    path_or_buf="./tests/datasets/test_dataset18_row_2_col_100000_dtype_float_min_1000_anomaly_003.csv", index=False
)
df4_neg_float_1000_003.to_csv(
    path_or_buf="./tests/datasets/test_dataset19_row_2_row_1000000_dtype_float_min_1000_anomaly_003.csv", index=False
)
df5_neg_float_1000_003.to_csv(
    path_or_buf="./tests/datasets/test_dataset20_col_2_row_10000000_dtype_float_min_1000_anomaly_003.csv", index=False
)

df1_pos_int_10000_003.to_csv(
    path_or_buf="./tests/datasets/test_dataset1_col_2_row_1000_dtype_int_max_10000_anomaly_003.csv", index=False
)
df2_pos_int_10000_003.to_csv(
    path_or_buf="./tests/datasets/test_dataset2_col_2_row_10000_dtype_int_max_10000_anomaly_003.csv", index=False
)
df3_pos_int_10000_003.to_csv(
    path_or_buf="./tests/datasets/test_dataset3_col_2_row_100000_dtype_int_max_10000_anomaly_003.csv", index=False
)
df4_pos_int_10000_003.to_csv(
    path_or_buf="./tests/datasets/test_dataset4_col_2_row_1000000_dtype_int_max_10000_anomaly_003.csv", index=False
)
df5_pos_int_10000_003.to_csv(
    path_or_buf="./tests/datasets/test_dataset5_col_2_row_10000000_dtype_int_max_10000_anomaly_003.csv", index=False
)
df1_neg_int_10000_003.to_csv(
    path_or_buf="./tests/datasets/test_dataset6_col_2_row_1000_dtype_int_min_10000_anomaly_003.csv", index=False
)
df2_neg_int_10000_003.to_csv(
    path_or_buf="./tests/datasets/test_dataset7_col_2_row_10000_dtype_int_min_10000_anomaly_003.csv", index=False
)
df3_neg_int_10000_003.to_csv(
    path_or_buf="./tests/datasets/test_dataset8_col_2_row_100000_dtype_int_min_10000_anomaly_003.csv", index=False
)
df4_neg_int_10000_003.to_csv(
    path_or_buf="./tests/datasets/test_dataset9_col_2_row_1000000_dtype_int_min_10000_anomaly_003.csv", index=False
)
df5_neg_int_10000_003.to_csv(
    path_or_buf="./tests/datasets/test_dataset10_col_2_row_1000000_dtype_int_min_10000_anomaly_003.csv", index=False
)
df1_pos_float_10000_003.to_csv(
    path_or_buf="./tests/datasets/test_dataset11_row_2_col_1000_dtype_float_max_10000_anomaly_003.csv", index=False
)
df2_pos_float_10000_003.to_csv(
    path_or_buf="./tests/datasets/test_dataset12_row_2_col_10000_dtypefloatt_max_10000_anomaly_003.csv", index=False
)
df3_pos_float_10000_003.to_csv(
    path_or_buf="./tests/datasets/test_dataset13_row_2_col_100000_dtype_float_max_10000_anomaly_003.csv", index=False
)
df4_pos_float_10000_003.to_csv(
    path_or_buf="./tests/datasets/test_dataset14_row_2_row_1000000_dtype_float_max_10000_anomaly_003.csv", index=False
)
df5_pos_float_10000_003.to_csv(
    path_or_buf="./tests/datasets/test_dataset15_col_2_row_10000000_dtype_float_max_10000_anomaly_003.csv", index=False
)
df1_neg_float_10000_003.to_csv(
    path_or_buf="./tests/datasets/test_dataset16_row_2_col_1000_dtype_float_min_10000_anomaly_003.csv", index=False
)
df2_neg_float_10000_003.to_csv(
    path_or_buf="./tests/datasets/test_dataset17_row_2_col_10000_dtype_float_min_10000_anomaly_003.csv", index=False
)
df3_neg_float_10000_003.to_csv(
    path_or_buf="./tests/datasets/test_dataset18_row_2_col_100000_dtype_float_min_10000_anomaly_003.csv", index=False
)
df4_neg_float_10000_003.to_csv(
    path_or_buf="./tests/datasets/test_dataset19_row_2_row_1000000_dtype_float_min_10000_anomaly_003.csv", index=False
)
df5_neg_float_10000_003.to_csv(
    path_or_buf="./tests/datasets/test_dataset20_col_2_row_10000000_dtype_float_min_10000_anomaly_003.csv", index=False
)

df1_pos_int_1000_01 = gen_data(
    total_cols=2,
    total_rows=1000,
    max_value=1000,
    anomaly_percentage=0.1,
    total_pos_inf=None,
    total_neg_inf=None,
    is_float=False,
    is_pos=True,
)
df2_pos_int_1000_01 = gen_data(
    total_cols=2,
    total_rows=10000,
    max_value=1000,
    anomaly_percentage=0.1,
    total_pos_inf=None,
    total_neg_inf=None,
    is_float=False,
    is_pos=True,
)
df3_pos_int_1000_01 = gen_data(
    total_cols=2,
    total_rows=100000,
    max_value=1000,
    anomaly_percentage=0.1,
    total_pos_inf=None,
    total_neg_inf=None,
    is_float=False,
    is_pos=True,
)
df4_pos_int_1000_01 = gen_data(
    total_cols=2,
    total_rows=1000000,
    max_value=1000,
    anomaly_percentage=0.1,
    total_pos_inf=None,
    total_neg_inf=None,
    is_float=False,
    is_pos=True,
)
df5_pos_int_1000_01 = gen_data(
    total_cols=2,
    total_rows=10000000,
    max_value=1000,
    anomaly_percentage=0.1,
    total_pos_inf=None,
    total_neg_inf=None,
    is_float=False,
    is_pos=True,
)
df1_pos_int_10000_01 = gen_data(
    total_cols=2,
    total_rows=1000,
    max_value=10000,
    anomaly_percentage=0.1,
    total_pos_inf=None,
    total_neg_inf=None,
    is_float=False,
    is_pos=True,
)
df2_pos_int_10000_01 = gen_data(
    total_cols=2,
    total_rows=10000,
    max_value=10000,
    anomaly_percentage=0.1,
    total_pos_inf=None,
    total_neg_inf=None,
    is_float=False,
    is_pos=True,
)
df3_pos_int_10000_01 = gen_data(
    total_cols=2,
    total_rows=100000,
    max_value=10000,
    anomaly_percentage=0.1,
    total_pos_inf=None,
    total_neg_inf=None,
    is_float=False,
    is_pos=True,
)
df4_pos_int_10000_01 = gen_data(
    total_cols=2,
    total_rows=1000000,
    max_value=10000,
    anomaly_percentage=0.1,
    total_pos_inf=None,
    total_neg_inf=None,
    is_float=False,
    is_pos=True,
)
df5_pos_int_10000_01 = gen_data(
    total_cols=2,
    total_rows=10000000,
    max_value=10000,
    anomaly_percentage=0.1,
    total_pos_inf=None,
    total_neg_inf=None,
    is_float=False,
    is_pos=True,
)

df1_neg_int_1000_01 = gen_data(
    total_cols=2,
    total_rows=1000,
    max_value=1000,
    anomaly_percentage=0.1,
    total_pos_inf=None,
    total_neg_inf=None,
    is_float=False,
    is_pos=False,
)
df2_neg_int_1000_01 = gen_data(
    total_cols=2,
    total_rows=10000,
    max_value=1000,
    anomaly_percentage=0.1,
    total_pos_inf=None,
    total_neg_inf=None,
    is_float=False,
    is_pos=False,
)
df3_neg_int_1000_01 = gen_data(
    total_cols=2,
    total_rows=100000,
    max_value=1000,
    anomaly_percentage=0.1,
    total_pos_inf=None,
    total_neg_inf=None,
    is_float=False,
    is_pos=False,
)
df4_neg_int_1000_01 = gen_data(
    total_cols=2,
    total_rows=1000000,
    max_value=1000,
    anomaly_percentage=0.1,
    total_pos_inf=None,
    total_neg_inf=None,
    is_float=False,
    is_pos=False,
)
df5_neg_int_1000_01 = gen_data(
    total_cols=2,
    total_rows=10000000,
    max_value=1000,
    anomaly_percentage=0.1,
    total_pos_inf=None,
    total_neg_inf=None,
    is_float=False,
    is_pos=False,
)
df1_neg_int_10000_01 = gen_data(
    total_cols=2,
    total_rows=1000,
    max_value=10000,
    anomaly_percentage=0.1,
    total_pos_inf=None,
    total_neg_inf=None,
    is_float=False,
    is_pos=False,
)
df2_neg_int_10000_01 = gen_data(
    total_cols=2,
    total_rows=10000,
    max_value=10000,
    anomaly_percentage=0.1,
    total_pos_inf=None,
    total_neg_inf=None,
    is_float=False,
    is_pos=False,
)
df3_neg_int_10000_01 = gen_data(
    total_cols=2,
    total_rows=100000,
    max_value=10000,
    anomaly_percentage=0.1,
    total_pos_inf=None,
    total_neg_inf=None,
    is_float=False,
    is_pos=False,
)
df4_neg_int_10000_01 = gen_data(
    total_cols=2,
    total_rows=1000000,
    max_value=10000,
    anomaly_percentage=0.1,
    total_pos_inf=None,
    total_neg_inf=None,
    is_float=False,
    is_pos=False,
)
df5_neg_int_10000_01 = gen_data(
    total_cols=2,
    total_rows=10000000,
    max_value=10000,
    anomaly_percentage=0.1,
    total_pos_inf=None,
    total_neg_inf=None,
    is_float=False,
    is_pos=False,
)

df1_pos_float_1000_01 = gen_data(
    total_cols=2,
    total_rows=1000,
    max_value=1000,
    anomaly_percentage=0.1,
    total_pos_inf=None,
    total_neg_inf=None,
    is_float=True,
    is_pos=True,
)
df2_pos_float_1000_01 = gen_data(
    total_cols=2,
    total_rows=10000,
    max_value=1000,
    anomaly_percentage=0.1,
    total_pos_inf=None,
    total_neg_inf=None,
    is_float=True,
    is_pos=True,
)
df3_pos_float_1000_01 = gen_data(
    total_cols=2,
    total_rows=100000,
    max_value=1000,
    anomaly_percentage=0.1,
    total_pos_inf=None,
    total_neg_inf=None,
    is_float=True,
    is_pos=True,
)
df4_pos_float_1000_01 = gen_data(
    total_cols=2,
    total_rows=1000000,
    max_value=1000,
    anomaly_percentage=0.1,
    total_pos_inf=None,
    total_neg_inf=None,
    is_float=True,
    is_pos=True,
)
df5_pos_float_1000_01 = gen_data(
    total_cols=2,
    total_rows=10000000,
    max_value=1000,
    anomaly_percentage=0.1,
    total_pos_inf=None,
    total_neg_inf=None,
    is_float=True,
    is_pos=True,
)
df1_pos_float_10000_01 = gen_data(
    total_cols=2,
    total_rows=1000,
    max_value=10000,
    anomaly_percentage=0.1,
    total_pos_inf=None,
    total_neg_inf=None,
    is_float=True,
    is_pos=True,
)
df2_pos_float_10000_01 = gen_data(
    total_cols=2,
    total_rows=10000,
    max_value=10000,
    anomaly_percentage=0.1,
    total_pos_inf=None,
    total_neg_inf=None,
    is_float=True,
    is_pos=True,
)
df3_pos_float_10000_01 = gen_data(
    total_cols=2,
    total_rows=100000,
    max_value=10000,
    anomaly_percentage=0.1,
    total_pos_inf=None,
    total_neg_inf=None,
    is_float=True,
    is_pos=True,
)
df4_pos_float_10000_01 = gen_data(
    total_cols=2,
    total_rows=1000000,
    max_value=10000,
    anomaly_percentage=0.1,
    total_pos_inf=None,
    total_neg_inf=None,
    is_float=True,
    is_pos=True,
)
df5_pos_float_10000_01 = gen_data(
    total_cols=2,
    total_rows=10000000,
    max_value=10000,
    anomaly_percentage=0.1,
    total_pos_inf=None,
    total_neg_inf=None,
    is_float=True,
    is_pos=True,
)

df1_neg_float_1000_01 = gen_data(
    total_cols=2,
    total_rows=1000,
    max_value=1000,
    anomaly_percentage=0.1,
    total_pos_inf=None,
    total_neg_inf=None,
    is_float=True,
    is_pos=False,
)
df2_neg_float_1000_01 = gen_data(
    total_cols=2,
    total_rows=10000,
    max_value=1000,
    anomaly_percentage=0.1,
    total_pos_inf=None,
    total_neg_inf=None,
    is_float=True,
    is_pos=False,
)
df3_neg_float_1000_01 = gen_data(
    total_cols=2,
    total_rows=100000,
    max_value=1000,
    anomaly_percentage=0.1,
    total_pos_inf=None,
    total_neg_inf=None,
    is_float=True,
    is_pos=False,
)
df4_neg_float_1000_01 = gen_data(
    total_cols=2,
    total_rows=10000000,
    max_value=1000,
    anomaly_percentage=0.1,
    total_pos_inf=None,
    total_neg_inf=None,
    is_float=True,
    is_pos=False,
)
df5_neg_float_1000_01 = gen_data(
    total_cols=2,
    total_rows=10000000,
    max_value=1000,
    anomaly_percentage=0.1,
    total_pos_inf=None,
    total_neg_inf=None,
    is_float=True,
    is_pos=False,
)
df1_neg_float_10000_01 = gen_data(
    total_cols=2,
    total_rows=1000,
    max_value=10000,
    anomaly_percentage=0.1,
    total_pos_inf=None,
    total_neg_inf=None,
    is_float=True,
    is_pos=False,
)
df2_neg_float_10000_01 = gen_data(
    total_cols=2,
    total_rows=10000,
    max_value=10000,
    anomaly_percentage=0.1,
    total_pos_inf=None,
    total_neg_inf=None,
    is_float=True,
    is_pos=False,
)
df3_neg_float_10000_01 = gen_data(
    total_cols=2,
    total_rows=100000,
    max_value=10000,
    anomaly_percentage=0.1,
    total_pos_inf=None,
    total_neg_inf=None,
    is_float=True,
    is_pos=False,
)
df4_neg_float_10000_01 = gen_data(
    total_cols=2,
    total_rows=10000000,
    max_value=10000,
    anomaly_percentage=0.1,
    total_pos_inf=None,
    total_neg_inf=None,
    is_float=True,
    is_pos=False,
)
df5_neg_float_10000_01 = gen_data(
    total_cols=2,
    total_rows=10000000,
    max_value=10000,
    anomaly_percentage=0.1,
    total_pos_inf=None,
    total_neg_inf=None,
    is_float=True,
    is_pos=False,
)

df1_pos_int_1000_01.to_csv(
    path_or_buf="./tests/datasets/test_dataset1_col_2_row_1000_dtype_int_max_1000_anomaly_01.csv", index=False
)
df2_pos_int_1000_01.to_csv(
    path_or_buf="./tests/datasets/test_dataset2_col_2_row_10000_dtype_int_max_1000_anomaly_01.csv", index=False
)
df3_pos_int_1000_01.to_csv(
    path_or_buf="./tests/datasets/test_dataset3_col_2_row_100000_dtype_int_max_1000_anomaly_01.csv", index=False
)
df4_pos_int_1000_01.to_csv(
    path_or_buf="./tests/datasets/test_dataset4_col_2_row_1000000_dtype_int_max_1000_anomaly_01.csv", index=False
)
df5_pos_int_1000_01.to_csv(
    path_or_buf="./tests/datasets/test_dataset5_col_2_row_10000000_dtype_int_max_1000_anomaly_01.csv", index=False
)
df1_neg_int_1000_01.to_csv(
    path_or_buf="./tests/datasets/test_dataset6_col_2_row_1000_dtype_int_min_1000_anomaly_01.csv", index=False
)
df2_neg_int_1000_01.to_csv(
    path_or_buf="./tests/datasets/test_dataset7_col_2_row_10000_dtype_int_min_1000_anomaly_01.csv", index=False
)
df3_neg_int_1000_01.to_csv(
    path_or_buf="./tests/datasets/test_dataset8_col_2_row_100000_dtype_int_min_1000_anomaly_01.csv", index=False
)
df4_neg_int_1000_01.to_csv(
    path_or_buf="./tests/datasets/test_dataset9_col_2_row_1000000_dtype_int_min_1000_anomaly_01.csv", index=False
)
df5_neg_int_1000_01.to_csv(
    path_or_buf="./tests/datasets/test_dataset10_col_2_row_1000000_dtype_int_min_1000_anomaly_01.csv", index=False
)
df1_pos_float_1000_01.to_csv(
    path_or_buf="./tests/datasets/test_dataset11_row_2_col_1000_dtype_float_max_1000_anomaly_01.csv", index=False
)
df2_pos_float_1000_01.to_csv(
    path_or_buf="./tests/datasets/test_dataset12_row_2_col_10000_dtypefloatt_max_1000_anomaly_01.csv", index=False
)
df3_pos_float_1000_01.to_csv(
    path_or_buf="./tests/datasets/test_dataset13_row_2_col_100000_dtype_float_max_1000_anomaly_01.csv", index=False
)
df4_pos_float_1000_01.to_csv(
    path_or_buf="./tests/datasets/test_dataset14_row_2_row_1000000_dtype_float_max_1000_anomaly_01.csv", index=False
)
df5_pos_float_1000_01.to_csv(
    path_or_buf="./tests/datasets/test_dataset15_col_2_row_10000000_dtype_float_max_1000_anomaly_01.csv", index=False
)
df1_neg_float_1000_01.to_csv(
    path_or_buf="./tests/datasets/test_dataset16_row_2_col_1000_dtype_float_min_1000_anomaly_01.csv", index=False
)
df2_neg_float_1000_01.to_csv(
    path_or_buf="./tests/datasets/test_dataset17_row_2_col_10000_dtype_float_min_1000_anomaly_01.csv", index=False
)
df3_neg_float_1000_01.to_csv(
    path_or_buf="./tests/datasets/test_dataset18_row_2_col_100000_dtype_float_min_1000_anomaly_01.csv", index=False
)
df4_neg_float_1000_01.to_csv(
    path_or_buf="./tests/datasets/test_dataset19_row_2_row_1000000_dtype_float_min_1000_anomaly_01.csv", index=False
)
df5_neg_float_1000_01.to_csv(
    path_or_buf="./tests/datasets/test_dataset20_col_2_row_10000000_dtype_float_min_1000_anomaly_01.csv", index=False
)

df1_pos_int_10000_01.to_csv(
    path_or_buf="./tests/datasets/test_dataset1_col_2_row_1000_dtype_int_max_10000_anomaly_01.csv", index=False
)
df2_pos_int_10000_01.to_csv(
    path_or_buf="./tests/datasets/test_dataset2_col_2_row_10000_dtype_int_max_10000_anomaly_01.csv", index=False
)
df3_pos_int_10000_01.to_csv(
    path_or_buf="./tests/datasets/test_dataset3_col_2_row_100000_dtype_int_max_10000_anomaly_01.csv", index=False
)
df4_pos_int_10000_01.to_csv(
    path_or_buf="./tests/datasets/test_dataset4_col_2_row_1000000_dtype_int_max_10000_anomaly_01.csv", index=False
)
df5_pos_int_10000_01.to_csv(
    path_or_buf="./tests/datasets/test_dataset5_col_2_row_10000000_dtype_int_max_10000_anomaly_01.csv", index=False
)
df1_neg_int_10000_01.to_csv(
    path_or_buf="./tests/datasets/test_dataset6_col_2_row_1000_dtype_int_min_10000_anomaly_01.csv", index=False
)
df2_neg_int_10000_01.to_csv(
    path_or_buf="./tests/datasets/test_dataset7_col_2_row_10000_dtype_int_min_10000_anomaly_01.csv", index=False
)
df3_neg_int_10000_01.to_csv(
    path_or_buf="./tests/datasets/test_dataset8_col_2_row_100000_dtype_int_min_10000_anomaly_01.csv", index=False
)
df4_neg_int_10000_01.to_csv(
    path_or_buf="./tests/datasets/test_dataset9_col_2_row_1000000_dtype_int_min_10000_anomaly_01.csv", index=False
)
df5_neg_int_10000_01.to_csv(
    path_or_buf="./tests/datasets/test_dataset10_col_2_row_1000000_dtype_int_min_10000_anomaly_01.csv", index=False
)
df1_pos_float_10000_01.to_csv(
    path_or_buf="./tests/datasets/test_dataset11_row_2_col_1000_dtype_float_max_10000_anomaly_01.csv", index=False
)
df2_pos_float_10000_01.to_csv(
    path_or_buf="./tests/datasets/test_dataset12_row_2_col_10000_dtypefloatt_max_10000_anomaly_01.csv", index=False
)
df3_pos_float_10000_01.to_csv(
    path_or_buf="./tests/datasets/test_dataset13_row_2_col_100000_dtype_float_max_10000_anomaly_01.csv", index=False
)
df4_pos_float_10000_01.to_csv(
    path_or_buf="./tests/datasets/test_dataset14_row_2_row_1000000_dtype_float_max_10000_anomaly_01.csv", index=False
)
df5_pos_float_10000_01.to_csv(
    path_or_buf="./tests/datasets/test_dataset15_col_2_row_10000000_dtype_float_max_10000_anomaly_01.csv", index=False
)
df1_neg_float_10000_01.to_csv(
    path_or_buf="./tests/datasets/test_dataset16_row_2_col_1000_dtype_float_min_10000_anomaly_01.csv", index=False
)
df2_neg_float_10000_01.to_csv(
    path_or_buf="./tests/datasets/test_dataset17_row_2_col_10000_dtype_float_min_10000_anomaly_01.csv", index=False
)
df3_neg_float_10000_01.to_csv(
    path_or_buf="./tests/datasets/test_dataset18_row_2_col_100000_dtype_float_min_10000_anomaly_01.csv", index=False
)
df4_neg_float_10000_01.to_csv(
    path_or_buf="./tests/datasets/test_dataset19_row_2_row_1000000_dtype_float_min_10000_anomaly_01.csv", index=False
)
df5_neg_float_10000_01.to_csv(
    path_or_buf="./tests/datasets/test_dataset20_col_2_row_10000000_dtype_float_min_10000_anomaly_01.csv", index=False
)
