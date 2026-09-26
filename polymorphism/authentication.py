class PasswordLogin:
    def login(self):
        print("Logged in using password.")


class OTPLogin:
    def login(self):
        print("Logged in using OTP.")


class BiometricLogin:
    def login(self):
        print("Logged in using biometric authentication.")


def authenticate(user):
    user.login()


authenticate(PasswordLogin())
authenticate(OTPLogin())
authenticate(BiometricLogin())