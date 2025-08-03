from aws_wsgi import make_lambda_handler
from django.core.wsgi import get_wsgi_application
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoHUD.settings')
application = get_wsgi_application()

lambda_handler = make_lambda_handler(application)