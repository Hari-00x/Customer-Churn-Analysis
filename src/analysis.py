from feature_engineering import engineer_features


def calculate_kpis():
    df_customer, df_subscription, df_support = engineer_features()

    # 1. Churn rate
    churn_rate = df_subscription["churn_flag"].mean() * 100

    # 2. Retention rate
    retention_rate = 100 - churn_rate

    # 3. Average tenure
    average_tenure = df_subscription["tenure_days"].mean()

    # 4. ARPU for active customers
    active_customers = df_subscription[
        df_subscription["churn_flag"] == 0
    ]

    arpu = (
        active_customers["monthly_charges"].sum()
        / active_customers["customerid"].nunique()
    )

    # 5. Revenue at risk
    revenue_at_risk = df_subscription.loc[
        df_subscription["churn_score"] > 70,
        "monthly_charges"
    ].sum()

    # 6. Churn rate by plan type
    churn_by_plan = (
        df_subscription
        .groupby("plan_type")["churn_flag"]
        .mean()
        .mul(100)
    )

    # 7. Churn rate by contract type
    churn_by_contract = (
        df_subscription
        .groupby("contract_type")["churn_flag"]
        .mean()
        .mul(100)
    )

    # 8. Merge customer and subscription data
    df_customer_subscription = df_customer.merge(
        df_subscription,
        on="customerid",
        how="inner"
    )

    # 9. Churn rate by state
    churn_by_state = (
        df_customer_subscription
        .groupby("state")["churn_flag"]
        .mean()
        .mul(100)
        .sort_values(ascending=False)
    )

    # 10. Escalation rate
    escalation_rate = (
        (df_support["escalations"] == "Y").sum()
        / len(df_support)
    ) * 100

    # 11. Average complaints per customer
    avg_complaints_per_customer = (
        len(df_support)
        / df_support["customerid"].nunique()
    )

    # 12. Merge support and churn data
    df_support_churn = df_support.merge(
        df_subscription[
            ["customerid", "churn_flag"]
        ],
        on="customerid",
        how="left"
    )

    # 13. Churn rate by escalation status
    churn_by_escalation = (
        df_support_churn
        .groupby("escalations")["churn_flag"]
        .mean()
        .mul(100)
    )

    return (
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
    )


if __name__ == "__main__":
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

    print("Churn Rate:", round(churn_rate, 2), "%")
    print("Retention Rate:", round(retention_rate, 2), "%")
    print("Average Tenure:", round(average_tenure, 2), "days")
    print("ARPU:", round(arpu, 2))
    print("Revenue at Risk:", round(revenue_at_risk, 2))

    print("\nChurn Rate by Plan:")
    print(churn_by_plan)

    print("\nChurn Rate by Contract:")
    print(churn_by_contract)

    print("\nChurn Rate by State:")
    print(churn_by_state)

    print("\nEscalation Rate:", round(escalation_rate, 2), "%")

    print(
        "Average Complaints per Customer:",
        round(avg_complaints_per_customer, 2)
    )

    print("\nChurn Rate by Escalation Status:")
    print(churn_by_escalation)