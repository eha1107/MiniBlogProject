from flask import Flask, render_template

#create a flask instance
app = Flask(__name__)

#create a route decorator
@app.route('/')
def home():
    # render the homepage
    return render_template("index.html")

# @app.route('/post/<int:post_id>')
# def post(post_id):
#     # render the detailed view for a blog post
#     return render_template('post.html',post_id=post_id)

# create custom error page

# invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"),500

# add more routes for admin actions

if __name__ == '__main__':
    app.run(debug=True)

