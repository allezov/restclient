from distutils.core import setup
REQUIRES=[
    'allure-pytest',
    'requests',
    'structlog',
    'curlify'


]
setup(
    name='restclient',
    version='0.0.1',
    packages=['restclient'],
    url='https://github.com/allezov/restclient.git',
    license='Apache-2.0 license',
    author='lezov',
    author_email='-',
    install_requires=REQUIRES,
    description='restclient + allure + logger'
)
