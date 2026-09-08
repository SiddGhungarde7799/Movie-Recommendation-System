import pickle
import streamlit as st
import requests

st.header('Movies Recommendation Systems Using Machine Learning')

movies = pickle.load(open('Artificats/movie_list.pkl','rb'))
similarity = pickle.load(open('Artificats/similarity.pkl','rb'))

movie_list = movies['title'].values
st.selectbox(
    'type or select the movie to get a recommendations',
    movie_list
)