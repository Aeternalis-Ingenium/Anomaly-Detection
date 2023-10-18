from os import listdir
from random import shuffle
from typing import Literal

from pandas import DataFrame, read_csv


def get_test_dataset(
    dtype: Literal[
        "int",
        "float",
    ],
    total_rows: Literal[
        "row_1000_",
        "row_10000_",
        "row_100000_",
        "row_1000000_",
        "row_10000000_",
    ],
    vals: Literal[
        "min_1000_",
        "min_10000_",
        "max_1000_",
        "max_10000_",
    ],
    anomaly_percentage: Literal[
        "anomaly_003",
        "anomaly_01",
    ],
) -> str:
    test_dataset_path = "tests/datasets/"
    for filename in listdir(test_dataset_path):
        if dtype in filename and total_rows in filename and vals in filename and anomaly_percentage in filename:
            return test_dataset_path + filename
    return "File doesn't exist!"


def init_test_df(
    dtype: Literal["int", "float"],
    total_rows: Literal[
        "row_1000_",
        "row_10000_",
        "row_100000_",
        "row_1000000_",
        "row_10000000_",
    ],
    vals: Literal[
        "min_1000_",
        "min_10000_",
        "max_1000_",
        "max_10000_",
    ],
    anomaly_percentage: Literal[
        "anomaly_003",
        "anomaly_01",
    ],
    is_shuffled: bool = False,
) -> DataFrame:
    test_dataset = get_test_dataset(
        dtype=dtype,
        total_rows=total_rows,
        vals=vals,
        anomaly_percentage=anomaly_percentage,
    )
    df = read_csv(filepath_or_buffer=test_dataset)
    if is_shuffled:
        for feature in df.columns:
            shuffle(df[feature].values)
    return df


test_df_int_row1000_max1000_a003 = init_test_df(
    dtype="int", total_rows="row_1000_", vals="max_1000_", anomaly_percentage="anomaly_003", is_shuffled=False
)
test_df_int_row10000_max1000_a003 = init_test_df(
    dtype="int", total_rows="row_10000_", vals="max_1000_", anomaly_percentage="anomaly_003", is_shuffled=False
)
test_df_int_row100000_max1000_a003 = init_test_df(
    dtype="int", total_rows="row_100000_", vals="max_1000_", anomaly_percentage="anomaly_003", is_shuffled=False
)
test_df_int_row1000000_max1000_a003 = init_test_df(
    dtype="int", total_rows="row_1000000_", vals="max_1000_", anomaly_percentage="anomaly_003", is_shuffled=False
)
test_df_int_row10000000_max1000_a003 = init_test_df(
    dtype="int", total_rows="row_1000_", vals="max_1000_", anomaly_percentage="anomaly_003", is_shuffled=False
)

test_df_int_row1000_max1000_a01 = init_test_df(
    dtype="int", total_rows="row_1000_", vals="max_1000_", anomaly_percentage="anomaly_01", is_shuffled=False
)
test_df_int_row10000_max1000_a01 = init_test_df(
    dtype="int", total_rows="row_10000_", vals="max_1000_", anomaly_percentage="anomaly_01", is_shuffled=False
)
test_df_int_row100000_max1000_a01 = init_test_df(
    dtype="int", total_rows="row_100000_", vals="max_1000_", anomaly_percentage="anomaly_01", is_shuffled=False
)
test_df_int_row1000000_max1000_a01 = init_test_df(
    dtype="int", total_rows="row_1000000_", vals="max_1000_", anomaly_percentage="anomaly_01", is_shuffled=False
)
test_df_int_row10000000_max1000_a01 = init_test_df(
    dtype="int", total_rows="row_1000_", vals="max_1000_", anomaly_percentage="anomaly_01", is_shuffled=False
)

test_df_int_row1000_max1000_a003_sd = init_test_df(
    dtype="int", total_rows="row_1000_", vals="max_1000_", anomaly_percentage="anomaly_003", is_shuffled=True
)
test_df_int_row10000_max1000_a003_sd = init_test_df(
    dtype="int", total_rows="row_10000_", vals="max_1000_", anomaly_percentage="anomaly_003", is_shuffled=True
)
test_df_int_row100000_max1000_a003_sd = init_test_df(
    dtype="int", total_rows="row_100000_", vals="max_1000_", anomaly_percentage="anomaly_003", is_shuffled=True
)
test_df_int_row1000000_max1000_a003_sd = init_test_df(
    dtype="int", total_rows="row_1000000_", vals="max_1000_", anomaly_percentage="anomaly_003", is_shuffled=True
)
test_df_int_row10000000_max1000_a003_sd = init_test_df(
    dtype="int", total_rows="row_1000_", vals="max_1000_", anomaly_percentage="anomaly_003", is_shuffled=True
)

test_df_int_row1000_max1000_a01_sd = init_test_df(
    dtype="int", total_rows="row_1000_", vals="max_1000_", anomaly_percentage="anomaly_01", is_shuffled=True
)
test_df_int_row10000_max1000_a01_sd = init_test_df(
    dtype="int", total_rows="row_10000_", vals="max_1000_", anomaly_percentage="anomaly_01", is_shuffled=True
)
test_df_int_row100000_max1000_a01_sd = init_test_df(
    dtype="int", total_rows="row_100000_", vals="max_1000_", anomaly_percentage="anomaly_01", is_shuffled=True
)
test_df_int_row1000000_max1000_a01_sd = init_test_df(
    dtype="int", total_rows="row_1000000_", vals="max_1000_", anomaly_percentage="anomaly_01", is_shuffled=True
)
test_df_int_row10000000_max1000_a01_sd = init_test_df(
    dtype="int", total_rows="row_1000_", vals="max_1000_", anomaly_percentage="anomaly_01", is_shuffled=True
)
