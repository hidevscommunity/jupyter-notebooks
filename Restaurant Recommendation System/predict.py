import streamlit as st
import pickle
import pandas as pd


similarity = pickle.load(open('/Users/amitpandey/Desktop/Cosine_IG.pkl', 'rb'))


def restaurant_recommendation(name, similarity = similarity):

    indices = pd.Series(df.index, index=df['Name']).drop_duplicates()

    index = indices[name]

    similarity_scores = list(enumerate(similarity[index]))

    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)

    similarity_scores = similarity_scores[0:10]

    restaurantindices = [i[0] for i in similarity_scores]

    return df['Name'].iloc[restaurantindices]




df =  pickle.load(open('/Users/amitpandey/Desktop/Instagram_recommender_model.pkl', 'rb'))
Rest = pd.DataFrame(df)




st.title("Restaurant Recommending Model")

st.header('To check for similar restaurant')

selected_Restaurant_name = st.selectbox(

"Here are the list of Restaurant, Select your Restaurant :", Rest['Name'].values)



if st.button('Recommend'):
    recommendations =  restaurant_recommendation((selected_Restaurant_name))
    for i in recommendations:
        st.write(i)


