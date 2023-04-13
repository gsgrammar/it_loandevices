import os

def read_env_vars(file_path):
    env_vars = {}
    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith('#') or not line.strip():
                continue
            key, value = line.strip().split('=', 1)
            env_vars[key] = value
    return env_vars

env_vars = read_env_vars('.env')
env_auth_token = env_vars.get('MY_AUTH_TOKEN')
env_api_url = env_vars.get('API_URL')
env_debug = env_vars.get('DEBUG')
env_timezone = env_vars.get('TZ')
env_allowed_hosts = env_vars.get('ALLOWED_HOSTS')
headers = {'Authorization': f'Bearer {env_auth_token}'}