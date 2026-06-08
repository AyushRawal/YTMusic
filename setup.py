from setuptools import setup, find_packages

setup(
    name='YTMusic',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        "requests",
        "youtube-dl @ git+https://github.com/ytdl-org/youtube-dl.git",
        "prettytable",
        "colorama"
    ],
    entry_points={
        'console_scripts': [
            'ytmusic = YTMusic.main:main',
        ],
    },
)
