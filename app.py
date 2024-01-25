import streamlit as st
from streamlit_option_menu import option_menu
import pickle
import numpy as np
from datetime import date

def predict_price(predict_data):
    with open('C:\pythan\DATA SCEINCE\Copper Modeling\Regression_model_Prdict_Price.pkl', 'rb' ) as file:
        model = pickle.load(file)
        data = np.exp(model.predict(predict_data))

        return data

def predict_status(predict_data):
    with open('C:\pythan\DATA SCEINCE\Copper Modeling\classification_model_Predict_Status.pkl', 'rb' ) as file:
        model = pickle.load(file)
        data = model.predict(predict_data)
        if data == 1.0:
          return 'Won'
        else:
          return 'Lost'

item_type_value = {'W': 5.0, 'S': 3.0, 'Others': 1.0, 'PL': 2.0, 'WI': 6.0, 'IPL': 0.0, 'SLAWR': 4.0}

status_values = {'Won': 7.0, 'Draft': 0.0, 'To be approved': 6.0, 
                'Lost': 1.0, 'Not lost for AM': 2.0, 'Wonderful': 8.0,
                'Revised': 5.0, 'Offered': 4.0, 'Offerable': 3.0}

classification_status = {'Won': 1.0, 'Lost': 0.0}

application_code = [10., 41., 28., 59., 15.,  4., 38., 56., 42., 26., 27., 19., 20.,
                66., 29., 22., 40., 25., 67., 79.,  3., 99.,  2.,  5., 39., 69.,
                70., 65., 58., 68.]

country_code = [ 28.,  25.,  30.,  32.,  38.,  78.,  27.,  77., 113.,  79.,  26.,
                 39.,  40.,  84.,  80., 107.,  89.]

# SETTING PAGE CONFIGURATIONS
st.set_page_config(page_title= "Industrial Copper Modeling Appication",
                   layout= "wide",
                   initial_sidebar_state= "expanded",
                   menu_items={'About': """# This Copper modeling app is created by R.AJITH KUMAR!"""})
st.markdown("<h1 style='text-align: center; color: white;'> Industrial Copper Modeling Appication</h1>", unsafe_allow_html=True)

# SETTING-UP BACKGROUND IMAGE
st.markdown("""
    <style>
        .stApp {
            background: linear-gradient(to right,#cfd8dc, #90a4ae, #607d8b, #37474f, #263238);
            background-size: cover;
        }
    </style>
""", unsafe_allow_html=True)

# CREATING OPTION MENU
selected = option_menu(None, ["Home","PREDICT SELLING PRICE","PREDICT STATUS"], 
                       icons=["house","dollar-sign","chart-line"],
                       default_index=0,
                       orientation="horizontal",
                       styles={"nav-link": {"font-size": "25px", "text-align": "centre", "margin": "0px", "--hover-color": "#90a4ae"},
                               "icon": {"color": "red","font-size": "25px"},
                               "container" : {"max-width": "6000px"},
                               "nav-link-selected": {"background-color": " #37474f"}})

if selected == "Home":
    col1,col2 = st.columns(2, gap = 'small')
    with col1:
       st.markdown("## :green[**Project:**] Business Card Data Extracting with OCR ")

if selected == "PREDICT SELLING PRICE":
    col1,col2,col3 = st.columns([0.5,0.1,0.5])
    with col1:
        item_date = st.date_input("Select the **Item Date**", date(2020, 7,2), min_value= date(2020, 7,2), max_value= date(2021, 4,1))

        quantity_tons = st.number_input('Enter the **Quantity Tons**', min_value = 1e-05, max_value= 1000000000.0, value = 5874.904 )

        customer = st.number_input('Enter the **Customer**', min_value = 12458.0, max_value= 2147483647.0, value = 30512207.0 )

        status = st.selectbox('Select The **Status**', status_values)

        item_type =  st.selectbox('Select The **Item Type**', item_type_value)

        application = st.selectbox('Select The **Application**', application_code)
    with col3:
        
        country = st.selectbox('Select the **Country**', country_code)

        thickness = st.number_input('Enter the **Thickness**', min_value = 0.18, max_value= 2500.0, value = 2.56482 )

        width = st.number_input('Enter the **Width**', min_value = 700.0, max_value= 1980.0, value = 1297.0455 )

        product_ref = st.number_input('Enter the **Product Reference**', min_value = 611728.0, max_value= 1722207590.0, value = 473967910.72 )

        delivery_date= st.date_input("Select the **Delivery Date**", date(2019, 4,1), min_value= date(2019, 4,1), max_value= date(2022, 1,1))

    st.markdown('Click below button to predict the **Selling Price**')
    prediction = st.button('**Predict**')

    day_difference = item_date - delivery_date
    quantity_tons_log = np.log1p(quantity_tons)
    thickness_log = np.log1p(thickness)
    
    predict_data =[[quantity_tons, customer, country,  status_values[status], item_type_value[item_type], application, thickness, width, product_ref, 
            quantity_tons_log, thickness_log ,day_difference.days, item_date.day, item_date.month, item_date.year,
            delivery_date.day, delivery_date.month, delivery_date.year]]
    
    if prediction:
        selling_price = predict_price(predict_data)
        rounded_selling_price = np.round(selling_price)

        st.markdown(f"### :blue[Selling Price :] :green[$ {rounded_selling_price}]")

if selected == "PREDICT STATUS":
    col4,col5,col6 = st.columns([0.5,0.1,0.5])


    with col4:
        item_date1 = st.date_input(" Select the **Item Date**", date(2020, 7,2), min_value= date(2020, 7,2), max_value= date(2021, 4,1))

        quantity_tons1 = st.number_input(' Enter the **Quantity Tons**', min_value = 1e-05, max_value= 1000000000.0, value = 5874.904 )

        customer1 = st.number_input(' Enter the **Customer**', min_value = 12458.0, max_value= 2147483647.0, value = 30512207.0 )

        item_type1 =  st.selectbox(' Select The **Item Type**', item_type_value)

        application1 = st.selectbox(' Select The **Application**', application_code)

        country1 = st.selectbox(' Select the **Country**', country_code)
    
    with col6:

        thickness1 = st.number_input(' Enter the **Thickness**', min_value = 0.18, max_value= 2500.0, value = 2.56482 )

        width1 = st.number_input(' Enter the **Width**', min_value = 700.0, max_value= 1980.0, value = 1297.0455 )

        product_ref1 = st.number_input(' Enter the **Product Reference**', min_value = 611728.0, max_value= 1722207590.0, value = 473967910.72 )

        selling_price = st.number_input(' Enter the **Selling Price**',  max_value= 100001015.0, value = 1918.06 )

        delivery_date1 = st.date_input(" Select the **Delivery Date**", date(2019, 4,1), min_value= date(2019, 4,1), max_value= date(2022, 1,1))

    st.markdown('Click below button to predict the **Status**')
    prediction1 = st.button('**Predict The Status**')

    day_difference1 = item_date1 - delivery_date1
    quantity_tons_log1 = np.log1p(quantity_tons1)
    thickness_log1 = np.log1p(thickness1)
    selling_price_log = np.log1p(selling_price)
    predict_data1 =[[quantity_tons1, customer1, item_type_value[item_type1], application1, country1, thickness1, width1, product_ref1, selling_price,
            selling_price_log,quantity_tons_log1, thickness_log1 , day_difference1.days, item_date1.day, item_date1.month, 
            item_date1.year, delivery_date1.day, delivery_date1.month, delivery_date1.year]]
    
    if prediction1:
        st.markdown(f"### :bule[Status :] :green[ { predict_status(predict_data1)}]")
