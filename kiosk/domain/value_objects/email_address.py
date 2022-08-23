import re


class EmailAddress:
    _email: str

    def __init__(self, email_value):
        self.email = email_value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        # Validate email
        regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"

        if not re.fullmatch(regex, value):
            raise EmailInvalidException()

        self._email = value


class EmailInvalidException(Exception):
    pass
