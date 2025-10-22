from gendiff.core.stubs import generate_diff_stubs
from gendiff.scripts.file_handler import parse_file_content
from gendiff.formatters.json_formatter import json_format
from gendiff.formatters.plain_formatter import plain_format
from gendiff.formatters.stylish_formatter import stylish_format


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
