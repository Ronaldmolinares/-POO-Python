class ExceptionLibrary(Exception):
    pass


class InvalidTitleError(ExceptionLibrary):
    pass


class BookNotAvailableError(ExceptionLibrary):
    pass


class LoanLimitError(ExceptionLibrary):
    pass


class UserNotFoundError(ExceptionLibrary):
    pass
