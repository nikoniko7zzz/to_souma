import streamlit as st
import pandas as pd
import numpy as np

to_souma_df = pd.read_csv("to_souma.csv")

st.title('颯真へ')
st.write('ITTOの授業後に届く授業日報を「颯真のがんばってきた記録」になると思ってまとめました')
st.markdown('颯真が懸命に取り組む**姿勢**や**努力**を間近で見た先生からのメッセージです')
st.write('やれるだけやった.と言い切れるように、最後までがんばろう')

def main():
    for index, row in to_souma_df.iterrows():
        # st.write(row)
        st.header(row[0])
        st.write(row[1])
        st.write(row[2])
        st.write(row[3])

if __name__ == '__main__':
    main()