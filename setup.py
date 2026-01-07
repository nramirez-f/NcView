from setuptools import setup, find_packages

setup(
    name="ncviewer",
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
            "ncviewer = ncviewer.cli:main",
            "ncinfo = ncviewer.cli:ncinfo",
            "ncdim = ncviewer.cli:ncdim",
            "ncvar = ncviewer.cli:ncvar",
            "ncsum = ncviewer.cli:ncsum",
            "ncp1d = ncviewer.cli:ncp1d",
        ],
    },
    include_package_data=True,
    python_requires=">=3.8",
)
