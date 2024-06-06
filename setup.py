from setuptools import find_packages, setup


setup(
    name="mcqgenerator",
    version="0.0.1",
    author="Nitish kumar",
    author_email="Nitish10795@gmail.com",
    include_package_data=True,
    install_requires=['pandas' ,'transformar','openai','huggingface','streamlit','python-dotenv','pyPDF2'],
    packages=find_packages()
)
