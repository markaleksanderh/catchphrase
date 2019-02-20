from flask import Flask, render_template
app = Flask(__name__)

gifs = ["Gif: " + str(i) for i in range(10)]

@app.route('/<int:gif_num>')
def catchphrase(gif_num):
    catchphrase = "Example catchphrase"
    return render_template('index.html', catchphrase=catchphrase, gif=gifs[gif_num])
