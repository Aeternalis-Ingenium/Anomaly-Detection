from pandas import DataFrame, Series


def calculate_peak_over_threshold(df: DataFrame, features: list[str], min_period: int, quantile: float) -> DataFrame:
    for feature in features:
        df[f"pot_th_{feature}"] = (
            df[feature]
            .expanding(min_periods=min_period)
            .apply(lambda x: Series(x).quantile(quantile), raw=True)
            .shift()
            .bfill()
        )
    return df


def get_data_over_threshold(df: DataFrame, features: list[str]) -> DataFrame:
    for feature in features:
        df[f"pot_data_{feature}"] = (df[feature] - df[f"pot_th_{feature}"]).clip(0, None)
    return df
