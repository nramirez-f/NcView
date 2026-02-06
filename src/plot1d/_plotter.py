import plotly.graph_objects as go
import numpy as np

def line_plot(ds, time_dim, time_idx, x_coords, var):
    """
    Create a 1D line plot using Plotly.

    Args:
        ds: xarray.Dataset
        time_dim: Name of the time dimension
        time_idx: Index of the time step to plot
        x_coords: Coordinates for the X axis
        var: Variable name to plot

    Returns:
        plotly.graph_objects.Figure
    """
    all_values = []
    
    fig = go.Figure()
    for v in var:
        values = ds[v].isel({time_dim: time_idx}).values
        fig.add_trace(go.Scatter(
            x=x_coords,
            y=values,
            mode='lines',
            name=v
        ))
        all_values.append(ds[v].values)

    # Calculate global y-axis limits across all time steps for the selected variable(s)
    if all_values:
        all_values = np.concatenate(all_values)
        y_min = np.min(all_values)
        y_max = np.max(all_values)
    else:
        y_min = 0
        y_max = 1

    fig.update_layout(
        showlegend=True,
        title={
            'text': f"{time_dim} = {ds[time_dim].values[time_idx]:.3f} (iteration: {time_idx})",
            'x': 0.5,
            'xanchor': 'center'
        },
        xaxis={
            'range': [np.min(x_coords), np.max(x_coords)]
        },
        yaxis={
            'range': [y_min, y_max]
        }
    )
    return fig