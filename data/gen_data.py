import pandas as pd
import numpy as np

# Parameters for synthetic dataset
num_campaigns = 100
np.random.seed(42)

# Generate synthetic data
campaign_data = {
    "campaign_id": [f"CAMP_{i+1:03}" for i in range(num_campaigns)],
    "impressions": np.random.randint(1000, 100000, size=num_campaigns),
    "clicks": np.random.randint(10, 5000, size=num_campaigns),
    "conversions": np.random.randint(0, 100, size=num_campaigns),
    "spend": np.round(np.random.uniform(10, 5000, size=num_campaigns), 2),
    "revenue": np.round(np.random.uniform(0, 10000, size=num_campaigns), 2),
    "status": np.random.choice(["Active", "Paused"], size=num_campaigns, p=[0.8, 0.2])
}

# Ensure logical consistency: Clicks <= Impressions, Revenue >= Spend
campaign_data["clicks"] = np.minimum(campaign_data["clicks"], campaign_data["impressions"])
campaign_data["revenue"] = np.maximum(campaign_data["revenue"], campaign_data["spend"])

# Convert to DataFrame
campaign_df = pd.DataFrame(campaign_data)

# Save to CSV with standardized column names
campaign_df.to_csv("synthetic_campaign_data.csv", index=False)
