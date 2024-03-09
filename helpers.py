import nibabel as nib
import numpy as np
from meta_data_dicts import get_dicts as dictter


def get_data():
    # Load the MD data and atlas
    md_path = 'Sub2_MD.nii'
    atlas_path = 'Sub2_AtlasBNA.nii'
    md_img = nib.load(md_path)
    atlas_img = nib.load(atlas_path)

    md_data = md_img.get_fdata()
    atlas_data = atlas_img.get_fdata()
    md_data = np.where(md_data > 0.00225, 0.00225, md_data)
    # Identify voxels in regions >= 1
    regions_mask = atlas_data >= 1

    # Identify where md_data is less than 0.0005 in these regions
    value_mask = md_data < 0.0005

    # Combine the two masks to identify where both conditions are True
    combined_mask = np.logical_and(regions_mask, value_mask)

    # Apply the second condition
    md_data[combined_mask] = 0.0005

    return md_data, atlas_data

def get_dicts():
    return dictter()