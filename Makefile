VERSION_FILE := src/django_rest_swagger_swaggerdoc/__init__.py
BUILD_LOG := .build.log

.PHONY: help
help:
	@echo "Subcommands:"
	@echo "- bump version=VERSION"
	@echo "- production"
	@echo "- staging"
	@echo "- version"

.PHONY: bump
bump:
	@if [ "$(version)" == "" ]; then echo "You must specify the version.\nex) make bump version=VERSION"; exit 1; fi
	@sed -i -e "s/$(shell make version)/$(version)/" $(VERSION_FILE)
	@git diff $(VERSION_FILE)
	@make version
	@git commit -m "bump version to $(version)" $(VERSION_FILE)

.PHONY: production
production:
	python setup.py sdist bdist_wheel upload

.PHONY: staging
staging:
	python setup.py sdist bdist_wheel upload -r https://testpypi.python.org/pypi

.PHONY: test
test:
	detox -v

.PHONY: version
version:
	@rm -f $(BUILD_LOG)
	@python setup.py build 2> $(BUILD_LOG) 1> /dev/null
	@if [ -s $(BUILD_LOG) ]; then cat $(BUILD_LOG); exit 1; fi
	@grep "^Version" `gfind -name PKG-INFO` | cut -d " " -f 2
