import pandas as pd

# Load the full FreightRates CSV
df = pd.read_csv("FreightRates-Table 1.csv")

def clean_freight_rates(df):
    # Drop columns that are entirely NaN
    df.dropna(axis=1, how='all', inplace=True)

    # Drop rows that are entirely NaN
    df.dropna(axis=0, how='all', inplace=True)

    # Strip whitespaces from column names
    df.columns = df.columns.str.strip()

    # Standardize column names (uppercase, underscores instead of spaces)
    df.columns = df.columns.str.replace(" ", "_").str.upper()

    # Remove leading/trailing whitespaces from each cell
    df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

    # Optionally drop rows missing critical fields (customize as needed)
    essential_columns = [col for col in df.columns if "PORT" in col or "PLANT" in col or "FREIGHT" in col]
    df.dropna(subset=essential_columns, inplace=True)

    # Drop duplicates if any
    df.drop_duplicates(inplace=True)

    return df

# Clean the freight rates dataset
cleaned_freight_df = clean_freight_rates(df)

# Save the cleaned version
cleaned_freight_df.to_csv("cleaned_freight_rates_FULL.csv", index=False)

print("✅ Freight Rates CSV cleaned and saved as 'cleaned_freight_rates_FULL.csv'")
