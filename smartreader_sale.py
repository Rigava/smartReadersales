import streamlit as st
from PIL import Image
from pathlib import Path

# --- PATH SETTINGS ---
THIS_DIR = Path(__file__).parent if "__file__" in locals() else Path.cwd()
ASSETS_DIR = THIS_DIR / "media"
STYLES_DIR = THIS_DIR / "styles"
CSS_FILE = STYLES_DIR / "main.css"


# --- GENERAL SETTINGS ---
STRIPE_COFFEE = "https://buy.stripe.com/test_aEUcNy6kTdR5e3eaEG" 
STRIPE_CHECKOUT = "https://buy.stripe.com/test_14k5l6dNlaETcZa145"
CONTACT_EMAIL = "shuniya064@gmail.COM"
DEMO_VIDEO = "https://joshpdfapp.streamlit.app/"
PRODUCT_NAME = "Smart Reader"
PRODUCT_TAGLINE = "Summarize articles in seconds so you can focus on what's important 🚀"
PRODUCT_DESCRIPTION = """
Smart Reader is an interactive app that uses artificial intelligence to help you find insights in your articles, 
papers,and other long-form content. It's perfect for students, professionals, 
and anyone else who wants to save time and get the most out of their reading.

- Get the key insights from your reading in minutes.
- It does a summary from the most of the relevant pages.

**Stay ahead of the curve with our easy-to-use Smart Reader**
"""

def load_css_file(css_file_path):
    with open(css_file_path) as f:
        return st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# --- PAGE CONFIG ---
st.set_page_config(
    page_title=PRODUCT_NAME,
    page_icon=":orange_heart:", #https://www.webfx.com/tools/emoji-cheat-sheet/
    layout="centered",
    initial_sidebar_state="collapsed",
)

load_css_file(CSS_FILE)

# --- MAIN SECTION ---
st.header(PRODUCT_NAME)
st.subheader(PRODUCT_TAGLINE)
left_col, right_col = st.columns((2, 1))
with left_col:
    st.text("")
    st.write(PRODUCT_DESCRIPTION)
    st.markdown(
        f'<a href={STRIPE_COFFEE} class="button">👉 Enjoy</a>',
        unsafe_allow_html=True,
    )
with right_col:
    product_image = Image.open(ASSETS_DIR / "ai.jpg")
    st.image(product_image, width=450)


# --- FEATURES ---
st.write("")
st.write("---")
st.subheader(":rocket: Features")
features = {
    "Feature_1.png": [
        "Load pdf file upto 200 MB",
        "In the Pro Version, you can also add multiple pdf files. This is helpful when you need to combine information from different domain.",
    ],
    "Feature_2.png": [
        "Create summary using the question and answering interface",
        "In the pro version get a comprehensive summary from multiple pdf files"
    ],
    "Feature_3.png": [
        "Chat with your document",
        "Have you ever wanted to do some quick chat with your document? Smart Reader can answer wide variety of question. This feature is a real time saver!",
    ],
}
for image, description in features.items():
    image = Image.open(ASSETS_DIR / image)
    new_image = image.resize((180,80))
    st.write("")
    left_col, right_col = st.columns(2)
    left_col.image(new_image, use_column_width=True)
    right_col.write(f"**{description[0]}**")
    right_col.write(description[1])


# --- DEMO ---
st.write("")
st.write("---")
st.subheader(":tv: Demo")

# st.video(DEMO_VIDEO, format="video/mp4", start_time=0)
st.markdown(
    f'<a href={DEMO_VIDEO} class="button">👉 Get the demo of whats in there</a>',
    unsafe_allow_html=True,
)

# --- FAQ ---
st.write("")
st.write("---")
st.subheader(":raising_hand: FAQ")
faq = {
    "What is Smart Reader?": "Smart Reader is an AI-powered app that helps smart people quickly and efficiently summarize articles. The app uses cutting-edge natural language processing technology to identify the key points of an article and generate a concise summary. This allows students to save time and focus on more important tasks, such as studying and completing assignments",
    "How much does Smart Reader cost?": "Smart Reader is available for free, however if you need the source code or want to customise the application lets talk.",
    "What are the benefits of using Smart Reader?": """ 
    * Save time: Smart Reader can help students save time by quickly and efficiently summarizing articles. This allows students to focus on more important tasks, such as studying and completing assignments.
    * Improve focus:  can help working professional improve their focus by reducing the amount of time they spend reading articles. This allows working professional to stay on track and avoid getting distracted.       
    * Improve grades: can help students improve their grades by providing them with concise summaries of articles. This allows students to better understand the material and perform better on exams.
    """,
    "Is Smart Reader compatible with all devices?": "Smart Reader is compatible with all devices that have a web browser. This includes laptops, desktops, tablets, and smartphones.",
    # "Question 5": "Some text goes here to answer question 5",
}
for question, answer in faq.items():
    with st.expander(question):
        st.write(answer)


# --- CONTACT FORM ---
# video tutorial: https://youtu.be/FOULV9Xij_8
st.write("")
st.write("---")
st.subheader(":mailbox: Have A Question? Ask Away!")
contact_form = f"""
<form method="POST" action="https://formsubmit.co/{CONTACT_EMAIL}" enctype="multipart/form-data">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here"></textarea>
     <input type="file" name="attachment" accept="pdf/txt">
     <button type="submit" class="button">Send ✉</button>
</form>
"""
st.markdown(contact_form, unsafe_allow_html=True)