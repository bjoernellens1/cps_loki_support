import os
from glob import glob
from setuptools import setup

package_name = 'loki_support'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'urdf'), glob('urdf/*.xacro')),
        (os.path.join('share', package_name, 'mesh'), glob('mesh/*.stl')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='bjorn',
    maintainer_email='bjoern.ellensohn@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
