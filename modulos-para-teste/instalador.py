import pytube
import streamlit as st

st.title('Instalador de videos do Youtube!')

link = st.text_input('digite o link do video aqui:')

yt = pytube.YouTube(link)

video = yt.streams.get_highest_resolution()
video.download()
