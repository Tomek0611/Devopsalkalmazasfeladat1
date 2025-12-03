from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Frissített üzenet: új fejlesztés a feature branch-en!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)


