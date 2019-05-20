from flask import Flask, render_template, jsonify, redirect
import pymongo
import scrape_mars

app = Flask(__name__)


client = pymongo.MongoClient()
db = client.mars_db
collection = db.mars_facts2



@app.route('/scrape')
def scrape():
    mars = scrape_mars.scrape()
    # Update the Mongo database using update and upsert=True
    db.mars_facts2.update({}, mars, upsert=True)
    return redirect("/")

@app.route("/")
def home():
    mars = list(db.mars_facts2.find())
    return render_template("index2.html", mars = mars)


if __name__ == "__main__":
    app.run(debug=True)