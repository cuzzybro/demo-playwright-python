import setuptools

setuptools.setup(
    install_requires=[
        'playwright==0.171.1', 'pytest==6.2.1', 'pytest-playwright==0.0.10', 'pytest_xdist',
        'requests', 'pymssql==2.1.5', 'cx-oracle==8.1.0'
    ]
)
