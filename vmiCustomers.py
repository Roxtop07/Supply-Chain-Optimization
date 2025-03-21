import pandas as pd

# Load the VMI Customers CSV
df = pd.read_csv("VmiCustomers-Table 1.csv")

def clean_vmi_customers(df):
    # Drop columns that are entirely NaN
    df.dropna(axis=1, how='all', inplace=True)

    # Drop rows that are entirely NaN
    df.dropna(axis=0, how='all', inplace=True)

    # Clean and standardize column headers
    df.columns = df.columns.str.strip().str.replace(" ", "_").str.upper()

    # Strip leading/trailing whitespace from all string fields
    df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

    # Drop rows where critical fields are missing (customize as per your columns)
    essential_columns = [col for col in df.columns if "CUSTOMER" in col or "PORT" in col or "PLANT" in col]
    df.dropna(subset=essential_columns, inplace=True)

    # Drop duplicate rows if any
    df.drop_duplicates(inplace=True)

    return df

# Clean the VMI Customers dataset
cleaned_vmi_df = clean_vmi_customers(df)

# Save the cleaned CSV
cleaned_vmi_df.to_csv("cleaned_vmi_customers_FULL.csv", index=False)

print("✅ VMI Customers CSV cleaned and saved as 'cleaned_vmi_customers_FULL.csv'")
