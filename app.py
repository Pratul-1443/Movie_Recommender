import streamlit as st
import pickle
import pandas as pd

def recommend(movie):
    movies_index=movies[movies["title"]==movie].index[0]
    distances=similarity[movies_index]
    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    Recommended_movies=[]
    for i in movies_list:
        Recommended_movies.append(movies.iloc[i[0]].title)
    return Recommended_movies

movies_dict=pickle.load(open("movie_dict.pkl","rb"))
movies=pd.DataFrame(movies_dict)
similarity=pickle.load(open("Similarity.pkl","rb"))


st.title("Movie Recommender System")

Select_Movie_Name = st.selectbox(
    "How would you like to be contacted?",
    movies["title"].values
)

if st.button("Search"):
    recommendations=recommend(Select_Movie_Name)
    for i in recommendations:
        st.write(i)

