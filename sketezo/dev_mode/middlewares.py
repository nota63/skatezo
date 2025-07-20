from django.shortcuts import redirect
from django.conf import settings

class DevModeByHTTPS:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if request is HTTPS (i.e., you're in production)
        is_https = request.is_secure()

        # If in production (HTTPS), redirect to the dev notice page
        if is_https:
            # Allow access to the dev notice page itself
            if request.path == '/dev_mode/sketezo_development/':
                return self.get_response(request)

            return redirect('sketezo_development')

        # Otherwise (local dev or HTTP), allow access
        return self.get_response(request)
