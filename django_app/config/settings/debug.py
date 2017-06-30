from .base import *

config_secret_debug = json.loads(open(CONFIG_SECRET_DEBUG_FILE).read())

# 오류를 숨겨주는 역할
DEBUG = True
ALLOWED_HOSTS = config_secret_debug['django']['allowed_hosts']