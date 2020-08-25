import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="FortniteNewsGrabber", # Replace with your own username
    version="0.0.1",
    author="Ninja Shoe aka Jacob",
    author_email="jacobhillman016@gmail.com",
    description="Python async library for pulling news off of https://www.epicgames.com/fortnite/en-US/news",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/BigBrain21/FortniteNewsGrabber",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
