import setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='amalfi',
    author='Arunav Gupta',
    author_email='arunavg@ucsd.edu',
    description='Quickly and easily transmit objects between Jupyter Notebooks',
    keywords='jupyter, developer',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/agupta01/amalfi',
    project_urls={
        'Documentation': 'https://github.com/agupta01/amalfi',
        'Bug Reports':
        'https://github.com/agupta01/amalfi/issues',
        'Source Code': 'https://github.com/agupta01/amalfi',
        # 'Funding': '',
        # 'Say Thanks!': '',
    },
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src'),
    classifiers=[
        # see https://pypi.org/classifiers/
	'Development Status :: 1 - Planning',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
	'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
    # install_requires=['Pillow'],
    extras_require={
        'dev': ['check-manifest'],
        # 'test': ['coverage'],
    },
    # entry_points={
    #     'console_scripts': [  # This can provide executable scripts
    #         'run=examplepy:main',
    # You can execute `run` in bash to run `main()` in src/examplepy/__init__.py
    #     ],
    # },
)
