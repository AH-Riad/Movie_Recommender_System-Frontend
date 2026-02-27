import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=38f54bf2a61923cc247f94ceac5b28f0&language=en-US')
    data = response.json()
    return "https://image.tmdb.org/t/p/w500" + data['poster_path']

def recommend(movie):
    movie_index = movies[movies["title"] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters= []

    for i in movies_list:
        movie_id = i[0]
        recommended_movies.append((movies.iloc[i[0]].title))

        # fetch poster from api
        recommended_movies_posters.append(fetch_poster(movie_id))

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
    names, posters = recommend(selected_movie_names)
    for i in recommendations:
        st.write(i)