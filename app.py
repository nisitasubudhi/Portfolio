from flask import Flask, render_template, request, url_for,request,redirect

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route('/submit_form', methods=['GET','POST'])
def submit():
	return render_template("index.html")




if __name__ == "__main__":
	app.debug=True
	app.run(host = '0.0.0.0', port =9000, debug=True) 
