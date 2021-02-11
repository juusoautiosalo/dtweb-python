# DTWeb-python
Python library for accessing the Digital Twin Web


## Install

In Ubuntu 20.04

Terminal calls to install dtweb

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

# Uninstall earlier install (required if earlier install with same/higher version number exists)
pip uninstall dtweb

# Install package
pip install dist/dtweb-0.0.1-py3-none-any.whl

# Show library info (optional)
pip show dtweb
```

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

## Development setup
With Ubuntu 20.04

### Clone Repo

```sh
git clone https://github.com/juusoautiosalo/dtweb-python.git
```

### Virtual environment (recommended)

Create new virtual environment:
```sh
python3 -m venv env
```

Activate the newly created virtual environment
```sh
source env/bin/activate
```

> To deactivate virtual environment:
> ```sh
> deactivate
> ```
