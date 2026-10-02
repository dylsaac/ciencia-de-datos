import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

map_data = pd.DataFrame(
np.random.randn(100, 2) / [50, 50] + [18.91534, -97.02848],
columns=['lat', 'lon'])
st.map(map_data)
