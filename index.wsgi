import sae
from weibome import wsgi

application = sae.create_wsgi_app(wsgi.application)
