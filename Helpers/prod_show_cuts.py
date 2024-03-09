import nibabel as nib
import numpy as np
import plotly.graph_objects as go

# Load your NIfTI file
md_path = '../Sub2_MD.nii'  # Make sure to use the correct path to your file
atlas_path = '../Sub2_AtlasBNA.nii'  # Make sure to use the correct path to your file
atlas_data = nib.load(atlas_path).get_fdata()
md_img = nib.load(md_path)
md_data = md_img.get_fdata()

md_data = md_img.get_fdata()

md_data = np.where(md_data > 0.00225, 0.00225, md_data)
# Identify voxels in regions >= 1
regions_mask = atlas_data >= 1

# Identify where md_data is less than 0.0005 in these regions
value_mask = md_data < 0.0005

# Combine the two masks to identify where both conditions are True
combined_mask = np.logical_and(regions_mask, value_mask)

# Apply the second condition
md_data[combined_mask] = 0.0005

def create_mri_figure(img_data, view="axial", figure_size=(600, 600)):
    fig = go.Figure()

    if view == "axial":
        num_slices = img_data.shape[2]
        slice_orientation = img_data[:, :, :]
    elif view == "sagittal":
        num_slices = img_data.shape[0]
        slice_orientation = np.rot90(img_data[:, :, :].transpose(2, 1, 0), 2)
    elif view == "coronal":
        num_slices = img_data.shape[1]
        slice_orientation = np.rot90(img_data[:, :, :].transpose(0, 2, 1), 2)

    # Add slices to the figure as individual traces
    for i in range(num_slices):
        fig.add_trace(
            go.Heatmap(
                z=np.rot90(slice_orientation[:, :, i]),
                colorscale="Gray",
                showscale=False,
                visible=(i == 0)  # Only the first slice is visible
            )
        )

    # Create and add slider
    steps = []
    for i in range(num_slices):
        step = dict(
            method="update",
            args=[{"visible": [False] * num_slices},
                  {"title": f"Slice: {i + 1}"}],  # slider-step label
        )
        step["args"][0]["visible"][i] = True  # Toggle i'th trace to "visible"
        steps.append(step)

    sliders = [dict(
        active=0,
        currentvalue={"prefix": "Slice: "},
        pad={"t": 50},
        steps=steps
    )]

    fig.update_layout(
        sliders=sliders,
        width=figure_size[0],
        height=figure_size[1],
    )

    return fig

# Create and display the figure for each view. Uncomment the view you need and run the cell.

# Axial view
fig_axial = create_mri_figure(md_data, view="axial", figure_size=(900, 600))
fig_axial.show()

# # Sagittal view
#fig_sagittal = create_mri_figure(md_data, view="sagittal", figure_size=(900, 600))
#fig_sagittal.show()

# # Coronal view
#fig_coronal = create_mri_figure(md_data, view="coronal", figure_size=(900, 600))
#fig_coronal.show()