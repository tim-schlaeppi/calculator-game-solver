class BaseOperation:
    def __init__(self, number):
        self.number = number

    is_meta_operation = False
    is_meta_resistant = False
    will_change_number = True
    number = 0


class SavedState:
    saved_number = None


class Portal:
    from_position = None
    to_position = None

    def __init__(self, from_position, to_position):
        self.from_position = from_position
        self.to_position = to_position

    def execute(self, number):
        is_negative = number < 0
        number = str(abs(number))

        portal_digit = number[-self.from_position]
        number = int(number[:-self.from_position] + number[-self.from_position + 1:])

        number = number + int(portal_digit) * 10**(self.to_position - 1)

        if is_negative:
            number *= -1
        return number

    def applies_to(self, number):
        if not isinstance(number, int):
            return False
        return len(str(abs(number))) >= self.from_position
