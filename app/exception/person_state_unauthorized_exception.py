from app.shared.root_exception import RootException


class PersonStateUnauthorizedException(RootException):
    def __init__(self):
        super().__init__("State unauthorized")
