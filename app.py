import flask

app = flask.Flask(__name__)

@app.route('/')
def homepage():
    return flask.render_template('index.html')

@app.route('/atlas')
def atlas():
    return flask.render_template('atlas.html')

@app.route('/download')
def download():
    return flask.send_file('static/RRFletcher_CV.pdf')

if __name__=='__main__':
    app.run(host='0.0.0.0',port=8080)
