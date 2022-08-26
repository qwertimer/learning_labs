import streamlit as st
import numpy as np
import pandas as pd

# Adding checkboxes is easy. Wrap the viewer in an if statement check
# box
if st.checkbox("Show Results"):
    chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])
    chart_data

