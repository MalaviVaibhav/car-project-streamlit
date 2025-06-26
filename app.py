#importing libraries
import streamlit as st
import pandas as pd
import numpy as np
import pickle as pkl
pipe=pkl.load(open("Car-price-prediction.pkl","rb+"))

# # Add background image
# st.markdown(
#     """
#     <style>
#     .stApp {
#         background-image: url("https://images.unsplash.com/photo-1549921296-3a6b71e20a29");
#         background-size: cover;
#         background-repeat: no-repeat;
#         background-attachment: fixed;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )


#reading dataset
df=pd.read_csv("EDA.csv")

# Title with subtitle
st.markdown("<h1 style='text-align: center; color: teal;'>🚗 Car Price Prediction Project</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Predict the resale price of any second-hand car by entering a few details below.</p>", unsafe_allow_html=True)
st.markdown("---")

# Info bullets
st.markdown("### ℹ️ We collect the following info:")
st.markdown("""
- **Car Brand**  
- **Car Name**  
- **Car Model Info**  
- **Year of Purchase**  
- **Fuel Type**  
- **Kilometers Driven**  
""")

st.info("If you're purchasing a second-hand car, we can help you predict a reasonable price.")

st.markdown("---")
st.sidebar.markdown("## 🚘 Input Car Details")

with st.sidebar.expander("Select Car Details 🔧", expanded=True):
    # selecting year
    years = list(range(2019, 1995, -1))
    year = st.selectbox("Select Year", years)

    # selecting companies
    companies = sorted(df[df["year"] == year]["company"].unique())
    company = st.selectbox("Select Company", companies)

    # selecting car name according to car brand 
    Car_Name = sorted(df[df["company"] == company]["Car_Name"].unique())
    select_car = st.selectbox("Select Car", Car_Name)

    # selecting car model according to car name 
    Model_Info = sorted(df[df["Car_Name"] == select_car]["Model_Info"].unique())
    select_model = st.selectbox("Select Car Model", Model_Info)

    # selecting fuel type
    fuel_types = sorted(df[df["Model_Info"] == select_model]["fuel_type"].unique())
    select_fuel_type = st.selectbox("Select Fuel Type", fuel_types)

    # getting input from user
    kms_Driven = st.number_input("How many kilometers would you prefer the car to be driven? (e.g. 30000)")

st.markdown("---")

if st.button("🔍 Predict Price", key="predict", help="Click to predict car price"):
    data = [[company, year, select_fuel_type, kms_Driven, select_car, select_model]]
    columns = ["company", "year", "fuel_type", "Driven", "Car_Name", "Model_Info"]
    myinput = pd.DataFrame(data=data, columns=columns)
    
    st.markdown("### ✅ Your Input Summary")
    st.dataframe(myinput)
    
    result = pipe.predict(myinput)
    
    st.markdown("## 💰 Predicted Price")
    st.success(f"🟢 You can buy this car for: ₹ **{int(result[0,0]):,}**")
