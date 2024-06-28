from setuptools import setup, find_packages

setup(
    name='FinanceBot',
    author='Megha Jadav',
    author_email='meghasaraiya@gmail.com',
    version='0.0',
    packages=find_packages(),
    install_requires=['langchain', 'langchain-openai', 'langchain-astradb',
                      'datasets', 'pypdf', 'python-dotenv', 'flask',
]
)