import operations
from calculate import calculate
from base_operation import Portal

config = {
    "start": 3002,
    "end": 3507,
    "moves": 6,
    "portal": Portal(5, 1),
    "operations": [
        operations.Append(7),
        operations.Replace(3,5),
        operations.Inverse10(),
        operations.ShiftRight(),
    ],
}

print(calculate(config))
