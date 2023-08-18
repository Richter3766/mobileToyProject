from firebase_admin import auth


def verify(token):
    decoded_token = auth.verify_id_token(token)
    uid = decoded_token['uid']
    print("uid: ", uid)
    return token


def login(data):
    print("test login", data)
    return data

