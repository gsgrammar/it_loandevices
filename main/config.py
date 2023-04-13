# config.py
import os

def read_env_vars(file_path):
    env_vars = {}
    with open(file_path, 'r') as file:
        for line in file:
            # Skip comments and empty lines
            if line.startswith('#') or not line.strip():
                continue
            # Split the line into key and value
            key, value = line.strip().split('=', 1)
            # Add key-value pair to dictionary
            env_vars[key] = value
    return env_vars

# Read environment variables from file
env_vars = read_env_vars('.env')

# Extract individual variables
auth_token = env_vars.get('MY_AUTH_TOKEN')
api_url = env_vars.get('API_URL')
debug = env_vars.get('DEBUG')
timezone = env_vars.get('TZ')

# Use the variables in your application
headers = {'Authorization': f'Bearer {auth_token}'}
# ... other logic using the environment variables

print(headers)