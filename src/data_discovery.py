import pandas as pd


def check_foreign_key(
    child_df: pd.DataFrame,
    child_column: str,
    parent_df: pd.DataFrame,
    parent_column: str,
) -> int:
    child_keys = child_df[child_column]
    parent_keys = parent_df[parent_column].dropna()

    missing_keys = child_keys.notna() & ~child_keys.isin(parent_keys)
    unmatched_count = int(missing_keys.sum())

    print(f"Foreign Key: {child_column} -> {parent_column}")
    print(f"Rows with unmatched keys: {unmatched_count}")

    return unmatched_count
