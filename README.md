# Deploy EC2

## requirements

### pip 
**Python**
3.6.1

**pip**

```
pip install -r requirements.txt
```

## Create secret config file
```
project_folder/
    .config_secret/
        settings_common.json
        settings_debug.json
        settings_deploy.json
    django_app/
    ...
    ...
```

### settings_common.json example
```
{
    "django": {
        "secret_key": "Django secret key"
    }
}

### settings_debug.json example
```
{
  "django": {
    "allowed_hosts": [
      "*"
    ]
  }
}```

### settings_deploy.json example
```
{
  "django": {
    "allowed_hosts": [
      "*"
    ]
  }
}
```

runserver
```
# local development
python3 manage.py runserver --settings=config.settings.debug
```
