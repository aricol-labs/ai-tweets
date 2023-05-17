from setuptools import setup, find_packages

setup(
    name='ai-tweets',
    version='1.0.0',
    description='Development practice: display write new tweets with AI',
    author='Ariel Colon',
    author_email='colonariel8@gmail.com',
    url='https://github.com/aricol-labs/ai-tweets',
    keywords=['Web App', 'Flask', 'API'],
    entry_points={},
    install_requires=[
        'requests==2.28.2',
        'flask',
        'requests_oauthlib',
        'pytz',
        'openai'
    ],
    packages=find_packages(),
)