from setuptools import setup, find_packages


setup(
    name="NcView",
    version="0.1.0",
    description="CLI tool for quick NetCDF file exploration (inspired by pangeo/xarray)",
    author="nramirez-f",
    packages=find_packages(),
    install_requires=[
        "xarray",
        "netCDF4",
        "matplotlib",
        "hvplot",
        "bokeh",
        "holoviews",
    ],
    entry_points={
        "console_scripts": [
            "ncv = ncview.cli:main",
        ],
    },
    include_package_data=True,
    python_requires=">=3.8",
)
