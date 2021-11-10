from flask import Flask

app = Flask(__name__)

@app.route("/project/")
def project():
    return 'The Project Page'

@app.route('/about')
def about():
    return 'The About Page'

