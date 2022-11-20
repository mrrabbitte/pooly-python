from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    lic = f.read()

setup(
    name='pooly-client',
    version='0.1.0',
    description='A client for pooly, a postgres pooling service and a grpc adapter.',
    long_description=readme,
    author='P. Gli',
    author_email='pgli@pm.me',
    url='https://github.com/mrrabbitte/pooly-python',
    license=lic,
    packages=find_packages(exclude=('ats', 'tests', 'docs'))
)
