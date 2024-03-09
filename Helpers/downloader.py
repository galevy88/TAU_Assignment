import nibabel as nib
import numpy as np
import pandas as pd
import os

def save_region_slice_to_csv(atlas_path, slice_number, view="coronal", csv_path="region_slice_data.csv"):
    atlas_img = nib.load(atlas_path)
    atlas_data = atlas_img.get_fdata()


    slice_idx = slice_number - 1

    if view == "axial":
        slice_data = atlas_data[:, :, slice_idx]
    elif view == "sagittal":
        slice_data = atlas_data[slice_idx, :, :]
        slice_data = np.rot90(slice_data)
    elif view == "coronal":
        slice_data = atlas_data[:, slice_idx, :]
        slice_data = np.rot90(slice_data)
    else:
        raise ValueError("Invalid view specified. Please choose from 'axial', 'coronal', or 'sagittal'.")


    df_slice = pd.DataFrame(slice_data)


    df_slice.index += 1
    df_slice.columns += 1

    os.makedirs(os.path.dirname(csv_path), exist_ok=True)

    df_slice.to_csv(csv_path, header=False, index=False)

# Example usage
atlas_path = '../Sub2_AtlasBNA.nii'
slice_number = 52
view = "coronal"
csv_path = "output_slices/region_slice_52_coronal.csv"

save_region_slice_to_csv(atlas_path, slice_number, view, csv_path)
