import pandas as pd

# Load the WH Costs CSV
df = pd.read_csv("WhCosts-Table 1.csv")

def clean_wh_costs(df):
    # Drop columns that are entirely NaN
    df.dropna(axis=1, how='all', inplace=True)

    # Drop rows that are entirely NaN
    df.dropna(axis=0, how='all', inplace=True)

    # Clean and standardize column headers
    df.columns = df.columns.str.strip().str.replace(" ", "_").str.upper()

    # Strip extra whitespaces from all string fields
    df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

    # Drop rows with missing critical fields
    essential_columns = [col for col in df.columns if "PLANT" in col or "WAREHOUSE" in col or "COST" in col]
    df.dropna(subset=essential_columns, inplace=True)

    # Drop duplicates, if any
    df.drop_duplicates(inplace=True)

    return df

# Clean the WH Costs dataset
cleaned_wh_costs_df = clean_wh_costs(df)

# Save the cleaned CSV
cleaned_wh_costs_df.to_csv("cleaned_wh_costs_FULL.csv", index=False)

print("✅ Warehouse Costs CSV cleaned and saved as 'cleaned_wh_costs_FULL.csv'")