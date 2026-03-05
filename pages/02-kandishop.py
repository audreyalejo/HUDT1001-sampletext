import streamlit as st
import pandas as pd

st.write("""follow me on instagram to look at my kandi""")

tab1, tab2 = st.tabs(["shop", "table"])

with tab1:
    st.write("""[FOLLOW ME HERE](https://example.com)""")

with tab2:
    df = pd.read_csv("media/all-voyages.csv")
    st.dataframe(df)