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

if place:
    
    try:
        filtered_data = get_data(place, days)


        if option == "Temperature":
            temperatures = [item["main"]["temp"] / 10 for item in filtered_data]
            dates = [item["dt_txt"] for item in filtered_data]
            
            figure = px.line(x= dates, y= temperatures, labels = {"x": "Date", "y": "Temperature (C)"})
            st.plotly_chart(figure)
            
        if option == "Sky":
            images = {
                "Clear": "images/clear.png",
                "Clouds": "images/cloud.png",
                "Rain": "images/rain.png",
                "Snow": "images/snow.png"
            }
            
            sky_conditions = [item["weather"][0]["main"] for item in filtered_data]
            # We got a dictionary mapping the weather condition with the proper image
            # Now to connect (translate):
            image_paths = [images[condition] for condition in sky_conditions]
            
            st.image(image_paths, width=115)
            
    except KeyError:
        st.write("That place does not exist.")