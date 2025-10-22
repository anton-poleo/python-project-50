### Hexlet tests and linter status:
[![Actions Status](https://github.com/anton-poleo/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/anton-poleo/python-project-50/actions)

[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=anton-poleo_python-project-50&metric=coverage)](https://sonarcloud.io/summary/new_code?id=anton-poleo_python-project-50)
# Вычислитель отличий (gendiff)

Утилита вычисления отличий между двумя файлами


## Зависимости

- python 3.12+

- uv 0.8.3+

## Установка

```shell
git clone git@github.com:anton-poleo/python-project-50.git
cd python-project-50
uv build
uv package-install
```

### Формат входных данных
- JSON
- YAML

*Определяется по расширению файла (json, yml, yaml)

### Формат выходных данных

- json (выводятся json стабы без форматирования)
- plain
- stylish


### Запуск
````
gendiff /path/to/file1.json /path/to/file2.json --format plain
````

*format опциональный, по дефолту stylish

