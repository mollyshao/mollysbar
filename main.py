from flask import Flask, render_template, request, redirect, make_response
import cocktail
app = Flask(__name__)


@app.route("/")
def home():
    return render_template('home.html', cocktail_string_list=cocktail.cocktail_string_list)


@app.route("/results", methods=['GET', 'POST'])
def results():
    print(str(request.form["ingredients"]))
    ingredients = str(request.form["ingredients"])
    print(ingredients)
    search_results = cocktail.search(ingredients)
    return render_template('results.html', ingredients=ingredients, results=search_results)


@app.route("/fav", methods=['GET', 'POST'])
def fav():
    print(request.form['drink'])
    df_result = cocktail.df1.loc[cocktail.df1['strDrink'] == request.form['drink']]
    df_result_ingre_list = df_result['clean_combined'].values
    ingredients = ' '.join(df_result_ingre_list)
    print(ingredients)
    search_results = cocktail.search(ingredients)
    return render_template('results.html', ingredients=ingredients, results=search_results)


@app.route("/soundsgood", methods=['GET', 'POST'])
def soundsgood():
    print(request.args['drink'])
    df_result = cocktail.df1.loc[cocktail.df1['strDrink'] == request.args['drink']]
    df_result_ingre_list = df_result['clean_combined'].values
    ingredients = ' '.join(df_result_ingre_list)
    print(ingredients)
    search_results = cocktail.search(ingredients)
    return render_template('results.html', ingredients=ingredients, results=search_results)


app.run()
