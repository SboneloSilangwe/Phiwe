from setuptools import setup, find_packages

setup(
    name='mypackag',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA example python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/SboneloSilangwe/mypackag.git',
    author='Sbonelo Silangwe',
    author_email='<silangwesbonelo08@gmail.com>'
)
