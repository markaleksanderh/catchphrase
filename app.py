from flask import Flask, render_template
app = Flask(__name__, static_url_path='/static')

gifs = ["startslide.gif", "bbfc.gif", "sounds.gif", "tvl.gif", "csc.gif"]


@app.route('/')
def index():
    title = "Mark + Lee WTF"
    image_link = None
    link_value = "studio"
    return render_template('index.html', title=title, link_value=link_value, image_link=image_link)

@app.route('/studio')
def studio():
    image_link = "static/studio.gif"
    link_value = "recruitment"
    title = "Studio updates"
    return render_template('index.html', title=title, link_value=link_value, image_link=image_link)

@app.route('/recruitment')
def recruitment():
    image_link = "static/recruitment.gif"
    link_value = "nb"
    title = "Recruitment updates"
    return render_template('index.html', title=title, link_value=link_value, image_link=image_link)

@app.route('/nb')
def nb():
    image_link = "static/newbusiness.gif"
    link_value = 0
    title = "New business"
    return render_template('index.html', title=title, link_value=link_value, image_link=image_link)

@app.route('/<int:gif_num>')
def game(gif_num):
    gif_len = len(gifs)
    return render_template('game.html', gif=gifs[gif_num], gif_num=gif_num, gif_len=gif_len)

@app.route('/aob')
def aob():
    image_link = 'static/aob.gif'
    link_value = 'wages'
    title = "Any other business?"
    return render_template('index.html', title=title, link_value=link_value, image_link=image_link)

@app.route('/wages')
def wages():
    image_link = "static/wages.gif"
    link_value = 'next'
    title = "Wages"
    return render_template('index.html', title=title, link_value=link_value, image_link=image_link)

@app.route('/next')
def next_week():
    image_link = None
    link_value = None
    title = "Next week: Chris + Sophie"
    return render_template('index.html', title=title, link_value=link_value, image_link=image_link)
