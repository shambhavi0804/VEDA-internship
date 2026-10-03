import streamlit as st
st.set_page_config(
    page_title="Temperature Converter",
    page_icon="🌡️",
    layout="centered"
)
st.markdown("""
<style>
    .main-title {
        font-size: 38px;
        font-weight: 700;
        text-align: center;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        font-size: 18px;
        color: #666;
        margin-bottom: 30px;
    }

    .result-box {
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        margin-top: 20px;
        border: 1px solid #ddd;
    }

    .result-value {
        font-size: 32px;
        font-weight: 700;
    }

    .formula-box {
        padding: 15px;
        border-radius: 10px;
        background-color: #f5f5f5;
        margin-top: 15px;
    }
</style>
""", unsafe_allow_html=True)
st.markdown(
    '<div class="main-title">🌡️ Temperature Converter</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Convert temperatures between Celsius, Fahrenheit and Kelvin</div>',
    unsafe_allow_html=True
)


def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def celsius_to_kelvin(celsius):
    return celsius + 273.15


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5 / 9 + 273.15


def kelvin_to_celsius(kelvin):
    return kelvin - 273.15


def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9 / 5 + 32

col1, col2 = st.columns(2)

with col1:
    from_unit = st.selectbox(
        "Convert From",
        ["Celsius", "Fahrenheit", "Kelvin"]
    )

with col2:
    to_unit = st.selectbox(
        "Convert To",
        ["Celsius", "Fahrenheit", "Kelvin"]
    )

value = st.number_input(
    "Enter Temperature",
    value=0.0,
    step=0.1,
    format="%.2f"
)

# -------------------------------------------------
# CONVERSION
# -------------------------------------------------

if st.button("Convert Temperature", use_container_width=True):

    # Validate Kelvin
    if from_unit == "Kelvin" and value < 0:
        st.error("Kelvin temperature cannot be below 0 K.")

    # Validate Celsius
    elif from_unit == "Celsius" and value < -273.15:
        st.error("Celsius temperature cannot be below -273.15 °C.")

    # Validate Fahrenheit
    elif from_unit == "Fahrenheit" and value < -459.67:
        st.error("Fahrenheit temperature cannot be below -459.67 °F.")

    else:

        # Same unit
        if from_unit == to_unit:
            result = value
            formula = "No conversion required."

        # Celsius conversions
        elif from_unit == "Celsius" and to_unit == "Fahrenheit":
            result = celsius_to_fahrenheit(value)
            formula = "°F = (°C × 9/5) + 32"

        elif from_unit == "Celsius" and to_unit == "Kelvin":
            result = celsius_to_kelvin(value)
            formula = "K = °C + 273.15"

        # Fahrenheit conversions
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            result = fahrenheit_to_celsius(value)
            formula = "°C = (°F − 32) × 5/9"

        elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
            result = fahrenheit_to_kelvin(value)
            formula = "K = (°F − 32) × 5/9 + 273.15"

        # Kelvin conversions
        elif from_unit == "Kelvin" and to_unit == "Celsius":
            result = kelvin_to_celsius(value)
            formula = "°C = K − 273.15"

        elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
            result = kelvin_to_fahrenheit(value)
            formula = "°F = (K − 273.15) × 9/5 + 32"

        # Display result
        st.markdown(
            f"""
            <div class="result-box">
                <div>Converted Temperature</div>
                <div class="result-value">
                    {result:.2f} {to_unit}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div class="formula-box">
                <strong>Formula:</strong><br>
                {formula}
            </div>
            """,
            unsafe_allow_html=True
        )

st.divider()

st.subheader("📘 Conversion Reference")

st.write("**Celsius → Fahrenheit:** °F = (°C × 9/5) + 32")
st.write("**Celsius → Kelvin:** K = °C + 273.15")
st.write("**Fahrenheit → Celsius:** °C = (°F − 32) × 5/9")
st.write("**Fahrenheit → Kelvin:** K = (°F − 32) × 5/9 + 273.15")
st.write("**Kelvin → Celsius:** °C = K − 273.15")
st.write("**Kelvin → Fahrenheit:** °F = (K − 273.15) × 9/5 + 32")