import sys
import os

# Add the parent directory to sys.path to import main
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import app

# For Vercel serverless function
def handler(environ, start_response):
    return app(environ, start_response)
