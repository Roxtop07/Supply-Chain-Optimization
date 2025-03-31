# 🚀 Supply Chain Optimization – AI-Driven Logistics Management

## 📌 Overview
This project focuses on **optimizing supply chain logistics** by analyzing **plant-port assignments, order fulfillment, warehouse efficiency, and freight cost estimation**. Using **Machine Learning (Python & Orange3)**, we aim to:  
✅ **Reduce logistics costs** by selecting optimal plant-port routes.  
✅ **Improve warehouse utilization** through cost analysis.  
✅ **Enhance freight cost prediction** using ML models.  
✅ **Optimize order fulfillment** with data-driven insights.  

---

## 🏭 **Project Objectives**
🔹 Find **the most cost-effective plant-port assignments**.  
🔹 Predict **freight costs** based on shipping mode & distance.  
🔹 Optimize **warehouse storage & manufacturing costs**.  
🔹 Improve **order fulfillment efficiency**.  

---

## 📂 **Dataset Details**
The project uses multiple **supply chain datasets**, including:  
- `Order List` → Shipment details (Order ID, Origin Port, Destination Port, Carrier).  
- `Freight Rates` → Cost per shipment mode (Air, Sea, Road).  
- `Plant-Port Relations` → Best plant-port assignments.  
- `Warehouse Capacities` → Storage limits & space utilization.  
- `Warehouse Costs` → Manufacturing & operational expenses.  

📁 **Datasets Used:**  
- `OrdersData.csv`  
- `FreightRates.csv`  
- `WarehouseData.csv`  
- `PlantPorts.csv`  

---

## 📊 **Methodology**
The project is divided into **four main components**:

### **1️⃣ Data Preprocessing & Cleaning**
- **Handle missing values** and duplicates.  
- **Convert categorical data** using Label Encoding.  
- **Standardize numerical values** for ML models.  

### **2️⃣ Freight Cost Prediction (Regression)**
- **Random Forest Regression** → Predicts freight costs based on shipment mode, port distance.  
- **Feature Engineering** → Distance, transport mode, carrier type impact prediction accuracy.  

### **3️⃣ Order Fulfillment & Warehouse Efficiency (Clustering)**
- **K-Means Clustering** → Groups warehouses into **efficient vs. inefficient storage units**.  
- **Warehouse Utilization Rate** → `Occupied Space / Total Capacity`.  

### **4️⃣ Plant-Port Assignment Optimization**
- **Graph Algorithms (Dijkstra’s Algorithm, NetworkX)** → Find **shortest, cost-effective routes**.  
- **Linear Programming (PuLP)** → Optimize supply chain costs.  

---

## 🔧 **Installation & Setup**
# **1️⃣ Install Python & Dependencies**
```sh
pip install pandas numpy scikit-learn matplotlib seaborn joblib networkx pulp
```

# **2️⃣ Install Orange3**
Download & install Orange3.

# **3️⃣ Clone This Repository**
sh
Copy
git clone https://github.com/Roxtop07/Supply-Chain-Optimization/

# **4️⃣ Run the Machine Learning Model**
sh
Copy
python model.py

# **5️⃣ Open & Run the Orange Workflow**
Open Orange3.
Click File → Open.

Load Supply_Chain_Optimization.ows.

Run the workflow.

# **🚀 Usage Guide**
# *1️⃣ Running the ML Model (Python)*
Run model.py to train & evaluate the model.
Model predicts freight cost, plant-port optimization, warehouse efficiency.
# **2️⃣ Using the Orange Workflow**
Open Orange3.

Load InnoUnity.ows.
Use visual ML pipelines to predict supply chain performance.

# **📊 Results & Insights**
✅ Predicts freight costs for efficient logistics.
✅ Optimizes plant-port assignments to reduce shipping delays.
✅ Clusters warehouses based on efficiency levels.
✅ Improves overall order fulfillment & storage utilization.



**🤝 Contributing**
We welcome contributions!

Fork this repo and make improvements.
Submit a pull request with your enhancements.
Open an issue for feature requests or bugs.





📝 License
This project is licensed under the MIT License.


