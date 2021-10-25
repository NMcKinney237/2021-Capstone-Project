
import streamlit as st

#Plotting and cleaning libraries
import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt
import seaborn as sns

#Audio libraries
import librosa
import librosa.display
from pydub import AudioSegment

#Other libraries
import os
import joblib

# Functions

#@st.cache(allow_output_mutation=True)
#def load_models():
	#model = load_model(MODEL_PATH)
   # model._make_predict_function()
    #model.summary()  # included to make it visible when model is reloaded
	#return model


def get_MFCC(sr,audio):
    
    features = mfcc.mfcc(audio, sr, 0.025, 0.01, 13, appendEnergy = False)
    features = preprocessing.scale(features)
    return features
	

def extract(wav_file, t1, t2):
	wav = AudioSegment.from_wav(wav_file)
	wav = wav[1000*t1:1000*t2]
	wav.export("extracted.wav", format='wav')

def load_model(model_path: str):
    model = open(model_path, "rb")
    return joblib.load(model)


def main():
	
	menu = ['Home'] #"About the model" "About the Developer", "Video"]
	choice = st.sidebar.selectbox("Menu", menu)



	if choice == "Home":
		st.sidebar.title("Emotion Classifier App")

		st.sidebar.markdown("This app predicts an emotion off of a given audio file")
		st.sidebar.markdown("* **Data Source**: [Ravdess](https://smartlaboratory.org/ravdess/)")
		st.sidebar.markdown("---")
		st.sidebar.markdown("## Upload A File Below")


		Audio_file = st.sidebar.file_uploader("Upload Audio", type=["wav"])
		if Audio_file is not None:
			st.sidebar.markdown("---")

			if Audio_file.type == "audio/x-wav":


				st.markdown('#')
				st.write("Play File")
				st.audio(Audio_file, format='audio/x-wav')

	
				model= load_model("/Users/nathanmckinney/Desktop/dsir-82/Streamlit/Chosen_Model.h5")

				y_hat = model.predict(Audio_file)

		

main()
