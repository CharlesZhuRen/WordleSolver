from flask import Flask, render_template, jsonify

app = Flask(__name__, static_folder='frontend/dist/assets', template_folder='frontend/dist')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify({"message": "Hello from Flask!"})


if __name__ == '__main__':
    app.run(debug=True)
