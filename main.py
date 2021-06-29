import operations
from calculate import calculate


config = {
    "start": 0,
    "end": 121,
    "moves": 5,
    "operations": [
        operations.Add(1),
        *operations.save()
    ]
}

calculate(config)
