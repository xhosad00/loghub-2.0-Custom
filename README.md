# Loghub-2.0 - Customization

This is a customization of the original Loghub-2.0 dataset, used for development and evaluation of the log parsing tool AGOREG and complies with `LICENSE OF LOGHUB-2.0`.

The original repository is located at [Loghub-2.0](https://github.com/logpai/loghub-2.0/tree/main).

## What was changed:

This repo mainly regards the customisation of the original 2k_dataset. The main idea is to have several diffrent versions with diffrent pre-processing, utilizing the original Loghub `post_process.py` script. 

## To create new 2k postprocessed dataset

1. copy the base dataset: `2k_dataset`. Customize the `post_process.py` script for the desired customazition and run `postProcessAll.py` which applies the changes ond saves over the original files. It's good practice to write your customization into the Dataset `README.md`.

## For running with AGOREG (GPMasterLoghubWrapper.py) or any other tool using the defaul Loghub evaluator script
The Loghub eval script is quite sensitive to the dataset folder name in relation to file names (since it was originally build with just '2k_' and 'full_' prefixes in mind). 

It is important that the folder still has suffix `_dataset`!!

So, for the new dataset folder (e.g. `2k_post_dataset`) that still holds the original files (e.g. `Apache_2k.log`), a renaming is required. So using the dataset directory prefix `2k_post`, rename the file parts containing the original dataset `2k`. The new Apache log will then be `Apache_2k_post.log`. Similliary the other files `Apache_2k_post.log_templates.csv`, `Apache_2k_post.log_structured.csv`, ...

You can use this renaming comand, run in the dataset folder
```bash
cd ./2k_post_dataset
find . -type f -name '*_2k*' -exec rename "s/_2k/_$(basename "$PWD" | sed 's/_dataset$//')/" {} +
# find . -type f -name '*_2k*' -exec rename 's/_2k/_2k_post/' {} + <- hardcoded version
#                       find                #replaceWith folder name
```