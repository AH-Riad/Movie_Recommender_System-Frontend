import streamlit as st
import pickle
import pandas as pd

def recommend(movie):
    movie_index = movies[movies["title"] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movies_list:
        recommended_movies.append((movies.iloc[i[0]].title))

    return recommended_movies


movies = pickle.load(open('movies.pkl', 'rb'))
movies = pd.DataFrame(movies)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title("Movie Recommendation System")

selected_movie_names = st.selectbox(
    'Which movie do you like best?',
    movies["title"].values
)

'You selected: ', selected_movie_names

if st.button("Recommend"):
    recommendations = recommend(selected_movie_names)
    for i in recommendations:
        st.write(i)