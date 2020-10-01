import numpy as np #giving alias name as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
def title_index(index):
    return df[df.index ==index]["title"].values[0]#takes title from index
def index_title(title):
    return df[df.title ==title]["index"].values[0] #takes index from title
df=pd.read_csv("movie_dataset.csv")#reads the csv file which should be available in your workspace folder
X=['keywords','cast','genres','director']#the key points on which the movie is recommended
for X in X:
    df[X]=df[X].fillna(' ')#if any data containg Null or na value it would be rplaced by blank space
def all_X(row):
    try:
        return row['keywords']+" "+row["cast"]+" "+row["genres"]
    except: print("error", row)#giving out the error fields.
df["all_X"]= df.apply(all_X,axis=1)
cv=CountVectorizer()
count_matrix=cv.fit_transform(df["all_X"])#The fit() function calculates the values of these parameters. The transform function applies the values of the parameters on the actual data and gives the normalized value. The fit_transform() function performs both in the same step. Note that the same value is got whether we perform in 2 steps or in a single step.
cosine=cosine_similarity(count_matrix) 
movie_user_likes=input("Enter the movie you like :")#movie in accordance to which recommendation should be given
movie_index=index_title(movie_user_likes)
similar_movies=list(enumerate(cosine[movie_index]))#finding the cosine similarity of the movies
sorted_similar_movies=sorted(similar_movies,key=lambda x:x[1],reverse=True)#we will get cosine similarity in ascending order therefore we need to reverse it to get vlues desirably and we'd remove the first as if cosine distance is 1 it would be the same movie which the user like
i=0
for movie in sorted_similar_movies:
    print (title_index(movie[0]))#printing the movies likewise
    i=i+1
    if i>10:
        break
