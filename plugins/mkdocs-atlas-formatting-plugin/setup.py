from setuptools import find_packages, setup

setup(
    name='mkdocs_atlas_formatting_plugin',
    version='1.0.0',
    author='Matthew Johnson',
    author_email='matthewj@netflix.com',
    description='Does things.',
    license='Apache License, Version 2.0',
    keywords='atlas docs',
    url='https://github.com/Netflix/atlas-docs',
    python_requires='>=3.6',
    install_requires=[],
    extras_require={},
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'mkdocs.plugins': [
            'foo = mkdocs_atlas_formatting_plugin.plugin:AtlasFormattingPlugin'
        ]
    }
)
