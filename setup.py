import os

from setuptools import setup

version = '5.1.0'

install_requires = [
    'cloudflare>=4.0, <5',
]

install_requires.extend([
        f'acme>=5.1.0',
        f'certbot>=5.1.0',
])


setup(
    version=version,
    install_requires=install_requires,
)
