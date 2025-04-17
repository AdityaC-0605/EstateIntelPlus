import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

def calculate_roi(price, down_payment_percent, interest_rate, tenure, expected_appreciation):
    loan_amount = price * (1 - down_payment_percent/100)
    monthly_rate = interest_rate/(12*100)
    emi = (loan_amount * monthly_rate * (1 + monthly_rate)**(tenure*12)) / ((1 + monthly_rate)**(tenure*12) - 1)
    total_payment = emi * tenure * 12
    future_value = price * (1 + expected_appreciation/100)**tenure
    roi = ((future_value - total_payment) / (price * down_payment_percent/100)) * 100
    return roi, emi, future_value

def run_investment_analysis():
    st.markdown("""
    ## 💰 Investment Analysis
    Calculate potential returns on your real estate investment
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        property_price = st.number_input("Property Price (Lakhs)", min_value=10.0, value=100.0)
        down_payment = st.slider("Down Payment (%)", min_value=20, max_value=100, value=20)
        interest_rate = st.slider("Interest Rate (%)", min_value=6.0, max_value=12.0, value=8.5)
    
    with col2:
        tenure = st.slider("Loan Tenure (Years)", min_value=5, max_value=30, value=20)
        appreciation = st.slider("Expected Annual Appreciation (%)", min_value=0.0, max_value=15.0, value=5.0)
    
    if st.button("Calculate Investment Returns"):
        roi, emi, future_value = calculate_roi(
            property_price, down_payment, interest_rate, tenure, appreciation)
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Monthly EMI", f"₹ {emi:,.2f}")
        with col2:
            st.metric("Expected Future Value", f"₹ {future_value:,.2f} Lakhs")
        with col3:
            st.metric("Expected ROI", f"{roi:.2f}%")
        
        # Investment Timeline Visualization
        years = list(range(tenure + 1))
        property_values = [property_price * (1 + appreciation/100)**year for year in years]
        
        fig = px.line(x=years, y=property_values,
                     title='Projected Property Value Over Time',
                     labels={'x': 'Years', 'y': 'Property Value (Lakhs)'})
        st.plotly_chart(fig, use_container_width=True)