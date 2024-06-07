"""
Example dashboard with Okta authentication.
"""

import streamlit as st
import pandas as pd

from auth import auth


if not auth.user:
    st.header('Sign in')
    st.text('Please sign in to view this dashboard.')
    st.button('Sign in', on_click=auth.login)

if auth.user:
    st.header('Sign out')
    st.text('Please sign out when you are done.')
    st.button('Sign out', on_click=auth.logout)

    st.header('Top Secret Data')
    st.text('It is crucial that this data remains secret.')
    st.text('Thank you for protecting out top secret bean data by not screenshotting this page.')

    df = pd.DataFrame({
        'bean': ['pinto', 'black', 'garbanzo', 'kidney', 'jelly'],
        'rating': ['2', '4', '5', '2', '1'],
        'notes': ['', '', '', '', 'bad for soup']
    })

    df