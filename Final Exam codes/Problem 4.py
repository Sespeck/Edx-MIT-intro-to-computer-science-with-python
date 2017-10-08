def max_val(t):
    """ t, tuple or list
        Each element of t is either an int, a tuple, or a list
        No tuple or list is empty
        Returns the maximum int in t or (recursively) in an element of t """
    # answer found on https://stackoverflow.com/questions/45391342/going-through-a-tuple-finding-max-number-nested-list-recursively
    def deep_flatten(t):

        # if t is an int, just return a list with that int in it. No recursions needed.
        if isinstance(t, int):
            return [t]

        # if t is a list or tuple, do some recursions to deep-flatten it:
        elif isinstance(t, (list, tuple)):

            # initialise result
            result = []

            # define a recursive function
            def update_result(t):
                for item in t:
                    if isinstance(item, (list, tuple)):
                        update_result(item)
                    else:
                        result.append(item)

            # mutate result by performing recursions
            update_result(t)

            # return it
            return result

    # use our helper deep flattening function to output a flatten list
    t_flatten = deep_flatten(t)

    # empty tuple / list case
    if len(t_flatten) == 0:
        return None

    # return the max element in a non-empty list / tuple input
    return max(t_flatten)
