class RootException(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __repr__(self):
        return f"<{self.__class__.__name__} {self.message}>"
