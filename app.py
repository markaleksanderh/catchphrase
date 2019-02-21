from flask import Flask, render_template
app = Flask(__name__, static_url_path='/static')

gifs = ["placeholder.png", "supportive.gif", "cat.gif"]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<int:gif_num>')
def game(gif_num):
    gif_len = len(gifs)
    return render_template('game.html', gif=gifs[gif_num], gif_num=gif_num, gif_len=gif_len)

@app.route('/aob')
def aob():
    return render_template('aob.html')
