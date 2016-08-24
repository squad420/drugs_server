#!flask/bin/python
import os
from app import app
port = int(os.environ.get('PORT', 5052))
app.run(host='127.0.0.1', port=port, debug=True)
