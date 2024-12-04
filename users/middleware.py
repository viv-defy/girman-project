import logging
from django.utils.timezone import now


logger = logging.getLogger('access_logger')


class AccessLogMiddleware:
    """
    Middleware to log each access attempt and its outcome (granted or denied).
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        user = request.user
        user_info = user.username if user.is_authenticated else "Anonymous"

        outcome = "granted" if response.status_code < 400 else "denied"

        logger.info(
            f"{now()} | User: {user_info} | Path: {request.path} | "
            f"Method: {request.method} | Outcome: {outcome} | Status: {response.status_code}"
        )

        return response
