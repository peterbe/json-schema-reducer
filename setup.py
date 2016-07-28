import os
import setuptools


_here = os.path.dirname(__file__)


setuptools.setup(
    name='json-schema-reducer',
    version='0.1.1',
    description='Extract from a JSON/dict only whats in the JSON Schema',
    long_description=open(os.path.join(_here, 'README.rst')).read(),
    author='Peter Bengtsson',
    author_email='mail@peterbe.com',
    license='MIT',
    py_modules=['json_schema_reducer'],
    url='https://github.com/peterbe/json-schema-reducer',
    include_package_data=False,
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest', 'pytest-mock'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
)
