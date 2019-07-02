def flatten_array(input):
    """
       :return: flatten array
       """
    output = []
    if isinstance(input, list):
        for item in input:
            if isinstance(item, list):
                output.extend(flatten_array(item))
            else:
                if isinstance(item, int):
                    output.append(item)
                else:
                    raise ValueError('input should contain only integers')
    else:
        raise ValueError('input should be a list')
    return output
