
import streamlit as st

#Plotting and cleaning libraries
import pandas as pd
import numpy as np
import time
#import matplotlib.pyplot as plt
import seaborn as sns

#Audio libraries
import librosa
import librosa.display
from pydub import AudioSegment

#Other libraries
import os
from tensorflow.keras.models import load_model

# load models
model = load_model("chosen_model.h5")

# Functions
Emotions = ['Angry', 'Calm', 'Disgust', 'Fearful', 'Happy', 'Neutral', 'Sad', 'Suprised']

@st.cache
def get_mfccs(audio, limit):
    '''Get mccs feature into array. format first developed by Maria Startseva, 
    Tal Baram, and Asher https://github.com/talbaram3192/Emotion_Recognition_project'''
    y, sr = librosa.load(audio, sr=22050)
    feat = librosa.feature.mfcc(y, sr=22050, n_mfcc = 40)
    if feat.shape[1] > limit:
        mfccs = feat[:,:limit]
    elif feat.shape[1] < limit:
        mfccs = np.zeros((feat.shape[0], limit))
        mfccs[:, :feat.shape[1]] = feat
    return mfccs


def main():
	
    menu = ['Home']
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.sidebar.title("Emotion Classifier App")
        st.sidebar.markdown("This app predicts an emotion off of a given audio file")
        st.sidebar.markdown("* **Data Source**:[Ravdess](https://smartlaboratory.org/ravdess/)")

        st.sidebar.markdown("---")
        st.markdown("## Upload A File Below")
        st.subheader("Upload audio")
        Audio_file=st.file_uploader("Upload Audio", type=["wav"])
        if Audio_file is not None:

            if Audio_file.type == "audio/x-wav":
                st.audio(Audio_file,format='audio/wav',start_time=0)

                with open(Audio_file.name, "wb") as f:
                    f.write(Audio_file.getbuffer())
                path = os.path.join("audio_files", Audio_file.name)
                
                #save_audio(Audio_file)

                wav, sr = librosa.load(Audio_file, sr=2200)

                mfccs = get_mfccs(path, model.input_shape[-1])
                mfccs = mfccs.reshape(1, *mfccs.shape)
                pred = model.predict(mfccs)[0]
                title = f"Emotion Prediction is: {categories[predictions.argmax()]} \- {predictions.max() * 100:.2f}%"
                st.write(title)


		
if __name__ == '__main__':
    main()

st.button("Predict Again")
