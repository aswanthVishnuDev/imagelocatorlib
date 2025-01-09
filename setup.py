from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="my_imagelocatorlib",
    version="0.1.0",
    author="Aswanth",
    author_email="aswanth.ravikumarjaya@nttdata.com",
    description="A library for locating image in a windows screen",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aswanthVishnuDev/imagelocatorlib",
    packages=find_packages(),
    install_requires=[
        "pyautogui >= 0.9.54",
        "PyScreeze >= 1.0.1",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    python_requires=">=3.7",
)