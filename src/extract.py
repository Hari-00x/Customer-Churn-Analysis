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

print("\nCustomer Table and Info")
print(df_customer.head())
print(df_customer.shape)
print(df_customer.columns)
print(df_customer.dtypes)
print(df_customer.isnull().sum())
print("Duplicate rows:",df_customer.duplicated().sum())

print("\nSubscription Table and Info")
print(df_subscription.head())
print(df_subscription.shape)
print(df_subscription.columns)
print(df_subscription.dtypes)
print(df_subscription.isnull().sum())
print("Duplicate rows:",df_subscription.duplicated().sum())

print("\nSupport Table and Info")
print(df_support.head())
print(df_support.shape)
print(df_support.columns)
print(df_support.dtypes)
print(df_support.isnull().sum())
print("Duplicate rows:",df_support.duplicated().sum())


connection.close()