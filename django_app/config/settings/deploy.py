from .base import *

config_secret_deploy = json.loads(open(CONFIG_SECRET_DEBUG_FILE).read())

# 배포모드니까 DEBUG는 FALSE로 둬야 한다.
DEBUG = False
ALLOWED_HOSTS = config_secret_deploy['django']['allowed_hosts']


# 0630 10:54
# deploy.py 를 추가