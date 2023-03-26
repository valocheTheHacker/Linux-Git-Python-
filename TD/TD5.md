## TD8/9: Linux, Git and Python
## Exercise 1: Working Directory

# 1. Create an empty working directory called `td4`.
mkdir td4

# 2. Initialize a Git repository in it.
cd td4
git init

# 3. Install the Linux `python3-pip` package using your Linux package manager.
sudo apt-get install python3-pip

# 4. Install the VirtualEnv Python package using `pip3`.
pip3 install virtualenv

# 5. Create a Python virtual environment called `.env`.
virtualenv .env

# Do you see the change in your working directory ?
# Yes, I see a new directory called `.env` in my working directory.

# 6. Activate your virtual environment.
source .env/bin/activate

# Do you see the change in your prompt ?
Answer: Yes, my prompt now includes the name of the virtual environment.

# 7. List the Python packages installed in your virtual environment.
pip list

# 8. Does Git want you to commit something?
# Do you think it is a good thing?
Answer: No, Git does not want me to commit anything yet. It's a good thing to wait until I have made some changes to my code before committing.

# 9. Create a `.gitignore` file to tell Git which files should be untracked.
nano .gitignore

# Do you think it is a good thing?
Answer: Yes, it's a good thing because it can prevent Git from tracking certain files.

# 10. Does Git want you to commit something?
# Do you think it is a good thing this time?
Answer: No, Git still does not want me to commit anything.

# 11. Do your first commit and check that Git is happy now.
git add .
git commit -m "Initial commit"
