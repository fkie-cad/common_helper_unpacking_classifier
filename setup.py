from setuptools import setup, find_packages

VERSION = '0.3'

setup(
    name='common_helper_unpacking_classifier',
    version=VERSION,
    package_dir={'': 'src'},
    packages=find_packages('src', exclude=['tests']),
    install_requires=[
        'entropy >= 0.9',
        'common_helper_files >= 0.2'
    ],
    dependency_links=[
        'https://github.com/fkie-cad/common_helper_files/tarball/master#egg=common_helper_files-0.2'
    ],
    author='Fraunhofer FKIE',
    author_email='peter.weidenbach@fkie.fraunhofer.de',
    url='http://www.fkie.fraunhofer.de',
    description='Functions that help guessing, if unpacking was successful.',
    license='GPL-3.0'
)
