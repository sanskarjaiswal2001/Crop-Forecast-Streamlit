import streamlit as st
import joblib
import numpy as np
import matplotlib.pyplot as plt
st.set_option('deprecation.showPyplotGlobalUse', False)
reload_model = joblib.load('forecast_model')
m = st.slider('MONTHS',1,30)
forecast1 = reload_model.make_future_dataframe(periods = m,freq = 'M')
forecast1 = reload_model.predict(forecast1)
plt.figure(figsize=(25,10))
reload_model.plot(forecast1)
st.pyplot()