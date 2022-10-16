from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    # return render_template('index.html')
    return "hello shubham "


# @app.route('/predict', methods=['POST'])
# def pedict_plecement():
#     name = request.form.get('name')
#     return "hello world."
if __name__ == "__main__":
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=8080)
