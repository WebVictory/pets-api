from rest_framework import permissions

from pets_api import settings

#А.  Реализация API Key Authentication:
class APIKeyPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        api_key = request.headers.get('X-API_KEY')
        if api_key == settings.API_KEY:
            return True
        else:
            return False

from rest_framework import exceptions, status, views

#если совпадает - обрабатываем запрос
#несовпадает-401 Unauthorized без это функции код 403
def custom_exception_handler(exc, context):
    response = views.exception_handler(exc, context)
    if isinstance(exc, (exceptions.AuthenticationFailed, exceptions.NotAuthenticated)):
        response.status_code = status.HTTP_401_UNAUTHORIZED
    return response
