import streamlit as st
import random

# Function to run the game logic
def play_game():
    # Initialize session state variables if not already set
    if 'secret_number' not in st.session_state:
        st.session_state.secret_number = random.randint(1, 100)
        st.session_state.attempts = 0
        st.session_state.max_attempts = 10
        st.session_state.game_over = False
        st.session_state.message = ""
        st.session_state.guess_history = []

    # Custom CSS for modern styling
    st.markdown("""
        <style>
            /* Gradient background with animation */
            @keyframes gradientAnimation {
                0% { background-position: 0% 50%; }
                50% { background-position: 100% 50%; }
                100% { background-position: 0% 50%; }
            }
            body {
                background: linear-gradient(135deg, #6a11cb, #2575fc, #6a11cb);
                background-size: 400% 400%;
                animation: gradientAnimation 15s ease infinite;
                font-family: 'Poppins', sans-serif;
                color: white;
            }
            /* Glassmorphism container */
            .main-container {
                background: rgba(255, 255, 255, 0.1);
                backdrop-filter: blur(10px);
                border-radius: 20px;
                border: 1px solid rgba(255, 255, 255, 0.2);
                padding: 30px;
                margin: 20px auto;
                max-width: 600px;
                box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
            }
            /* Title styling */
            .title {
                font-size: 48px !important;
                font-weight: 700;
                color: #6a11cb, #2575fc;
                text-align: center;
                margin-bottom: 20px;
                text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
            }
            /* Subtitle styling */
            .subtitle {
                font-size: 24px !important;
                color: rgba#c3bdbd;
                text-align: center;
                margin-bottom: 20px;
            }
            /* Message styling */
            .message {
                font-size: 20px !important;
                font-weight: 600;
                color: white;
                text-align: center;
                padding: 15px;
                border-radius: 10px;
                background: rgba(255, 255, 255, 0.1);
                backdrop-filter: blur(5px);
                margin-bottom: 20px;
                box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1);
            }
            /* Button styling */
            .stButton>button {
                background: linear-gradient(135deg, #6a11cb, #2575fc);
                color: white;
                padding: 12px 28px;
                border-radius: 12px;
                border: none;
                font-size: 18px;
                font-weight: 600;
                transition: transform 0.3s ease, box-shadow 0.3s ease;
                width: 100%;
                box-shadow: 0 4px 16px rgba(0, 0, 0, 0.2);
            }
            .stButton>button:hover {
                transform: scale(1.05);
                box-shadow: 0 6px 20px rgba(0, 0, 0, 0.3);
            }
            /* Progress bar styling */
            .progress-bar {
                background: rgba(255, 255, 255, 0.2);
                border-radius: 10px;
                padding: 3px;
                margin-bottom: 20px;
            }
            .progress-bar-fill {
                background: linear-gradient(135deg, #6a11cb, #2575fc);
                height: 20px;
                border-radius: 10px;
                transition: width 0.5s ease;
            }
            /* Guess history styling */
            .guess-history {
                font-size: 16px;
                color: rgba(255, 255, 255, 0.9);
                margin-top: 20px;
                background: rgba(255, 255, 255, 0.1);
                backdrop-filter: blur(5px);
                padding: 15px;
                border-radius: 10px;
                box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1);
            }
            .guess-history ul {
                list-style-type: none;
                padding: 0;
            }
            .guess-history li {
                padding: 10px;
                background: rgba(255, 255, 255, 0.1);
                margin-bottom: 5px;
                border-radius: 5px;
            }
            /* Input field styling */
            .stNumberInput>div>div>input {
                background: rgba(255, 255, 255, 0.1);
                color: white;
                border: 1px solid rgba(255, 255, 255, 0.2);
                border-radius: 10px;
                padding: 10px;
            }
            .stNumberInput>div>div>input:focus {
                border-color: #6a11cb;
                box-shadow: 0 0 8px rgba(106, 17, 203, 0.5);
            }
        </style>
        """, unsafe_allow_html=True)

    # Main container
    st.markdown('<div class="main-container">', unsafe_allow_html=True)

    # Title and subtitle
    st.markdown('<p class="title">🎮 Number Guessing Game 🎮</p>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Can you guess the number between 1 and 100? 🧐</p>', unsafe_allow_html=True)

    # Progress bar for attempts
    progress = st.session_state.attempts / st.session_state.max_attempts
    st.markdown(f"""
        <div class="progress-bar">
            <div class="progress-bar-fill" style="width: {progress * 100}%;"></div>
        </div>
        <p style="text-align: center; font-size: 16px; color: rgba(255, 255, 255, 0.9);">
            Attempts: {st.session_state.attempts} / {st.session_state.max_attempts}
        </p>
    """, unsafe_allow_html=True)

    # Input for player's guess
    guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1, key="guess_input")

    # Button to submit guess
    if st.button("🚀 Submit Guess") and not st.session_state.game_over:
        st.session_state.attempts += 1
        st.session_state.guess_history.append(guess)

        if guess == st.session_state.secret_number:
            st.session_state.message = f"🎉🎉 **Congratulations!** You guessed the number **{st.session_state.secret_number}** in **{st.session_state.attempts}** attempts! 🎉🎉"
            st.session_state.game_over = True
        elif guess < st.session_state.secret_number:
            st.session_state.message = "⬆️ **Too low!** Try a higher number."
        else:
            st.session_state.message = "⬇️ **Too high!** Try a lower number."

        if st.session_state.attempts >= st.session_state.max_attempts:
            st.session_state.message = f"😢 **Game Over!** The number was **{st.session_state.secret_number}**. Better luck next time! 😢"
            st.session_state.game_over = True

    # Display the message
    if st.session_state.message:
        st.markdown(f'<p class="message">{st.session_state.message}</p>', unsafe_allow_html=True)

    # Display guess history
    if st.session_state.guess_history:
        st.markdown('<p class="guess-history">📜 <strong>Your Guess History:</strong></p>', unsafe_allow_html=True)
        history_html = "<ul>"
        for g in st.session_state.guess_history:
            if g < st.session_state.secret_number:
                history_html += f"<li>⬆️ {g} (Too low)</li>"
            elif g > st.session_state.secret_number:
                history_html += f"<li>⬇️ {g} (Too high)</li>"
            else:
                history_html += f"<li>🎯 {g} (Correct!)</li>"
        history_html += "</ul>"
        st.markdown(f'<div class="guess-history">{history_html}</div>', unsafe_allow_html=True)

    # Play again button
    if st.session_state.game_over:
        if st.button("🔄 Play Again"):
            # Reset the game
            st.session_state.secret_number = random.randint(1, 100)
            st.session_state.attempts = 0
            st.session_state.game_over = False
            st.session_state.message = ""
            st.session_state.guess_history = []
            st.rerun()  # Rerun the app to refresh the UI

    # Close main container
    st.markdown('</div>', unsafe_allow_html=True)

# Run the game
if __name__ == "__main__":
    play_game()