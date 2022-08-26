import streamlit as st
import numpy as np
import pandas as pd

map_data = pd.DataFrame(
    np.random.randn(40, 2) / [50, 50] + [-34.93, 138.6007],
    columns=['lat', 'lon'])

st.map(map_data)
