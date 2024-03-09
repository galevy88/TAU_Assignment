brain_areas = {
    "Frontal lobe" : { "start" : 1, "end" : 68,
                       "sub_areas" : {
                           "Superior frontal gyrus" : { "start" : 1, "end" : 12},
                           "Middle frontal gyrus" : { "start" : 13, "end" : 28},
                           "Inferior frontal gyrus" : { "start" : 29, "end" : 40},
                           "Orbital gyrus" : { "start" : 41, "end" : 52},
                           "Precentral gyrus" : { "start" : 53, "end" : 68}
                       } },
    "Temporal lobe" : { "start" : 69, "end" : 124,
                       "sub_areas" : {
                           "Superior temporal gyrus" : { "start" : 69, "end" : 80},
                           "Middle temporal gyrus" : { "start" : 81, "end" : 88},
                           "Inferior temporal gyrus" : { "start" : 89, "end" : 102},
                           "Fusiform gyrus" : { "start" : 103, "end" : 108},
                           "Parahippocampal gyrus" : { "start" : 109, "end" : 120},
                           "Posterior superior temporal sulcus" : { "start" : 121, "end" : 124}
                       } },
    "Parietal lobe" : { "start" : 125, "end" : 162,
                       "sub_areas" : {
                           "Superior parietal lobule" : { "start" : 125, "end" : 134},
                           "Inferior parietal lobule" : { "start" : 135, "end" : 146},
                           "Precuneus" : { "start" : 147, "end" : 154},
                           "Postcentral gyrus" : { "start" : 155, "end" : 162}
                       } },
    "Insular lobule" : { "start" : 163, "end" : 174,
                        "sub_areas" : {
                            "Insular gyrus" : { "start" : 163, "end" : 174},
                        } },
    "Limbic lobe" : { "start" : 175, "end" : 188,
                      "sub_areas" : {
                          "Cingulate gyrus" : { "start" : 175, "end" : 188},
                      } },
    "Occipital lobe" : { "start" : 189, "end" : 210,
                         "sub_areas" : {
                             "MedioVentral occipital cortex" : { "start" : 189, "end" : 198},
                             "Cuneus" : { "start" : 199, "end" : 210},
                         } },
    "Subcortical nuclei" : { "start" : 211, "end" : 246,
                             "sub_areas" : {
                                 "Amygdala" : { "start" : 211, "end" : 214},
                                 "Hippocampus" : { "start" : 215, "end" : 218},
                                 "Basal ganglia" : { "start" : 219, "end" : 230},
                                 "Thalamus" : { "start" : 231, "end" : 246},
                             } },
    "Cerebellum" : { "start" : 247, "end" : 274}
}

brain_area_colors = {
    "Frontal lobe": {
        "color": "#1f77b4",
        "sub_areas": {
            "Superior frontal gyrus": "#aec7e8",
            "Middle frontal gyrus": "#9edae5",
            "Inferior frontal gyrus": "#6baed6",
            "Orbital gyrus": "#c6dbef",
            "Precentral gyrus": "#4292c6"
        }
    },
       "Temporal lobe": {
        "color": "#ff7f0e",
        "sub_areas": {
            "Superior temporal gyrus": "#ffbb78",  # Lighter shade
            "Middle temporal gyrus": "#ff9c50",  # Medium-light shade
            "Inferior temporal gyrus": "#ff7f0e",  # Base color
            "Fusiform gyrus": "#e6550d",  # Slightly darker
            "Parahippocampal gyrus": "#d84a05",  # Darker shade
            "Posterior superior temporal sulcus": "#c23500"  # Darkest shade
        }
    },
    "Parietal lobe": {
        "color": "#2ca02c",
        "sub_areas": {
            "Superior parietal lobule": "#74c476",
            "Inferior parietal lobule": "#a1d99b",
            "Precuneus": "#31a354",
            "Postcentral gyrus": "#41ab5d"
        }
    },
    "Insular lobule": {
        "color": "#d62728",
        "sub_areas": {
            "Insular gyrus": "#fcae91"
        }
    },
    "Limbic lobe": {
        "color": "#9467bd",
        "sub_areas": {
            "Cingulate gyrus": "#bcbddc"
        }
    },
    "Occipital lobe": {
        "color": "#8c564b",
        "sub_areas": {
            "MedioVentral occipital cortex": "#c49c94",
            "Cuneus": "#e7ba52"
        }
    },
    "Subcortical nuclei": {
        "color": "#e7cb94",
        "sub_areas": {
            "Amygdala": "#e7ba52",
            "Hippocampus": "#bd9e39",
            "Basal ganglia": "#8c6d31",
            "Thalamus": "#ad494a"
        }
    },
    "Cerebellum": {
        "color": "#eb4b4b",
        "sub_areas": {}
    }
}


def get_dicts():
    return brain_areas, brain_area_colors