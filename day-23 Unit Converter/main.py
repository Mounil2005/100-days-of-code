import streamlit as st

st.title("🧮 Universal Unit Converter")

# Dropdown for category
category = st.selectbox("Select Category", ["Length", "Weight", "Temperature"])

# Define unit options
units = {
    "Length": ["Meters", "Feet", "Inches", "Kilometers", "Miles"],
    "Weight": ["Kilograms", "Pounds", "Grams"],
    "Temperature": ["Celsius", "Fahrenheit"]
}

# Input
value = st.number_input("Enter value to convert", format="%.4f")

from_unit = st.selectbox("From", units[category], key="from")
to_unit = st.selectbox("To", units[category], key="to")

# Conversion logic
def convert(value, from_unit, to_unit, category):
    if category == "Length":
        conversion_factors = {
            "Meters": 1,
            "Feet": 3.28084,
            "Inches": 39.3701,
            "Kilometers": 0.001,
            "Miles": 0.000621371
        }
        meters = value / conversion_factors[from_unit]
        result = meters * conversion_factors[to_unit]
        return result

    elif category == "Weight":
        conversion_factors = {
            "Kilograms": 1,
            "Pounds": 2.20462,
            "Grams": 1000
        }
        kg = value / conversion_factors[from_unit]
        result = kg * conversion_factors[to_unit]
        return result

    elif category == "Temperature":
        if from_unit == to_unit:
            return value
        if from_unit == "Celsius":
            return (value * 9/5) + 32 if to_unit == "Fahrenheit" else value
        if from_unit == "Fahrenheit":
            return (value - 32) * 5/9 if to_unit == "Celsius" else value

# Result
if st.button("Convert"):
    try:
        output = convert(value, from_unit, to_unit, category)
        st.success(f"{value} {from_unit} = {output:.4f} {to_unit}")
    except:
        st.error("Conversion failed. Please check inputs.")
