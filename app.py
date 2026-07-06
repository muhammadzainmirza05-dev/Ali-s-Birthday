import streamlit as st
import requests
from streamlit_lottie import st_lottie
import time
import os
from PIL import Image

# 1. Page Configuration
st.set_page_config(page_title="Happy Birthday Ali!", page_icon="🎂", layout="centered")

# 2. Helper functions to load animations
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
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        password = st.text_input("Enter the secret password to enter:", type="password")
        login_button = st.button("Unlock Celebration 🎉", use_container_width=True)
        
        # We'll use your password here: 'ali123'
        if login_button:
            if password == "Mohmmad Ali": 
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
        <h1 style='text-align: center; color: #FF4B4B; font-size: 50px; font-family: Arial; font-weight: bold;'>
            🎉 HAPPY BIRTHDAY, ALI! 🎂
        </h1>
    """, unsafe_allow_html=True)
    
    st.write("---")
    
    # --- ADDED: Picture of Ali ---
    # Center the image using columns
    img_col1, img_col2, img_col3 = st.columns([1, 2, 1])
    with img_col2:
        # Step 1: Add a photo named 'ali.jpg' (or ali.png) in your GitHub repo folder
        pic_filename = "ali.jpg" 
        
        if os.path.exists(pic_filename):
            ali_photo = Image.open(pic_filename)
            # This makes the image smaller and centers it
            st.image(ali_photo, caption="Birthday Boy: Ali ❤️", use_column_width=True)
        else:
            # Placeholder/Instruction if the image is missing
            st.info("💡 To show Ali's picture, upload a file named 'ali.jpg' to the same folder where app.py is located on GitHub.")

    # --- UPDATED: Play Audio automatically ---
    # Using the standard Happy Birthday to You audio
    os.path.exists("birthday.mp3")
        st.audio("birthday.mp3", format="audio/mp3", autoplay=True)
    # Display Lottie Animation
    if lottie_cake:
        st_lottie(lottie_cake, height=300, key="cake")
    
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
