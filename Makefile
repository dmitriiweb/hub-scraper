.PHONY: test
test:
	pytest --cov=hub_scraper -vv tests/
	flake8 hub_scraper tests/
	mypy hub_scraper --implicit-reexport
	black hub_scraper tests/
	isort hub_scraper tests/

.PHONY: docs-serve
docs-serve:
	mkdocs serve

.PHONY: docs-publish
docs-publish:
	mkdocs mkdocs gh-deploy --force

.PHONY: publish
publish:
	poetry build
	poetry publish
