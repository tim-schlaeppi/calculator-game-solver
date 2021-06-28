import operations
import calculate


config = {
    "start": 0,
    "end": 10,
    "moves": 4,
    "operations": [
        operations.Add(1),
        operations.AddToButton(3)
    ]
}

calculate.calculate(config["start"], config, config["moves"], [])
