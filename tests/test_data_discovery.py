import pandas as pd

from src.data_discovery import check_foreign_key


def test_check_foreign_key_returns_zero_when_all_keys_match():
    child_df = pd.DataFrame({
        "customer_id": ["C001", "C002"]
    })

    parent_df = pd.DataFrame({
        "customer_id": ["C001", "C002", "C003"]
    })

    result = check_foreign_key(
        child_df,
        "customer_id",
        parent_df,
        "customer_id",
    )

    assert result == 0


def test_check_foreign_key_counts_unmatched_keys():
    child_df = pd.DataFrame({
        "customer_id": ["C001", "C999", "C002"]
    })

    parent_df = pd.DataFrame({
        "customer_id": ["C001", "C002"]
    })

    result = check_foreign_key(
        child_df,
        "customer_id",
        parent_df,
        "customer_id",
    )

    assert result == 1
