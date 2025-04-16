import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast For The Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forecasted days.")
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} days in {place}")

data = get_data(place, days, option)


if option == "Temperature":
    filtered_data = [item["main"]["temp"] for item in filtered_data]
    figure = px.line(x= dates, y= temperatures, labels = {"x": "Date", "y": "Temperature (C)"})
    st.plotly_chart(figure)
    
if option == "Sky":
    filtered_data = [item["weather"][0]["main"] for item in filtered_data]
    st.image()