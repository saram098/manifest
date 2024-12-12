from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/embed', methods=['GET', 'POST'])
def embed():
    if request.method == 'POST':
        url = request.form['url']
        return f'''
            <h1>Website Embedder</h1>
            <p>Preview of the website: <a href="{url}" target="_blank">{url}</a></p>
            <iframe src="{url}" width="800" height="600" style="border:1px solid #ccc;"></iframe>
        '''
    return '''
        <h1>Embed Website</h1>
        <form method="post">
            <label for="url">Enter website URL:</label><br>
            <input type="url" id="url" name="url" required><br><br>
            <button type="submit">Embed</button>
        </form>
    '''

if __name__ == "__main__":
    app.run(ssl_context='adhoc', port=5000)
