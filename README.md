# 🏢 Employee Attrition Analysis – Green Destinations  

## 📌 Project Overview  
This project analyzes employee attrition at **Green Destinations**, a well-known travel agency. The HR Director noticed an increase in employee turnover and wanted to identify key factors influencing attrition. This analysis leverages **Python, Pandas, Matplotlib, and Seaborn** to uncover insights and provide actionable recommendations.  

## 🎯 Objectives  
- ✅ **Calculate the Attrition Rate** – Determine the percentage of employees leaving the company.  
- ✅ **Identify Key Factors** – Analyze the impact of **age, experience, and income** on attrition.  
- ✅ **Data Visualization** – Use charts to identify trends and patterns.  
- ✅ **Provide Recommendations** – Suggest strategies to **reduce attrition** based on data-driven insights.  

## 📂 Project Structure  
```
📦 Green-Destinations-Attrition-Analysis  
 ├ 🐛 Unified_project_code.ipynb  # Jupyter Notebook with full analysis  
 ├ 🐛 greendestination.csv        # Dataset used for analysis  
 ├ 🐛 Project Report.docx         # Final project report  
 ├ 🐛 README.md                   # Project documentation  
 └ 🐛 requirements.txt            # Python dependencies  
```

## 🛠️ Technologies Used  
- **Python** 🐍  
- **Jupyter Notebook** 📚  
- **Pandas & NumPy** 📊  
- **Matplotlib & Seaborn** 📈  

## 🚀 How to Run This Project  
1. Clone the repository:  
```bash
 git clone https://github.com/yourusername/Green-Destinations-Attrition.git
 cd Green-Destinations-Attrition
```
2. Install required libraries:  
```bash
 pip install -r requirements.txt
```
3. Open **Jupyter Notebook** and run `Unified_project_code.ipynb`.  

## 📊 Key Findings  
📌 Employees who left the company had:  
- **Lower monthly income** than those who stayed.  
- **Less experience** at the company.  
- **Higher attrition rates in certain age groups.**  

## 💡 Recommendations  
✅ Implement **retention programs** for high-risk employees.  
✅ Offer **competitive salaries** to reduce income-based attrition.  
✅ Improve **workplace engagement** for new employees.  

## 🐜 Data Cleaning  
Before conducting the analysis, the dataset underwent a thorough cleaning process to ensure accuracy and reliability. The key steps involved are as follows:  

### **1. Loading the Dataset**  
- The dataset, `greendestination.csv`, was imported using Pandas for analysis.  
```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = "greendestination.csv"
df = pd.read_csv(file_path)
```
### **2. Dropping Irrelevant Columns**  
- Certain columns such as `StandardHours` and `EmployeeNumber` were removed since they did not contribute to the analysis.  
```python
drop_cols = ["StandardHours", "EmployeeNumber"]
df_cleaned = df.drop(columns=drop_cols)
```
### **3. Attrition Rate Calculation**  
- The percentage of employees who left the company was computed to get an overview of attrition levels.  
```python
total_employees = len(df_cleaned)
employees_left = len(df_cleaned[df_cleaned["Attrition"] == "Yes"])
attrition_rate = (employees_left / total_employees) * 100
print(f"Attrition Rate: {attrition_rate:.2f}%")
```
### **4. Grouping Data for Analysis**  
- The dataset was grouped by attrition status to analyze **age, years at company, and monthly income**.  
```python
attrition_analysis = df_cleaned.groupby("Attrition")[["Age", "YearsAtCompany", "MonthlyIncome"]].mean()
print(attrition_analysis)
```
### **5. Data Visualization for Better Insights**  
- **Attrition vs Age:** A histogram was created to see how attrition varies across different age groups.  
```python
plt.figure(figsize=(8, 5))
sns.histplot(df_cleaned[df_cleaned["Attrition"] == "Yes"]["Age"], bins=15, kde=True, color='red', label='Left')
sns.histplot(df_cleaned[df_cleaned["Attrition"] == "No"]["Age"], bins=15, kde=True, color='blue', label='Stayed')
plt.title("Attrition Count by Age Group")
plt.xlabel("Age")
plt.ylabel("Count")
plt.legend()
plt.show()
```
### **6. Importance of Data Cleaning**  
Cleaning the dataset ensures that our analysis is **based on accurate, complete, and relevant data**. It removes inconsistencies and prevents misleading conclusions, leading to more reliable insights.  

## 🏆 Conclusion  
This study aimed to analyze employee attrition at **Green Destinations** to identify key factors influencing employee turnover. By cleaning and preprocessing the dataset, we ensured that the analysis was based on **accurate and relevant data**.  
### **Key Insights**  
- The **overall attrition rate** was calculated, providing a baseline for understanding employee departures.  
- Employees who left the company exhibited notable differences in **age, years at the company, and monthly income** compared to those who stayed.  
- **Visualization techniques** helped in understanding attrition trends, highlighting potential patterns among employees at risk of leaving.  

### **Future Recommendations**  
By leveraging data-driven insights, **Green Destinations** can make informed decisions to **reduce attrition and improve workforce stability**.  

## 🐝 License  
This project is for educational purposes. Feel free to use and modify it!  

---  
🔥 **Let's use data to make better business decisions!** 🚀  
