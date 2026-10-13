from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello():
    return "Halo dari Flask + Docker + Jenkins!"


@app.route('/github-webhook', methods=['POST'])
def github_webhook():
    payload = request.get_json(silent=True)

    print("Webhook diterima dari GitHub")
    print(payload)

    return "Webhook received", 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
