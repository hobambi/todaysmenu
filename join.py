from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.qpskyvt.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.todaysmenu

from flask import Flask, render_template, request, jsonify
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')

@app.route("/join", methods=["POST"])
def join_post():
    id_receive = request.form['id_give']
    pw_receive = request.form['pw_give']

    doc = {
        'id': id_receive,
        'pw': pw_receive
    }
    db.users.insert_one(doc)
    return render_template('index.html')

@app.route("/join/idcheck", methods=["POST"])
def idcheck():
    id_receive = request.form['id_give']
    find = db.users.find_one({'id':id_receive})
    idcheck = 0
    print(find)
    if find is None:
        idcheck =1
        print('같은 id가 없습니다')
    else:
        print('같은 id가 있습니다.')
    return jsonify({'checknum':idcheck})

@app.route('/join')
def contact_join():
    return render_template('join.html')

#--------------------------------------------------
@app.route('/login')
def contact_login():
    return render_template('login.html')

@app.route("/login", methods=["POST","GET"])
def login_post():
    id_receive = request.form['id_give']
    pw_receive = request.form['pw_give']
    find = db.users.find_one({'id':id_receive,'pw':pw_receive})
    logincheck =0
    if(find is None):
        logincheck =0
    else:
        logincheck =1
        global fixid
        fixid = id_receive
        print(fixid)
    return jsonify({'loginchecknum': logincheck})

#-------------------------------------------------
if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)