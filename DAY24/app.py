import streamlit as st
import json
import random

st.set_page_config(
    page_title="Python Quiz",
    page_icon="🧠",
    layout="centered"
)

def load_questions():
    """Load quiz questions from JSON file."""

    try:
        with open("questions.json", "r", encoding="utf-8") as file:
            questions = json.load(file)

        if not isinstance(questions, list):
            raise ValueError("Question data must be a list.")

        return questions

    except FileNotFoundError:
        st.error("questions.json file was not found.")
        return []

    except json.JSONDecodeError:
        st.error("Invalid JSON format in questions.json.")
        return []

    except Exception as error:
        st.error(f"Unable to load questions: {error}")
        return []

def validate_questions(questions):
    """Validate that each question has required fields."""

    required_keys = {
        "question",
        "options",
        "answer"
    }

    valid_questions = []

    for question in questions:

        if not isinstance(question, dict):
            continue

        if not required_keys.issubset(question.keys()):
            continue

        if not isinstance(question["options"], list):
            continue

        if len(question["options"]) < 2:
            continue

        if question["answer"] not in question["options"]:
            continue

        valid_questions.append(question)

    return valid_questions

def initialize_quiz():

    questions = load_questions()
    questions = validate_questions(questions)

    if len(questions) < 10:
        st.error(
            "The quiz must contain at least 10 valid questions."
        )
        return

    random.shuffle(questions)

    st.session_state.questions = questions
    st.session_state.current_question = 0
    st.session_state.score = 0
    st.session_state.answers = []
    st.session_state.quiz_started = True
    st.session_state.quiz_completed = False

def restart_quiz():

    for key in [
        "questions",
        "current_question",
        "score",
        "answers",
        "quiz_started",
        "quiz_completed"
    ]:
        if key in st.session_state:
            del st.session_state[key]

    initialize_quiz()

st.title("🧠 Python Quiz Application")

st.write(
    "Test your Python programming knowledge "
    "with this interactive quiz."
)

st.divider()

if "quiz_started" not in st.session_state:

    st.subheader("🎯 Ready to Start?")

    st.write(
        "This quiz contains at least 10 randomized questions."
    )

    st.info(
        "Select the correct answer for each question. "
        "Your final score will be displayed at the end."
    )

    if st.button(
        "🚀 Start Quiz",
        type="primary",
        use_container_width=True
    ):
        initialize_quiz()
        st.rerun()

elif (
    st.session_state.quiz_started
    and not st.session_state.quiz_completed
):

    questions = st.session_state.questions
    current_index = st.session_state.current_question

    total_questions = len(questions)

    # Progress
    progress = (
        current_index / total_questions
    )

    st.progress(progress)

    st.caption(
        f"Question {current_index + 1} "
        f"of {total_questions}"
    )

    current_question = questions[current_index]

    st.subheader(
        f"Q{current_index + 1}. "
        f"{current_question['question']}"
    )

    # Options
    options = current_question["options"]

    selected_answer = st.radio(
        "Choose your answer:",
        options,
        index=None,
        key=f"question_{current_index}"
    )

    st.write("")

    if st.button(
        "Submit Answer",
        type="primary",
        use_container_width=True
    ):

        # Invalid answer handling
        if selected_answer is None:

            st.warning(
                "⚠️ Please select an answer before submitting."
            )

        else:

            correct_answer = current_question["answer"]

            # Store answer
            st.session_state.answers.append({
                "question": current_question["question"],
                "selected": selected_answer,
                "correct": correct_answer
            })

            # Check answer
            if selected_answer == correct_answer:

                st.session_state.score += 1

                st.success(
                    "✅ Correct answer!"
                )

            else:

                st.error(
                    f"❌ Incorrect. "
                    f"The correct answer is "
                    f"**{correct_answer}**."
                )

            # Move to next question
            if current_index + 1 >= total_questions:

                st.session_state.quiz_completed = True

            else:

                st.session_state.current_question += 1

            st.button(
                "Continue",
                disabled=True
            )

            st.rerun()

elif st.session_state.quiz_completed:

    score = st.session_state.score
    total = len(st.session_state.questions)

    percentage = (score / total) * 100

    st.success("🎉 Quiz Completed!")

    st.subheader("📊 Final Result")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Score",
            f"{score}/{total}"
        )

    with col2:
        st.metric(
            "Percentage",
            f"{percentage:.1f}%"
        )

    with col3:
        st.metric(
            "Questions",
            total
        )

    st.divider()

    # Performance message
    if percentage >= 90:

        st.balloons()

        st.success(
            "🏆 Excellent performance! "
            "You have a strong understanding of Python."
        )

    elif percentage >= 75:

        st.success(
            "👏 Great job! "
            "Your Python fundamentals are strong."
        )

    elif percentage >= 50:

        st.info(
            "👍 Good attempt! "
            "Keep practicing to improve further."
        )

    else:

        st.warning(
            "📚 Keep learning and practicing. "
            "You can improve your score!"
        )

    # Answer summary
    st.subheader("📝 Answer Summary")

    for index, answer in enumerate(
        st.session_state.answers,
        start=1
    ):

        st.write(
            f"**{index}. {answer['question']}**"
        )

        st.write(
            f"Your answer: `{answer['selected']}`"
        )

        st.write(
            f"Correct answer: `{answer['correct']}`"
        )

        if (
            answer["selected"]
            == answer["correct"]
        ):
            st.success("Correct")
        else:
            st.error("Incorrect")

        st.divider()

    # Restart
    if st.button(
        "🔄 Restart Quiz",
        type="primary",
        use_container_width=True
    ):

        restart_quiz()
        st.rerun()

st.divider()

st.caption(
    "Task 24 | CLI Quiz Application | "
    "Python + Streamlit + JSON"
)