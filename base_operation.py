class BaseOperation:
    def __init__(self, number):
        self.number = number

    is_meta_operation = False
    is_meta_resistant = False
    will_change_number = True
    number = 0


class SavedState:
    saved_number = None

