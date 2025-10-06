import pandas as pd
from PIL import Image
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def run_eda_app():
	st.subheader("Real Estate : Data Analysis")

	submenu = st.sidebar.selectbox("Submenu", ["Descriptive", "Plots"])
	df = pd.read_csv("Final_Project.csv")

	if submenu == "Descriptive":
		try:
			img1 = Image.open("IMG/Real_Estate.jpg")
			st.image(img1)
		except FileNotFoundError:
			st.info("📊 Real Estate Analysis Dashboard")
		
		with st.expander("Dataset"):
			st.dataframe(df)

		with st.expander("Data Types"):
			st.dataframe(df.dtypes)

		with st.expander("Data Summary"):
			st.dataframe(df.describe())

		with st.expander("Location Distribution"):
			st.dataframe(df["Region"].value_counts().head(30))

	elif submenu == "Plots":

		with st.expander("Price Range Distribution"):
			try:
				img2 = Image.open("IMG/Price_Range_Distribution.png")
				st.image(img2)
			except FileNotFoundError:
				st.info("Price range distribution chart would be displayed here")

		with st.expander("Price with respect to Floor"):
			try:
				img3 = Image.open("IMG/Property_Floor_Numbers_Bar.png")
				st.image(img3)
			except FileNotFoundError:
				st.info("Floor vs Price chart would be displayed here")
		
		with st.expander("Price with respect to Bedroom and Bathroom"):
			try:
				img4 = Image.open("IMG/BednBath_Price_Bar.png")
				st.image(img4)
			except FileNotFoundError:
				st.info("Bedroom/Bathroom vs Price chart would be displayed here")

		with st.expander("Price with respect to Property Age"):
			try:
				img5 = Image.open("IMG/Price_Age_Distribution.png")
				st.image(img5)
			except FileNotFoundError:
				st.info("Property Age vs Price chart would be displayed here")

		with st.expander("Price with respect to SqFt Area"):
			try:
				img6 = Image.open("IMG/SqFt_Area_Price_Scatter.png")
				st.image(img6)
			except FileNotFoundError:
				st.info("Area vs Price scatter plot would be displayed here")

		with st.expander("Central Mumbai Property Price"):
			try:
				img7 = Image.open("IMG/Central Mumbai.png")
				st.image(img7)
			except FileNotFoundError:
				st.info("Central Mumbai price analysis would be displayed here")

		with st.expander("South Mumbai Property Price"):
			try:
				img8 = Image.open("IMG/South Mumbai.png")
				st.image(img8)
			except FileNotFoundError:
				st.info("South Mumbai price analysis would be displayed here")

		with st.expander("Thane Property Price"):
			try:
				img9 = Image.open("IMG/Thane.png")
				st.image(img9)
			except FileNotFoundError:
				st.info("Thane price analysis would be displayed here")