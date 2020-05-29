from setuptools import find_packages, setup

import readonly_model


setup(
    name='django-readonly-model',
    url=readonly_model.__url__,
    version=readonly_model.__version__,
    license=readonly_model.__license__,
    description='The easiest way to create read-only models for django',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author=readonly_model.__author__,
    author_email=readonly_model.__email__,
    packages=find_packages(exclude=['tests*']),
    include_package_data=True,
    zip_safe=False,
    setup_requires=('wheel'),
    classifiers=[
        'Topic :: Internet :: WWW/HTTP',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Development Status :: 5 - Production/Stable',
        'Framework :: Django',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.0',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Operating System :: MacOS',
        'Operating System :: Microsoft',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only'
    ],
    project_urls={
        'Source': readonly_model.__url__,
    }
)
