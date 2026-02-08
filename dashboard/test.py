import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency

print("Imports successful")

# Load cleaned data
all_df = pd.read_csv("all_data.csv")
print("Data loaded, shape:", all_df.shape)

datetime_columns = ["order_purchase_timestamp"]
all_df.sort_values(by="order_purchase_timestamp", inplace=True)
all_df.reset_index(inplace=True)

for column in datetime_columns:
    all_df[column] = pd.to_datetime(all_df[column])
print("Datetime conversion successful")

print("Test completed successfully")