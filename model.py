# import pandas as pd
# import numpy as np
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import LabelEncoder
# from sklearn.ensemble import RandomForestRegressor
# from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
# import joblib

# # Step 1: Load dataset
# df = pd.read_csv("Cleaned Datasets/cleaned_freight_rates_FULL.csv")

# # Step 2: Drop rows with missing target
# df = df[df["MINIMUM_COST"].notna()]

# # Step 3: Print column dtypes to identify string columns
# print("\n🔍 Column Data Types:\n", df.dtypes)

# # Step 4: Automatically detect all object (non-numeric) columns
# object_cols = df.select_dtypes(include=['object']).columns.tolist()
# print("\n🧠 Categorical Columns (object dtype):", object_cols)

# # Step 5: Label Encode all categorical columns
# le_dict = {}
# for col in object_cols:
#     le = LabelEncoder()
#     df[col] = df[col].astype(str)
#     df[col] = le.fit_transform(df[col])
#     le_dict[col] = le  # Save encoder if needed later

# # Step 6: Handle NaNs in numeric columns
# numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
# numeric_cols.remove("MINIMUM_COST")  # Don't impute target column

# for col in numeric_cols:
#     median_val = df[col].median()
#     df[col] = df[col].fillna(median_val)

# # Step 7: Feature-target split
# X = df.drop(columns=["MINIMUM_COST"])
# y = df["MINIMUM_COST"]

# # Step 8: Train-Test Split
# X_train, X_test, y_train, y_test = train_test_split(
#     X, y, test_size=0.2, random_state=42
# )

# # Step 9: Train Random Forest Model
# model = RandomForestRegressor(n_estimators=100, max_depth=10, random_state=42)
# model.fit(X_train, y_train)

# # Step 10: Evaluate model
# y_pred = model.predict(X_test)
# mae = mean_absolute_error(y_test, y_pred)
# rmse = np.sqrt(mean_squared_error(y_test, y_pred))
# r2 = r2_score(y_test, y_pred)

# print("\n📊 Model Evaluation:")
# print(f"🔸 MAE : {mae:.2f}")
# print(f"🔸 RMSE: {rmse:.2f}")
# print(f"🔸 R²  : {r2:.2f}")

# # Step 11: Save model
# joblib.dump(model, "freight_cost_model.pkl")
# print("\n💾 Model saved as 'freight_cost_model.pkl'")

# # Step 12: Load and test sample prediction
# loaded_model = joblib.load("freight_cost_model.pkl")
# sample_data = X_test.iloc[0].values.reshape(1, -1)
# predicted_cost = loaded_model.predict(sample_data)

# print("\n📦 Sample Prediction:")
# print(f"Predicted Freight Cost: {predicted_cost[0]:.2f}")

# model.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

# Load the data
df = pd.read_csv("Cleaned Datasets/cleaned_OrderList.csv")

# Preview
print("🔍 Columns in dataset:", df.columns.tolist())

# Drop rows with missing values (if any)
df.dropna(inplace=True)

# Define features and targets
features = ['Origin_Port', 'Carrier', 'TPT', 'Service_Level',
            'Ship_Ahead_Day_Count', 'Ship_Late_Day_Count',
            'Customer', 'Product_ID', 'Unit_Quantity', 'Weight']

target1 = 'Plant_Code'
target2 = 'Destination_Port'

# Convert categorical columns to strings
for col in ['Origin_Port', 'Carrier', 'Service_Level', 'Customer', 'Product_ID']:
    df[col] = df[col].astype(str)

# Encode categorical columns
feature_encoders = {}
for col in features:
    if df[col].dtype == 'object':
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        feature_encoders[col] = le

# Encode target columns
plant_encoder = LabelEncoder()
port_encoder = LabelEncoder()

df[target1] = plant_encoder.fit_transform(df[target1])
df[target2] = port_encoder.fit_transform(df[target2])

# Split for Plant_Code prediction
X1 = df[features]
y1 = df[target1]

X1_train, X1_test, y1_train, y1_test = train_test_split(X1, y1, test_size=0.2, random_state=42)

plant_model = RandomForestClassifier(n_estimators=100, random_state=42)
plant_model.fit(X1_train, y1_train)
y1_pred = plant_model.predict(X1_test)

print("\n📍 Plant_Code Prediction Report:")
print(classification_report(y1_test, y1_pred, target_names=plant_encoder.classes_[:len(set(y1_test))]))
print("Plant Accuracy:", accuracy_score(y1_test, y1_pred))

# Split for Destination_Port prediction
X2 = df[features]
y2 = df[target2]

X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y2, test_size=0.2, random_state=42)

port_model = RandomForestClassifier(n_estimators=100, random_state=42)
port_model.fit(X2_train, y2_train)
y2_pred = port_model.predict(X2_test)

print("\n📦 Destination_Port Prediction Report:")
print(classification_report(y2_test, y2_pred, target_names=port_encoder.classes_[:len(set(y2_test))]))
print("Port Accuracy:", accuracy_score(y2_test, y2_pred))

# Optionally: save models
import joblib
joblib.dump(plant_model, "plant_model.pkl")
joblib.dump(port_model, "port_model.pkl")
joblib.dump(plant_encoder, "plant_encoder.pkl")
joblib.dump(port_encoder, "port_encoder.pkl")

print("\n✅ Models and encoders saved successfully.")