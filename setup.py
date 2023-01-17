import setuptools

with open("README.md","r",encoding="utf-8") as f:
    long_desc = f.read()

__version__ = "0.0.0"

REPO_NAME = "python_package"
AUTHOUR_USER_NAME = "Biswajit"
SRC_REPO = "scrape_google"
AUTHOR_EMAIL = "jeetmohapatra98@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOUR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for craping google search results.",
    long_description=long_desc,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOUR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker":f"https://github.com/{AUTHOUR_USER_NAME}/{REPO_NAME}/issues"
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src"),
    install_requires=['ensure == 1.0.2'],
)