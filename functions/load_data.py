import pandas as pd
from sklearn.preprocessing import MinMaxScaler


def load_campaign_data(file_path):
    """
    Load and preprocess campaign data from a CSV file.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Preprocessed campaign data.
    """
    # Load the data
    df = pd.read_csv(file_path)

    # Handle missing values
    num_cols = df.select_dtypes(include=["float64", "int64"]).columns
    df[num_cols] = df[num_cols].fillna(df[num_cols].median())

    # Fill categorical columns with their mode
    cat_cols = df.select_dtypes(include=["object"]).columns
    df[cat_cols] = df[cat_cols].fillna(df[cat_cols].mode().iloc[0])

    # Normalize numerical metrics
    scaler = MinMaxScaler()
    df[num_cols] = scaler.fit_transform(df[num_cols])

    # Add derived metrics
    if "Spend" in df.columns and "Revenue" in df.columns:
        df["ROAS"] = df["Revenue"] / df["Spend"]
        df["ROAS"] = df["ROAS"].fillna(0)  # Handle division by zero

    return df


if __name__ == "__main__":

    file_path = "data/synthetic_campaign_data.csv"
    campaign_df = load_campaign_data(file_path)
    print(campaign_df.head())
