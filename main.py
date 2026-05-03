import streamlit as st
import pandas


data = {
    "series_1": [1, 3, 4, 5, 6, 7],
    "series_2": [33, 4, 5, 6, 2, 2]
}

st.title("Our first Streamlit APP")
st.subheader("Introducing Streamlit in Automating Everything with Python")
st.write("""This is our first Web APP.
Enjoy it!
""")



df = pandas.DataFrame(data)
st.write(df)
