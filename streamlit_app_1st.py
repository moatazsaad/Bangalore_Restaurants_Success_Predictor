import streamlit as st
import pandas as pd 
import joblib
import sklearn
import xgboost
import category_encoders

Inputs = joblib.load("Inputs_One.pkl")
Model = joblib.load("Model_One.pkl")

def prediction(online_order , book_table , location , approx_cost , listed_in_type , listed_in_city , cuisines_counts , rest_type_counts):
    test_df = pd.DataFrame(columns = Inputs)
    test_df.at[0 , "online_order"] = online_order
    test_df.at[0 , "book_table"] = book_table
    test_df.at[0 , "location"] = location
    test_df.at[0 , "rest_type_counts"] = rest_type_counts
    test_df.at[0 , "approx_cost(for two people)"] = approx_cost
    test_df.at[0 , "cuisines_counts"] = cuisines_counts
    test_df.at[0 , "listed_in(type)"] = listed_in_type
    test_df.at[0 , "listed_in(city)"] = listed_in_city
    st.dataframe(test_df)
    result = Model.predict(test_df)[0]
    return result
    
def main():
    st.title("Bangalore Resturants")
    online_order = st.selectbox("Online Ordering" , ['Yes', 'No'])
    book_table = st.selectbox("Table Booking" , ['Yes', 'No'])
    location = st.selectbox("Location" ,['Banashankari', 'Basavanagudi', 'other', 'Jayanagar', 'JP Nagar',
       'Bannerghatta Road', 'BTM', 'Electronic City', 'Shanti Nagar',
       'Koramangala 5th Block', 'Richmond Road', 'HSR',
       'Koramangala 7th Block', 'Bellandur', 'Sarjapur Road',
       'Marathahalli', 'Whitefield', 'Old Airport Road', 'Indiranagar',
       'Koramangala 1st Block', 'Frazer Town', 'MG Road', 'Brigade Road',
       'Lavelle Road', 'Church Street', 'Ulsoor', 'Residency Road',
       'Shivajinagar', 'St. Marks Road', 'Cunningham Road',
       'Commercial Street', 'Vasanth Nagar', 'Domlur',
       'Koramangala 8th Block', 'Ejipura', 'Jeevan Bhima Nagar',
       'Kammanahalli', 'Koramangala 6th Block', 'Brookefield',
       'Koramangala 4th Block', 'Banaswadi', 'Kalyan Nagar',
       'Malleshwaram', 'Rajajinagar', 'New BEL Road'] )
    rest_type_counts = st.selectbox("Number of Restaurant Type " , [1,2])
    approx_cost = st.slider( "Approximate Cost for Two" , min_value = 40 , max_value = 6000 , value = 0 , step = 1)
    cuisines_counts = st.selectbox("Number of Cuisines" , [3 , 2 , 1 , 4 , 5 , 8 , 7 , 6])
    listed_in_type = st.selectbox("Type" , ['Buffet', 'Cafes', 'Delivery', 'Desserts', 'Dine-out',
       'Drinks & nightlife', 'Pubs and bars'])
    listed_in_city = st.selectbox("City" , ['Banashankari', 'Bannerghatta Road', 'Basavanagudi', 'Bellandur',
       'Brigade Road', 'Brookefield', 'BTM', 'Church Street',
       'Electronic City', 'Frazer Town', 'HSR', 'Indiranagar',
       'Jayanagar', 'JP Nagar', 'Kalyan Nagar', 'Kammanahalli',
       'Koramangala 4th Block', 'Koramangala 5th Block',
       'Koramangala 6th Block', 'Koramangala 7th Block', 'Lavelle Road',
       'Malleshwaram', 'Marathahalli', 'MG Road', 'New BEL Road',
       'Old Airport Road', 'Rajajinagar', 'Residency Road',
       'Sarjapur Road', 'Whitefield'])
    
    if st.button("Predict"):
        results = prediction(online_order , book_table , location , approx_cost , listed_in_type , listed_in_city, cuisines_counts , rest_type_counts)
        label = ["Unsuccessful" , "Successful"]
        st.text(f"The restaurant will be {label[results]}")
        
if __name__ == '__main__':
    main()    
    
