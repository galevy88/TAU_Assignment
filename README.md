# Yaniv Assaf Lab Assignment – Gal Levy
## For PDF Assignment Report You Can Check: 
Yaniv Assaf Lab Assignment - Gal Levy.pdf In This Repo
## Pre-Abstract
In this assignment, I explore the spatial distribution of mean diffusivity across various brain regions using Python to analyze NIfTI-formatted neuroimaging data. The goal is to process a mean-diffusivity map and a registered atlas, remove outliers, and calculate the average mean diffusivity for indexed brain regions. This analysis aims to enhance our understanding of mean diffusivity's significance across different areas of the brain.

Assignment source: [Yaniv Assaf Lab Apply](https://yanivassaflab.com/apply/)

## Abstract
This study processes neuroimaging data to investigate the spatial distribution of mean diffusivity (MD) across the brain. By focusing on outlier removal and calculating average MD for each region, the analysis reveals consistent distribution patterns and provides deeper insights into the microstructural properties of brain regions.

## Introduction
Diffusion Tensor Imaging (DTI) and Mean Diffusivity (MD) offer insights into the microstructural organization of brain tissue. This study uses two NIfTI format files: a mean-diffusivity file and a registered brain atlas, to analyze MD values across 274 distinct brain regions.

## Analysis Results
The initial analysis confirmed data alignment and informed the selection of analytical techniques. Outlier identification and removal were crucial for accurate mapping of MD values. Despite challenges, the study proceeded with data identical to the original set, except for adjustments made to remove outliers and correct extreme values.

## Visualization and Webserver
To enhance this project, I developed a Flask web server for interactive brain visualization, offering atlas-based and MD value-based modes. This tool aids in understanding the brain's structural organization and diffusivity profile.

Webserver: [http://brain.freetruthworld.com/](http://brain.freetruthworld.com/)
GitHub Repo: [TAU Assignment Repo](https://github.com/galevy88/TAU_Assignment)
