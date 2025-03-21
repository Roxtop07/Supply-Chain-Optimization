import pandas as pd

# Load the OrderList sheet
orders_df = pd.read_excel("SCL_Data.xlsx", sheet_name="OrderList")

def clean_orders(df):
    # Handle missing values
    df.dropna(subset=["Plant Code", "Destination Port", "Product ID"], inplace=True)
    
    # Standardize text columns
    df["Origin Port"] = df["Origin Port"].str.upper().str.strip()
    df["Destination Port"] = df["Destination Port"].str.upper().str.strip()
    df["Carrier"] = df["Carrier"].str.replace(" ", "_")
    
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