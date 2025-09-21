import streamlit as st
import pandas as pd
import numpy as np

st.title("Hello Streamlit")

st.write("This is the simple text")

df = pd.DataFrame(
    {
        "First Column" : [1, 2, 3, 4, 5], 
        "Second Column" : [6, 7, 8, 9, 10]
    }
)

st.write(df)

chart_data = pd.DataFrame(
    np.random.randn(20, 3), columns = ['a', 'b', 'c']
)
st.line_chart(chart_data)