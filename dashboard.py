"""
Example dashboard with Okta authentication.
"""

import streamlit as st
import pandas as pd
from auth import show_auth

from dotenv import load_dotenv
load_dotenv()

if 'token' not in st.session_state:
    st.header('Sign in')
    st.text('Please sign in to protect this very important data.')

show_auth()

if 'token' in st.session_state:
    st.header('Top Secret Data')
    st.text('It is crucial that this data remains secret.')
    st.text('Thank you for protecting out top secret bean data by not screenshotting this page.')

    df = pd.DataFrame({
        'bean': ['pinto', 'black', 'garbanzo', 'kidney', 'jelly'],
        'rating': ['2', '4', '5', '2', '1'],
        'notes': ['', '', '', '', 'bad for soup']
    })

    df