import streamlit as st
import requests

city = st.text_input("Enter City Name:")
key = '67ba64fcbd81ba6c52da7e77b6b1c14a'
url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={key}'

res = requests.get(url).json()

if 'name' in res:
    st.write('Country:', res['sys']['country'])
    st.write('City:', res['name'])
    st.write('Longitude:', res['coord']['lon'])
    st.write('Latitude:', res['coord']['lat'])
    st.write('Temperature:', res['main']['temp'], 'C')
    st.write('Min Temp:', res['main']['temp_min'], 'C')
    st.write('Max Temp:', res['main']['temp_max'], 'C')
    st.write('Humidity:', res['main']['humidity'])
    st.write('Pressure:', res['main']['pressure'])
else:
    st.write('City not found')



