import streamlit as st
from ques_cl import questions
import time

class Question:
    def __init__(self, text, options, correct_option):
        self.text = text
        self.options = options
        self.correct_option = correct_option

def display_question(question):
    st.write(question.text)
    selected_option = st.radio("Select an answer:", question.options)
    return selected_option

def calculate_score(questions, user_responses):
    score = 0
    for i, question in enumerate(questions):
        if question.correct_option == user_responses[i]:
            score += 1
    return score

def main():
    
    st.title("Round 1 birthday quiz")
    if 'user_responses' not in st.session_state:
        st.session_state.user_responses = []
    if 'trys' not in st.session_state:
        st.session_state.trys = 0

    st.session_state.user_responses = ['' for i in range(5)]

    st.session_state.user_responses[0] = display_question(questions[0])
    st.session_state.user_responses[1] = display_question(questions[1])
    st.session_state.user_responses[2] = display_question(questions[2])
    st.session_state.user_responses[3] = display_question(questions[3])
    st.session_state.user_responses[4] = display_question(questions[4])



    if st.button('Submit'):

        score = calculate_score(questions, st.session_state.user_responses)
        st.subheader("Quiz Result")
        time.sleep(3**st.session_state.trys)
        st.write(f"You scored {score}/{len(questions)}")
        st.session_state.trys += 1

if __name__ == "__main__":
    
    main()

