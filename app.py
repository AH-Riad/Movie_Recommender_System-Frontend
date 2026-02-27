import streamlit as st
import pickle

movies_list = pickle.load(open('movies.pkl', 'rb'))
movies_list = movies_list["title"].values

st.title("Movie Recommendation System")

selected_movie_names = st.selectbox(
    'Which movie do you like best?',
    movies_list)
'You selected: ', selected_movie_names

if st.button("Recommend"):
    recommend(selected_movie_names)
    st.write(selected_movie_names)