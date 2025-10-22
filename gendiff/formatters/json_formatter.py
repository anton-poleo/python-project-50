import json


def json_format(diff_stubs):
    return json.dumps(diff_stubs, indent=4, separators=(',', ': '))
