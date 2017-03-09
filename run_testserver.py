''' Runs a test server using the built in web server - Not suitable to deploy

This script runs the flask server. While suitable for development, it can only
handle one request at a time. It isn't enough for a full-scale deployment.
See: http://flask.pocoo.org/docs/0.12/api/#application-object
'''
from app import app

def main():
    ''' Runs the built-in flask server '''
    
    ssl_context = None
    ''' This points to the SSL certs to run with https '''
    # ssl_context = ('./cert.crt', './key.key')
        # Cloud9 does not support self-signed dev certs
    
    app.run(host='0.0.0.0', port=8080, debug=True, ssl_context=ssl_context)
    
if __name__ == '__main__':
    main()
