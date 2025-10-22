install:
	uv sync

build:
	uv build

package-install:
	uv tool install --force dist/*.whl

lint:
	uv run ruff check gendiff

test-cov:
	uv run pytest --cov=gendiff --cov-report=xml:coverage.xml
