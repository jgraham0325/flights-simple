"""Shared Python functions for transformations."""

from pyspark.sql.functions import current_date, current_timestamp, lit


def add_metadata_columns(df, include_time=True):
    if include_time:
        df = df.withColumn("last_updated_time", current_timestamp())
    else:
        df = df.withColumn("last_updated_date", current_date())

    df = df.withColumn("source_project", lit("flights_simple"))

    return df
