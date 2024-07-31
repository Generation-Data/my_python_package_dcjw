import pandas as pd
import pytest
from analytics.turnout_tier_categorization import add_turnout_tier

def test_add_turnout_tier():
    # Example DataFrame
    data = {
        'vb_tsmart_midterm_general_turnout_score': [85, 75, 60, 45, 25, 95, 5]
    }
    df = pd.DataFrame(data)

    # Expected result
    expected_tiers = [
        "Very likely to vote regardless of campaign", 
        "Turnout Tier 1",
        "Turnout Tier 2",
        "Turnout Tier 3",
        "Very unlikely to vote regardless of campaign",
        "Very likely to vote regardless of campaign",
        "Very unlikely to vote regardless of campaign"
    ]

    # Apply the function
    result_df = add_turnout_tier(df, 'vb_tsmart_midterm_general_turnout_score')

    # Check the results
    assert 'turnout_tier' in result_df.columns, "Column 'turnout_tier' not found in the result DataFrame"
    assert result_df['turnout_tier'].tolist() == expected_tiers, "The 'turnout_tier' column values are not as expected"

if __name__ == "__main__":
    pytest.main()

