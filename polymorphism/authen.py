from abc import ABC, abstractmethod


class Authentication(ABC):

    @abstractmethod
    def login(self):
        pass


class PasswordAuth(Authentication):
    def login(self):
        print("Login using password.")


class OTPAuth(Authentication):
    def login(self):
        print("Login using OTP.")


class BiometricAuth(Authentication):
    def login(self):
        print("Login using fingerprint.")


methods = [PasswordAuth(), OTPAuth(), BiometricAuth()]

for method in methods:
    method.login()