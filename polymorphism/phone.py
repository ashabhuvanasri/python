class AndroidPhone:
    def call(self):
        print("Calling from Android phone.")


class iPhone:
    def call(self):
        print("Calling from iPhone.")


def make_call(phone):
    phone.call()


make_call(AndroidPhone())
make_call(iPhone())