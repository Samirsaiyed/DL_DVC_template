import setuptools

with open("README.md", "r", encoding="utf-8") as f:

    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "deepCNNClassifier"
AUTHOR_USER_NAME = "Samirsaiyed"
SRC_REPO = "deepCNNClassifier"
AUTHOR_EMAIL = "samirsaiyed49@gmail.com"

setuptools.setup(
    name = SRC_REPO,
    version = __version__,
    author = AUTHOR_USER_NAME,
    description ="A small python package for CNN app",
    Long_description = long_description,
    Long_description = "text/markdown",
    url = f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_url = {
        "Bug Tracker" : f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)