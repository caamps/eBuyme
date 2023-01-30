from django.contrib.auth.tokens import PasswordResetTokenGenerator

class AtivarContaTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp: int) -> str:
        return super()._make_hash_value(user, timestamp)

activationToken = AtivarContaTokenGenerator()
