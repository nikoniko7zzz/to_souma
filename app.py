import streamlit as st
import pandas as pd
import numpy as np

to_souma_df = pd.read_csv("to_souma.csv")

def main():
    for index, row in to_souma_df.iterrows():
        # st.write(row)
        st.header(row[0])
        st.write(row[1])
        st.write(row[2])
        st.write(row[3])

if __name__ == '__main__':
    main()