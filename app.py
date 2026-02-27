import streamlit as st
import pickle
import pandas as pd
import requests


def fetch_poster(movie_id):
    response = requests.get(
        f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=38f54bf2a61923cc247f94ceac5b28f0&language=en-US')
    data = response.json()
    print(data)

    if 'poster_path' in data and data['poster_path'] is not None:
        return "https://image.tmdb.org/t/p/w500" + data['poster_path']
    else:
        return "https://via.placeholder.com/500x750?text=No+Image"


def recommend(movie):
    movie_index = movies[movies["title"] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append((movies.iloc[i[0]].title))

        # fetch poster from api
        recommended_movies_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_movies_posters


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

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])