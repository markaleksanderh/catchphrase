from flask import Flask, render_template
app = Flask(__name__, static_url_path='/static')

gifs = ["supportive.gif"]+["Gif: " + str(i) for i in range(10)]

@app.route('/<int:gif_num>')
def catchphrase(gif_num):
    gif_len = len(gifs)
    return render_template('index.html', gif=gifs[gif_num], gif_num=gif_num, gif_len=gif_len)
