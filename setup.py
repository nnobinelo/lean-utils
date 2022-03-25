from setuptools import setup


def read_file(path):
    with open(path, "r") as fp:
        return fp.read()


# List of dependencies installed via `pip install -e .`
# by virtue of the Setuptools `install_requires` value below.
requires = read_file("./requirements.txt")
version = read_file("./VERSION")

setup(
    name="LeanUtils",
    version=version,
    install_requires=requires,
    entry_points={
        "console_scripts": ["lean-utils-plot=LeanUtils.plot_backtest:main"]
    }
)
