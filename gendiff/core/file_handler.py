import json
import yaml


def get_file_content(path):
    with open(path, mode='r') as fd:
        return fd.read()


def parse_file_content(path):
    extension = path.split('.')[-1]
    if extension == 'json':
        content = get_file_content(path)
        return json.loads(content)
    elif extension in ('yml', 'yaml'):
        content = get_file_content(path)
        return yaml.safe_load(content)
    else:
        raise ValueError(f'Unknown file format {extension}')
