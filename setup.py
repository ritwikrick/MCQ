# to install local package in my virtual enviroment
from setuptools import find_packages,setup
setup(
    name='mcq_generator',
    version="0.0.1",
    author="Rick Riwtik",
    email="rickritwik901@gmail.com",
    install_require=["openai","langchain","streamlit","python-dotenv","PyPDF2"],
    packages=find_packages()
)

    