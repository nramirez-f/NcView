"""
Configuration settings for ncviewer.

This module contains configurable constants and settings used across the package.
"""

# Time dimension detection
# Order matters: first match will be used
TIME_DIMENSION_NAMES = ['time', 't', 'Time', 'TIME', 'ocean_time']

# Spatial dimension detection for X-axis (longitude/horizontal)
X_DIMENSION_NAMES = ['x', 'X', 'lon', 'longitude', 'Longitude', 'xi', 'xi_rho', 'nx']

# Spatial dimension detection for Y-axis (latitude/vertical)
Y_DIMENSION_NAMES = ['y', 'Y', 'lat', 'latitude', 'Latitude', 'eta', 'eta_rho', 'ny']

# Z dimension detection (depth/vertical levels)
Z_DIMENSION_NAMES = ['z', 'Z', 'depth', 'Depth', 'level', 'lev', 's_rho', 'nz']

# Numeric tolerance settings for coordinate comparison
COORDINATE_RTOL = 1e-9  # Relative tolerance
COORDINATE_ATOL = 1e-12  # Absolute tolerance

# Display settings
SEPARATOR_LENGTH = 80
SEPARATOR_CHAR = '='

# Memory formatting thresholds (in bytes)
KB_THRESHOLD = 1024
MB_THRESHOLD = 1024**2
GB_THRESHOLD = 1024**3

# Error computation defaults
DEFAULT_ERROR_NORM = '2'  # L2 norm by default
AVAILABLE_NORMS = ['1', '2', 'inf', 'max']

# Expression operators (for detecting mathematical expressions)
EXPRESSION_OPERATORS = ['+', '-', '*', '/', '**', '(', ')']

# Statistical precision for display
STAT_PRECISION = 4  # Number of decimal places
ERROR_PRECISION = 6  # Number of decimal places for errors

# File display limits
MAX_VARIABLES_PREVIEW = 5  # Max variables to show in error messages

# Default cell volume when grid spacing cannot be determined
DEFAULT_CELL_VOLUME = 1.0