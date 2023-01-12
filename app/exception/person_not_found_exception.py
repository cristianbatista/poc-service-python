from app.shared.root_exception import RootException


class PersonNotFoundException(RootException):
    def __init__(self):
        super().__init__("Person was not found")
