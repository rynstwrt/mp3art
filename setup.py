from setuptools import setup, find_packages
from pathlib import Path


long_description = (Path(__file__).parent / "README.md").read_text()


setup(
    name='mp3art',
    version='1.0.0',
    description='A command line command to add/remove art to MP3 files.',
    url='https://github.com/rynstwrt/mp3art',
    author='rynstwrt',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'mp3art=mp3art.mp3art:run'
        ]
    },
    long_description=long_description,
    long_description_content_type='text/markdown'
)
