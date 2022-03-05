.PHONY: test
test:
	pytest --cov=hab_scraper -vv tests/
	flake8 hab_scraper tests/
	mypy hab_scraper --implicit-reexport
	black hab_scraper tests/
	isort hab_scraper tests/

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
