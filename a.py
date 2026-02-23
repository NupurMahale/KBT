import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Nupur's Smart App",
    page_icon="🌸",
    layout="wide"
)

# Custom CSS for Attractive Design
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(to right, #89CFF0, #FFC0CB);
    }
    .title {
        font-size:50px !important;
        font-weight: bold;
        text-align: center;
        color: white;
    }
    .subtitle {
        font-size:20px;
        text-align: center;
        color: white;
    }
    .card {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 2px 2px 20px rgba(0,0,0,0.2);
        margin: 10px;
    }
    .footer {
        text-align: center;
        font-size: 14px;
        color: white;
        margin-top: 50px;
    }
    </style>
""", unsafe_allow_html=True)

# Title Section
st.markdown('<div class="title">🌸 Welcome to Nupur\'s Smart Dashboard</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">An Attractive Streamlit Web Application</div>', unsafe_allow_html=True)

st.write("")

# Sidebar
st.sidebar.title("Navigation")
option = st.sidebar.radio("Go to", ["Home", "About", "Contact"])

# HOME PAGE
if option == "Home":
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown('<div class="card"><h3>🚀 Fast Performance</h3><p>Streamlit runs instantly and is easy to use.</p></div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="card"><h3>🎨 Beautiful UI</h3><p>Custom CSS makes your app modern and stylish.</p></div>', unsafe_allow_html=True)

    with col3:
        st.markdown('<div class="card"><h3>💡 Smart Features</h3><p>Add charts, ML models, forms and more.</p></div>', unsafe_allow_html=True)

    st.write("")
    if st.button("Click Me 💖"):
        st.success("You clicked the button! Streamlit is working perfectly!")

# ABOUT PAGE
elif option == "About":
    st.markdown('<div class="card"><h2>About This Project</h2><p>This app is created using Streamlit with attractive UI design using custom CSS.</p></div>', unsafe_allow_html=True)

# CONTACT PAGE
elif option == "Contact":
    name = st.text_input("Enter Your Name")
    message = st.text_area("Enter Your Message")

    if st.button("Submit"):
        st.success(f"Thank you {name}! We received your message.")

# Footer
st.markdown('<div class="footer">Made with ❤️ using Streamlit | By Nupur A. Mahale</div>', unsafe_allow_html=True)