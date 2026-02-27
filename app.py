import streamlit as st
import pickle

def recommend(movie):
    movie_index = movies_list[movies_list["title"] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse  = True, key = lambda x:x[1])[1:6]

    recommended_movies = []
    for i in movies_list:
        recommended_movies.append((movies.iloc[i[0]].title))

    return recommended_movies

movies = pickle.load(open('movies.pkl', 'rb'))
movies = movies["title"].values

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title("Movie Recommendation System")

selected_movie_names = st.selectbox(
    'Which movie do you like best?',
    movies_list)
'You selected: ', selected_movie_names

if st.button("Recommend"):
    recommend(selected_movie_names)
    st.write(selected_movie_names)