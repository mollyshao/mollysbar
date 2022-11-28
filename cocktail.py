#!/usr/bin/env python
# coding: utf-8

import re
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import ipywidgets as widgets
from IPython.display import display

def clean_combined(combined):
    return re.sub("[^a-zA-Z0-9 ]", "", combined)

def search(comb_ingre_str):
    #combined = "Creme de Cacao Vodka"
    name = df1.strDrink
    comb_ingre_str = clean_combined(comb_ingre_str)
    query_vec = vectorizer.transform([comb_ingre_str])
    similarity = cosine_similarity(query_vec, tfidf).flatten()
    indices = np.argpartition(similarity,-5)[-5:]
    output_results = df1.iloc[indices][::-1]
    results = output_results.to_dict('records')
    print(results)
    for k in results:
        print(k['strDrink'])
        print(k['clean_combined'])
        print(k['strDrinkThumb'])
        print(k['strInstructions'])
        print("")
    return results

def on_type(data):
    with cocktail_list:
        cocktail_list.clear_output()
        combined = data["new"]
        if len(combined) > 1:
            display(search(combined))

df = pd.read_csv("all_drinks.csv")

#print(df)

df1 = df.replace(np.nan, '', regex=True)

df1 = df1.replace("\\r\\n", "")

cols = ['strIngredient1','strIngredient10','strIngredient11','strIngredient12','strIngredient13','strIngredient14','strIngredient15','strIngredient2','strIngredient3','strIngredient4','strIngredient5','strIngredient6','strIngredient7','strIngredient8','strIngredient9']
df1['combined'] = df1[cols].apply(lambda row: ' '.join(row.values.astype(str)), axis=1)
df1["clean_combined"] = df1["combined"].apply(clean_combined)

#print(df1)

vectorizer = TfidfVectorizer(ngram_range=(1,2))
tfidf = vectorizer.fit_transform(df1["clean_combined"])

#search("vodka")
# df1_input = widgets.Text(
#     value = "Vodka",
#     description = "Ingredients:",
#     disabled=False
# )
#cocktail_list = widgets.Output()
#df1_input.observe(on_type, names='value')
#display(df1_input, cocktail_list)
