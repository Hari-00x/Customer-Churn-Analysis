from analysis import calculate_kpis
from feature_engineering import engineer_features

import matplotlib.pyplot as plt
import seaborn as sns
import os


def create_visualizations():

    # Create charts folder if it does not already exist
    os.makedirs("outputs/charts", exist_ok=True)

    # Get KPI results from analysis.py
    (
        churn_rate,
        retention_rate,
        average_tenure,
        arpu,
        revenue_at_risk,
        churn_by_plan,
        churn_by_contract,
        churn_by_state,
        escalation_rate,
        avg_complaints_per_customer,
        churn_by_escalation
    ) = calculate_kpis()

    # Get feature-engineered DataFrames
    df_customer, df_subscription, df_support = engineer_features()


    # -------------------------------------------------
    # 1. Churn Rate by Plan Type
    # -------------------------------------------------

    plt.figure(figsize=(8, 5))

    sns.barplot(
        x=churn_by_plan.index,
        y=churn_by_plan.values
    )

    plt.title("Churn Rate by Plan Type")
    plt.xlabel("Plan Type")
    plt.ylabel("Churn Rate (%)")

    plt.tight_layout()
    plt.savefig("outputs/charts/churn_by_plan.png")
    plt.show()


    # -------------------------------------------------
    # 2. Churn Rate by Contract Type
    # -------------------------------------------------

    plt.figure(figsize=(8, 5))

    sns.barplot(
        x=churn_by_contract.index,
        y=churn_by_contract.values
    )

    plt.title("Churn Rate by Contract Type")
    plt.xlabel("Contract Type")
    plt.ylabel("Churn Rate (%)")

    plt.tight_layout()
    plt.savefig("outputs/charts/churn_by_contract.png")
    plt.show()


    # -------------------------------------------------
    # 3. Churn Rate by State
    # -------------------------------------------------

    plt.figure(figsize=(10, 6))

    sns.barplot(
        x=churn_by_state.values,
        y=churn_by_state.index
    )

    plt.title("Churn Rate by State")
    plt.xlabel("Churn Rate (%)")
    plt.ylabel("State")

    plt.tight_layout()
    plt.savefig("outputs/charts/churn_by_state.png")
    plt.show()


    # -------------------------------------------------
    # 4. Churn Rate by Escalation Status
    # -------------------------------------------------

    plt.figure(figsize=(7, 5))

    sns.barplot(
        x=churn_by_escalation.index,
        y=churn_by_escalation.values
    )

    plt.title("Churn Rate by Support Escalation")
    plt.xlabel("Escalated")
    plt.ylabel("Churn Rate (%)")

    plt.tight_layout()
    plt.savefig("outputs/charts/churn_by_escalation.png")
    plt.show()


    # -------------------------------------------------
    # 5. Cancellation Reasons
    # -------------------------------------------------

    cancellation_reasons = (
        df_subscription["cancellation_reason"]
        .dropna()
        .value_counts()
    )

    plt.figure(figsize=(10, 6))

    sns.barplot(
        x=cancellation_reasons.values,
        y=cancellation_reasons.index
    )

    plt.title("Customer Cancellation Reasons")
    plt.xlabel("Number of Customers")
    plt.ylabel("Cancellation Reason")

    plt.tight_layout()
    plt.savefig("outputs/charts/cancellation_reasons.png")
    plt.show()


    # -------------------------------------------------
    # 6. Churn Score Distribution
    # -------------------------------------------------

    plt.figure(figsize=(9, 5))

    sns.histplot(
        data=df_subscription,
        x="churn_score",
        bins=10
    )

    plt.title("Distribution of Customer Churn Scores")
    plt.xlabel("Churn Score")
    plt.ylabel("Number of Customers")

    plt.tight_layout()
    plt.savefig("outputs/charts/churn_score_distribution.png")
    plt.show()


if __name__ == "__main__":
    create_visualizations()