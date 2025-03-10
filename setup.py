from setuptools import setup, find_packages

setup(
    name="github_api_cli",
    version="1.0.0",
    packages=find_packages(),  # Automatically finds package directories
    install_requires=[],  # No external dependencies needed
    entry_points={  
        "console_scripts": [
            "github-activity=github_api_cli.main:main"  # Links CLI command to main()
        ]
    },
    author="Lewie Jackson",
    author_email="LewieJ08@gmail.com",
    description="A simple app that allowing the user to fetch github user infomation",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/LewieJ08/github_api_cli",  # Add your GitHub repo link once it's created
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)