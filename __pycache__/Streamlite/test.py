import streamlit as st

st.set_page_config(
    page_title="Calculator",
    page_icon=":material/calculate:",
    layout="centered",
)

st.title("Calculator", icon=":material/calculate:")
st.caption("A little math, made simple.")

with st.container(border=True):
    st.subheader("Make a calculation")

    first_column, operation_column, second_column = st.columns(
        [2, 1, 2],
        vertical_alignment="bottom",
    )

    with first_column:
        first_number = st.number_input(
            "First number",
            value=0.0,
            step=1.0,
            format="%g",
            key="first_number",
        )

    with operation_column:
        operation = st.selectbox(
            "Operation",
            options=["Add (+)", "Subtract (−)", "Multiply (×)", "Divide (÷)"],
            key="operation",
        )

    with second_column:
        second_number = st.number_input(
            "Second number",
            value=0.0,
            step=1.0,
            format="%g",
            key="second_number",
        )

    st.space("small")

    if operation == "Add (+)":
        result = first_number + second_number
        symbol = "+"
    elif operation == "Subtract (−)":
        result = first_number - second_number
        symbol = "−"
    elif operation == "Multiply (×)":
        result = first_number * second_number
        symbol = "×"
    elif second_number == 0:
        st.error("A number cannot be divided by zero.")
        result = None
        symbol = "÷"
    else:
        result = first_number / second_number
        symbol = "÷"

    if result is not None:
        st.metric("Result", f"{result:,.12g}")
        st.caption(
            f"{first_number:,.12g} {symbol} "
            f"{second_number:,.12g} = {result:,.12g}"
        )

st.caption(":material/bolt: Results update automatically as you change the inputs.")
