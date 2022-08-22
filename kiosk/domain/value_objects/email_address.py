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
        self._email = value


class EmailInvalidException(Exception):
    pass
