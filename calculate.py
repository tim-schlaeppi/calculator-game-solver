from copy import deepcopy


def calculate(number, config, moves_left, operations_list):
    # Checks if the number is not invalid among other things
    if number is None:
        return
    if moves_left <= -1:
        return
    if number % 1 != 0:
        return
    if len(str(number)) > 6:
        return

    # Success!
    if number == config["end"]:
        print("\n".join(operations_list))
        return number

    # Goes deeper into recursion for each Operation
    for operation in config["operations"]:
        # In case the Operation is successful, prepare the list how to get there
        new_operations_list = operations_list + [str(operation)]

        # If it's a meta operation, it modifies the config instead of the number
        # Deepcopy, because th config is only changed after this point, not up the tree
        if operation.is_meta_operation:
            new_number = calculate(number, operation(deepcopy(config)), moves_left - 1, new_operations_list)
        else:
            new_number = calculate(operation(number), config,  moves_left - 1, new_operations_list)

        # calculate only returns a number if it's the result. Pass this result up the tree
        if new_number is not None:
            return new_number
