from setuptools import find_packages, setup
import os

package_name = 'manipulator_amr'

# 파일 경로 수정: 실제 경로를 정확히 지정
launch_file_path = os.path.join('manipulator_amr', 'launch', 'launch.py')

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', [launch_file_path]),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='viator',
    maintainer_email='pedralation@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'server = manipulator_amr.server.server_node:main',
            'gui = manipulator_amr.gui.gui_node:main',
            'amr = manipulator_amr.amr.amr_node:main',
            'manipulator = manipulator_amr.manipulator.manipulator_node:main',
        ],
    },
)
