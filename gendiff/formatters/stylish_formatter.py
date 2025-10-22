def sanitize_stylish_value(value, tab_num):
    if value is None:
        return 'null'
    if isinstance(value, bool):
        return str(value).lower()
    elif not isinstance(value, dict):
        return value

    tab = '    ' * tab_num
    result = []
    for k, v in value.items():
        result.append(f'{tab}    {k}: {sanitize_stylish_value(v, tab_num + 1)}')
    return '{\n' + '\n'.join(result) + f'\n{tab}}}'


def stylish_format(diff_stubs, tab_num=0):
    tab = '    ' * tab_num
    result = []
    for stub in diff_stubs:
        value = sanitize_stylish_value(stub['value'], tab_num + 1)
        if stub['action'] == 'inline':
            result.append(
                f'{tab}    {stub["key"]}: '
                f'{stylish_format(stub["value"], tab_num + 1)}',
            )
        elif stub['action'] == 'added':
            result.append(f'{tab}  + {stub["key"]}: {value}')
        elif stub['action'] == 'deleted':
            result.append(f'{tab}  - {stub["key"]}: {value}')
        elif stub['action'] == 'not_modified':
            result.append(f'{tab}    {stub["key"]}: {value}')
        elif stub['action'] == 'modified':
            new_value = sanitize_stylish_value(stub['new_value'], tab_num + 1)
            result.append(f'{tab}  - {stub["key"]}: {value}')
            result.append(f'{tab}  + {stub["key"]}: {new_value}')

    content = '\n'.join(result)
    return f'{{\n{content}\n{tab}}}'
