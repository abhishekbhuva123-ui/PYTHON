# Copilot Instructions for PYTHON-1

## Project Overview
This is a simple Python project with a single script (`Hello.py`) located in `PYTHON/PYTHON-1/`. The project uses a local virtual environment in `PYvenv/` for dependency management and isolation.

## Architecture & Structure
- **Main Script:** `PYTHON/PYTHON-1/Hello.py` is the entry point and currently the only source file.
- **Virtual Environment:** All Python dependencies are installed in `PYvenv/`. The `Scripts/` directory contains executables for Python, pip, and Jupyter tools.
- **No Frameworks:** The project does not use any web frameworks, build systems, or test runners by default.

## Developer Workflows
- **Running Code:**
  - Activate the virtual environment before running scripts:
    - PowerShell: `./PYvenv/Scripts/Activate.ps1`
    - CMD: `PYvenv\Scripts\activate.bat`
  - Run scripts using the Python executable in the venv:
    - `./PYvenv/Scripts/python.exe PYTHON/PYTHON-1/Hello.py`
- **Installing Packages:**
  - Use pip from the venv: `./PYvenv/Scripts/pip.exe install <package>`
- **Jupyter Notebooks:**
  - Notebooks can be run using `jupyter.exe` in the venv. Example: `./PYvenv/Scripts/jupyter.exe notebook`

## Conventions & Patterns
- **Single Script:** All logic is currently in `Hello.py`. If expanding, place new scripts in `PYTHON/PYTHON-1/`.
- **No Custom Modules:** Only standard library and installed packages are used. No custom package structure.
- **No Tests:** There are no test files or test runners configured.
- **No README or Documentation:** No markdown files or project documentation are present.

## External Dependencies
- All dependencies are managed via the local venv (`PYvenv/Lib/site-packages`).
- Common packages installed include Jupyter, IPython, and various utilities (see `site-packages/`).

## Integration Points
- **Jupyter:** Notebooks can be created and run using the venv's Jupyter installation.
- **No External Services:** The project does not currently integrate with databases, APIs, or other services.

## Example Workflow
```powershell
# Activate venv
./PYvenv/Scripts/Activate.ps1
# Run main script
./PYvenv/Scripts/python.exe PYTHON/PYTHON-1/Hello.py
# Install a package
./PYvenv/Scripts/pip.exe install requests
```

## Key Files & Directories
- `PYTHON/PYTHON-1/Hello.py`: Main script
- `PYvenv/`: Virtual environment
- `PYvenv/Scripts/`: Python, pip, Jupyter executables
- `PYvenv/Lib/site-packages/`: Installed packages

---

If you add new scripts, tests, or documentation, update this file to reflect new conventions and workflows.
