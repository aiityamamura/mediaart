import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def harmonic_graph(freq, amplitude):
    time = np.arange(0, 10, 0.1)
    wave = amplitude * np.sin(2 * np.pi * freq * time)
    plt.plot(time, wave)
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.title('Harmonic Graph')
    st.pyplot()

def main():
    st.title('Harmonic Graph Visualization')
    freq = st.slider('Frequency', min_value=1, max_value=10, value=5)
    amplitude = st.slider('Amplitude', min_value=1, max_value=10, value=5)
    
    harmonic_graph(freq, amplitude)

if __name__ == "__main__":
    main()
