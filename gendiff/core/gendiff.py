from gendiff.core.file_handler import parse_file_content
from gendiff.formatter.json_formatter import json_format
from gendiff.formatter.plain_formatter import plain_format
from gendiff.formatter.stylish_formatter import stylish_format


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


def generate_diff(first_file, second_file, format_type='stylish'):
    diff = generate_diff_stubs(
        parse_file_content(first_file),
        parse_file_content(second_file),
    )
    if format_type == 'plain':
        return plain_format(diff)
    elif format_type == 'json':
        return json_format(diff)
    elif format_type == 'stylish':
        return stylish_format(diff)
