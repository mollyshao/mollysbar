from flask import Flask, render_template, request, redirect, make_response
import cocktail
from waitress import serve
import socket

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('home.html', cocktail_string_list=cocktail.cocktail_string_list)


@app.route("/results", methods=['GET', 'POST'])
def results():
    # print(str(request.form["ingredients"]))
    ingredients = str(request.form["ingredients"])
    # print(ingredients)
    search_results = cocktail.search(ingredients)
    return render_template('results.html', ingredients=ingredients, results=search_results)


@app.route("/fav", methods=['GET', 'POST'])
def fav():
    # print(request.form['drink'])
    df_result = cocktail.df1.loc[cocktail.df1['strDrink'] == request.form['drink']]
    df_result_ingre_list = df_result['clean_combined'].values
    ingredients = ' '.join(df_result_ingre_list)
    # print(ingredients)
    search_results = cocktail.search(ingredients)
    return render_template('results.html', ingredients=ingredients, results=search_results)


@app.route("/soundsgood", methods=['GET', 'POST'])
def soundsgood():
    # print(request.args['drink'])
    df_result = cocktail.df1.loc[cocktail.df1['strDrink'] == request.args['drink']]
    df_result_ingre_list = df_result['clean_combined'].values
    ingredients = ' '.join(df_result_ingre_list)
    # print(ingredients)
    search_results = cocktail.search(ingredients)
    return render_template('results.html', ingredients=ingredients, results=search_results)


if __name__ == "__main__":
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    # local_url = "http://{}:{}".format(local_ip, PORT)
    local_url = "http://{}".format(local_ip)
    # print("http://{}:{}".format(local_ip, PORT))
    print("http://{}".format(local_ip))
    # -- prod using waitress --
    serve(app, host="0.0.0.0", port=5000)   # prod run with waitress server
    # serve(app, host="0.0.0.0", port=80, threads=6, _quiet=True)   # prod run with waitress server
    # -- --
    # app.run()
