from flask import Flask, render_template, request
import os
import re, regex
import pickle

SK = os.getenv("SECRET_KEY") # 環境変数を取得
app = Flask(__name__)
app.secret_key = SK

""" ここから """

file = open("/home/probabilityhill/mysite/static/pickle/all-words.pickle", "rb")
data = pickle.load(file)
file.close()

def Search(data_list, word, radio):
    input_word = word.replace("*", ".").replace("~", ".*").replace("]", "]+").replace("(", "(?=").replace("=!", "!").replace("{", "(").replace("}", ")")

    if(radio == "1"):
        p = re.compile('[\u3041-\u309F]+')
    elif(radio == "2"):
        p = regex.compile(r'\p{Script=Han}+')
    elif(radio == "3"):
        p = re.compile('[a-z]+')

    l = []
    for i in range(len(data_list)):
        m = re.fullmatch(r"{}".format(input_word), data_list[i])
        if bool(m):
            if radio != "1" and radio != "2" and radio != "3":
                l.append(m.group())
            else:
                if p.fullmatch(m.group()):
                    l.append(m.group())

    return '　'.join(sorted(l))

""" ここまで """


# トップページにユーザーがアクセスしたときの動作
@app.route("/")
def index():
    return render_template('index.html',
            title = 'KOTOBA SAGASHI (ことばさがし)',
            description = '',
            url = 'https://probabilityhill.pythonanywhere.com/',
            )

# postのときの処理
@app.route("/result", methods=['POST'])
def post():
    word = request.form.get('word')
    radio = request.form.get('radio')
    return render_template('result.html',
        title = 'search results | KOTOBA SAGASHI (ことばさがし)',
        description = '',
        url = 'https://probabilityhill.pythonanywhere.com/result',
        word = Search(data, word, radio)
        )

"""
@app.route("/sub")
def sub():
    return render_template(
        'sub.html',
        title = 'Sub | KOTOBA SAGASHI (ことばさがし)',
        description = '',
        url = 'https://probabilityhill.pythonanywhere.com/sub.html',
        contents = 'サブページです'
        )
"""

# 「.py」ファイルの実行時の動作
if __name__ == "__main__":
    # 127.0.0.1はローカルホストと呼ばれる「自分を表すホスト名」を意味しています。『http://localhost:5000/』というURLにアクセスしても『http://127.0.0.1:5000/』と同じ結果になります。
    # 『debug=True』とすると、何かエラーが出た際の修正などが楽になります。
    app.run(host='127.0.0.1', port=5000, debug=True)