from flask import Flask
import random
app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too
#making a comment so that it updates?

@app.route("/")
def index():
    status = """ <!DOCTYPE = html>
    <html>
        <body>
            <h1>
                C.A.R.L.
                <br>
                Computer Assistied Realistic Lifeform
                <br>
                v0
            </h1>
            <a href="/page2"> link </a>
            <h2>
                <a href="/WholeHomeManagement"> Whole Home Management </a>
                <br>
                Garage
                <br>
                Basement
                <br>
                Livingroom
                <br>
                Practice Room
                <br>
                Kitchen
                <br>
                Ian's Bedroom
                <br>
                Lauren/Jess Bedroom
                <br>
                Bathroom
                <br>
            </h2>
        </body>
    </html>
    """
    return status
@app.route("/WholeHomeManagement")
def WholeHomeManagement():
    WHM = """ <!DOCTYPE = html>
    <html>
        whole home page test
    </html>
    """
    return WHM


@app.route("/page2")
def page2():
    page = """ <!DOCTYPE = html>
    <html>
        <body>
            something
        </body>
    </html>
    """
    return page 

app.run()
