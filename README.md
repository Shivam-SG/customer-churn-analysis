
# Customer Churn Analysis

## 📌 Project Overview

This project analyzes customer churn using the **IBM Telco Customer Churn Dataset**.

The analysis was performed using Microsoft Excel, PostgreSQL, SQL, and Python to identify customer segments with higher churn rates and understand patterns associated with customer retention.

## 🛠️ Tools Used

- Microsoft Excel
- Pivot Tables
- Excel Formulas
- Data Visualization
- PostgreSQL
- SQL Queries
- Python
- Pandas

## 🎯 Project Objective

The main objectives of this project are:

- Analyze overall customer churn.
- Identify customer segments with higher churn rates.
- Understand churn patterns across different customer attributes.
- Generate business recommendations based on observed churn patterns.

## 📊 Key Insights

1. The overall customer churn rate was **26.54%**.
2. Month-to-month contract customers had a churn rate of **42.71%**.
3. Fiber optic customers had a churn rate of **41.89%**.
4. Electronic check payment users had a churn rate of **45.29%**.
5. Customers with 0–12 months of tenure had a churn rate of **47.44%**.
6. Senior citizens had a churn rate of **41.68%**, compared to **23.61%** for non-senior citizens.
7. Customers without dependents had a churn rate of **32.55%**.
8. Customers with monthly charges above $70 had a churn rate of **35.36%**.
9. Customers with month-to-month contracts and fiber optic internet had a churn rate of **54.61%**.

## 📈 Excel Analysis

The Excel workbook includes:

- Dataset
- Pivot Tables
- Churn Dashboard
- Key Insights

The dashboard contains key performance indicators (KPIs), charts, and customer churn analysis by different categories.

## 🗄️ SQL Analysis

SQL analysis was performed using **PostgreSQL**.

The following analyses were conducted:

- Overall Churn Rate
- Churn Rate by Contract Type
- Churn Rate by Internet Service
- Churn Rate by Payment Method
- Churn Rate by Tenure
- Churn Rate by Customer Segments

## 🐍 Python Analysis

Python analysis was performed using **Pandas**.

The following analyses were conducted:

- Overall Churn Rate
- Churn Rate by Contract Type
- Churn Rate by Internet Service
- Churn Rate by Payment Method
- Churn Rate by Tenure
- Churn Rate by Senior Citizen
- Churn Rate by Partner
- Churn Rate by Dependents
- Churn Rate by Monthly Charges
- Combined Customer Segment Analysis

## 💡 Business Recommendations

Based on the observed churn patterns, the following recommendations can be considered:

1. Encourage month-to-month contract customers to move toward longer-term contracts.
2. Investigate service quality and pricing concerns among fiber optic customers.
3. Promote automatic payment methods to reduce payment-related friction.
4. Improve customer onboarding and engagement during the first 12 months.
5. Design targeted retention offers for customers with high monthly charges.
6. Focus retention efforts on customer segments with higher observed churn rates.

> **Note:** These recommendations are based on observed churn patterns and do not establish causation.

## 📁 Project Structure

```text
customer-churn-analysis/
│
├── data/
│   ├── Telco_customer_churn.xlsx
│   └── telco_customer_churn.csv
│
├── python/
│   ├── churn_analysis.py
│   └── requirements.txt
│
├── screenshots/
│   └── requirements.txt
│
├── sql/
│   └── customer_churn_analysis.sql
│
└── README.md
```

## 📂 Project Files

- `Telco_customer_churn.xlsx` – Dataset and Excel analysis workbook.
- `telco_customer_churn.csv` – CSV version of the dataset.
- `customer_churn_analysis.sql` – SQL queries used for PostgreSQL analysis.
- `churn_analysis.py` – Python analysis using Pandas.
- `requirements.txt` – Python libraries required for the project.
- `README.md` – Project documentation.

## 🧾 Conclusion

This project demonstrates the use of Excel, SQL, and Python to analyze customer churn and identify customer segments with higher observed churn rates.

The analysis can support further investigation into customer retention strategies and help businesses understand potential churn-risk patterns.
```