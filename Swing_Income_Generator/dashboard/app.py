import streamlit as st
import pandas as pd

st.title("📈 Swing Income Dashboard")
df = pd.read_csv("results/monthly_report.csv")
st.line_chart(df.set_index("Month"))
st.dataframe(df)