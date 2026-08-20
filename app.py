import streamlit as st
import requests
from streamlit_lottie import st_lottie
import time
import os
from PIL import Image

# ── Page Config ────────────────────────────────────────────────
st.set_page_config(page_title="Happy Birthday Ali!", page_icon="🎂", layout="centered")

# ── Global CSS Override ─────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;0,900;1,400&family=Inter:wght@300;400;500;600&display=swap');

/* ── Hide Streamlit chrome ── */
#MainMenu, footer, header,
[data-testid="stToolbar"],
[data-testid="stDecoration"],
.stDeployButton { display: none !important; }

/* ── Cosmic Background ── */
.stApp {
    background: radial-gradient(ellipse at 20% 10%, #1a0a3e 0%, #080818 45%, #0b1a2e 100%);
    font-family: 'Inter', sans-serif;
}

/* Starfield overlay */
.stApp::before {
    content: '';
    position: fixed;
    inset: 0;
    background-image:
        radial-gradient(1px 1px at 8%  15%, rgba(255,255,255,.55) 0%, transparent 100%),
        radial-gradient(1px 1px at 22% 6%,  rgba(255,255,255,.40) 0%, transparent 100%),
        radial-gradient(2px 2px at 38% 20%, rgba(255,215,0,.50)   0%, transparent 100%),
        radial-gradient(1px 1px at 55% 9%,  rgba(255,255,255,.35) 0%, transparent 100%),
        radial-gradient(1px 1px at 74% 3%,  rgba(201,184,255,.45) 0%, transparent 100%),
        radial-gradient(2px 2px at 90% 14%, rgba(255,107,138,.40) 0%, transparent 100%),
        radial-gradient(1px 1px at 4%  55%, rgba(255,255,255,.40) 0%, transparent 100%),
        radial-gradient(1px 1px at 18% 72%, rgba(201,184,255,.50) 0%, transparent 100%),
        radial-gradient(2px 2px at 33% 88%, rgba(255,215,0,.35)   0%, transparent 100%),
        radial-gradient(1px 1px at 50% 65%, rgba(255,255,255,.30) 0%, transparent 100%),
        radial-gradient(1px 1px at 67% 80%, rgba(255,255,255,.40) 0%, transparent 100%),
        radial-gradient(1px 1px at 83% 60%, rgba(201,184,255,.35) 0%, transparent 100%),
        radial-gradient(2px 2px at 96% 78%, rgba(255,107,138,.35) 0%, transparent 100%),
        radial-gradient(1px 1px at 12% 93%, rgba(255,255,255,.30) 0%, transparent 100%),
        radial-gradient(1px 1px at 78% 95%, rgba(255,255,255,.35) 0%, transparent 100%);
    pointer-events: none;
    z-index: 0;
}

/* Content above starfield */
.main .block-container {
    position: relative;
    z-index: 1;
    padding: 2.5rem 1.5rem 3rem;
    max-width: 680px;
}

/* ── Text Input ── */
div[data-testid="stTextInput"] label {
    color: #c9b8ff !important;
    font-size: 11px !important;
    font-weight: 600 !important;
    letter-spacing: 0.14em !important;
    text-transform: uppercase !important;
    margin-bottom: 6px !important;
}

div[data-testid="stTextInput"] input {
    background: rgba(255,255,255,0.06) !important;
    border: 1px solid rgba(255,107,138,0.30) !important;
    border-radius: 14px !important;
    color: #f0e6ff !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 15px !important;
    padding: 14px 18px !important;
    caret-color: #ff6b8a;
    transition: border-color .25s, box-shadow .25s, background .25s;
}

div[data-testid="stTextInput"] input::placeholder {
    color: rgba(201,184,255,0.3) !important;
}

div[data-testid="stTextInput"] input:focus {
    border-color: #ff6b8a !important;
    background: rgba(255,107,138,0.07) !important;
    box-shadow: 0 0 28px rgba(255,107,138,0.22) !important;
}

/* ── Buttons ── */
.stButton > button {
    background: linear-gradient(135deg, #ff6b8a 0%, #d63a72 100%) !important;
    color: #fff !important;
    border: none !important;
    border-radius: 14px !important;
    font-family: 'Inter', sans-serif !important;
    font-weight: 600 !important;
    font-size: 15px !important;
    padding: 13px 28px !important;
    letter-spacing: 0.04em !important;
    box-shadow: 0 4px 28px rgba(255,107,138,0.38) !important;
    transition: transform .25s, box-shadow .25s !important;
    width: 100%;
}

.stButton > button:hover {
    transform: translateY(-3px) !important;
    box-shadow: 0 12px 40px rgba(255,107,138,0.55) !important;
}

.stButton > button:active { transform: translateY(0) !important; }

/* ── Alerts ── */
div[data-testid="stAlert"] {
    border-radius: 14px !important;
    backdrop-filter: blur(8px);
}

/* ── Divider ── */
hr {
    border: none !important;
    border-top: 1px solid rgba(255,107,138,0.15) !important;
    margin: 1.8rem 0 !important;
}

/* ── Image ── */
[data-testid="stImage"] img {
    border-radius: 20px !important;
    border: 2px solid rgba(255,107,138,0.28) !important;
    box-shadow: 0 16px 48px rgba(255,107,138,0.18) !important;
}

/* ── Audio ── */
audio {
    width: 100% !important;
    border-radius: 12px !important;
    margin: 0.6rem 0 !important;
    opacity: .85;
}

/* ── Scrollbar ── */
::-webkit-scrollbar { width: 5px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb {
    background: rgba(255,107,138,0.28);
    border-radius: 10px;
}

/* ── Keyframes ── */
@keyframes shimmer {
    from { background-position: -200% center; }
    to   { background-position:  200% center; }
}
@keyframes float {
    0%, 100% { transform: translateY(0px); }
    50%       { transform: translateY(-10px); }
}
@keyframes fadeUp {
    from { opacity: 0; transform: translateY(24px); }
    to   { opacity: 1; transform: translateY(0); }
}
</style>
""", unsafe_allow_html=True)


# ── Helpers ────────────────────────────────────────────────────
def load_lottieurl(url: str):
    try:
        r = requests.get(url)
        return r.json() if r.status_code == 200 else None
    except Exception:
        return None

lottie_cake     = load_lottieurl("https://lottie.host/809c9584-699a-4c28-98e6-b60fc18ccdc1/MhNcbqK7R9.json")
lottie_confetti = load_lottieurl("https://lottie.host/ddb70bda-d7a5-4f36-9b0d-ce0b8e6270b2/9ZpPbe6n8C.json")

if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False


# ══════════════════════════════════════════════════════════════
#  LOGIN SCREEN
# ══════════════════════════════════════════════════════════════
if not st.session_state['logged_in']:

    st.markdown("""
    <div style='text-align:center; padding: 2rem 0 2.5rem; animation: fadeUp .7s ease both;'>
        <div style='font-size: 60px; display: inline-block; animation: float 3s ease-in-out infinite; filter: drop-shadow(0 0 24px rgba(255,107,138,.55)); margin-bottom: 16px;'>🎂</div>
        <h1 style='font-family: Playfair Display, serif; font-size: 2.3rem; font-weight: 900; color: #f0e6ff; margin: 0 0 10px; letter-spacing: -0.01em; text-shadow: 0 0 40px rgba(255,107,138,.25);'>Private Birthday Portal</h1>
        <p style='color: rgba(201,184,255,.5); font-size: 11.5px; font-weight: 400; letter-spacing: .18em; text-transform: uppercase; margin: 0;'>A special surprise awaits ✨</p>
    </div>
    """, unsafe_allow_html=True)

    # Login card shell (visual only)
    st.markdown("<div style='background: rgba(255,255,255,0.04); border: 1px solid rgba(255,107,138,0.18); border-radius: 24px; padding: 2.4rem 2rem 2rem; margin: 0 auto; box-shadow: 0 24px 64px rgba(0,0,0,.45), inset 0 1px 0 rgba(255,255,255,.06); animation: fadeUp .8s ease .15s both;'>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([0.5, 5, 0.5])
    with col2:
        password = st.text_input("Secret Password", type="password", placeholder="Enter the magic word…")
        st.write("")
        login_btn = st.button("Unlock Celebration 🎉", use_container_width=True)

        if login_btn:
            if password == "Mohmmad Ali":
                st.session_state['logged_in'] = True
                st.success("✅ Access granted! Loading your surprise…")
                time.sleep(1)
                st.rerun()
            else:
                st.error("❌ Wrong password — try again!")

    st.markdown("</div>", unsafe_allow_html=True)  # close card shell

    st.markdown("<p style='text-align:center; color: rgba(201,184,255,.22); font-size: 11px; letter-spacing: .08em; margin-top: 2.2rem;'>Made with ❤️ — for someone special</p>", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════
#  CELEBRATION SCREEN
# ══════════════════════════════════════════════════════════════
else:
    st.balloons()
    st.snow()

    # ── Hero Header ──
    st.markdown("<div style='text-align:center; padding: 1.5rem 0 2rem; animation: fadeUp .6s ease both;'><div style='font-size: 65px; display: inline-block; animation: float 3s ease-in-out infinite; filter: drop-shadow(0 0 30px rgba(255,215,0,.6)); margin-bottom: 14px;'>🎂</div><h1 style='font-family: Playfair Display, serif; font-size: clamp(2rem, 8vw, 3.2rem); font-weight: 900; background: linear-gradient(90deg, #ff6b8a, #ffd700, #c9b8ff, #ff6b8a); background-size: 200% auto; -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; animation: shimmer 3.5s linear infinite; margin: 0 0 10px; line-height: 1.15;'>Happy Birthday,<br>Ali! 🎉</h1><p style='color: rgba(201,184,255,.48); font-size: 11.5px; letter-spacing: .18em; text-transform: uppercase; margin: 0;'>A birthday surprise — just for you ✨</p></div>", unsafe_allow_html=True)

    st.write("---")

    # ── Photo ──
    c1, c2, c3 = st.columns([1, 2, 1])
    with c2:
        if os.path.exists("ali.jpg"):
            ali_photo = Image.open("ali.jpg")
            st.image(ali_photo, caption="Birthday Boy: Ali ❤️", use_container_width=True)
        else:
            st.markdown("<div style='background: rgba(255,107,138,0.07); border: 1px dashed rgba(255,107,138,0.28); border-radius: 20px; padding: 2rem; text-align: center; color: rgba(201,184,255,.55); font-size: 13.5px; line-height: 1.7;'>📷 Add <code style='color:#ff6b8a; background:rgba(255,107,138,.12); padding:2px 6px; border-radius:5px;'>ali.jpg</code> to your repo folder to display Ali's photo here.</div>", unsafe_allow_html=True)

    st.write("")

    # ── Audio ──
    if os.path.exists("birthday.mp3"):
        st.audio("birthday.mp3", format="audio/mp3", autoplay=True)
    else:
        st.audio(
            "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3",
            format="audio/mp3", autoplay=True
        )

    # ── Lottie Animation ──
    if lottie_cake:
        st_lottie(lottie_cake, height=260, key="cake")

    # ── Personal Message Card ──
    st.markdown("""
    <div style='background: rgba(255,107,138,0.05); border: 1px solid rgba(255,107,138,0.18); border-left: 4px solid #ff6b8a; border-radius: 22px; padding: 2.2rem 2rem; margin: 1.2rem 0 1.8rem; box-shadow: 0 12px 48px rgba(0,0,0,.35), inset 0 1px 0 rgba(255,255,255,.05); backdrop-filter: blur(12px); animation: fadeUp .8s ease .2s both;'>
        <p style='font-family: Playfair Display, serif; font-size: 1.2rem; font-style: italic; color: #ff6b8a; font-weight: 700; margin: 0 0 1.1rem;'>Dear Brother Ali,</p>
        <p style='font-family: Inter, sans-serif; font-size: 15.5px; color: rgba(240,230,255,.85); line-height: 1.9; font-weight: 300; margin: 0 0 1.3rem;'>
            Happy Birthday my brother Ali! Allah aapko dunya aur akhirat mein kamyab karein.
            Jo khwahishein aapke dil mein hain, woh sab Allah puri karein. Allah aapko acha ghar, gaari,
            aur family naseeb karein. Aapko bohat success mile. Aapke aur aapki family ke saare issues
            resolve karein aur aap sab ke liye asaniyan farmayein.
            <strong style='color:#ffd700; font-weight:600;'>Ameen.</strong> ❤️
        </p>
        <div style='background: rgba(255,107,138,0.07); border-radius: 14px; padding: 1.1rem 1.3rem; border-left: 2px solid rgba(255,107,138,0.35);'>
            <p style='font-family: Inter, sans-serif; font-size: 15px; color: rgba(255,185,200,.88); line-height: 1.85; margin: 0; font-style: italic; font-weight: 300;'>
                Ik tum mujhse naraz ho, main maafi chahta hoon. You are the only friend I have.
                I swear to God, I miss you every day. I always think about you. 🥺✨
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ── Lock Button ──
    lc1, lc2, lc3 = st.columns([1, 2, 1])
    with lc2:
        if st.button("🔒  Lock App", use_container_width=True):
            st.session_state['logged_in'] = False
            st.rerun()

    st.markdown("<p style='text-align:center; color: rgba(201,184,255,.2); font-size: 11px; letter-spacing: .08em; margin-top: 2rem;'>✨ Made with love — a surprise just for Ali ✨</p>", unsafe_allow_html=True)
