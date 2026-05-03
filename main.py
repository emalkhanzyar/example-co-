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
st.line_chart(data)
st.area_chart(data)
myslider = st.slider('Celsius')
st.write(myslider, 'in Fahrenheit is', myslider * 9/5 + 32)
st.write(df)
