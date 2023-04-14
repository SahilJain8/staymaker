from django.contrib.sessions.middleware import SessionMiddleware

class CustomSessionMiddleware(SessionMiddleware):
    def process_request(self, request):
        if not request.user.is_authenticated:
            request.session.flush()
        super().process_request(request)
