import streamlit as st

st.title("Our first Streamlit APP")
st.subheader("Introducing Streamlit in Automating Everything with Python")
st.write("""This is our first Web APP.
Enjoy it!
""")

import pandas

df = pandas.DataFrame(data)
st.write(df)

