import json

from flask import request, Flask, redirect
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['JSON_AS_ASCII'] = False

with open('./handson.json', mode='r') as f:
    sub_domains = json.load(f)


@app.route('/', defaults={'u_path': ''})
@app.route('/<path:u_path>')
def catch_all(u_path):
    print(f"{request.host=}", f"{u_path=}")
    if sub_domain := sub_domains.get(request.host):
        print(sub_domain)
        if target := sub_domain.get("paths", {}).get(u_path):
            print(u_path)
            return redirect(target)
    return redirect(f'https://handson.today/?from="{request.url}"')


if __name__ == '__main__':
    app.run(port=3421)
