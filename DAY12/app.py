import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Palindrome Checker",
    page_icon="🔄",
    layout="centered"
)

# Custom CSS
st.markdown("""
<style>
    .title {
        text-align: center;
        font-size: 40px;
        font-weight: bold;
    }

    .subtitle {
        text-align: center;
        font-size: 18px;
        margin-bottom: 25px;
    }

    .result {
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        font-size: 24px;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown(
    '<div class="title">🔄 Palindrome Checker</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Check whether a word or sentence reads the same forward and backward'
    '</div>',
    unsafe_allow_html=True
)

st.divider()

# Input
st.subheader("✍️ Enter a Word or Sentence")

text = st.text_input(
    "Enter your text:",
    placeholder="Example: Madam or Never odd or even"
)

# Check button
if st.button("🔍 Check Palindrome", use_container_width=True):

    if not text.strip():
        st.warning("⚠️ Please enter a word or sentence.")

    else:
        # Normalize input:
        # Convert to lowercase and remove spaces
        normalized_text = "".join(text.lower().split())

        # Reverse the normalized string
        reversed_text = normalized_text[::-1]

        # Compare original and reversed strings
        if normalized_text == reversed_text:
            st.success("🎉 Yes! It is a palindrome.")

            st.markdown(
                '<div class="result">✅ PALINDROME</div>',
                unsafe_allow_html=True
            )
        else:
            st.error("❌ No! It is not a palindrome.")

            st.markdown(
                '<div class="result">❌ NOT A PALINDROME</div>',
                unsafe_allow_html=True
            )

        st.divider()

        # Show processing details
        st.subheader("📊 Analysis")

        col1, col2 = st.columns(2)

        with col1:
            st.write("**Original Text:**")
            st.info(text)

        with col2:
            st.write("**Normalized Text:**")
            st.info(normalized_text)

        st.write("**Reversed Text:**")
        st.code(reversed_text)


# Examples
st.divider()

st.subheader("💡 Examples")

st.write("✅ **Madam** → Palindrome")
st.write("✅ **Racecar** → Palindrome")
st.write("✅ **Never odd or even** → Palindrome")
st.write("❌ **Python** → Not a palindrome")

st.divider()

st.markdown(
    """
    <div style="text-align:center;">
        🐍 VEDA Internship | Python Programming Track | Day 12<br>
        Built with Python & Streamlit
    </div>
    """,
    unsafe_allow_html=True
)