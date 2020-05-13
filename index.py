from flask import *

app=Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
	return render_template("index.html",name="chandini")


@app.route("/about")
def about_page():
	data=["chandini","madhuri","bhargavi"]
	return render_template("about.html",data=data)


if __name__=="__main__":
	app.run(debug=True)


