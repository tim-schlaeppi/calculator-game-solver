from copy import deepcopy
from base_operation import SavedState
from context import Context


def calculate(config):
    #global count
    #count = 0


    context = Context(config["start"], config, SavedState(), config["moves"] + 1, [])
    result = calculate_recursive(context)
    #print(count)
    return result


def calculate_recursive(context):
    global count
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

    old_num = context.number
    # Goes deeper into recursion for each Operation
    for operation in context.config["operations"]:
        new_context = deepcopy(context)

        # In case the Operation is successful, prepare the list how to get there
        new_context.operations_list = new_context.operations_list + [str(operation)]

        new_context.moves_left -= 1

        # Modifies Opbject 'context', to be passed down the tree
        operation(new_context)

        if "portal" in context.config:
            portal = context.config["portal"]
            number = new_context.number

            while portal.applies_to(number):
                number = portal.execute(number)

            new_context.number = number


        #count += 1
        if new_context.invalid_operation or (new_context.number == old_num and operation.will_change_number):
            continue

        result = calculate_recursive(new_context)

        # calculate only returns the List if it's the result. Pass this result up the tree
        if result is not None:
            return result
