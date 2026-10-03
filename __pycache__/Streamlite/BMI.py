import streamlit as st
# Title
st.title("BMI Calculator") 
# Input for weight and height   
weight = st.number_input("Enter your weight (kg):")
height = st.number_input("Enter your height (m):")
if st.button("Calculate BMI"):
    bmi = weight / (height ** 2)
    st.write("Your BMI is:", bmi)
    if bmi < 18.5:
        st.write("You are underweight.")
    elif 18.5 <= bmi < 24.9:
        st.write("You have a normal weight.")
    elif 25 <= bmi < 29.9:
        st.write("You are overweight.")
    else:
        st.write("You are obese.")          
    st.write("End of BMI calculation.")
    st.write("Thank you for using the BMI Calculator!")
    st.write("Goodbye!")
    st.write("Exiting the BMI Calculator.")
    st.write("Goodbye for real this time!")
    st.write("See you later!")
    st.write("Farewell!")
    st.write("Until next time!")
    st.write("Goodbye for real this time!")
    st.write("See you next time!")
    st.write("End of script.")
    st.balloons()
    st.write("Congratulations! You have completed the BMI calculation.")
    