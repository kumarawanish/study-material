from typing import Any


class Mymiddleware:
    def __init__(self, get_response) -> None:
        self.get_response = get_response



    def __call__(self, request, **kwargs):
        print("Before the view")
        response = self.get_response(request)
        request.session['data'] = 'hellow'
        print("session",request.session.get('data'))

        print("After the view",request.META.get('HTTP_USER_AGENT'))

        return response


        