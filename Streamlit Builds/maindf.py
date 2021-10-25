
import streamlit as st

import pandas as pd
import numpy as np
import time
import librosa
import librosa.display
from pydub import AudioSegment
import soundfile
import wave
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from IPython.display import Audio as playback
import os
from keras.models import load_model


import joblib
#from tensorflow.keras.models import load_model

# Functions




def get_MFCC(sr,audio):
    
    features = mfcc.mfcc(audio, sr, 0.025, 0.01, 13, appendEnergy = False)
    features = preprocessing.scale(features)
    return features

#def waveplot(Audio_File):
    #y, sr = librosa.load(Audio_File)
 	#librosa.display.waveplot(y.numpy(), sr=sr, ax=ax1)
	
def convert_mp3(file):
	sound = AudioSegment.from_mp3(Audio_file)
	sound.export(Audio_file, format= "wav")
	return st.audio(Audio_file, format='audio/mpeg')

def extract(wav_file, t1, t2):
	wav = AudioSegment.from_wav(wav_file)
	wav = wav[1000*t1:1000*t2]
	wav.export("extracted.wav", format='wav')

def load_model(model_path: str):
    model = open(model_path, "rb")
    return joblib.load(model)


@st.cache(allow_output_mutation=True)
def load_models():

	model = load_model(MODEL_PATH)
	model._make_predict_function()
    model.summary()  # included to make it visible when model is reloaded
	return model

if __name__ == '__main__':
    st.title('My first app')
    Audio_file = st.sidebar.file_uploader("Upload Audio", type=["wav"])


    sentence = st.text_input('Input your sentence here:')
    model, session = load_model()
    if sentence:
        y_hat = model.predict(sentence)

	Audio_file = st.sidebar.file_uploader("Upload Audio", type=["wav"])
		if Audio_file is not None:
			#filedetails= {"FileName":Audio_file.name,"FileType":Audio_file.type,"FileSize":Audio_file}
			#st.sidebar.write(filedetails)
			st.sidebar.markdown("---")

			if Audio_file.type == "audio/x-wav":

				st.markdown('#')
				st.write("Play File")
				st.audio(Audio_file, format='audio/x-wav')

def main():
	
	menu = ['Home'] #"About the model" "About the Developer", "Video"]
	choice = st.sidebar.selectbox("Menu", menu)



	if choice == "Home":
		st.sidebar.title("Emotion Classifier App")

		st.sidebar.markdown("This app predicts an emotion off of a given audio file")
		st.sidebar.markdown("* **Data Source**: [Ravdess](https://smartlaboratory.org/ravdess/)")
		st.sidebar.markdown("---")
		st.sidebar.markdown("## Upload A File Below")


		

	
				model= load_model("/Users/nathanmckinney/Desktop/dsir-82/Streamlit/Chosen_Model.h5")

			y_hat = model.predict(Audio_file)

		#model. 



#if __name__ == '__main__'
	#st.title('My first app')
	#sentence = st.text_input('Input your sentence here:')
	#model= load_model()
	#if sentence:
	#	y_hat = model.predict(sentence)

main()
