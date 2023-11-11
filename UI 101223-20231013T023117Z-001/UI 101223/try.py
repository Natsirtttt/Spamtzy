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

    

app = Flask(__name__)

@app.route("/")

def get_sms_data():
    snapshot = db_sms_list_ref.get()
    sms_list = []
    
    if snapshot:
        for sender_snapshot in snapshot.items():
            content = sender_snapshot.get('content', '')
            sender = sender_snapshot.get('sender', '')
            timestamp = sender_snapshot.get('timestamp', '')

            sms_data = {
                'content': content,
                'sender': sender,
                'timestamp': timestamp
            }

            sms_list.append(sms_data)

    return sms_list


if __name__ == '__main__':
    app.run(host='0.0.0.0')