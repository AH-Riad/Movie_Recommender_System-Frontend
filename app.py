import streamlit as st
import pickle

movies_list = pickle.load(open('movies.pkl', 'rb'))
movies_list = movies_list["title"].values

st.title("Movie Recommendation System")

option = st.selectbox(
    'Which movie do you like best?',
    movies_list)
'You selected: ', option
