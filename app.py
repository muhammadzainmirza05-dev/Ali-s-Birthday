import streamlit as st
import requests
from streamlit_lottie import st_lottie
import time
import os
from PIL import Image

# 1. Page Configuration (Must be the first command)
st.set_page_config(page_title="Happy Birthday Ali!", page_icon="🎂", layout="centered")

# --- CUSTOM CSS INJECTION ---
# This completely changes the look of Streamlit
st.markdown("""
<style>
    /* Import Google Font */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');

    /* Hide Streamlit Branding */
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}

    /* Apply global font and background */
    html, body, [class*="css"]  {
        font-family: 'Poppins', sans-serif;
    }
    
    .stApp {
        background: linear-gradient(135deg, #fff3f3 0%, #ffdfdf 100%);
    }

    /* Style the input box */
    .stTextInput > div > div > input {
        border-radius: 15px;
        border: 2px solid #FF4B4B;
        padding: 10px;
        text-align: center;
    }

    /* Style the buttons */
    div.stButton > button:first-child {
        background-color: #FF4B4B;
        color: white;
        border-radius: 25px;
        border: none;
        padding: 10px 24px;
        font-weight: 600;
        font-size: 16px;
        transition: all 0.3s ease;
        box-shadow: 0px 4px 10px rgba(255, 75, 75, 0.3);
    }
    
    div.stButton > button:first-child:hover {
        background-color: #e63946;
        transform: translateY(-2px);
        box-shadow: 0px 6px 15px rgba(255, 75, 75, 0.5);
    }
    
    /* Beautiful Message Box */
    .message-box {
        background: white;
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0px 10px 25px rgba(0,0,0,0.08);
        border-top: 8px solid #FF4B4B;
        margin-top: 20px;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

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
    st.markdown("<br><br><br>", unsafe_allow_html=True) # Adds breathing room at the top
    st.markdown("<h1 style='text-align: center; color: #FF4B4B; font-weight: 700;'>🔒 Private Birthday Portal</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #555;'>A special surprise awaits. Please verify your identity.</p>", unsafe_allow_html=True)
    st.write("")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        password = st.text_input("", placeholder="Enter the secret password...", type="password")
        login_button = st.button("Unlock Celebration 🎉", use_container_width=True)
        
        if login_button:
            if password == "Mohmmad Ali": 
                st.session_state['logged_in'] = True
                st.success("✨ Access Granted! Preparing your surprise...")
                time.sleep(1.5)
                st.rerun()
            else:
                st.error("Incorrect password! Try again.")

# 5. Celebration Screen (After successful login)
else:
    # Trigger Streamlit's built-in balloon celebration
    st.balloons()
    
    # Custom Header styling
    st.markdown("""
        <h1 style='text-align: center; color: #FF4B4B; font-size: 55px; font-weight: 800; text-shadow: 2px 2px 4px rgba(0,0,0,0.1); margin-bottom: 0px;'>
            🎉 HAPPY BIRTHDAY, ALI! 🎂
        </h1>
    """, unsafe_allow_html=True)
    
    # Adding the confetti animation you loaded at the top
    if lottie_confetti:
        st_lottie(lottie_confetti, height=150, key="confetti")
    
    # --- Picture of Ali ---
    img_col1, img_col2, img_col3 = st.columns([1, 2, 1])
    with img_col2:
        pic_filename = "ali.jpg" 
        if os.path.exists(pic_filename):
            ali_photo = Image.open(pic_filename)
            st.image(ali_photo, caption="Birthday Boy: Ali ❤️", use_container_width=True)
        else:
            st.info("💡 Upload 'ali.jpg' to the folder to display a photo here.")

    # --- Play Audio automatically ---
    if os.path.exists("birthday.mp3"):
        st.audio("birthday.mp3", format="audio/mp3", autoplay=True)
    else:
        # Fallback music just in case
        st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3", format="audio/mp3", autoplay=True)
        
    # Display Lottie Cake Animation
    if lottie_cake:
        st_lottie(lottie_cake, height=250, key="cake")
    
    # Your Personal and Emotional Message Box using custom CSS class
    st.markdown("""
        <div class="message-box">
            <h3 style="color: #FF4B4B; margin-top: 0;">Dear Brother Ali,</h3>
            <p style="font-size: 18px; color: #2d3748; line-height: 1.8;">
                Happy Birthday my brother Ali! Allah aapko dunya aur akhirat mein kamyab karein. 
                Jo khwahishein aapke dil mein hain, woh sab Allah puri karein. Allah aapko acha ghar, gaari, 
                aur family naseeb karein. Aapko bohat success mile. Aapke aur aapki family ke saare issues 
                resolve karein aur aap sab ke liye asaniyan farmayein. <b>Ameen.</b> ❤️
            </p>
            <hr style="border: 1px solid #ffdfdf; margin: 20px 0;">
            <p style="font-size: 19px; color: #e53e3e; font-weight: 600; line-height: 1.6;">
                Ik tum mujhse naraz ho, main maafi chahta hoon. You are the only friend I have.<br>
                I swear to God, I miss you every day. I always think about you. 🥺✨
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Lock Button
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("Lock App 🔒", use_container_width=True):
            st.session_state['logged_in'] = False
            st.rerun()
