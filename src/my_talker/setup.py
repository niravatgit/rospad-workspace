from setuptools import setup

package_name = 'my_talker'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    install_requires=['setuptools'],
    entry_points={
        'console_scripts': [ 
            'talker  = my_talker.talker:main',
            'listener = my_talker.listener:main'
            ],
    },
)