import streamlit as st
import re

# Page configuration
st.set_page_config(
    page_title="Word & Character Counter",
    page_icon="📝",
    layout="centered"
)

# Custom styling
st.markdown("""
<style>
    .main-title {
        text-align: center;
        font-size: 40px;
        font-weight: bold;
    }

    .subtitle {
        text-align: center;
        font-size: 18px;
        margin-bottom: 25px;
    }

    .stat-box {
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #ddd;
        text-align: center;
        margin-bottom: 10px;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown(
    '<div class="main-title">📝 Word & Character Counter</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Analyze your text using Python and Streamlit'
    '</div>',
    unsafe_allow_html=True
)

st.divider()

# Text input
st.subheader("✍️ Enter Your Paragraph")

text = st.text_area(
    "Type or paste your text below:",
    height=220,
    placeholder="Enter a paragraph here..."
)

# Analyze button
if st.button("🔍 Analyze Text", use_container_width=True):

    if not text.strip():
        st.warning("⚠️ Please enter some text before analyzing.")

    else:
        # Character count including spaces
        characters = len(text)

        # Character count excluding spaces
        characters_without_spaces = len(
            text.replace(" ", "").replace("\n", "")
        )

        # Word count
        words = text.split()
        word_count = len(words)

        # Space count
        space_count = text.count(" ")

        # Sentence count
        sentences = re.findall(r"[.!?]+", text)
        sentence_count = len(sentences)

        # Display results
        st.success("✅ Text analyzed successfully!")

        st.subheader("📊 Text Statistics")

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "🔤 Characters",
                characters
            )

            st.metric(
                "📝 Words",
                word_count
            )

        with col2:
            st.metric(
                "📄 Sentences",
                sentence_count
            )

            st.metric(
                "⬜ Spaces",
                space_count
            )

        st.divider()

        st.subheader("📌 Detailed Statistics")

        st.write(
            f"**Total Characters:** {characters}"
        )

        st.write(
            f"**Characters Without Spaces:** "
            f"{characters_without_spaces}"
        )

        st.write(
            f"**Total Words:** {word_count}"
        )

        st.write(
            f"**Total Sentences:** {sentence_count}"
        )

        st.write(
            f"**Total Spaces:** {space_count}"
        )

        st.divider()

        st.subheader("📖 Entered Text")

        st.info(text)


# Footer
st.divider()

st.markdown(
    """
    <div style="text-align:center;">
        🐍 VEDA Internship | Python Programming Track | Day 11<br>
        Built with Python & Streamlit
    </div>
    """,
    unsafe_allow_html=True
)