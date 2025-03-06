import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Load the dataset
file_path = "greendestination.csv"  # Update this if needed
df = pd.read_csv("File_path")
# Drop unnecessary columns
drop_cols = ["StandardHours", "EmployeeNumber"]
df_cleaned = df.drop(columns=drop_cols)
# Calculate Attrition Rate
total_employees = len(df_cleaned)
employees_left = len(df_cleaned[df_cleaned["Attrition"] == "Yes"])
attrition_rate = (employees_left / total_employees) * 100
print(f"Attrition Rate: {attrition_rate:.2f}%")
# Group by Attrition and calculate mean values
attrition_analysis = df_cleaned.groupby("Attrition")[["Age", "YearsAtCompany", "MonthlyIncome"]].mean()
print(attrition_analysis)
# Visualization: Attrition count by age group
plt.figure(figsize=(8, 5))
sns.histplot(df_cleaned[df_cleaned["Attrition"] == "Yes"]["Age"], bins=15, kde=True, color='red', label='Left')
sns.histplot(df_cleaned[df_cleaned["Attrition"] == "No"]["Age"], bins=15, kde=True, color='blue', label='Stayed')
plt.title("Attrition Count by Age Group")
plt.xlabel("Age")
plt.ylabel("Count")
plt.legend()
plt.show()
# Visualization: Years at company vs Attrition
plt.figure(figsize=(8, 5))
sns.boxplot(x="Attrition", y="YearsAtCompany", data=df_cleaned)
plt.title("Years at Company vs Attrition")
plt.show()
# Save cleaned dataset
df_cleaned.to_csv("cleaned_greendestination.csv", index=False)
