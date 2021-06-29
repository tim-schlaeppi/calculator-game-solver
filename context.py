class Context:
    number = None
    config = None
    saved_state = None
    moves_left = None
    operations_list = None
    invalid_operation = False

    def __init__(self, number, config, saved_state, moves_left, operations_list):
        self.number = number
        self.config = config
        self.saved_state = saved_state
        self.moves_left = moves_left
        self.operations_list = operations_list
