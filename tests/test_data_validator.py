# tests/test_data_validator.py

import pytest

from src import validate_dataframe


def test_validate_dataframe_removes_invalid_ratings(sample_df):
    # TODO: Set the required and numeric column names.
    # TODO: Call validate_dataframe().
    # TODO: Assert that 98 rows remain and all five columns are preserved.
    required_columns = sample_df.columns.tolist()
    numeric_columns = ["rating"]

    result = validate_dataframe(
        sample_df.copy(),
        required_columns=required_columns,
        numeric_columns=numeric_columns,
    )

    assert len(result) == 98
    assert list(result.columns) == list(sample_df.columns)

def test_validate_dataframe_with_missing_column(sample_df):
    # TODO: Set required_columns to include a nonexistent column.
    # TODO: Use pytest.raises(ValueError) around validate_dataframe().
    required_columns = ["column_that_does_not_exist"]
    numeric_columns = ["rating"]

    with pytest.raises(ValueError):
        validate_dataframe(
            sample_df.copy(),
            required_columns=required_columns,
            numeric_columns=numeric_columns,
        )