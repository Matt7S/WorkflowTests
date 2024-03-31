from setuptools import setup


setup (
    name='bakery',
    verion='1.1',
    description='A useful module',
    author='MS',
    packages=['bakery'],
    install_requires=['numpy'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
)