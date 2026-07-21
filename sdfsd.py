import numpy as np
import pandas as pd
import matplotlib.pyplot as pypl
import streamlit as st

xplots = np.array([0,5])

yplots = np.array([0,5])

pypl.plot(xplots, yplots)
pypl.show()

st.header("header")

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["A", "B", "C"])

st.line_chart(chart_data)

