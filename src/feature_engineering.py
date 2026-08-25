import pandas as pd

from clean import load_and_clean_data


def engineer_features():
    df_customer, df_subscription, df_support = load_and_clean_data()

    today = pd.Timestamp.today()

    # customer age
    df_customer["customer_age"] = (
        today.year
        - df_customer["dob"].dt.year
        - (
            (today.month < df_customer["dob"].dt.month)
            | (
                (today.month == df_customer["dob"].dt.month)
                & (today.day < df_customer["dob"].dt.day)
            )
        )
    )

    # churn flag is whether a customer has cancelled their subscription
    df_subscription["churn_flag"] = (
        df_subscription["cancellation_date"]
        .notna()
        .astype(int)
    )

    # tenure_end_date is used temporarily to calculate tenure_days
    df_subscription["tenure_end_date"] = (
        df_subscription["cancellation_date"]
        .fillna(today)
    )

    # tenure_days is the number of days the customer has been subscribed
    df_subscription["tenure_days"] = (
        df_subscription["tenure_end_date"]
        - df_subscription["subscription_start_date"]
    ).dt.days

    # drop temporary tenure_end_date column
    df_subscription = df_subscription.drop(
        columns=["tenure_end_date"]
    )

    return df_customer, df_subscription, df_support


if __name__ == "__main__":
    df_customer, df_subscription, df_support = engineer_features()

    print(
        df_customer[
            ["customerid", "dob", "customer_age"]
        ].head()
    )

    print(
        df_subscription[
            [
                "customerid",
                "subscription_start_date",
                "cancellation_date",
                "churn_flag",
                "tenure_days",
            ]
        ].head()
    )