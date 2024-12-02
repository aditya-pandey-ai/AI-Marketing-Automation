def calculate_metrics(row):
    ctr = row["Clicks"] / row["Impressions"] if row["Impressions"] > 0 else 0
    cpa = row["Spend"] / row["Conversions"] if row["Conversions"] > 0 else float("inf")
    roas = row["Revenue"] / row["Spend"] if row["Spend"] > 0 else 0
    return {"CTR": ctr, "CPA": cpa, "ROAS": roas}
