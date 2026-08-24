import sqlite3
import pandas as pd

connection=sqlite3.connect("data/database/customer_churn.db")

df_customer=pd.read_sql_query(
    "select * from db_customer",
    connection
)

df_customer["dob"]=pd.to_datetime(df_customer["dob"])

df_customer=df_customer.drop(columns=["pincode","interests"])

df_subscription=pd.read_sql_query(
    "select * from db_subscription",
    connection
)

df_subscription["subscription_start_date"]=pd.to_datetime(df_subscription["subscription_start_date"])

df_subscription["renewal_date"]=pd.to_datetime(df_subscription["renewal_date"])

df_subscription["cancellation_date"]=pd.to_datetime(df_subscription["cancellation_date"])\

df_subscription["subscription_type"] = df_subscription["subscription_type"].replace(
    "Refferal",
    "Referral"
)


df_support=pd.read_sql_query(
    "select * from db_support",
    connection
)

df_support["complaint_date"]=pd.to_datetime(df_support["complaint_date"])

df_support=df_support.drop(columns="col_1")

connection.close()



