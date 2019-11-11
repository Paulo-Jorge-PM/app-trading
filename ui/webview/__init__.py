"""from flask import Flask, render_template

app = Flask(__name__)
#app.config.from_object('config')

db = "teste"

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

from ui.webview.controllers.routes import flaskRoutes
app.register_blueprint(flaskRoutes)"""

# Later on you'll import the other blueprints the same way:
#from app.comments.views import mod as commentsModule
#from app.posts.views import mod as postsModule
#app.register_blueprint(commentsModule)
#app.register_blueprint(postsModule)