import nibabel as nib
import numpy as np
import matplotlib.pyplot as plt


def plot_voxel_with_surroundings(nifti_path, view, voxel_coord):
    # Load the NIfTI file
    img = nib.load(nifti_path)
    img_data = img.get_fdata()

    # Determine the slice based on the view
    if view == "axial":
        slice_index = voxel_coord[2]
        slice_data = img_data[:, :, slice_index]
        x, y = voxel_coord[0], voxel_coord[1]
    elif view == "coronal":
        slice_index = voxel_coord[1]
        slice_data = img_data[:, slice_index, :]
        x, y = voxel_coord[0], voxel_coord[2]
    elif view == "sagittal":
        slice_index = voxel_coord[0]
        slice_data = img_data[slice_index, :, :]
        x, y = voxel_coord[1], voxel_coord[2]
    else:
        raise ValueError("Invalid view specified. Please choose from 'axial', 'coronal', or 'sagittal'.")

    # Display the original slice in grayscale
    plt.figure(figsize=(8, 8))
    plt.imshow(slice_data, cmap='gray', interpolation='none')

    # Overlay the central voxel in its grayscale value (simply emphasizing it, could adjust size or color if needed)

    # Overlay the surrounding voxels as dots
    for i in range(-1, 2):
        for j in range(-1, 2):
            # Skip the central voxel to keep its marking unique
            if i == 0 and j == 0:
                continue
            if 0 <= x + i < slice_data.shape[0] and 0 <= y + j < slice_data.shape[1]:
                plt.scatter([y + j], [x + i], c='green', s=3)  # Smaller green dots for surroundings

    plt.title(f'Slice {slice_index + 1} - {view.capitalize()} view\nVoxel ({voxel_coord}) Highlighted')
    plt.axis('off')
    plt.show()


# Example usage
nifti_path = '../Sub2_MD.nii'  # Path to the NIfTI file
view = "axial"  # View from which to extract the slice
voxel_coord = (30, 89, 80)  # Voxel coordinates (x, y, slice_index) for axial; adjust accordingly for coronal/sagittal

plot_voxel_with_surroundings(nifti_path, view, voxel_coord)
