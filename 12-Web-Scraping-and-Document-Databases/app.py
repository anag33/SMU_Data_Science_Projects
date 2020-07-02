from flask import Flask, render_template, redirect
#from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
#app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

# Or set inline
# mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")


@app.route("/")
def index():
    mars = client.db.mars.find_one({"active": 1})
    return render_template("index.html", mars=mars)


@app.route("/scrape")
def scrape():
    mars_app = client.db.mars
    mars = scrape_mars.scrape_all()
    
    #deactivate old data
    #When you run the scraper the data that is set as 
    #1 from the scrape_mars.py is set to inactive as 0 
    mars_app.update_many(
        {'active': 1},
        {"$set": {'active': 0}
        }
    )

    mars_app.insert_one(mars)
    
    mars.replace_one({}, mars_data, upsert=True)
    return "Scraping Successful!"
    #return redirect('/')


if __name__ == "__main__":
    app.run()