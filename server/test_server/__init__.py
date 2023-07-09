from flask import Flask
from flask import request, make_response

app = Flask(__name__)


@app.route("/")
def root():
    return "Hello, world."


# data = JSON.stringify([{key: "general", value: "kenobi", domain: "a.com"},{key: "hello", value: "there"},{key: "no", value: "way", domain: "b.com"}])
# fetch('https://a.com/cookies', {method: "POST", headers: {"Content-Type": "application/json"}, body: data})
@app.route("/cookies", methods=['GET', 'POST'])
def cookies():
    response = make_response(
        'Hello there! Set cookies as get parameters and the server will set them!')

    if request.content_type == 'application/json':
        for cookie in request.get_json():
            app.logger.critical(cookie)
            try:
                response.set_cookie(**cookie)
            except:
                pass

    return response
