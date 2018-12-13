from flask import Flask, render_template, request, redirect, send_from_directory
import os
import vsearch

app = Flask(__name__)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route('/')
def hello() -> '302':
    return redirect('/entry')


@app.route('/search', methods=['POST'])
def search() -> 'html':
    title = 'Here are your results:'
    phrase = request.form['phrase']
    letters = request.form['letters']
    results = vsearch.search_for_letters(phrase, letters)
    return render_template('results.html',
                           the_phrase=phrase,
                           the_letters=letters,
                           the_title=title,
                           the_results=results,
                           )


@app.route('/entry')
def entry() -> 'html':
    return render_template('entry.html', the_title='Welcome to search4letters on the web!')


if __name__ == '__main__':
    app.run(debug=True)
