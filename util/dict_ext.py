def combine_dicts(*dicts) -> dict:
    if dicts is None or dicts == tuple():
        return {}

    final_dict = dict()
    for dict_item in dicts:
        if not isinstance(dict_item, dict):
            raise TypeError("combine_dicts only takes in type dict")

        final_dict.update(dict_item)
        # final_dict = dict(final_dict | dict_item)
        # for key, value in dict_item.items():
        #     final_dict[key] = value

    return final_dict


# Example
dict_a = {1: 10, 2: 20}
dict_b = {3: 30, 4: 40}
dict_c = {5: 50, 6: 60}

print(combine_dicts(dict_a, dict_b, dict_c))
