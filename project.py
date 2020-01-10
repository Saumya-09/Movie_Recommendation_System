import panda as pd
import numpy as np 
from sklearn.feature_extraction.text import CounterVectorizer
from sklearn.metrics.pairwise import Cousine_simlarity

def get_title_from_index(index):
	return df[df.index == index]["title"].values[0]

def get_title_from_index(index):
	return df[df.title == title]["index"].values[0]
 
df = pd.read_csv("")