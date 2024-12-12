from flask import Flask, send_from_directory

app = Flask(__name__)

# Serve the index.html file
@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

# Serve static assets (if any, such as images or stylesheets)
@app.route('/<path:path>')
def serve_file(path):
    return send_from_directory('.', path)

if __name__ == "__main__":
    # Run the Flask app with SSL for Office Add-in compatibility
    app.run(ssl_context='adhoc', port=5000)
