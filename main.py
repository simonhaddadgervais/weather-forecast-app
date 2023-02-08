import streamlit as st
import plotly.express as px
from backend import get_data

# Adds user interface
st.title("Weather Forecast")
place = st.text_input("Location: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forecasted days")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

if place:
    try:
        # Gets the data from API
        filtered_data = get_data(place, days)
        # Creates plot
        if option == "Temperature":
            temperatures = [dict["main"]["temp"] for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (C)"})
            st.plotly_chart(figure)

        if option == "Sky":
            sky = [dict["weather"][0]["main"] for dict in filtered_data]
            images = {"Clear":"images/clear.png", "Clouds":"images/cloud.png", "Rain":"images/rain.png", "Snow":"images/snow.png"}
            print_images = [images[condition] for condition in sky]
            st.image(print_images, width=100)
    # If user enter a wrong name:
    except KeyError:
        st.write("This place does not exist. Please enter correct city name.")
