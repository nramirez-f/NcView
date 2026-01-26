"""Common utilities for ncviewer modules.

Shared functionality used by both _inspect.py and _plot.py.
Only imports lightweight dependencies (pathlib, xarray).
"""
from pathlib import Path
import xarray as xr


def open_dataset(path):
    """
    Open a NetCDF file and return xarray Dataset.
    
    Centralized file opening with validation.
    
    Args:
        path: Path to NetCDF file (str or Path)
        
    Returns:
        xarray.Dataset
        
    Raises:
        FileNotFoundError: If file doesn't exist
    """
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"File not found: {path}")
    return xr.open_dataset(p)


def check_variable(ds, varname):
    """
    Check if variable exists in dataset.
    
    Args:
        ds: xarray.Dataset
        varname: Variable name to validate
        
    Returns:
        bool: True if variable exists, False otherwise
    """
    return varname in ds.data_vars


def check_dimension(ds, dimname):
    """
    Check if dimension exists in dataset.
    
    Args:
        ds: xarray.Dataset
        dimname: Dimension name to validate
        
    Returns:
        bool: True if dimension exists, False otherwise
    """
    return dimname in ds.dims
