from setuptools import setup

setup(
    name='repo_curso_cnad',
    install_requires=[
        'Flask==3.0.3',
        'peewee==3.17.6',
        'python-decouple==3.8',
        'python-dotenv==1.0.1',
        'pyFirmata2==2.5.0',
        'setuptools==70.3.0',
    ],
    scripts=[
        'src',
    ],
    packages=[
        'src',
        'src.helpers',
        'src.model',
        'src.hardware',
    ],
    package_dir={"": "src"},
)
