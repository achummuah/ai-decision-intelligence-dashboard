#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# ==========================================
# 1. IMPORT LIBRARIES
# ==========================================

import pandas as pd
import numpy as np


# In[ ]:


# ==========================================
# 2. LOAD DATA
# ==========================================

df = pd.read_excel("sample_dataset.xlsx")

# Standardize column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")


# In[ ]:


# ==========================================
# 3. DATA CLEANING
# ==========================================

# Remove duplicates
df = df.drop_duplicates()

# Convert date columns
df["order_delivered_customer_date"] = pd.to_datetime(
    df["order_delivered_customer_date"], errors="coerce"
)

df["order_estimated_delivery_date"] = pd.to_datetime(
    df["order_estimated_delivery_date"], errors="coerce"
)

# Remove invalid revenue
df = df[df["payment_value"] > 0]

# Fill missing categorical values
categorical_cols = ["payment_status", "stock_status", "delivery_status"]
for col in categorical_cols:
    if col in df.columns:
        df[col] = df[col].fillna("unknown")


# In[ ]:


# ==========================================
# 4. FEATURE ENGINEERING
# ==========================================

# Delivery delay in days
df["delivery_delay_days"] = (
    df["order_delivered_customer_date"]
    - df["order_estimated_delivery_date"]
).dt.days

df["delivery_delay_days"] = df["delivery_delay_days"].fillna(0)


# In[ ]:


# ==========================================
# 5. AI DECISION ENGINE (Risk Score Model)
# ==========================================

df["risk_score"] = (
    (df["payment_status"].str.lower() == "failed") * 40 +
    (df["stock_status"].str.lower() == "out of stock") * 35 +
    (df["delivery_delay_days"] > 0) * 25 +
    (df["payment_value"] > 5000) * 20
)


# In[ ]:


# ==========================================
# 6. RISK CLASSIFICATION
# ==========================================

def classify_risk(score):
    if score >= 80:
        return "High Risk"
    elif score >= 40:
        return "Medium Risk"
    else:
        return "Low Risk"

df["risk_level"] = df["risk_score"].apply(classify_risk)


# In[ ]:


# ==========================================
# 7. PREDICTED REVENUE LOSS
# ==========================================

df["predicted_loss"] = (df["risk_score"] / 100) * df["payment_value"]


# In[ ]:


# ==========================================
# 8. AUTOMATED INTERVENTION ENGINE
# ==========================================
def suggest_action(row):
    actions = []

    if row["payment_status"].lower() == "failed":
        actions.append("Trigger payment retry notification")

    if row["stock_status"].lower() == "out of stock":
        actions.append("Activate stock reservation alert")

    if row["delivery_delay_days"] > 0:
        actions.append("Send delivery tracking update")

    if row["risk_level"] == "High Risk":
        actions.append("Escalate to priority monitoring")

    return ", ".join(actions)

df["system_action"] = df.apply(suggest_action, axis=1)


# In[ ]:


# ==========================================
# 9. REVENUE SAVED (Simulation)
# ==========================================

# Assume medium-risk orders are recovered
recovered_orders = df[df["risk_level"] == "Medium Risk"]

revenue_saved = recovered_orders["payment_value"].sum()


# In[ ]:


# ==========================================
# 10. EXECUTIVE SUMMARY
# ==========================================

summary = {
    "Total Orders": len(df),
    "High Risk Orders": (df["risk_level"] == "High Risk").sum(),
    "Medium Risk Orders": (df["risk_level"] == "Medium Risk").sum(),
    "Low Risk Orders": (df["risk_level"] == "Low Risk").sum(),
    "Total Predicted Revenue Loss": df["predicted_loss"].sum(),
    "Revenue Saved (Recovered Orders)": revenue_saved
}

summary_df = pd.DataFrame(summary.items(), columns=["Metric", "Value"])
# ==============================
# DASHBOARD DATA TABLES
# ==============================

# Risk distribution (for dashboard pie chart)
risk_distribution = (
    df["risk_level"]
    .value_counts()
    .reset_index()
)

risk_distribution.columns = ["Risk Level", "Orders"]


# Revenue loss by risk level (financial impact chart)
revenue_risk = (
    df.groupby("risk_level")["predicted_loss"]
    .sum()
    .reset_index()
)

revenue_risk.columns = ["Risk Level", "Predicted Revenue Loss"]


# AI intervention frequency (automation simulation)
actions_summary = (
    df["system_action"]
    .value_counts()
    .reset_index()
)

actions_summary.columns = ["Action", "Triggered Count"]


# In[ ]:


# =====================================
# EXPORT + AUTO DASHBOARD CREATION
# =====================================

with pd.ExcelWriter(
    "AI_Decision_Intelligence_Report.xlsx",
    engine="xlsxwriter"
) as writer:

    # Write data sheets
    df.to_excel(writer, sheet_name="Processed_Data", index=False)
    summary_df.to_excel(writer, sheet_name="Executive_Summary", index=False)
    risk_distribution.to_excel(writer, sheet_name="Risk_Distribution", index=False)
    revenue_risk.to_excel(writer, sheet_name="Revenue_Risk", index=False)
    actions_summary.to_excel(writer, sheet_name="AI_Actions", index=False)

    workbook  = writer.book
    dashboard = writer.sheets["Executive_Summary"]

    # ==============================
    # PIE CHART — Risk Distribution
    # ==============================
    pie_chart = workbook.add_chart({"type": "pie"})

    pie_chart.add_series({
        "name": "Risk Distribution",
        "categories": ["Risk_Distribution", 1, 0, len(risk_distribution), 0],
        "values":     ["Risk_Distribution", 1, 1, len(risk_distribution), 1],
        "data_labels": {"percentage": True},
    })

    pie_chart.set_title({"name": "Order Risk Monitoring"})

    dashboard.insert_chart("D2", pie_chart)


    # ==============================
    # COLUMN CHART — Revenue Risk
    # ==============================
    column_chart = workbook.add_chart({"type": "column"})

    column_chart.add_series({
        "name": "Predicted Revenue Loss",
        "categories": ["Revenue_Risk", 1, 0, len(revenue_risk), 0],
        "values":     ["Revenue_Risk", 1, 1, len(revenue_risk), 1],
    })

    column_chart.set_title({"name": "Financial Risk Impact"})

    dashboard.insert_chart("D20", column_chart)


    # ==============================
    # BAR CHART — AI Actions
    # ==============================
    bar_chart = workbook.add_chart({"type": "bar"})

    bar_chart.add_series({
        "name": "AI Interventions",
        "categories": ["AI_Actions", 1, 0, len(actions_summary), 0],
        "values":     ["AI_Actions", 1, 1, len(actions_summary), 1],
    })

    bar_chart.set_title({"name": "Automated System Actions"})

    dashboard.insert_chart("D38", bar_chart)

print("✅ Fully Automated AI Dashboard Generated")

