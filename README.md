# Online-learning-with-LSTM-for-real-time-power-demand-forecast.

### Software and Account Requirement

1. [Github Account](https://github.com)
2. [Heroku Account](https://dashboard.heroku.com/login)
3. [VS Code IDE](https://code.visualstudio.com/download)
4. [GIT CLI](https://git-scm.com/downloads)
5. [Anaconda](https://www.anaconda.com/download)

**Install Anaconda**
Download the .exe file from the link and install it.

If the default direcory is selected for installation, add the following PATHs to the environment variable:
```
C:/<base_install_location>\anaconda3\Scripts
C:/<base_install_location>\anaconda3\Library\bin
C:/<base_install_location>\anaconda3\Library\usr\bin
C:/<base_install_location>\anaconda3\Library\mingw-w64\bin
C:/<base_install_location>\anaconda3
```

**Creating a conda environment**
```
conda create -p venv python==3.7 -y
```
```
conda activate venv/
```

**Install dependency and packages using requirements file:**
```
pip install -r requirements.txt
```

**To check for the state of the working directory and the staging area:**
```
git status
```

**To add the untracked files and unstaged file to the staging area:**

1. For all the files in the directory:
```
git add .
```
2. For specific files:
```
git add <file_name>
```

> Note: To ignore file or folder from git, we can add the file/folder names in .gitignore file

**To check all the version maintained by git**
```
git log
```

**To create version/commit all changes by git**
```
git commit -m "<message>"
```

**To push all the changes to github**
```
git push origin -u main
```

**To check the remote 'origin' URL**
```
git remote -v
```