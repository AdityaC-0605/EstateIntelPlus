import pandas as pd
import numpy as np  # Add this import
import streamlit as st
import plotly.express as px
from datetime import datetime, timedelta

def generate_trend_data(df):
    # Simulate historical data based on current prices
    dates = pd.date_range(end=datetime.now(), periods=12, freq='M')
    trends = {}
    
    for region in df['Region'].unique():
        avg_price = df[df['Region'] == region]['Price_Lakh'].mean()
        # Create synthetic trend with some randomness
        trend = [avg_price * (1 + (i-6)*0.01 + np.random.normal(0, 0.02)) 
                for i in range(12)]
        trends[region] = trend
    
    trend_df = pd.DataFrame(trends, index=dates)
    return trend_df

def run_trend_analysis():
    df = pd.read_csv("Final_Project.csv")
    trend_df = generate_trend_data(df)
    
    st.markdown("""
    ## 📈 Price Trend Analysis
    Analyze historical price trends and future projections
    """)
    
    # Region Selection
    selected_regions = st.multiselect(
        "Select Regions to Compare",
        options=df['Region'].unique(),
        default=df['Region'].unique()[:3]
    )
    
    # Plot trends
    fig = px.line(trend_df[selected_regions], 
                  title='Price Trends by Region (Last 12 Months)')
    st.plotly_chart(fig, use_container_width=True)
    
    # Price Growth Analysis
    growth_df = pd.DataFrame({
        'Region': selected_regions,
        'Current Avg Price': [df[df['Region'] == region]['Price_Lakh'].mean() 
                            for region in selected_regions],
        'YoY Growth': [((trend_df[region].iloc[-1] / trend_df[region].iloc[0]) - 1) * 100 
                      for region in selected_regions]
    })
    
    st.subheader("Price Growth Analysis")
    st.dataframe(growth_df.round(2))