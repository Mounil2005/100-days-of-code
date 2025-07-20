# import streamlit as st

# st.set_page_config(page_title="BMI Calculator", page_icon="💪", layout="centered")

# st.title("💪 BMI Calculator")
# st.markdown("Calculate your Body Mass Index (BMI) and understand your health status.")

# # Input
# weight = st.number_input("Enter your weight (in kg):", min_value=1.0, max_value=300.0, step=0.1)
# height_cm = st.number_input("Enter your height (in cm):", min_value=30.0, max_value=250.0, step=0.1)

# # Calculate BMI
# if st.button("Calculate BMI"):
#     height_m = height_cm / 100
#     bmi = weight / (height_m ** 2)
#     bmi = round(bmi, 2)

#     # Determine category
#     if bmi < 18.5:
#         category = "Underweight"
#         color = "🔵"
#     elif 18.5 <= bmi < 24.9:
#         category = "Normal weight"
#         color = "🟢"
#     elif 25 <= bmi < 29.9:
#         category = "Overweight"
#         color = "🟠"
#     else:
#         category = "Obese"
#         color = "🔴"

#     # Display result
#     st.subheader(f"Your BMI is: **{bmi}**")
#     st.markdown(f"### {color} Category: **{category}**")

#     st.info("BMI = weight (kg) / (height (m))²")

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title="BMI Calculator", page_icon="💪", layout="centered")
st.title("💪 BMI Calculator")
st.markdown("Calculate your Body Mass Index (BMI) and understand your health status.")

# Input
weight = st.number_input("Enter your weight (in kg):", min_value=1.0, max_value=300.0, step=0.1)
height_cm = st.number_input("Enter your height (in cm):", min_value=30.0, max_value=250.0, step=0.1)

if height_cm > 0:
    height_m = height_cm / 100
    ideal_weight_min = round(18.5 * (height_m ** 2), 1)
    ideal_weight_max = round(24.9 * (height_m ** 2), 1)
    st.markdown(
        f"🎯 Ideal weight range for your height: **{ideal_weight_min} kg – {ideal_weight_max} kg**"
    )

# Calculate BMI
if st.button("Calculate BMI"):
    if height_cm == 0:
        st.error("Please enter your height.")
    else:
        bmi = round(weight / (height_m ** 2), 2)

        # Determine category
        if bmi < 18.5:
            category = "Underweight"
            color = "🔵"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
            color = "🟢"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
            color = "🟠"
        else:
            category = "Obese"
            color = "🔴"

        st.subheader(f"Your BMI is: **{bmi}**")
        st.markdown(f"### {color} Category: **{category}**")
        st.info("BMI = weight (kg) / (height (m))²")

        # Draw BMI bar chart
        fig, ax = plt.subplots(figsize=(8, 1.5))

        # Ranges and colors
        ranges = [10, 18.5, 24.9, 29.9, 40]
        colors = ['#87CEEB', '#90EE90', '#FFD580', '#FF6961']
        labels = ['Underweight', 'Normal', 'Overweight', 'Obese']

        for i in range(len(ranges) - 1):
            ax.barh(0, width=ranges[i+1]-ranges[i], left=ranges[i], color=colors[i], edgecolor='black')

        # Marker for your BMI
        ax.plot(bmi, 0, 'ko', markersize=12, label='Your BMI')

        ax.set_xlim(10, 40)
        ax.set_yticks([])
        ax.set_xlabel('BMI')
        ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.3), ncol=5)
        # ax.set_capt("📊 BMI Indicator Bar")

        st.pyplot(fig)
