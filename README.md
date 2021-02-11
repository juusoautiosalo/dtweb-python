# DTWeb-python
Python library for accessing the Digital Twin Web


| :exclamation: Alpha release :exclamation: |
|:------------------------------------------|
|*0.0.x denotes an alpha phase release. Anything may change in future releases without notice.* |


## Install

```sh
# Create and activate virtual environment (recommended)
python3 -m venv env
source env/bin/activate

# Install with pip
pip install dtweb
```

> To deactivate virtual environment:
> ```sh
> deactivate
> ```

## Usage

```python
import dtweb

dtweb.client.fetch_host_url('<DTID>')

dtweb.client.fetch_dt_doc('<DTID>')
```

### Usage example:
```python
import dtweb

# Fetch and pring hosting URL from DTID of Ilmatar crane
crane_hosturl = dtweb.client.fetch_host_url('http://d-t.fi/konecranes-K16052')
print(crane_hosturl)

# Fetch and pring DT document from DTID of Ilmatar crane
crane_doc = dtweb.client.fetch_dt_doc('http://d-t.fi/konecranes-K16052')
print(crane_doc)
```

## Development instructions

<details>
<summary>Click to show</summary>

OS: Ubuntu 20.04 WSL (Ubuntu 20.04.1 LTS (GNU/Linux 4.4.0-18362-Microsoft x86_64))

### Setup new computer

> Hint: You can just copy and paste this whole code block to terminal. Dirty but works.

```sh
# Clone repository
git clone https://github.com/juusoautiosalo/dtweb-python.git

# Change directory
cd dtweb-python

# Create virtual environment (recommended)
python3 -m venv env

# Activate virtual environment (recommended)
source env/bin/activate

# Install python package builder
pip install build

# Build the dtweb package
python3 -m build

# Uninstall earlier installation (required if earlier install with same/higher version number exists)
pip uninstall dtweb

# Install package (edit version number if needed)
pip install dist/dtweb-0.0.1-py3-none-any.whl

# Show library info (optional)
pip show dtweb
```

### Uploading to TestPyPI

```sh
# Install twine
pip install twine

# Upload to test repository (You will need TestPyPI credentials for this)
twine upload --repository testpypi dist/*
```

### Install from TestPyPI

```sh
pip install -i https://test.pypi.org/simple/ dtweb
```

</details>
