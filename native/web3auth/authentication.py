from native.users.models import User

from .utils import recover_to_addr

class Web3Backend:
    def authenticate(self, request, token, signature):
        try:
            addr = recover_to_addr(token, signature)
            return User.objects.get(username__iexact=addr)
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None