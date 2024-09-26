class InvalidVideoFile(Exception):
    status_code = 400

    def __init__(self, message):
        super().__init__(message)
        self.message = message

class NoVideoFileSelected(Exception):
    status_code = 400

    def __init__(self, message):
        super().__init__(message)
        self.message = message