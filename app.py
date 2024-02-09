import streamlit as st
import pickle
import numpy as np

st.title('TravelPlanner Hotel Price Predictor')

city_dict={'Kullu': 316,
 'Rishikesh': 315,
 'Kochi': 296,
 'Pune': 289,
 'Goa': 280,
 'Chennai': 279,
 'Hyderabad': 279,
 'Mumbai': 278,
 'Gurgaon': 267,
 'Chandigarh': 264,
 'Ahmedabad': 264,
 'Noida': 254,
 'Varanasi': 243,
 'New Delhi': 234,
 'Jaipur': 212,
 'Lucknow': 200,
 'Kolkata': 179,
 'Bhopal': 172,
 'Munnar': 151,
 'Banglore': 134,
 'Nagpur': 117,
 'Leh': 111,
 'Visakhapatnam, Andhra Pradesh, India': 102,
 'Tirupati, Andhra Pradesh, India': 83}


city_selected = st.selectbox(
    'Enter the city you want to visit ?',
    ('Kullu', 'Rishikesh', 'Kochi', 'Pune', 'Goa', 'Chennai', 'Hyderabad', 'Mumbai', 'Gurgaon', 'Chandigarh', 'Ahmedabad', 'Noida', 'Varanasi', 'New Delhi', 'Jaipur', 'Lucknow', 'Kolkata', 'Bhopal', 'Munnar', 'Banglore', 'Nagpur', 'Leh', 'Visakhapatnam, Andhra Pradesh, India', 'Tirupati, Andhra Pradesh, India'),
     index=None,
     placeholder="Select city...")

distance_to_centercity= st.number_input('Input the distance to the city center in km', min_value=0, max_value=100, value=0, step=1)
distance_to_airport= st.number_input('Input the distance to the airport in km', min_value=0, max_value=100, value=0, step=1)
check_in_month,check_in_year,check_in_day,check_out_year,check_out_month,check_out_day=0,0,0,0,0,0
check_in_date= st.date_input('Input the check-in date',value=None)
check_out_date= st.date_input('Input the check-out date',value=None)

st.subheader("Facilities")
pool_fac = st.radio(
    "Do you want pool facility",
    [ "Yes", "No:"],
    index=None,
)

freepark_fac=st.radio(
    "Do you want free parking facility",
    [ "Yes", "No:"],
    index=None,
)
spa_fac=st.radio(
    "Do you want spa facility",
    [ "Yes", "No:"],
    index=None,
)
restaurant_fac=st.radio(
    "Do you want hotel to be equipped with a restaurant",
    [ "Yes", "No:"],
    index=None,
)

gym_fac=st.radio(
    "Do you want hotel to be equipped with a gym",
    [ "Yes", "No:"],
    index=None,
)

kitchen_fac=st.radio(
    "Do you want sepearate kitchen facility",
    [ "Yes", "No:"],
    index=None,
)

internet_fac=st.radio(
    "Do you want internet access facility",
    [ "Yes", "No:"],
    index=None,
)

def get_facility(facility):
    if facility == "Yes":
        return 1
    else:
        return 0

pool_facility = get_facility(pool_fac)
freepark_facility = get_facility(freepark_fac)
restaurant_facility = get_facility(restaurant_fac)
spa_facility = get_facility(spa_fac)
gym_facility = get_facility(gym_fac)
kitchen_facility = get_facility(kitchen_fac)
internet_facility = get_facility(internet_fac)
if check_in_date is not None:
    check_in_year=str(check_in_date).split('-')[0]
    check_in_month=str(check_in_date).split('-')[1]
    check_in_day=str(check_in_date).split('-')[2]
if check_out_date is not None:
    check_out_year=str(check_out_date).split('-')[0]
    check_out_month=str(check_out_date).split('-')[1]
    check_out_day=str(check_out_date).split('-')[2]

city_input = ''
if city_selected is not None:
    city_input = city_dict.get(city_selected, '') 


model=pickle.load(open('rfpipe.pkl','rb'))


if st.button("Predict", type="primary"):
    input=np.array([city_input,distance_to_centercity,distance_to_airport,check_in_month,check_in_year,check_in_day,check_out_year,check_out_month,check_out_day,pool_facility,freepark_facility,spa_facility,restaurant_facility,gym_facility,kitchen_facility,internet_facility],dtype=object)
    prediction=model.predict(input.reshape(1,16))
    st.write('The predicted price for the hotel is: Rs. {:.2f}'.format(prediction[0]))
