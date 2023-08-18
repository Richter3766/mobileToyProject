from firebase_admin import auth


def verify(token):
    decoded_token = auth.verify_id_token(token)
    uid = decoded_token['uid']
    return uid


def getToken(uid):
    custom_token = auth.create_custom_token(uid)
    return str(custom_token)

