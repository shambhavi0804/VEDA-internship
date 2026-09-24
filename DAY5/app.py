import streamlit as st
import random

st.set_page_config(
    page_title="Number Guessing Game",
    page_icon="🎯",
    layout="centered"
)
st.markdown("""
<style>
    .main {
        padding-top: 2rem;
    }

    .game-title {
        text-align: center;
        font-size: 42px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        font-size: 18px;
        margin-bottom: 30px;
    }

    .info-card {
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        margin-bottom: 15px;
        border: 1px solid #ddd;
    }

    .attempt-number {
        font-size: 28px;
        font-weight: bold;
    }

    .success-box {
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        background-color: #d1fae5;
        border: 1px solid #10b981;
    }

    .hint-box {
        padding: 18px;
        border-radius: 12px;
        text-align: center;
        font-size: 18px;
        margin-top: 15px;
    }

    .footer {
        text-align: center;
        margin-top: 40px;
        font-size: 14px;
    }
</style>
""", unsafe_allow_html=True)

if "target_number" not in st.session_state:
    st.session_state.target_number = random.randint(1, 100)

if "attempts" not in st.session_state:
    st.session_state.attempts = 0

if "game_over" not in st.session_state:
    st.session_state.game_over = False

if "message" not in st.session_state:
    st.session_state.message = ""

st.markdown(
    '<div class="game-title">🎯 Number Guessing Game</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Guess the secret number between <b>1 and 100</b>!'
    '</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:
    st.markdown(
        f"""
        <div class="info-card">
            <div>🎲 Number Range</div>
            <div class="attempt-number">1 - 100</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        f"""
        <div class="info-card">
            <div>🔢 Attempts</div>
            <div class="attempt-number">{st.session_state.attempts}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

st.divider()
if not st.session_state.game_over:

    guess = st.number_input(
        "Enter your guess:",
        min_value=1,
        max_value=100,
        value=50,
        step=1
    )

    if st.button("🎯 Check My Guess", use_container_width=True):

        st.session_state.attempts += 1

        # Correct Guess
        if guess == st.session_state.target_number:

            st.session_state.game_over = True

            st.markdown(
                f"""
                <div class="success-box">
                    <h2>🎉 Congratulations!</h2>
                    <p>You guessed the correct number:</p>
                    <h1>{st.session_state.target_number}</h1>
                    <p>You found it in <b>{st.session_state.attempts}</b> attempts.</p>
                </div>
                """,
                unsafe_allow_html=True
            )

            st.balloons()

        # Guess is too low
        elif guess < st.session_state.target_number:

            st.markdown(
                """
                <div class="hint-box">
                    🔼 <b>Too Low!</b><br>
                    Try a higher number.
                </div>
                """,
                unsafe_allow_html=True
            )

        # Guess is too high
        else:

            st.markdown(
                """
                <div class="hint-box">
                    🔽 <b>Too High!</b><br>
                    Try a lower number.
                </div>
                """,
                unsafe_allow_html=True
            )

# ---------------------------------------------------------
# Game Over / New Game
# ---------------------------------------------------------
else:

    st.success(
        f"Game completed in {st.session_state.attempts} attempts!"
    )

    if st.button("🔄 Start New Game", use_container_width=True):

        st.session_state.target_number = random.randint(1, 100)
        st.session_state.attempts = 0
        st.session_state.game_over = False
        st.session_state.message = ""

        st.rerun()

# ---------------------------------------------------------
# Instructions
# ---------------------------------------------------------
with st.expander("📖 How to Play"):

    st.write("""
    1. The computer generates a random number between **1 and 100**.
    2. Enter your guessed number.
    3. Click **Check My Guess**.
    4. The game tells you whether your guess is **too high** or **too low**.
    5. Continue guessing until you find the correct number.
    6. Your total number of attempts is displayed.
    """)

# ---------------------------------------------------------
# Footer
# ---------------------------------------------------------
st.markdown(
    """
    <div class="footer">
        🐍 Python Programming Track | Day 5<br>
        Built using Python, Random Module & Streamlit
    </div>
    """,
    unsafe_allow_html=True
)