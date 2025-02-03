from django.http import HttpResponse

class AdminAPIKeyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/admin/') and request.headers.get('X-API-KEY') != 'your_secret_key':
            return HttpResponse('Unauthorized', status=401)
        return self.get_response(request)
