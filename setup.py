from setuptools import setup
from os import path
this_dir = path.abspath(path.dirname(__file__))
with open(path.join(this_dir, 'README.md')) as f:
    long_description = f.read()

setup(
    name='jq-api-core',
    packages=['jq-api-core'],
    version='0.1',
    license='MIT',
    description='API core services for the Jaram Quest',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Joseph Kim',
    author_email='cloudeyes@gmail.com',
    url='https://github.com/jaramquest/api-core/',
    download_url='https://github.com/jaramquest/api-core/archive/v0.1.tar.gz',
    keywords=['jaram-quest', 'api', 'openapi'],
    install_requires=[
        'fastapi',
        'fastalchemy',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
    ])
