import pickle
from PIL import Image
import streamlit as st
import streamlit.components.v1 as stc
import os

# importing the smaller apps
from ml_app import run_ml_app
from eda_app import run_eda_app

# Set page configuration
st.set_page_config(
    page_title="Real Estate Price Prediction",
    page_icon="🏠",
    layout="wide"
)

# Constants
IMG_DIR = os.path.join(os.path.dirname(__file__), "IMG")
SOCIAL_LINKS = {
    "LinkedIn": "https://www.linkedin.com/in/aditya-choudhary-2a36542b5/",
    "Github": "https://github.com/AdityaC-0605",
    "GMail": "adityachdhr555@gmail.com"
}

html_temp = """
    <div style="background-color:#2E4053;padding:20px;border-radius:15px;margin-bottom:20px">
        <h1 style="color:white;text-align:center;"> 🏠 Mumbai Real Estate Price Predictor</h1>
    </div>
"""

def load_image(image_path):
    try:
        return Image.open(image_path)
    except Exception as e:
        st.error(f"Error loading image: {str(e)}")
        return None

def display_home():
    img1 = load_image(os.path.join(IMG_DIR, "Realty_Growth.jpg"))
    if img1:
        st.image(img1, use_container_width=True)
    
    st.markdown("""
        ## 🎯 Welcome to Smart Property Valuation
        
        ### Why Use This Tool?
        - 📊 **Data-Driven Decisions**: Get accurate price predictions based on real market data
        - 🔍 **Detailed Analysis**: Explore property trends across different Mumbai locations
        - 💡 **Smart Insights**: Understand what factors influence property prices
        - 📈 **Market Understanding**: Get a better grip on real estate market dynamics
        
        ### How It Works
        1. 📝 Input your property details
        2. 🤖 Our AI model analyzes the data
        3. 💰 Get instant price estimation
        4. 📊 View detailed market analysis
    """)
    
    # Add feature highlights
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        ### 🎯 Precise Predictions
        Advanced ML model trained on extensive Mumbai real estate data
        """)
    
    with col2:
        st.markdown("""
        ### 📊 Market Analysis
        Comprehensive insights into property trends and valuations
        """)
    
    with col3:
        st.markdown("""
        ### 💡 Smart Recommendations
        Get intelligent suggestions based on your requirements
        """)

def display_about():
    try:
        with open(os.path.join(IMG_DIR, "mumbai_property.html"), 'r') as f:
            html_data = f.read()
        
        st.subheader("📊 Data points working on the project:")
        st.components.v1.html(html_data, height=500)
        
        st.subheader("👨‍💻 About:")
        
        with st.expander("🔗 Check my Social Links"):
            selected_social = st.selectbox("Select Platform", list(SOCIAL_LINKS.keys()))
            st.markdown(f"[{selected_social}]({SOCIAL_LINKS[selected_social]})")
        
        st.markdown("### Thank You! 🙏")
    except Exception as e:
        st.error(f"Error in About section: {str(e)}")

# Add new imports
from trend_analysis import run_trend_analysis
from investment_analysis import run_investment_analysis

# Update menu
menu = {
    "Home": "🏠",
    "Market Analysis": "📊",
    "Price Trends": "📈",
    "Price Predictor": "🎯",
    "Investment Calculator": "💰",
    "About": "ℹ️"
}

# Update main() function
def main():
    stc.html(html_temp)

    choice = st.sidebar.selectbox(
        "Menu",
        list(menu.keys()),
        format_func=lambda x: f"{menu[x]} {x}"
    )

    if choice == "Home":
        display_home()
    elif choice == "Market Analysis":
        run_eda_app()
    elif choice == "Price Trends":
        run_trend_analysis()
    elif choice == "Price Predictor":
        run_ml_app()
    elif choice == "Investment Calculator":
        run_investment_analysis()
    else:
        display_about()

if __name__ == "__main__":
    main()