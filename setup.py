import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="calc-invest-DaringDane", # Replace with your own username
    version="0.0.1",
    author="Dane Gunther",
    author_email="danecgunther@gmail.com",
    description="Future Investment Portfolio Calculator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DaringDane/Calc_Invest",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

# reference for setup file:
# https://packaging.python.org/tutorials/packaging-projects/
