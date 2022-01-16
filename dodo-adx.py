from flask import Flask, request, Response
from flask_cors import CORS
import logging
import uuid
import json
logging.getLogger().setLevel(logging.INFO)
app = Flask(__name__)
cors = CORS(app, supports_credentials=True)
dodouid = 'DODOUID'

@app.route('/dodouid')
def uid():
    resp = Response(json.dumps({
    'data': {
        'status': True
    },
    'code': 200}))
    logging.info('cookie is')
    logging.info(request.cookies.get(dodouid))
    if not request.cookies.get(dodouid):
        uid = str(uuid.uuid4())
        resp.set_cookie(dodouid, uid, path='/adx', domain='http://www.ayang818.top')
        logging.info(f'uid is {uid}')
    return resp

if __name__ == '__main__':
    app.run('localhost', 5000)