import pandas as pd

# Load the OrderList sheet
orders_df = pd.read_excel("SCL_Data.xlsx", sheet_name="PlantPorts")


def clean_orders(df):
    # Handle missing values
    df.dropna(subset=["Plant Code", "Port"], inplace=True)

    # Standardize text columns
    df["Plant Code"] = df["Plant Code"].str.upper().str.strip()
    df["Port"] = df["Port"].str.upper().str.strip()

    # Validate numeric fields
    df = df[(df["Unit quantity"] > 0) & (df["Weight"] > 0)]

    # Fix dates
    df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")
    df = df[df["Order Date"].notnull()]

    # Remove duplicates
    df.drop_duplicates(subset="Order ID", keep="first", inplace=True)

    return df


cleaned_orders = clean_orders(orders_df.copy())

# List valid plant-port pairs from the OrderList data
valid_plant_port = cleaned_orders.groupby(["Plant Code", "Origin Port"]).size().reset_index()
print("Valid Plant-Port Relationships:")
print(valid_plant_port[["Plant Code", "Origin Port"]])

cleaned_orders.to_csv("cleaned_orders.csv", index=False)
import pandas as pd

# Load the PlantPorts CSV
plant_ports_df = pd.read_csv("PlantPorts-Table 1.csv")

def clean_plant_ports(df):
    # Strip column names and convert them to consistent format
    df.columns = df.columns.str.strip()

    # Remove all columns that contain any NaN values
    df.dropna(axis=1, inplace=True)

    # Drop rows with missing crucial values (just in case)
    df.dropna(subset=["Plant Code", "Port"], inplace=True)

    # Standardize text fields
    df["Plant Code"] = df["Plant Code"].astype(str).str.strip().str.upper()
    df["Port"] = df["Port"].astype(str).str.strip().str.upper()

    # Remove duplicates
    df.drop_duplicates(subset=["Plant Code", "Port"], inplace=True)

    return df

# Clean the PlantPorts data
cleaned_plant_ports = clean_plant_ports(plant_ports_df.copy())

# Display the cleaned data
print("✅ Cleaned Plant–Port Mapping (NaN columns removed):")
print(cleaned_plant_ports)

# Save cleaned data to CSV
cleaned_plant_ports.to_csv("cleaned_plant_ports.csv", index=False)
