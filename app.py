import streamlit as st
import requests
from streamlit_lottie import st_lottie
import time

# 1. Page Configuration
st.set_page_config(page_title="Happy Birthday Ali!", page_icon="🎂", layout="centered")

# 2. Helper function to load Lottie Animations
def load_lottieurl(url: str):
    try:
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    except Exception:
        return None

# Load birthday animations from public Lottie links
lottie_cake = load_lottieurl("https://lottie.host/809c9584-699a-4c28-98e6-b60fc18ccdc1/MhNcbqK7R9.json")
lottie_confetti = load_lottieurl("https://lottie.host/ddb70bda-d7a5-4f36-9b0d-ce0b8e6270b2/9ZpPbe6n8C.json")

# 3. Session State for Login Tracking
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

# 4. Login Screen
if not st.session_state['logged_in']:
    st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>🔒 Private Birthday Portal</h1>", unsafe_allow_html=True)
    st.write("---")
    
    # Center the login box
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        password = st.text_input("Enter the secret password to enter:", type="password")
        login_button = st.button("Unlock Celebration 🎉", use_container_width=True)
        
        # Define your password here (e.g., 'ali2026' or 'bestbrother')
        if login_button:
            if password.lower() == "Mohmmad Ali": 
                st.session_state['logged_in'] = True
                st.success("Access Granted! Loading your surprise...")
                time.sleep(1)
                st.rerun()
            else:
                st.error("Incorrect password! Try again.")

# 5. Celebration Screen (After successful login)
else:
    # Trigger Streamlit's built-in balloon celebration
    st.balloons()
    
    # Custom Header styling
    st.markdown("""
        <h1 style='text-align: center; color: #FF4B4B; font-size: 50px; font-family: Arial;'>
            🎉 HAPPY BIRTHDAY, ALI! 🎂
        </h1>
    """, unsafe_allow_html=True)
    
    st.write("---")
    
    # Display Lottie Animation
    if lottie_cake:
        st_lottie(lottie_cake, height=300, key="cake")
    else:
        # Fallback if the URL fails to load
        st.header("🎂🎈✨🎁🎉")

    # Birthday Message Box
    st.markdown("""
        <div style="background-color: #f0f2f6; padding: 20px; border-radius: 10px; border-left: 5px solid #FF4B4B;">
            <p style="font-size: 18px; color: #31333F; line-height: 1.6;">
                <b>Dearest Ali,</b><br>
                Wishing you a fantastic year ahead filled with endless happiness, great health, and massive success! 
                Thank you for being an amazing brother. Today is all about celebrating you! 🥂✨
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # Secondary celebration effect (Snow-like sparkle effect)
    st.snow()
    
    # Optional: Log out button to reset the app
    st.write("")
    if st.button("Lock App 🔒"):
        st.session_state['logged_in'] = False
        st.rerun()