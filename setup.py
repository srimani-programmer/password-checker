from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="password-checker",
    version="1.0.0",
    description="A Python package to check vulnerability and strength pf a password.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="",
    author="Sri Manikanta Palakollu",
    author_email="srimani.crypter@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.5"
    ],
    packages=["password_checker"],
    include_package_data=True,
    install_requires=["requests"],
    entry_points={
        "console_scripts": [
            "weather-reporter=weather_reporter.cli:main",
        ]
    },
)