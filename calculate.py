from copy import deepcopy
from base_operation import SavedState
from context import Context


def calculate(config):
    context = Context(config["start"], config, SavedState(), config["moves"] + 1, [])
    result = calculate_recursive(context)
    return result


def calculate_recursive(context):
    # Checks if the number is not invalid among other things
    if context.number is None:
        return
    if context.moves_left <= 0:
        return
    if context.number % 1 != 0:
        return
    if len(str(context.number)) > 6:
        return

    # Success!
    if context.number == context.config["end"]:
        print("\n".join(context.operations_list))
        return context.operations_list

    # Goes deeper into recursion for each Operation
    for operation in context.config["operations"]:
        new_context = deepcopy(context)

        # In case the Operation is successful, prepare the list how to get there
        new_context.operations_list = new_context.operations_list + [str(operation)]

        new_context.moves_left -= 1

        # Modifies Opbject 'context', to be passed down the tree
        operation(new_context)

        result = calculate_recursive(new_context)

        # calculate only returns the List if it's the result. Pass this result up the tree
        if result is not None:
            return result
