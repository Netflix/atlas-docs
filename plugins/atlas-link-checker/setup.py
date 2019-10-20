from setuptools import find_packages, setup


setup(
    name='atlas_link_checker',
    version='1.0.0',
    author='Matthew Johnson',
    author_email='matthewj@netflix.com',
    description='Check HTML links for correctness in the MkDocs build output for Atlas Docs.',
    license='Apache License, Version 2.0',
    keywords='atlas link checker',
    url='https://github.com/Netflix/atlas-docs/tree/master/plugins/link-checker',
    python_requires='>=3.6',
    install_requires=[
        'beautifulsoup4'
    ],
    extras_require={},
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': ['atlas-link-checker = atlas_link_checker.main:main'],
    },
)
