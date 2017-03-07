'''
Desc.:      Runs the test server
Purpose:    Testing the website on a localhost
Author:     Joel Tannas
Date:       MAR 03, 2017
'''
from app import app

ssl_context = None
# ssl_context = ('./cert.crt', './key.key')
    # Cloud9 does not support self-signed dev certs

app.run(host='0.0.0.0', port=8080, debug=True, ssl_context=ssl_context)
