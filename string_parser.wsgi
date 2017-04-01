import os
import sys
import site

# Add the site-packages of the chosen virtualenv to work with
site.addsitedir('/var/www/venv/lib/python2.7/site-packages')

INTERP = os.path.expanduser("/var/www/venv/bin/python")

if sys.executable != INTERP: os.execl(INTERP, INTERP, *sys.argv)

sys.path.insert(0,'/var/www/venv/bin')
sys.path.insert(0,'/var/www/venv/lib/python2.7/site-packages/django')
sys.path.insert(0,'/var/www/venv/lib/python2.7/site-packages')

# Add the app's directory to the PYTHONPATH
sys.path.append('/var/www/string_parser')

os.environ['DJANGO_SETTINGS_MODULE'] = 'educat.settings'

# Activate your virtual env
activate_env=os.path.expanduser("/var/www/venv/bin/activate_this.py")
execfile(activate_env, dict(__file__=activate_env))

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()