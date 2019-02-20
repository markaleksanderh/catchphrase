from flask import Flask, render_template
app = Flask(__name__)

gifs = ["gif 1", "gif 2", "gif 3", "gif 4"]

@app.route('/<int:gif_num>')
def catchphrase(gif_num):
    catchphrase = "Example catchphrase"
    return render_template('index.html', catchphrase=catchphrase, gif=gifs[gif_num])
