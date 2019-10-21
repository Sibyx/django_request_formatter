import os
from distutils.core import setup

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

REQUIRED = [
    'Django>=2.0'
]


def read_files(files):
    data = []
    for file in files:
        with open(file) as f:
            data.append(f.read())
    return "\n".join(data)


meta = {}
with open('./django_request_formatter/__version__.py') as f:
    exec(f.read(), meta)

setup(
    name='django_request_fromatter',
    version=meta['__version__'],
    packages=['django_request_fromatter'],
    install_requires=REQUIRED,
    url='https://github.com/Sibyx/django_request_formatter',
    license='MIT',
    author='Jakub Dubbec',
    author_email='jakub.dubec@gmail.com',
    description='Declarative Django request validation ',
    long_description=read_files(['README.md', 'CHANGELOG.md']),
    long_description_content_type='text/markdown',
    keywords=['django', 'forms', 'request', 'validation', 'python'],
    classifiers=[
        # As from https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 2.1',
        'Framework :: Django :: 2.2'
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: HTTP Servers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Environment :: Web Environment',
    ]
)
