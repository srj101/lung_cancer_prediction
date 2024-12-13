import streamlit as st
from pathlib import Path
import subprocess
import sys

# Function to install dependencies from requirements.txt


def install_requirements():
    try:
        # Attempt to install requirements
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("Requirements installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while installing requirements: {e}")
        st.error("There was an error installing the necessary requirements.")


# Install requirements before running the app
install_requirements()

# Function to read markdown files


def read_markdown_file(markdown_file):
    return Path(markdown_file).read_text()


# Dictionary to map page names to their respective files
pages = {
    "Home": "pages/home.py",
    "Motivation": "pages/motivation.py",
    "Objectives": "pages/objectives.py",
    "Related Study": "pages/related_study.py",
    "Methodology": "pages/methodology.py",
    "Results": "pages/results.py",
    "Prediction": "pages/prediction.py"
}

# Streamlit sidebar for navigation
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(pages.keys()))

# Load the selected page
page = pages[selection]
exec(Path(page).read_text())
