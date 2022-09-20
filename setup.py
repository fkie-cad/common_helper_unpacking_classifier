from setuptools import setup, find_packages

VERSION = '0.4.2'

setup(
    name='common_helper_unpacking_classifier',
    version=VERSION,
    package_dir={'': 'src'},
    packages=find_packages('src', exclude=['tests']),
    install_requires=[
        'entropython',
        'common_helper_files @ git+https://github.com/fkie-cad/common_helper_files.git@0.2.2#egg=common_helper_files'
    ],
    dependency_links=[
        'git+https://github.com/fkie-cad/common_helper_files.git@0.2.2#egg=common_helper_files'
    ],
    author='Fraunhofer FKIE',
    author_email='peter.weidenbach@fkie.fraunhofer.de',
    url='http://www.fkie.fraunhofer.de',
    description='Functions that help guessing, if unpacking was successful.',
    license='GPL-3.0'
)
