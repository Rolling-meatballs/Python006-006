学习笔记

### database setting
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ji_ke',
        'PORT': 3306,
        'PASSWORD': '123456',
        'HOST': 'localhost',
        'USER': 'root',
        'OPTIONS': {
            "init_command": "SET GLOBAL max_connections = 100000",
        }
    }
}
```
### url 解析
```python
ROOT_URLCONF = 'mysite.urls'
```
