class Password(object):
    def __init__(self, password):
        self.__password = password

    def __str__(self):
        return len(self.__password) * '*'

    def resolve_password(self):
        return self.__password

    def change_password(self, new_password):
        self.__password = new_password

    def check_validity(self, ):

        if no_shorter_than_8(self.__password):
            func1 = True
        elif contains_special_chars(self.__password):
            func2 = True
        elif starts_upper_case(self.__password):
            func3 = True
        else:
            func1 = False
        if func1 and func2 and func3 is True:
            return True
        else:
            return False


def no_shorter_than_8(string):
    return len(string) >= 8


def contains_special_chars(string):
    return not string.isalnum()


def starts_upper_case(string):
    if string[0].isupper():
        return True
    return False


pw1 = Password('Password_1234')
print(pw1)
print(pw1.resolve_password())
print(pw1.check_validity(no_shorter_than_8, contains_special_chars, starts_upper_case))
pw1.change_password('password_1234')
print(pw1.check_validity(starts_upper_case))
