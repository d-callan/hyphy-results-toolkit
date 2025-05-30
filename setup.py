import os
from setuptools import setup, find_packages

# Read the contents of README.md
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Read version from version.txt or define it here
version = '0.1.0'

setup(
    name="hyphy-results-toolkit",  # Use hyphen for PyPI name
    version=version,
    packages=find_packages(include=['hyphy_results_toolkit', 'hyphy_results_toolkit.*']),
    install_requires=[
        "numpy>=1.20.0",
        "pandas>=1.3.0",
        "scipy>=1.7.0",
    ],
    extras_require={
        'dev': [
            'pytest>=7.0.0',
            'pytest-cov>=4.0.0',
        ],
    },
    entry_points={
        'console_scripts': [
            'hyphy-results=hyphy_results_toolkit.cli:main',
        ],
    },
    author="Danielle Callan, Hannah Verdonk, Sergei L Kosakovsky Pond",
    author_email="spond@temple.edu",
    description="A toolkit for analyzing and summarizing HyPhy evolutionary selection analysis results",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/veg/hyphy-results-toolkit",
    project_urls={
        'Bug Reports': 'https://github.com/veg/hyphy-results-toolkit/issues',
        'Source': 'https://github.com/veg/hyphy-results-toolkit',
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    include_package_data=True,
    zip_safe=False,
)
