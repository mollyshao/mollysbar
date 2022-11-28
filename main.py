from flask import Flask, render_template, request, redirect, make_response
import cocktail
app = Flask(__name__)
@app.route("/")
def home():
    return render_template('home.html')
@app.route("/results", methods=['GET', 'POST'])
def results():
    print(str(request.form["ingredients"]))
    ingredients = str(request.form["ingredients"])
    search_results = cocktail.search(ingredients)
    return render_template('results.html', results=search_results)


app.run()