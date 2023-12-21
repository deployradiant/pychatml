from setuptools import setup, find_packages

setup(
    name="pychatml",
    version="0.0.4",
    description="A package for converting chat messages to and from ChatML format",
    author="Radiant AI",
    author_email="jakob@radiantai.com",
    packages=find_packages(),
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    install_requires=["anthropic", "openai"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
