import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'amanawit_backend.settings')
sys.path.insert(0, r'c:/Users/NAWAB/Desktop/amanawit design/backend')
django.setup()

from django.core.management import execute_from_command_line

# Start server
execute_from_command_line(['runserver', '127.0.0.1:8000'])
