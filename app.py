from flask import Flask, render_template
app = Flask(__name__, static_url_path='/static')

gifs = ["startslide.gif", "bbfc.gif", "sounds.gif", "tvl.gif", "csc.gif"]


@app.route('/')
def index():
    title = "Mark + Lee WTF"
    link_value = "studio"
    return render_template('index.html', title=title, link_value=link_value)

@app.route('/studio')
def studio():
    link_value = "recruitment"
    title = "Studio updates"
    return render_template('index.html', title=title, link_value=link_value)

@app.route('/recruitment')
def recruitment():
    link_value = "nb"
    title = "Recruitment updates"
    return render_template('index.html', title=title, link_value=link_value)

@app.route('/nb')
def nb():
    link_value = 0
    title = "New business"
    return render_template('index.html', title=title, link_value=link_value)

@app.route('/<int:gif_num>')
def game(gif_num):
    gif_len = len(gifs)
    return render_template('game.html', gif=gifs[gif_num], gif_num=gif_num, gif_len=gif_len)

@app.route('/aob')
def aob():
    title = "Any other business?"
    return render_template('index.html', title=title)
