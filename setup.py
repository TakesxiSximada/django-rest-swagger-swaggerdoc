import os
import re

from setuptools import setup, find_packages
from setuptools.command import test as setuptools_test


class PyTest(setuptools_test.test):
    def finalize_options(self):
        setuptools_test.test.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        pytest.main(self.test_args)


def here(name):
    return os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        name)


def read(name, mode='rb', encoding='utf8'):
    with open(here(name), mode) as fp:
        return fp.read().decode(encoding)


def get_requirements(name, mode='rb', encoding='utf8'):
    with open(here(name), mode) as fp:
        return [line.strip().decode() for line in fp]


def get_version_str(file_path):
    version_file = read(file_path)
    version_match = re.search(
        r"^__version__ = ['\"]([^'\"]*)['\"]",
        version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise ValueError("Unable to find version string.")


def find_version(path, pattern='.*\.py$'):
    regx = re.compile(pattern)
    for root, dirs, files in os.walk(path):
        for filename in files:
            filepath = os.path.join(root, filename)
            if regx.match(filepath):
                try:
                    return get_version_str(filepath)
                except ValueError:
                    pass  # next
    else:
        raise ValueError('Version file not found: {}'.format(path))

# Development Status :: 1 - Planning
# Development Status :: 2 - Pre-Alpha
# Development Status :: 3 - Alpha
# Development Status :: 4 - Beta
# Development Status :: 5 - Production/Stable
# Development Status :: 6 - Mature
# Development Status :: 7 - Inactive

setup(
    name='django-rest-swagger-swaggerdoc',
    version=find_version('src'),
    license='Apache License 2.0',
    description='django-rest-swagger-swaggerdoc',
    long_description=read('README.rst'),
    url='https://github.com/TakesxiSximada/django-rest-swagger-swaggerdoc',
    keywords='Documentation, Swagger',
    classifiers=[
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        # 'Programming Language :: Python :: 3.6',
        'Topic :: Software Development',
    ],
    author='TakesxiSximada',
    author_email='sximada+django-rest-swagger-swaggerdoc@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    platforms='any',
    include_package_data=True,
    zip_safe=False,
    install_requires=get_requirements('./requirements/install.txt'),
    tests_require=get_requirements('./requirements/test.txt'),
    extras_require={
        'testing': get_requirements('./requirements/test.txt') + get_requirements('./requirements/install.txt'),  # noqa
    },
    cmdclass={
        'test': PyTest,
    },
    entry_points="""\
    """,
)
