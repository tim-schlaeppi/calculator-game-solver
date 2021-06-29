import operations
from calculate import calculate


config = {
    "start": 12,
    "end": 101,
    "moves": 5,
    "operations": [
        operations.Add(4),
        operations.Inverse10(),
        operations.Sum()
    ]
}

print(calculate(config))
