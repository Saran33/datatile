from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
	
setup(
    name='datatile',
    packages=find_packages(include=['datatile']),
    version='0.2.0',
	author='Polyaxon, Inc',
    description='A data catalog, summary, viz, and profiling package.',
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/polyaxon/datatile",
    project_urls={
        "Bug Tracker": "https://github.com/polyaxon/datatile/issues",
    },
	classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Apache 2.0",
        "Operating System :: OS Independent",
    ],
	install_requires = [
        'pandas', 'numpy', 'six',
],
	#package_dir={"": "src"},
    #packages=find_packages(where="astrium"),
    python_requires=">=3.3",
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)
