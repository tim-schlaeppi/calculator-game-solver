from base_operation import BaseOperation


"""
Each operation consist of two parts: __call__ and __str__:
    __call__: each time the operation is called, __call__ is passed the current number x, performs the specified
        operation to this number and returns it
    __str__: When the correct way is found, the path to the solution gets displayed as a list of operations. This
        list consists of the string representations of these operations.  

Each implementation of __call__ must must return an int. If by doing that an error is hidden, it must check for that
error itself and pass one, meaniing no valid result. Example: DivideBy

The x passed to __call__ always meets the following requirements:
    -99'999 < x < 999'999
    x % 1 == 0
    isinstance(x, int)
"""


class Add(BaseOperation):
    def __call__(self, context):
        context.number += self.number

    def __str__(self):
        return f"x + {self.number}"


class Subtract(BaseOperation):
    def __call__(self, context):
        context.number -= self.number

    def __str__(self):
        return f"x - {self.number}"


class MultiplyBy(BaseOperation):
    def __call__(self, context):
        context.number *= self.number

    def __str__(self):
        return f"x * {self.number}"


class DivideBy(BaseOperation):
    def __call__(self, context):
        x = context.number / self.number
        if x % 1 != 0:
            context.number = None
        else:
            context.number = int(x)

    def __str__(self):
        return f"x / {self.number}"


class RaiseBy(BaseOperation):
    def __call__(self, context):
        context.number = context.number ** self.number

    def __str__(self):
        return f"x ** {self.number}"


class DeleteLast(BaseOperation):
    def __init__(self):
        pass

    def __call__(self, context):
        x = str(context.number)
        x = x[:-1]
        if x == "" or x == "-":
            x = "0"
        context.number = int(x)

    def __str__(self):
        return f"x <-"


class Append(BaseOperation):
    def __call__(self, context):
        x = str(context.number)
        x = x + str(self.number)
        context.number = int(x)

    def __str__(self):
        return f"x || {self.number}"


class Replace(BaseOperation):
    def __init__(self, number, replace_with):
        self.number = number
        self.replace_with = replace_with

    def __call__(self, context):
        x = str(context.number)
        x = x.replace(str(self.number), str(self.replace_with))
        if x == "":
            x = "0"
        context.number = int(x)

    def __str__(self):
        return f"{self.number} -> {self.replace_with}"


class FlipSign(BaseOperation):
    def __init__(self):
        pass

    def __call__(self, context):
        context.number *= -1

    def __str__(self):
        return f"-x"


class Reverse(BaseOperation):
    def __init__(self):
        pass

    def __call__(self, context):
        x = str(context.number)[::-1].replace("-", "")
        x = int(x)

        if context.number < 0:
            x *= -1

        context.number = x

    def __str__(self):
        return f"x -><-"


class Sum(BaseOperation):
    def __init__(self):
        pass

    def __call__(self, context):
        x = str(abs(context.number))

        x = sum(map(lambda n: int(n), x))

        if context.number < 0:
            x *= -1
        context.number = x

    def __str__(self):
        return f"Σ x"


class ShiftLeft(BaseOperation):
    def __init__(self):
        pass

    def __call__(self, context):
        x = str(abs(context.number))
        if len(x) > 1:
            x = x[1:] + x[0]

        x = int(x)

        if context.number < 0:
            x *= -1

        context.number = x

    def __str__(self):
        return f"x <<"


class ShiftRight(BaseOperation):
    def __init__(self):
        pass

    def __call__(self, context):
        x = str(abs(context.number))
        if len(x) > 1:
            x = x[-1] + x[:-1]

        x = int(x)

        if context.number < 0:
            x *= -1

        context.number = x

    def __str__(self):
        return f"x >>"


class Mirror(BaseOperation):
    def __init__(self):
        pass

    def __call__(self, context):
        x = str(abs(context.number))
        x = x + x[::-1]
        x = int(x)

        if context.number < 0:
            x *= -1

        context.number = x

    def __str__(self):
        return f"x || x -><-"


class Inverse10(BaseOperation):
    def __init__(self):
        pass

    def __call__(self, context):
        result = ""
        x = str(context.number)
        for digit in x:
            if digit == "-":
                result += "-"
            else:
                result += str((10 - int(digit)) % 10)

        context.number = int(result)

    def __str__(self):
        return f"inv10 x"


class AddToButton(BaseOperation):
    is_meta_resistant = True
    will_change_number = False

    def __call__(self, context):
        for operation in context.config["operations"]:
            if not operation.is_meta_resistant:
                operation.number += self.number

    def __str__(self):
        return f"[+] {self.number}"


class MultiplyOnButton(BaseOperation):
    is_meta_resistant = True
    will_change_number = False

    def __call__(self, context):
        for operation in context.config["operations"]:
            if not operation.is_meta_resistant:
                operation.number *= self.number

    def __str__(self):
        return f"[*] {self.number}"


class SaveOperation(BaseOperation):
    def __init__(self):
        pass

    will_change_number = False
    is_meta_resistant = True

    def __call__(self, context):
        context.saved_state.saved_number = abs(context.number)

    def __str__(self):
        return f"save"


class RestoreOperation(BaseOperation):
    def __init__(self):
        pass

    is_meta_resistant = True

    def __call__(self, context):
        if context.saved_state.saved_number is None:
            context.invalid_operation = True
            return
        context.number = int(str(context.number) + str(context.saved_state.saved_number))

    def __str__(self):
        return f"restore"


def save():
    save_operation = SaveOperation()
    restore_operation = RestoreOperation()

    return save_operation, restore_operation

