class BaseOperation:
    def __init__(self, number):
        self.number = number

    is_meta_operation = False
    is_meta_resistant = False
    number = 0


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
    def __call__(self, x):
        return self.number + x

    def __str__(self):
        return f"x + {self.number}"


class Subtract(BaseOperation):
    def __call__(self, x):
        return x - self.number

    def __str__(self):
        return f"x - {self.number}"


class MultiplyBy(BaseOperation):
    def __call__(self, x):
        return self.number * x

    def __str__(self):
        return f"x * {self.number}"


class DivideBy(BaseOperation):
    def __call__(self, x):
        x = x / self.number
        if x % 1 != 0:
            return
        return int(x)

    def __str__(self):
        return f"x / {self.number}"


class RaiseBy(BaseOperation):
    def __call__(self, x):
        return x ** self.number

    def __str__(self):
        return f"x ** {self.number}"


class DeleteLast(BaseOperation):
    def __init__(self):
        pass

    def __call__(self, x):
        x = str(x)
        x = x[:-1]
        if x == "" or x == "-":
            x = "0"
        return int(x)

    def __str__(self):
        return f"x <-"


class Append(BaseOperation):
    def __call__(self, x):
        x = str(x)
        x = x + str(self.number)
        return int(x)

    def __str__(self):
        return f"x || {self.number}"


class Replace(BaseOperation):
    def __init__(self, number, replace_with):
        self.number = number
        self.replace_with = replace_with

    def __call__(self, x):
        x = str(x)
        x = x.replace(str(self.number), str(self.replace_with))
        if x == "":
            x = "0"
        return int(x)

    def __str__(self):
        return f"{self.number} -> {self.replace_with}"


class FlipSign(BaseOperation):
    def __init__(self):
        pass

    def __call__(self, x):
        return -x

    def __str__(self):
        return f"-x"


class Reverse(BaseOperation):
    def __init__(self):
        pass

    def __call__(self, x):
        is_negative = x < 0
        x = str(x)[::-1].replace("-", "")
        x = int(x)

        if is_negative:
            x *= -1

        return x

    def __str__(self):
        return f"x -><-"


class Sum(BaseOperation):
    def __init__(self):
        pass

    def __call__(self, x):
        is_negative = x < 0
        x = str(abs(x))

        if is_negative:
            return -sum(map(lambda n: int(n), x))
        else:
            return sum(map(lambda n: int(n), x))

    def __str__(self):
        return f"Σ x"


class ShiftLeft(BaseOperation):
    def __init__(self):
        pass

    def __call__(self, x):
        is_negative = x < 0
        x = str(abs(x))
        if len(x) > 1:
            x = x[1:] + x[0]

        x = int(x)

        if is_negative:
            x *= -1

        return x

    def __str__(self):
        return f"x <<"


class ShiftRight(BaseOperation):
    def __init__(self):
        pass

    def __call__(self, x):
        is_negative = x < 0
        x = str(abs(x))
        if len(x) > 1:
            x = x[-1] + x[:-1]

        x = int(x)

        if is_negative:
            x *= -1

        return x

    def __str__(self):
        return f"x >>"


class Mirror(BaseOperation):
    def __init__(self):
        pass

    def __call__(self, x):
        is_negative = x < 0
        x = str(abs(x))
        x = x + x[::-1]
        x = int(x)

        if is_negative:
            x *= -1

        return x

    def __str__(self):
        return f"x || x -><-"


class AddToButton(BaseOperation):
    is_meta_operation = True
    is_meta_resistant = True

    def __call__(self, config):
        for operation in config["operations"]:
            if not operation.is_meta_resistant:
                operation.number += self.number

        return config

    def __str__(self):
        return f"[+] {self.number}"


class MultiplyOnButton(BaseOperation):
    is_meta_operation = True
    is_meta_resistant = True

    def __call__(self, config):
        for operation in config["operations"]:
            if not operation.is_meta_resistant:
                operation.number *= self.number

        return config

    def __str__(self):
        return f"[*] {self.number}"
