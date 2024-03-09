import nibabel as nib
import numpy as np
import pandas as pd
import os

def save_region_slice_to_csv(atlas_path, slice_number, view="coronal", csv_path="region_slice_data.csv"):
    # Load the atlas NIfTI file
    atlas_img = nib.load(atlas_path)
    atlas_data = atlas_img.get_fdata()

    # Adjust slice_number for 0-based indexing inside the function
    slice_idx = slice_number - 1

    # Extract the specified slice based on the view
    if view == "axial":
        slice_data = atlas_data[:, :, slice_idx]
    elif view == "sagittal":
        slice_data = atlas_data[slice_idx, :, :]
        slice_data = np.rot90(slice_data)  # Adjust orientation if necessary
    elif view == "coronal":
        slice_data = atlas_data[:, slice_idx, :]
        slice_data = np.rot90(slice_data)  # Adjust orientation if necessary
    else:
        raise ValueError("Invalid view specified. Please choose from 'axial', 'coronal', or 'sagittal'.")

    # Convert the slice to a pandas DataFrame
    df_slice = pd.DataFrame(slice_data)

    # Adjust index and column to start from 1 for 1-based indexing
    df_slice.index += 1
    df_slice.columns += 1

    # Ensure the directory for the CSV exists
    os.makedirs(os.path.dirname(csv_path), exist_ok=True)

    # Save the DataFrame to a CSV file without header and index to match the exact layout of the slice
    df_slice.to_csv(csv_path, header=False, index=False)

# Example usage
atlas_path = '../Sub2_AtlasBNA.nii'  # Path to the atlas NIfTI file
slice_number = 52  # 1-based index of the slice to save
view = "coronal"  # View from which to extract the slice
csv_path = "output_slices/region_slice_52_coronal.csv"  # Path to save the CSV file

save_region_slice_to_csv(atlas_path, slice_number, view, csv_path)
