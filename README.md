[![CI](https://github.com/Jason-Guo1999/IDS706-Python-Template/actions/workflows/main.yml/badge.svg)](https://github.com/Jason-Guo1999/IDS706-Python-Template/actions/workflows/main.yml)
# IDS706-Week3-MiniProj
In this mini project, I read students' scores from data.csv. Then used Polars to analysis the data and created data visualization by main.py. The output shows the distribution of input data.csv file.
- ``.devcontainer`` The `Dockerfile` lists configurations for Docker, the `devcontainer.json` is for Visual Studio Code extension.

- ``workflows`` is for github actions, enables automated CI/CD for the project

- ``Makefile`` lists make instruments

- ``requirements.txt`` lists the dependencies for the project
  
- ``main.py`` uses polars to do data analysis on input .csv file, including mean, median and std. I also plot the distribution of grades using matplot.

- ``test_main.py`` testing scripts for CI
