from flask import Flask, render_template, redirect
import flask
app = Flask(__name__)

# default-page
@app.route("/blog")
def welcome_to_user():
   return render_template('homepage.html')

@app.route("/blog/articles")
def all_articles():
   my_articles =[
      {
         'title': 'Difference Between Flask and Django',
         'content': 'Django is more powerfull terminé',
         'author': 'John Doe'
      },
      {
         'title': 'All about Reacts js',
         'content': 'React js is a library of js for frontend development',
         'author': 'Joker'
      },
   ]
   
   return render_template('articles.html', articles = my_articles )


@app.route("/profile")
def redirecting_view():
    return redirect(flask.url_for('welcome_to_user'))

if __name__ == "__main__":
   app.run()

