import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access variables
database_url = os.getenv('DATABASE_URL')
api_key = os.getenv('API_KEY')
debug_mode = os.getenv('DEBUG')

print(f"Database URL: {database_url}")
print(f"API Key: {api_key}")
print(f"Debug Mode: {debug_mode}")