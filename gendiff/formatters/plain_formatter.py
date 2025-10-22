from typing import MutableMapping, MutableSequence


def sanitize_plain_value(value):
    if value is None:
        return 'null'
    elif isinstance(value, bool):
        return str(value).lower()
    elif isinstance(value, str):
        return f'\'{value}\''
    elif isinstance(value, (MutableSequence, MutableMapping)):
        return '[complex value]'
    return value


def _plain_format(diff_stubs, prefix, buf):
    """
    Copy result for plain format into buf
    """

    for stub in diff_stubs:
        key = f'{prefix}{stub["key"]}'
        value = sanitize_plain_value(stub['value'])
        match stub['action']:
            case 'added':
                buf.append(
                    f'Property \'{key}\' was added with value: {value}'
                )
            case 'deleted':
                buf.append(
                    f'Property \'{key}\' was removed'
                )
            case 'modified':
                new_value = sanitize_plain_value(stub['new_value'])
                buf.append(
                    f'Property \'{key}\' was updated. '
                    f'From {value} to {new_value}',
                )
            case 'inline':
                _plain_format(stub['value'], f'{key}.', buf)


def plain_format(diff_stubs):
    buf = []
    _plain_format(diff_stubs, '', buf)
    return '\n'.join(buf)
