def make_deleted_stub(key, value):
    return {
        'action': 'deleted',
        'key': key,
        'value': value
    }


def make_added_stub(key, value):
    return {
        'action': 'added',
        'key': key,
        'value': value
    }


def make_not_modified_stub(key, value):
    return {
        'action': 'not_modified',
        'key': key,
        'value': value
    }


def make_inline_stub(key, value):
    return {
        'action': 'inline',
        'key': key,
        'value': value,
    }


def make_modified_stub(key, value, new_value):
    return {
        'action': 'modified',
        'key': key,
        'value': value,
        'new_value': new_value,
    }


def generate_diff_stubs(left, right):
    stubs = []

    all_keys = left.keys() | right.keys()

    for key in sorted(all_keys):
        if isinstance(left.get(key), dict) and isinstance(right.get(key), dict):
            stubs.append(
                make_inline_stub(
                    key,
                    generate_diff_stubs(left[key], right[key]),
                ),
            )
        elif key in left and key in right and left[key] == right[key]:
            stubs.append(make_not_modified_stub(key, left[key]))
        elif key in left and key in right:
            stubs.append(make_modified_stub(key, left[key], right[key]))
        elif key in left:
            stubs.append(make_deleted_stub(key, left[key]))
        else:
            stubs.append(make_added_stub(key, right[key]))

    return stubs
