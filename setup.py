# vim:fileencoding=utf-8
import os
from setuptools import setup

version = '0.3.2+whyfly.3'


def get_packages(package):
    """
    Return root package and all sub-packages.
    """
    return [dirpath
            for dirpath, dirnames, filenames in os.walk(package)
            if os.path.exists(os.path.join(dirpath, '__init__.py'))]


def get_package_data(package):
    """
    Return all files under the root package, that are not in a
    package themselves.
    """
    walk = [(dirpath.replace(package + os.sep, '', 1), filenames)
            for dirpath, dirnames, filenames in os.walk(package)
            if not os.path.exists(os.path.join(dirpath, '__init__.py'))]

    filepaths = []
    for base, filenames in walk:
        filepaths.extend([os.path.join(base, filename)
                          for filename in filenames])
    return {package: filepaths}


setup(
    name='django-sirtrevor',
    version=version,
    packages=get_packages('sirtrevor'),
    package_data=get_package_data('sirtrevor'),
    include_package_data=True,
    license='MIT License',
    description='A simple Django app that provides a model field and ' +
                'corresponding widget based on the fantastic Sir Trevor ' +
                'project',
    url='https://github.com/philippbosch/django-sirtrevor/',
    author='Philipp Bosch',
    author_email='hello@pb.io',
    install_requires=['markdown2', 'django-appconf', 'django', 'six'],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
