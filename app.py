import streamlit as st
import pandas as pd
import numpy as np
import joblib  
st.set_page_config(layout="wide")


st.markdown("<h1 style='font-size: 36px; margin-top: -70px;'>Demand Forecaster</h1>", unsafe_allow_html=True)


uploaded_file = st.sidebar.file_uploader("Upload your sales data (CSV)", type="csv")

if uploaded_file:
    sales_data = pd.read_csv(uploaded_file)  
    model_file_path = "random_forest_model.pkl"  
    random_forest_model = joblib.load(model_file_path)  

    sales_data['lag_sales_1'] = sales_data['W50']  
    sales_data['lag_sales_2'] = sales_data['W49'] 
    sales_data['diff_sales_1'] = sales_data['W51'] - sales_data['W50']  
    sales_data['diff_sales_2'] = sales_data['W50'] - sales_data['W49'] 
    sales_data['mean_sales_4'] = sales_data[['W48', 'W49', 'W50', 'W51']].mean(axis=1)  

   
    product_names = list(sales_data["Product"].unique())  
    forecasted_results = {}

    for product in product_names:
        product_data = sales_data[sales_data["Product"] == product]  
        
        product_inputs = product_data[['W51', 'lag_sales_1', 'lag_sales_2', 'diff_sales_1', 'diff_sales_2', 'mean_sales_4']]
        
        forecasted_result = random_forest_model.predict(product_inputs)
        
        forecasted_results[product] = pd.DataFrame(
            forecasted_result,
            columns=["Forecast Week 1", "Forecast Week 2", "Forecast Week 3", "Forecast Week 4"]
        )

    # Step 6: Sidebar Product Selector
    product_names = ["Sales Overview"] + product_names  # Add "Sales Overview" to the product list
    selected_product = st.sidebar.selectbox("Select an option:", product_names)

    # Step 7: Display Data for Selected Product
    if selected_product == "Sales Overview":
        st.markdown("<h1 style='font-size: 26px;'>This Week's Sales</h1>", unsafe_allow_html=True)
        st.image("salespred.png",use_column_width=False, width=900)



    else:
        # Show past 4 weeks' sales and forecasted sales for the selected product
        product_data = sales_data[sales_data["Product"] == selected_product]
        forecasted_data = forecasted_results.get(selected_product, pd.DataFrame())  # Get forecasted data for the selected product

        # Display Past 4 Weeks' Sales
        st.markdown(f"<h1 style='font-size: 24px;'>Past 4 Weeks Record for {selected_product}</h1>", unsafe_allow_html=True)


        col1, col2, col3, col4 = st.columns(4)  # Create four columns to show past sales

        with col1:
            st.info('Week-3 Sales')
            st.info(f"{product_data['W48'].iloc[0]} x100 Boxes")

        with col2:
            st.info('Week-2 Sales')
            st.info(f"{product_data['W49'].iloc[0]} x100 Boxes")

        with col3:
            st.info('Week-1 Sales')
            st.info(f"{product_data['W50'].iloc[0]} x100 Boxes")

        with col4:
            st.info('Current Week Sales')
            st.info(f"{product_data['W51'].iloc[0]} x100 Boxes")

        # Display Forecast for Next 4 Weeks
        st.markdown(f"<h1 style='font-size: 24px;'>Forecast for Next 4 Weeks for {selected_product}</h1>", unsafe_allow_html=True)


        col1, col2, col3, col4 = st.columns(4)  # Create four columns for the forecasted sales

        with col1:
            st.info('Week+1')
            st.info(f"{int(forecasted_data['Forecast Week 1'].iloc[0])} x100 Boxes")
        with col2:
            st.info('Week+2')
            st.info(f"{int(forecasted_data['Forecast Week 2'].iloc[0])} x100 Boxes")

        with col3:
            st.info('Week+3')
            st.info(f"{int(forecasted_data['Forecast Week 3'].iloc[0])} x100 Boxes")
        with col4:
            st.info('Week+4')
            st.info(f"{int(forecasted_data['Forecast Week 4'].iloc[0])} x100 Boxes")


else:
    st.write("Please upload a CSV file to proceed.")  # Default message if no file is uploaded
