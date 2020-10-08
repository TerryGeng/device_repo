PYTHON = venv/bin/python
PYTEST = venv/bin/python -m pytest
SLICE2PY = venv/bin/slice2py

.PHONY: all clean test build
all: clean $(SLICE2PY)
	(cd device_repo && ../$(SLICE2PY) --underscore -Islices/ $(shell (cd device_repo && find slices -name "*.ice")))
	(cd device_repo && find device_repo_ice/ -name "*.py" -exec sed -e 's/import device_repo_ice\.\(.*\)/from . import \1/g' -e "s/'device_repo_ice'/'device_repo.device_repo_ice'/g" -i '' {} \;)
	$(PYTHON) device_repo/setup.py develop

clean:
	rm -rf device_repo/device_repo_ice/

test: $(PYTHON)
	$(PYTEST) -x -v --show-capture=log tests/test_dummy.py

build:
	$(PYTHON) -m pip install wheel
	$(PYTHON) device_repo/setup.py bdist_wheel

$(SLICE2PY) $(PYTHON):
	python -m venv venv
	$(PYTHON) -m pip install zeroc-ice pyyaml pytest
