from setuptools import setup

setup(
    name='measurements',
    version='0.2.3',
    description='A package that provides a simple error propagation class',
    url='https://github.com/NoahDavid/measurements',
    author='Noah Koliadko',
    author_email='gluoniclepton@gmail.com',
    license='None for now',
    packages=['measurements'],
    install_requires=[
        'numpy',
    ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
