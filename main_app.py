import streamlit as st

# Page configuration
st.set_page_config(
    page_title="AI Model Hub",
    page_icon="🚀",
    layout="wide"
)

# Main Landing Page Content
st.title("Welcome to My AI Project 🤖")

st.markdown("""
### Overview
This is a Multi-page Streamlit application where you can interact with and test the AI models I have developed.

**How to use this app:**
* Look at the **Sidebar** on the left.
* You will see the different pages listed there (based on the files in your `pages/` folder).
* Click on a page name to navigate directly to that model's interface.
""")

st.info("Select a model from the left sidebar to start making predictions!")