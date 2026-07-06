import streamlit as st
import requests
from streamlit_lottie import st_lottie
import time
import os

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

# Load birthday animations
lottie_cake = load_lottieurl("https://lottie.host/809c9584-699a-4c28-98e6-b60fc18ccdc1/MhNcbqK7R9.json")

# 3. Session State for Login Tracking
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

# 4. Login Screen
if not st.session_state['logged_in']:
    st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>🔒 Private Birthday Portal</h1>", unsafe_allow_html=True)
    st.write("---")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        password = st.text_input("Enter the secret password to enter:", type="password")
        login_button = st.button("Unlock Celebration 🎉", use_container_width=True)
        
        if login_button:
            if password.lower() == "ali123": 
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
    st.snow()
    
    # Custom Header styling
    st.markdown("""
        <h1 style='text-align: center; color: #FF4B4B; font-size: 45px; font-family: Arial; font-weight: bold;'>
            🎉 HAPPY BIRTHDAY, ALI! 🎂
        </h1>
    """, unsafe_allow_html=True)
    
    st.write("---")
    
    # Audio Setup (Autoplay feature)
    # Agar birthday.mp3 file maujood hai toh woh play hogi, nahi toh background music play hoga
    if os.path.exists("birthday.mp3"):
        st.audio("birthday.mp3", format="audio/mp3", autoplay=True)
    else:
        # Fallback royalty-free music link agar file upload nahi ki abhi tak
        st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3", format="audio/mp3", autoplay=True)
    
    # Display Lottie Animation
    if lottie_cake:
        st_lottie(lottie_cake, height=250, key="cake")
    
    # Your Personal and Emotional Message Box
    st.markdown("""
        <div style="background-color: #fff5f5; padding: 25px; border-radius: 15px; border-left: 6px solid #FF4B4B; box-shadow: 0px 4px 10px rgba(0,0,0,0.05); margin-top: 20px;">
            <p style="font-size: 18px; color: #2d3748; line-height: 1.8; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;">
                <b>Dear Brother Ali,</b><br><br>
                Happy Birthday my brother Ali, Allah apko dunya or akhirat main kamyab karain. 
                Jo khawahish apke dill main hain wo sub Allah puri karain. Allah Apko acha ghar, gari 
                and family Naseeb karain. Apko bhot success mile. Apke or Apki Family ke sare issues 
                resolve karain and ap sub ke lye asaniyan farmyein. <b>Ameen.</b> ❤️<br><br>
                <span style="color: #e53e3e; font-weight: 500;">
                Ik tum mujh se naraz hoo. main maafi chahta hoon. you are the only one friend i have. 
                i swear to God i miss u everyday. i always think about you. 🥺✨
                </span>
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    st.write("")
    if st.button("Lock App 🔒"):
        st.session_state['logged_in'] = False
        st.rerun()
