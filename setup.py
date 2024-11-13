from setuptools import find_packages, setup

setup(
    name="Zomato Chatbot",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        "chainlit==0.5.1",
        "openai==0.27.0",
    ],
    author="Suryansh Pandey",
    author_email="suryanshp1@gmail.com",
)