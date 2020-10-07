from setuptools import setup, find_packages

setup(
    name="device_repo",
    version="0.1",
    packages=find_packages(),

    author="Yanda Geng",
    author_email="gengyanda16@smail.nju.edu.cn",
    description="Remote device access solution based on Zeroc ICE.",
    keywords="remote device",
    platforms="any",
    install_requires=["zeroc-ice", "pyyaml"],
    classifiers=[
        "License :: OSI Approved :: GNU Lesser General Public License v2 "
        "or later (LGPLv2+)",
    ],
    entry_points={
        'console_scripts': [
            'devicerepo=device_repo.host:main'
        ]
    }
)
