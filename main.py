# import pandas as pd

# # Load the OrderList sheet
# orders_df = pd.read_excel("SCL_Data.xlsx", sheet_name="PlantPorts")


# def clean_orders(df):
#     # Handle missing values
#     df.dropna(subset=["Plant Code", "Port"], inplace=True)

#     # Standardize text columns
#     df["Plant Code"] = df["Plant Code"].str.upper().str.strip()
#     df["Port"] = df["Port"].str.upper().str.strip()

#     # Validate numeric fields
#     df = df[(df["Unit quantity"] > 0) & (df["Weight"] > 0)]

#     # Fix dates
#     df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")
#     df = df[df["Order Date"].notnull()]

#     # Remove duplicates
#     df.drop_duplicates(subset="Order ID", keep="first", inplace=True)

#     return df


# cleaned_orders = clean_orders(orders_df.copy())

# # List valid plant-port pairs from the OrderList data
# valid_plant_port = cleaned_orders.groupby(["Plant Code", "Origin Port"]).size().reset_index()
# print("Valid Plant-Port Relationships:")
# print(valid_plant_port[["Plant Code", "Origin Port"]])

# cleaned_orders.to_csv("cleaned_orders.csv", index=False)
# import pandas as pd

# # Load the PlantPorts CSV
# plant_ports_df = pd.read_csv("PlantPorts-Table 1.csv")

# def clean_plant_ports(df):
#     # Strip column names and convert them to consistent format
#     df.columns = df.columns.str.strip()

#     # Remove all columns that contain any NaN values
#     df.dropna(axis=1, inplace=True)

#     # Drop rows with missing crucial values (just in case)
#     df.dropna(subset=["Plant Code", "Port"], inplace=True)

#     # Standardize text fields
#     df["Plant Code"] = df["Plant Code"].astype(str).str.strip().str.upper()
#     df["Port"] = df["Port"].astype(str).str.strip().str.upper()

#     # Remove duplicates
#     df.drop_duplicates(subset=["Plant Code", "Port"], inplace=True)

#     return df

# # Clean the PlantPorts data
# cleaned_plant_ports = clean_plant_ports(plant_ports_df.copy())

# # Display the cleaned data
# print("✅ Cleaned Plant–Port Mapping (NaN columns removed):")
# print(cleaned_plant_ports)

# # Save cleaned data to CSV
# cleaned_plant_ports.to_csv("cleaned_plant_ports.csv", index=False)

# import pandas as pd

# # Load the full CSV file
# df = pd.read_csv("ProductsPerPlant-Table 1.csv")

# def clean_full_dataframe(df):
#     # Drop columns that are completely NaN
#     df.dropna(axis=1, how='all', inplace=True)

#     # Drop rows that are completely NaN
#     df.dropna(axis=0, how='all', inplace=True)

#     # Strip whitespaces from column names
#     df.columns = df.columns.str.strip()

#     # If column names or values need standardization:
#     df.columns = df.columns.str.replace(" ", "_").str.upper()

#     # Remove leading/trailing whitespaces from string data
#     df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

#     # Drop rows where essential columns are missing (customize if needed)
#     essential_columns = [col for col in df.columns if "PLANT" in col or "PRODUCT" in col]
#     df.dropna(subset=essential_columns, inplace=True)

#     # Remove duplicates (optional)
#     df.drop_duplicates(inplace=True)

#     return df

# # Clean the full dataset
# cleaned_df = clean_full_dataframe(df)

# # Save the cleaned dataset
# cleaned_df.to_csv("cleaned_products_per_plant_FULL.csv", index=False)

# import pandas as pd

# # Load the full FreightRates CSV
# df = pd.read_csv("FreightRates-Table 1.csv")

# def clean_freight_rates(df):
#     # Drop columns that are entirely NaN
#     df.dropna(axis=1, how='all', inplace=True)

#     # Drop rows that are entirely NaN
#     df.dropna(axis=0, how='all', inplace=True)

#     # Strip whitespaces from column names
#     df.columns = df.columns.str.strip()

#     # Standardize column names (uppercase, underscores instead of spaces)
#     df.columns = df.columns.str.replace(" ", "_").str.upper()

#     # Remove leading/trailing whitespaces from each cell
#     df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

#     # Optionally drop rows missing critical fields (customize as needed)
#     essential_columns = [col for col in df.columns if "PORT" in col or "PLANT" in col or "FREIGHT" in col]
#     df.dropna(subset=essential_columns, inplace=True)

#     # Drop duplicates if any
#     df.drop_duplicates(inplace=True)

#     return df

# # Clean the freight rates dataset
# cleaned_freight_df = clean_freight_rates(df)

# # Save the cleaned version
# cleaned_freight_df.to_csv("cleaned_freight_rates_FULL.csv", index=False)

# print("✅ Freight Rates CSV cleaned and saved as 'cleaned_freight_rates_FULL.csv'")

# import pandas as pd

# # Load the VMI Customers CSV
# df = pd.read_csv("VmiCustomers-Table 1.csv")

# def clean_vmi_customers(df):
#     # Drop columns that are entirely NaN
#     df.dropna(axis=1, how='all', inplace=True)

#     # Drop rows that are entirely NaN
#     df.dropna(axis=0, how='all', inplace=True)

#     # Clean and standardize column headers
#     df.columns = df.columns.str.strip().str.replace(" ", "_").str.upper()

#     # Strip leading/trailing whitespace from all string fields
#     df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

#     # Drop rows where critical fields are missing (customize as per your columns)
#     essential_columns = [col for col in df.columns if "CUSTOMER" in col or "PORT" in col or "PLANT" in col]
#     df.dropna(subset=essential_columns, inplace=True)

#     # Drop duplicate rows if any
#     df.drop_duplicates(inplace=True)

#     return df

# # Clean the VMI Customers dataset
# cleaned_vmi_df = clean_vmi_customers(df)

# # Save the cleaned CSV
# cleaned_vmi_df.to_csv("cleaned_vmi_customers_FULL.csv", index=False)

# print("✅ VMI Customers CSV cleaned and saved as 'cleaned_vmi_customers_FULL.csv'")

# import pandas as pd

# # Load the WH Capacities CSV
# df = pd.read_csv("WhCapacities-Table 1.csv")

# def clean_wh_capacities(df):
#     # Drop columns that are entirely NaN
#     df.dropna(axis=1, how='all', inplace=True)

#     # Drop rows that are entirely NaN
#     df.dropna(axis=0, how='all', inplace=True)

#     # Clean and standardize column headers
#     df.columns = df.columns.str.strip().str.replace(" ", "_").str.upper()

#     # Strip leading/trailing whitespace from all string-type fields
#     df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

#     # Drop rows where essential values (e.g., warehouse, plant code, or capacity) are missing
#     essential_columns = [col for col in df.columns if "PLANT" in col or "CAPACITY" in col or "WAREHOUSE" in col]
#     df.dropna(subset=essential_columns, inplace=True)

#     # Drop duplicates, if any
#     df.drop_duplicates(inplace=True)

#     return df

# # Clean the WH Capacities dataset
# cleaned_wh_df = clean_wh_capacities(df)

# # Save the cleaned CSV
# cleaned_wh_df.to_csv("cleaned_wh_capacities_FULL.csv", index=False)

# print("✅ Warehouse Capacities CSV cleaned and saved as 'cleaned_wh_capacities_FULL.csv'")

# import pandas as pd

# # Load the WH Costs CSV
# df = pd.read_csv("WhCosts-Table 1.csv")

# def clean_wh_costs(df):
#     # Drop columns that are entirely NaN
#     df.dropna(axis=1, how='all', inplace=True)

#     # Drop rows that are entirely NaN
#     df.dropna(axis=0, how='all', inplace=True)

#     # Clean and standardize column headers
#     df.columns = df.columns.str.strip().str.replace(" ", "_").str.upper()

#     # Strip extra whitespaces from all string fields
#     df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

#     # Drop rows with missing critical fields
#     essential_columns = [col for col in df.columns if "PLANT" in col or "WAREHOUSE" in col or "COST" in col]
#     df.dropna(subset=essential_columns, inplace=True)

#     # Drop duplicates, if any
#     df.drop_duplicates(inplace=True)

#     return df

# # Clean the WH Costs dataset
# cleaned_wh_costs_df = clean_wh_costs(df)

# # Save the cleaned CSV
# cleaned_wh_costs_df.to_csv("cleaned_wh_costs_FULL.csv", index=False)

# print("✅ Warehouse Costs CSV cleaned and saved as 'cleaned_wh_costs_FULL.csv'")