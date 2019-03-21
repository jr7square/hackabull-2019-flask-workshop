from flask import Flask, render_template, request,redirect, url_for
from data import blogs

app = Flask(__name__)


# endpoint for main page
@app.route('/')
def home():
    return render_template('blogs.html', t_blogs=blogs)


# endpoint for blog details
@app.route('/blog/<int:id>', methods=['GET', 'POST'])
def blog(id):
    if request.method== 'POST':
        del blogs[id]
        return redirect(url_for('home'))
    blog = blogs[id]
    return render_template('blog_details.html', t_blog=blog)


# endpoint for creating new blog
@app.route('/new-blog', methods=['GET', 'POST'])
def new_blog():
    if request.method == 'POST':
        new_id = max(k for k, _ in blogs.items()) + 1
        new_blog = {}
        new_blog['id'] = new_id
        new_blog['title'] = request.form['title']
        new_blog['content'] = request.form['content']
        blogs[new_id] = new_blog
        return redirect(url_for('home'))
    return render_template('create_blog.html')


if __name__ == '__main__':
    app.run(debug=True)