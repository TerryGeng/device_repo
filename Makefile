PYTHON = venv/bin/python
PYTEST = venv/bin/pytest
SLICE2PY = venv/bin/slice2py

.PHONY: all clean test
all: clean device_repo/slices/AWG.ice device_repo/slices/host.ice device_repo/slices/Dummy.ice $(SLICE2PY)
	(cd device_repo && ../$(SLICE2PY) --underscore -Islices/ slices/host.ice slices/AWG.ice slices/Dummy.ice)
	(cd device_repo && find device_repo_ice/ -name "*.py" -exec sed -e 's/import device_repo_ice\.\(.*\)/from . import \1/g' -e "s/'device_repo_ice'/'device_repo.device_repo_ice'/g" -i '' {} \;)
	$(PYTHON) device_repo/setup.py develop

clean:
	rm -rf device_repo/device_repo_ice/

test: $(PYTEST)
	$(PYTEST) -x -v --show-capture=log tests/test_dummy.py

$(PYTEST) $(SLICE2PY) $(PYTHON):
	python -m venv venv
	venv/bin/python -m pip install zeroc-ice pyyaml pytest
