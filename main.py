import streamlit as st 
# import plotly.express as px
from backend import get_data


st.title("Weather Forecast for the next Days")
place =st.text_input("Place: ")
days= st.slider("Forecast Days", min_value=1, max_value=5, 
                help="Select the number of forecasted days")

option= st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")



if place:
    
    try:
        
        filtered_data= get_data(place, days)
        if option=="Temperature":
            st.header("This functionality doesn't work on streamlit cloud :((")
            temperatures= [value["main"]["temp"] /10 for value in filtered_data]
            temperatures= [temp-273.15 for temp in temperatures]
            dates=[value["dt_txt"] for value in filtered_data]
            st.write(dates, temperatures)
            # figure= px.line(x=dates, y=temperatures, labels={"x":"Date", "y":"Temperature(c)"})
            # st.plotly_chart(figure)


        if option=="Sky":
            
            images={"Clear":"images/clear.png","Clouds":"images/cloud.png","Rain":"images/rain.png","Snow":"images/snow.png"}
            sky_condition= [value["weather"][0]["main"] for value in filtered_data]   
            image_paths= [images[condition] for condition in sky_condition]

            st.image(image_paths,width=115,caption=sky_condition)
            
    except KeyError:
        st.header(f"No data found   ~ {place} ~   Does not exist :)")