import sqlite3
import pandas as pd

connection=sqlite3.connect("data/database/customer_churn.db")

df_customer=pd.read_sql_query(
    "select * from db_customer",connection 
)

df_subscription=pd.read_sql_query(
    "select * from db_subscription",connection
)

df_support=pd.read_sql_query(
    "select * from db_support",connection
)

print("\nCustomer Table")
print(df_customer.head())

print("\nSubscription Table")
print(df_subscription.head())

print("\nSupport Table")
print(df_support.head())


connection.close()