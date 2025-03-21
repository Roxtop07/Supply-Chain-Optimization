import pandas as pd

# Load the WH Capacities CSV
df = pd.read_csv("WhCapacities-Table 1.csv")

def clean_wh_capacities(df):
    # Drop columns that are entirely NaN
    df.dropna(axis=1, how='all', inplace=True)

    # Drop rows that are entirely NaN
    df.dropna(axis=0, how='all', inplace=True)

    # Clean and standardize column headers
    df.columns = df.columns.str.strip().str.replace(" ", "_").str.upper()

    # Strip leading/trailing whitespace from all string-type fields
    df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

    # Drop rows where essential values (e.g., warehouse, plant code, or capacity) are missing
    essential_columns = [col for col in df.columns if "PLANT" in col or "CAPACITY" in col or "WAREHOUSE" in col]
    df.dropna(subset=essential_columns, inplace=True)

    # Drop duplicates, if any
    df.drop_duplicates(inplace=True)

    return df

# Clean the WH Capacities dataset
cleaned_wh_df = clean_wh_capacities(df)

# Save the cleaned CSV
cleaned_wh_df.to_csv("cleaned_wh_capacities_FULL.csv", index=False)

print("✅ Warehouse Capacities CSV cleaned and saved as 'cleaned_wh_capacities_FULL.csv'")
