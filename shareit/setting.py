ALLOWED_HOSTS = ['shareit-community.herokuapp.com', 'localhost']

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]

# Application definition

@@ -59,8 +66,7 @@

SITE_ID = 1

# LOGIN_REDIRECT_URL = 'home'
# LOGOUT_REDIRECT_URL = 'index'
LOGIN_REDIRECT_URL = 'index'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',