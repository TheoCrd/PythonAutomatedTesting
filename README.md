# PythonAutomatedTesting
<p align="center">
    <strong>Initiation to Automated Testing in Python (w/ Pytest, tox & GitHub Actions).</strong>
</p>

<p align="center">
    <img src="https://github.com/TheoCrd/PythonAutomatedTesting/actions/workflows/tests.yml/badge.svg" alt="Tests">
    <a href="https://codecov.io/gh/TheoCrd/PythonAutomatedTesting" >
        <img src="https://codecov.io/gh/TheoCrd/PythonAutomatedTesting/graph/badge.svg?token=WS88R8LVLC"/>
    </a>
    <a href="https://github.com/pre-commit/pre-commit">
        <img src="https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white" alt="pre-commit">
    </a>
    <a href="https://results.pre-commit.ci/latest/github/TheoCrd/PythonAutomatedTesting/master">
        <img src="https://results.pre-commit.ci/badge/github/TheoCrd/PythonAutomatedTesting/master.svg" alt="pre-commit.ci status">
    </a>
</p>

<p align="center">
    <strong>Coverage on master branch</strong>
</p>

<p align="center">
    <a href="https://app.codecov.io/gh/TheoCrd/PythonAutomatedTesting">
        <img src="https://codecov.io/gh/TheoCrd/PythonAutomatedTesting/graphs/sunburst.svg?token=WS88R8LVLC" alt="Coverage on master branch">
    </a>
</p>

<p align="center">
    Click on the graph to access Codecov overview
</p>

1. **Clone the Repository**:
    ```sh
    git clone https://github.com/TheoCrd/PythonAutomatedTesting.git
    cd PythonAutomatedTesting
    ```

2. **Create a Virtual Environment**:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the `requirements`**:
    ```sh
    pip install -r requirements.txt
    ```

4. **(Optional) Install the `requirements_dev`**:
    ```sh
    pip install -r requirements_dev.txt
    ```

5. **Run `tox`**:
    ```sh
    tox
    ```
