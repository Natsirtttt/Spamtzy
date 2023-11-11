from flask import Flask, render_template
import joblib
import pyrebase

config = {
    "apiKey": "AIzaSyD9OWx4sOkXzh7_V_V4llDSkxJ7SP1Uh0s",
    "authDomain": "trydb-f963b.firebaseapp.com",
    "projectId": "trydb-f963b",
    "storageBucket": "trydb-f963b.appspot.com",
    "messagingSenderId": "548490302104",
    "appId": "1:548490302104:web:3e875c0dd82069d985b6ed"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

# Reference to your database
db_sms_list_ref = db.reference('/dbSmsList')

def get_sms_data():
    snapshot = db_sms_list_ref.get()
    sms_data = {}

    if snapshot:
        for sender_id, sender_snapshot in snapshot.items():
            sender_data = sender_snapshot
            sms_list = sms_data.get(sender_id, [])
            sms_list.append(sender_data)
            sms_data[sender_id] = sms_list

    return sms_data

app = Flask(__name__)

def classify(text):
    vectorizer = joblib.load('svm_vectorizer.joblib')
    model = joblib.load('SVM_model.joblib')
    
    vec = vectorizer.transform([text])
    res = model.predict(vec)
    
    return res

@app.route("/smsList")

def sms():
    text = "FREE entry into our ÃƒÂ¥Ã‚Â£250 weekly comp just send the word ENTER to 84128 NOW. 18 T&C www.textcomp.com cust care 08712405020."
    cls = classify(text)
    
    res = "spam" if cls == 1 else "ham"
    return render_template('interface.html', res=res, text = text)


if __name__ == '__main__':
    app.run(host='0.0.0.0')