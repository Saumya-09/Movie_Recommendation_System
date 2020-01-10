import panda as pd
import numpy as np 
from sklearn.feature_extraction.text import CounterVectorizer
from sklearn.metrics.pairwise import Cousine_simlarity

def get_title_from_index(index):
	return df[df.index == index]["title"].values[0]

def get_title_from_index(index):
	return df[df.title == title]["index"].values[0]
 
df = pd.read_csv("")
features = ['keywords','cast','genres','director']

for feature in features:
	df[feature] = df[feature].fillna('') 

def combine_features(row):
	try:
		return row['keywords']+" "+row['cast']+" "+row['genres']+" "+row['director']
	except:
		print("Error", row)	
df["combined_features"] = df.apply(combine_features,axis=1)

#print(df["combined_features"].head())

cv = CountVectorizer()
count_matrix = cv.fit_transform(df["combined_features"])

cosine_simi = cosine_similarity(count_matrix)

movie_user_likes = "The Avengers"

movie_index = get_index_from_title(movie_user_likes)

similar_movies = list(enumerate(cosine_simi[movie_index]))
sorted_similar_movies = sorted(similar_movies, key=lambda x:x[1],reverse=True)
i=0
for movie in sorted_similar_movies:
	print(get_title_from_index(movie[0]))
	i+=1
	if i>8:
		break
