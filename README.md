# Instructions

From within VSCode...

1. Press `Cmd + Shift + P`
2. Select `Python: Create Environment`
3. Select `Venv`
4. Add new terminal below (`+`) and ensure the new console has a prefix of `(.venv)`.
5. You may now `pip3 install` needed packages, such as `pip3 install pandas`.

# Recommendations

Install the following extensions:

1. `Python` (by Microsoft)
2. `Black Formatter` (by Microsoft)
3. `Jupyter` (by Microsoft)

# Notes

- If you'd like to create a Jupyter Notebook, press `Cmd + Shift + P`, then search for and select `Create: New Jupyter Notebook`.
- Ensure that the kernel in the upper right corner of your notebook is set to your `venv`.
- The first time you try to execute a cell in a notebook, VSCode will ask to install `ipykernel`, simply accept this (will result in some additional pip3 installs within your virtual environment, which can be observed by typing `pip3 list`).
- All dependencies for this project exist within the `.venv` folder.
- You can generate the `requirement.txt` file by typing `pip3 freeze > requirement.txt` from within your `venv` terminal.
