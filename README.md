# Data Visualization DSL :chart_with_downwards_trend:
Access the powerful data-processing and visualization capabilities of the python 
ecosystem as well as programmatic dynamic updating using a friendly syntax.

## Development
### Getting started
In order to start developing the project, follow these simple steps:
1. Clone the repository if you haven't already
2. In the root project directory, run `make init` (Make should be installed). Follow
the output of this script closely and make sure you perform and required actions.
3. When this is done, you should have a Python virtual environment set up directly
 in the project. You can use the command `make run` to run the main program.
4. Have fun!
### JetBrains IDE setup (Tested for IntelliJ)
It might be useful to run, test, and debug the program through the IDE.
To set up JetBrains configurations with the correct environment, follow these
steps:
1. Open the project normally in the IDE.
2. In project structure (File > Project Structure on Mac), go to
the SDKs tab under Platform Settings.
3. Click the `+` button to add an SDK. Select "Add Python SDK".
4. From the list of options, select "Pipenv Environment". Check that the base 
interpreter path points to a valid Python 3.8 installation, and "Install packages
from Pipfile" is checked. Click `OK` and wait for the process to complete.
5. Go to the Project tab and make sure Project SDK is set to "Pipenv
 (cpsc410_project1_team17) Python 3.8.5". In Modules , click cpsc410_project1_team17.
 In the Dependencies tab, make sure Module SDK is set to "Project SDK Pipenv
 ". Click `OK`.
6. When editing a Python file, if you see an option to "Use Pipenv Interpreter", click
it, and click install from Pipfile.
#### Create a run configuration
1. Click "ADD CONFIGURATION". Click `+` and select "Python" from the list.
2. Call the configuration "Main". For the main script, select `main.py` in the
 root project directory. Check the box for "Use SDK of module" (the module should be
 cpsc410_project1_team17). Click `OK`.
#### Create a testing configuration
1. Click "ADD CONFIGURATION". Click `+` and select "Python tests / Unittests" from the
 list.
2. Call the configuration "Tests" and select "Custom" as the target.
3. In the Additional Arguments field, past the following:
```
discover -s tests -p "test_*.py"
```
Choose to use the SDK of the main module as before. Click `OK`.
### FAQ
1. **How do I add source code?**

    Simply edit or add python files to those found in the `code` directory.

2. **How do I add tests?**

    Add test cases to the files in the `test` directory where appropriate.
See the [unittest docs](https://docs.python.org/3/library/unittest.html)
for more info. If you need to add a new test file, it should be placed directly
in the tests directory and have a name starting with "test_".

3. **How do I add dependencies?**

    Ideally, consult with the team and Dev Lead first. To add to the project,
run `pipenv install <package>` from the root directory and make sure everybody
runs `make-update` upon getting the new Pipfile.

4. **What tools do we use?**
Python (obviously) for our central logic, [numpy](https://numpy.org/doc/stable/user/quickstart.html) for numerical computations, [PyQtGraph](https://pyqtgraph.readthedocs.io/en/latest/introduction.html#examples) for visualization.

### Git Procedure:
- Create new branches for functionality that you're working on
- Commit and push to the branch (make sure you run tests first!)
- Create a pull request to master when you're ready
  - Try to keep pull requests small
  - Squash commits into one if your pull request includes multiple
  - Pull requests require at least one approver to be merged in
