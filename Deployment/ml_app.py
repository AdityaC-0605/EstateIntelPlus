import pickle
import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px

# Load data and model
df = pd.read_csv("Final_Project.csv")
with open('regression_model.pkl', 'rb') as pickle_in:
    reg = pickle.load(pickle_in)

def predict_price(Area_SqFt, Floor_No, Bedroom):
    x = np.zeros(7)
    x[0] = Area_SqFt
    x[1] = Floor_No
    x[2] = Bedroom
    return reg.predict([x])[0]

def run_ml_app():
    st.markdown("""
    ## 🏘️ Property Price Prediction
    Enter the details below to get an estimated property price
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        Location = st.selectbox('📍 Location', 
                              options=df['Region'].sort_values().unique(),
                              help="Select the area where the property is located")
        
        Area_SqFt = st.number_input("📏 Total Area (in SqFt)", 
                                   min_value=500,
                                   max_value=int(max(df['Area_SqFt'])),
                                   step=100,
                                   help="Enter the total area of the property")
        
        Floor_No = st.selectbox("🏢 Floor Number",
                              options=df['Floor_No'].sort_values().unique(),
                              help="Select the floor number of the property")
    
    with col2:
        Bathroom = st.selectbox("🚽 Number of Bathrooms",
                              options=df['Bathroom'].sort_values().unique(),
                              help="Select the number of bathrooms")
        
        Bedroom = st.selectbox("🛏️ Number of Bedrooms",
                             options=df['Bedroom'].sort_values().unique(),
                             help="Select the number of bedrooms")
        
        Property_Age = st.selectbox('🏗️ Property Age',
                                  options=df['Property_Age'].sort_values().unique(),
                                  help="Select the age of the property")

    # Fix: Change 'Price' to 'Price_Lakh'
    avg_price = df[df['Region'] == Location]['Price_Lakh'].mean()
    st.info(f"💡 Average price in {Location}: {avg_price:.2f} Lakhs")
    
    if st.button("📊 Calculate Price", use_container_width=True):
        result = predict_price(Area_SqFt, Floor_No, Bedroom)
        
        # Create columns for the result display
        res_col1, res_col2 = st.columns(2)
        
        with res_col1:
            st.metric(label="Predicted Price", 
                     value=f"₹ {result:.2f} Lakhs",
                     delta=f"{((result-avg_price)/avg_price)*100:.1f}% from area average")
        
        with res_col2:
            # Add a simple visualization
            fig = px.scatter(df[df['Region'] == Location], 
                           x='Area_SqFt', 
                           y='Price_Lakh',  # Fix: Change 'Price' to 'Price_Lakh'
                           title=f'Price vs Area in {Location}')
            fig.add_hline(y=result, line_dash="dash", line_color="red",
                         annotation_text="Predicted Price")
            st.plotly_chart(fig, use_container_width=True)
        
        # Additional insights
        st.markdown("""
        ### 📈 Price Analysis
        - This prediction is based on current market trends
        - Factors considered: Location, Area, Floor Number, and Room configuration
        - Prices may vary based on additional amenities and market conditions
        """)

if __name__ == '__main__':
    run_ml_app()