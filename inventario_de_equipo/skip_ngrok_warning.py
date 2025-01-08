# myproject/middleware/skip_ngrok_warning.py
from django.utils.deprecation import MiddlewareMixin

class SkipNgrokWarningMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        # Añadir el encabezado a la respuesta
        response['ngrok-skip-browser-warning'] = 'true'
        return response
