import os
from setuptools import setup, find_packages

def readfile(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='pywikilinks',
    version='0.0.1',
    description='Python package for downloading wiki-links corpus',
    long_description=readfile('README.md'),
    ext_modules=[],
    packages=find_packages(),
    author='Jonathan Raiman',
    author_email='jraiman at mit dot edu',
    url='https://github.com/JonathanRaiman/pywikilinks',
    download_url='https://github.com/JonathanRaiman/pywikilinks',
    keywords='Machine Learning, NLP',
    license='MIT',
    platforms='any',
    zip_safe=False,
    classifiers=[
        'Intended Audience :: Science/Research',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.3',
        'Topic :: Text Processing :: Linguistic',
    ],
    # test_suite="something.test",
    setup_requires = [],
    install_requires=[
        'thrift'
    ],
    include_package_data=True,
)
