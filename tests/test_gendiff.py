from pathlib import PosixPath

import pytest

from gendiff.core.gendiff import generate_diff

BASE_TESTS_PATH = PosixPath(__file__).parent


@pytest.mark.parametrize(
    '_dir, ext, format_type',
    [
        ('json', 'json', 'stylish'),
        ('yaml', 'yaml', 'stylish'),
        ('recursive_json', 'json', 'stylish'),
        ('plain', 'json', 'plain'),
        ('json_format', 'json', 'json'),
    ]
)
def test_generate_diff(_dir, ext, format_type):
    output = generate_diff(
        (BASE_TESTS_PATH / 'test_data' / _dir / f'file1.{ext}').as_posix(),
        (BASE_TESTS_PATH / 'test_data' / _dir / f'file2.{ext}').as_posix(),
        format_type=format_type,
    )
    print(output)

    with open(BASE_TESTS_PATH / 'test_data' / _dir / 'output.txt') as fd:
        result = fd.read()

    assert output == result
