import nibabel as nib
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Load your NIfTI file
md_path = '../Sub2_MD.nii'  # Make sure to use the correct path to your file
md_img = nib.load(md_path)
md_data = md_img.get_fdata()

def create_mri_slices_side_by_side(img_data, slices, view="coronal", figure_size=(900, 600)):
    num_slices = len(slices)
    # Create a subplot figure with 1 row and num_slices columns
    fig = make_subplots(rows=1, cols=num_slices, subplot_titles=[f'Slice {s}' for s in slices])

    if view == "axial":
        slice_orientation = img_data[:, :, slices]
    elif view == "sagittal":
        slice_orientation = img_data[slices, :, :].transpose(1, 0, 2)
    elif view == "coronal":
        slice_orientation = img_data[:, slices, :].transpose(0, 2, 1)

    for i, slice_idx in enumerate(slices):
        # Adjust orientation and rotation as needed based on view
        if view == "coronal":
            slice_img = np.rot90(slice_orientation[:, :, i])
        elif view == "sagittal":
            slice_img = np.rot90(slice_orientation[:, i, :])
        elif view == "axial":
            slice_img = np.rot90(slice_orientation[:, :, i])

        # Add heatmap for each slice to the respective subplot
        fig.add_trace(
            go.Heatmap(
                z=slice_img,
                colorscale="Gray",
                showscale=False
            ),
            row=1, col=i+1  # Place in the correct subplot position
        )

    fig.update_layout(height=figure_size[1], width=figure_size[0]*num_slices, title_text="MRI Slices Side by Side")
    return fig

# Specify the slices you want to display, adjusting for 0-based indexing
slices_to_display = [51, 52, 53, 54]

# Create and display the figure for coronal view with specific slices
fig_slices = create_mri_slices_side_by_side(md_data, slices_to_display, view="coronal", figure_size=(300, 300))
fig_slices.show()
