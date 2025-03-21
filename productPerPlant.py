import pandas as pd

# Load the full CSV file
df = pd.read_csv("ProductsPerPlant-Table 1.csv")

def clean_full_dataframe(df):
    # Drop columns that are completely NaN
    df.dropna(axis=1, how='all', inplace=True)

    # Drop rows that are completely NaN
    df.dropna(axis=0, how='all', inplace=True)

    # Strip whitespaces from column names
    df.columns = df.columns.str.strip()

    # If column names or values need standardization:
    df.columns = df.columns.str.replace(" ", "_").str.upper()

    # Remove leading/trailing whitespaces from string data
    df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

    # Drop rows where essential columns are missing (customize if needed)
    essential_columns = [col for col in df.columns if "PLANT" in col or "PRODUCT" in col]
    df.dropna(subset=essential_columns, inplace=True)

    # Remove duplicates (optional)
    df.drop_duplicates(inplace=True)

    return df

# Clean the full dataset
cleaned_df = clean_full_dataframe(df)

# Save the cleaned dataset
cleaned_df.to_csv("cleaned_products_per_plant_FULL.csv", index=False)
