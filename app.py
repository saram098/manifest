from flask import Flask, send_from_directory

app = Flask(__name__)

# Serve the main index.html file
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

# Serve other static files (like icons or support.html)
@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory('.', filename)

if __name__ == "__main__":
    # Run Flask with HTTPS (required for Office Add-ins)
    app.run(ssl_context='adhoc', host='0.0.0.0', port=5000)
