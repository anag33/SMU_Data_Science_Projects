from flask import Flask, render_template, redirect
#from flask_pymongo import PyMongo
import pymongo
import scrape_mars

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
conn = 'mongodb://localhost:27017'

client = pymongo.MongoClient(conn)

#Scrape Route to import scrape_mars.py script and call scrape function
@app.route("/") 
def index():
    mars = client.db.mars.find_one()
    return render_template("index.html", mars=mars)

@app.route("/scrape")
def scrape():
    mars_app = client.db.mars
    mars = scrape_mars.scrapemarsNews()


    mars_app.replace_one({}, mars, upsert=True)
    #return "Scraping Successful!"
    return redirect('/')

#Define Main Behavior
if __name__ == "__main__":
    app.run()
