import streamlit as st
from pathlib import Path
from PIL import Image
import base64

THIS_DIR = Path(__file__).parent
image1 = THIS_DIR / "images" / "pic1.jpg"
image2 = THIS_DIR / "images" / "pic2.jpg"
image3 = THIS_DIR / "images" / "pic3.jpg"
image4 = THIS_DIR / "images" / "pic4.jpg"
image5 = THIS_DIR / "images" / "pic5.jpg"
image6 = THIS_DIR / "images" / "pic6.jpg"
image7_path = THIS_DIR / "images" / "pic7.jpg"

audio_path = THIS_DIR / "images" / "audio.mp3"  

# --- Helpers ---
def autoplay_audio(file_path: str, file_type: str = "audio/mp3"):
    try:
        with open(file_path, "rb") as f:
            data = f.read()
            b64 = base64.b64encode(data).decode()
            md = f"""
                <audio autoplay loop style="display:none;">
                    <source src="data:{file_type};base64,{b64}" type="{file_type}">
                </audio>
            """
            st.markdown(md, unsafe_allow_html=True)
    except FileNotFoundError:
        st.error("Audio file not found. Please check the file path.")

# Page config
st.set_page_config(page_title="Happy Valentine's Day ❤️", page_icon="💖")

# ✅ Call autoplay once, early
autoplay_audio(str(audio_path), "audio/mp3")

# Load + rotate pic7 using PIL (because rotate won't work on a Path)
image7 = Image.open(image7_path).rotate(-90, expand=True)

st.markdown("""
<style>
/* Main app background */
[data-testid="stAppViewContainer"] {
    background-color: #ff99cc;
}

/* Optional: sidebar background */
[data-testid="stSidebar"] {
    background-color: #ffccdd;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>

/* Target Streamlit buttons */
div.stButton > button {
    background-color: #ff4da6;
    color: white;
    border-radius: 12px;
    border: none;
    padding: 0.6em 1.2em;
    font-size: 18px;
    font-weight: bold;
}

/* Hover effect */
div.stButton > button:hover {
    background-color: #ff1a8c;
    color: white;
}

</style>
""", unsafe_allow_html=True)



# Title
st.title("TO MY BEAUTIFUL WIFEY ❤️")
st.write("A little surprise made with love 💕")

images = [image2,image1,image3,image4,image5,image6,image7]

captions = [
    "Our first Valentines date 💑",
    "Our very first BingSu together ✨",
    "The first time I gave you flowers 🌹",
    "You have the smiles that light up my life 💕",
    "And you're forever my favorite person 💖",
    "I LOVE YOU SO MUCH BABYY💋",
    "HAPPY VALENTINES DAY MY ONE AND ONLY😘"
]

for i, (img, caption) in enumerate(zip(images, captions)):

    col1, col2 = st.columns([1, 1], gap="large")

    if i % 2 == 0:
        # Image LEFT
        with col1:
            st.image(img, use_container_width=True)

        # Caption RIGHT (centered)
        with col2:
            st.markdown(
                f"""
                <div style="
                    display:flex;
                    justify-content:center;
                    align-items:center;
                    text-align:center;
                    height:100%;
                    font-size:24px;
                    padding:20px;
                ">
                    💖 {caption}
                </div>
                """,
                unsafe_allow_html=True
            )

    else:
        # Caption LEFT (centered)
        with col1:
            st.markdown(
                f"""
                <div style="
                    display:flex;
                    justify-content:center;
                    align-items:center;
                    text-align:center;
                    height:100%;
                    font-size:24px;
                    padding:20px;
                ">
                    {caption} 💕
                </div>
                """,
                unsafe_allow_html=True
            )

        # Image RIGHT
        with col2:
            st.image(str(img), use_container_width=True)

    st.write("")
    st.write("")

# Button to reveal message
if st.button("Click for a Special Message 💌"):
    st.snow()
    st.markdown("""
<div style="
    background-color:##ffd6e7;
    padding:25px;
    border-radius:15px;
    color:white;
    font-size:14px;
    text-align:left;
    box-shadow:0 0 25px rgba(255, 0, 128, 0.6);
">
    <b>My hot and gorgeous wifey ❤️</b><br><br>
    From the moment you came into my life, everything became brighter, warmer, and more beautiful.<br>
    You are my peace, my happiness, and my truly my daylight.<br>
    I’m so grateful for every laugh, every hug, and every memory we share.  
    I promise to love you, support you, and cherish you today and always.<br>
    And I AM TRULY THE LUCKIEST GUY IN THE WHOLE UNIVERSE!!<br><br>
    Happy Valentine's Day once again, my hottie💖
</div>
""", unsafe_allow_html=True)
    
    
    #st.info("""
    #My hot and gorgeous wifey❤️,

    #From the moment you came into my life, everything became brighter, warmer, and more beautiful.  
    #You are my peace, my happiness, and truly my daylight. 

    #I’m so grateful for every laugh, every hug, and every memory we share.  
    #I promise to love you, support you, and cherish you today and always.

    #And I AM TRULY THE LUCKIEST GUY IN THE WHOLE UNIVERSE!!

    #Happy Valentine's Day once again, my hottie💖
    #""")
