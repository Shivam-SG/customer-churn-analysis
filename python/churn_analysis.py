import pandas as pd

df = pd.read_csv("./data/Telco_customer_churn.csv")

print(df.head())
print("Total rows:", len(df))

# Check Data Information

print(df.info())

# Check Missing Values

print(df.isnull().sum())

# Overall Churn Rate in Python

churn_rate = (df["Churn Label"] == "Yes").mean() * 100

print("Overall Churn Rate:", round(churn_rate, 2), "%")

# Churn Rate by Contract Type

contract_analysis = df.groupby("Contract").agg(
    total_customers=("CustomerID", "count"),
    churned_customers=("Churn Label", lambda x: (x == "Yes").sum())
)

contract_analysis["churn_rate_percentage"] = (
    contract_analysis["churned_customers"]
    / contract_analysis["total_customers"] * 100
).round(2)

print(contract_analysis)

# Churn Rate by Internet Service

internet_analysis = df.groupby("Internet Service").agg(
    total_customers=("CustomerID", "count"),
    churned_customers=("Churn Label", lambda x: (x == "Yes").sum())
)

internet_analysis["churn_rate_percentage"] = (
    internet_analysis["churned_customers"]
    / internet_analysis["total_customers"] * 100
).round(2)

print(internet_analysis)

# Churn Rate by Payment Method

payment_analysis = df.groupby("Payment Method").agg(
    total_customers=("CustomerID", "count"),
    churned_customers=("Churn Label", lambda x: (x == "Yes").sum())
)

payment_analysis["churn_rate_percentage"] = (
    payment_analysis["churned_customers"]
    / payment_analysis["total_customers"] * 100
).round(2)

print(payment_analysis)

# Churn Rate by Tenure

df["tenure_group"] = pd.cut(
    df["Tenure Months"],
    bins=[-1, 12, 24, 48, float("inf")],
    labels=["0-12 months", "13-24 months", "25-48 months", "49+ months"]
)

tenure_analysis = df.groupby("tenure_group", observed=False).agg(
    total_customers=("CustomerID", "count"),
    churned_customers=("Churn Label", lambda x: (x == "Yes").sum())
)

tenure_analysis["churn_rate_percentage"] = (
    tenure_analysis["churned_customers"]
    / tenure_analysis["total_customers"] * 100
).round(2)

print(tenure_analysis)

# Churn Rate by Senior Citizen

senior_analysis = df.groupby("Senior Citizen").agg(
    total_customers=("CustomerID", "count"),
    churned_customers=("Churn Label", lambda x: (x == "Yes").sum())
)

senior_analysis["churn_rate_percentage"] = (
    senior_analysis["churned_customers"]
    / senior_analysis["total_customers"] * 100
).round(2)

print(senior_analysis)

# Churn Rate by Partner

partner_analysis = df.groupby("Partner").agg(
    total_customers=("CustomerID", "count"),
    churned_customers=("Churn Label", lambda x: (x == "Yes").sum())
)

partner_analysis["churn_rate_percentage"] = (
    partner_analysis["churned_customers"]
    / partner_analysis["total_customers"] * 100
).round(2)

print(partner_analysis)

# Churn Rate by Dependents

dependents_analysis = df.groupby("Dependents").agg(
    total_customers=("CustomerID", "count"),
    churned_customers=("Churn Label", lambda x: (x == "Yes").sum())
)

dependents_analysis["churn_rate_percentage"] = (
    dependents_analysis["churned_customers"]
    / dependents_analysis["total_customers"] * 100
).round(2)

print(dependents_analysis)

# Monthly Charges Analysis

df["charge_group"] = pd.cut(
    df["Monthly Charges"],
    bins=[-float("inf"), 35, 70, float("inf")],
    labels=["Low (<=35)", "Medium (35-70)", "High (>70)"]
)

charge_analysis = df.groupby("charge_group", observed=False).agg(
    total_customers=("CustomerID", "count"),
    churned_customers=("Churn Label", lambda x: (x == "Yes").sum())
)

charge_analysis["churn_rate_percentage"] = (
    charge_analysis["churned_customers"]
    / charge_analysis["total_customers"] * 100
).round(2)

print(charge_analysis)

# Combined Segment Analysis

segment = df[
    (df["Contract"] == "Month-to-month") &
    (df["Internet Service"] == "Fiber optic")
]

total_customers = len(segment)
churned_customers = (segment["Churn Label"] == "Yes").sum()

churn_rate = (churned_customers / total_customers * 100)

print("Total Customers:", total_customers)
print("Churned Customers:", churned_customers)
print("Churn Rate:", round(churn_rate, 2), "%")