from flask import Flask, request, render_template
import APP.views.handleMsg

app = Flask(__name__)


@app.route('/login', methods=['GET', 'POST'])
def login(name=None):
    if request.method == 'POST':
        print(request.headers)
        print(request.get_json())
        return "success"
    return render_template('user/chat.html')


@app.route('/getMsg', methods=['POST'])
def getMsg(msg=None):
    data = request.get_data()
    if request.method == 'POST':
        handleMsg = APP.views.handleMsg.AIResponse(data)
        return handleMsg


if __name__ == '__main__':
    app.run()
