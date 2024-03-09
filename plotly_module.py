import plotly.graph_objects as go
import numpy as np
from helpers import get_data, get_dicts

md_data, atlas_data = get_data()
brain_areas, brain_area_colors = get_dicts()

def plot_brain_areas_by_name(area_name, mode='color', color_sub=False):
    x, y, z, color_data, hover_text_data = [], [], [], [], []

    # Determine the regions to plot based on area_name
    if area_name != "All":
        if area_name in brain_areas:
            start_region, end_region = brain_areas[area_name]['start'], brain_areas[area_name]['end']
        elif any(area_name in info.get('sub_areas', {}) for info in brain_areas.values()):
            for info in brain_areas.values():
                sub_areas = info.get('sub_areas', {})
                if area_name in sub_areas:
                    start_region, end_region = sub_areas[area_name]['start'], sub_areas[area_name]['end']
                    break
        else:
            print(f"Area '{area_name}' not found.")
            return
        regions_to_plot = range(start_region, end_region + 1)
    else:
        regions_to_plot = range(1, 275)  # Assuming 274 regions

    for region_number in regions_to_plot:
        mask = atlas_data == region_number
        if not np.any(mask):
            continue
        xi, yi, zi = np.where(mask)
        x.extend(xi.tolist())
        y.extend(yi.tolist())
        z.extend(zi.tolist())

        voxel_md_values = md_data[mask]
        color, hover_text = 'black', 'Unknown Area'

        for area, info in brain_areas.items():
            if info["start"] <= region_number <= info["end"]:
                if mode == 'color':
                    color = brain_area_colors[area]["color"]
                name = area
                md_major = np.mean(md_data[(atlas_data >= info["start"]) & (atlas_data <= info["end"])]).item()

                hover_text = f"{name}<br>MD (major): {md_major:.6f}"

                if color_sub and "sub_areas" in info:
                    for sub_area, sub_info in info["sub_areas"].items():
                        if sub_info["start"] <= region_number <= sub_info["end"]:
                            if mode == 'color':
                                color = brain_area_colors[area]["sub_areas"][sub_area]
                            md_sub = np.mean(md_data[(atlas_data >= sub_info["start"]) & (atlas_data <= sub_info["end"])]).item()
                            hover_text += f"<br>MD (sub): {md_sub:.6f}"
                break

        if mode == 'md_value':
            color_data.extend(voxel_md_values.tolist())
        else:
            color_data.extend([color] * len(xi))

        for i in range(len(xi)):
            voxel_hover_text = hover_text + f"<br>Voxel: ({xi[i]},{yi[i]},{zi[i]})<br>Voxel MD: {voxel_md_values[i]:.6f}"
            hover_text_data.append(voxel_hover_text)

    colorscale = 'hsv' if mode == 'md_value' else None
    colorbar_title = "MD Values" if mode == 'md_value' else None

    fig = go.Figure(data=[go.Scatter3d(
        x=x, y=y, z=z,
        mode='markers',
        marker=dict(
            size=3,
            color=color_data,
            colorscale=colorscale,
            colorbar=dict(title=colorbar_title),
            opacity=0
        ),
        text=hover_text_data,
        hoverinfo='text'
    )])

    fig.update_layout(title=f"{area_name} Brain Area Visualization ({'Color' if mode == 'color' else 'MD Value'})", margin=dict(l=0, r=0, b=0, t=30))
    return fig
