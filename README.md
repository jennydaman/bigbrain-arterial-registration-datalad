# Overlay Cerebrovasculature Data on BigBrain

This is a [Datalad](https://www.datalad.org/) repository in which we registered
the dataset from https://zenodo.org/record/3707179 to the [BigBrain](https://bigbrainproject.org/).

This work was started during **HIBALL Hackathon 2023**.
See https://github.com/FZJ-INM1-BDA/HIBALL-Hackathon-2023/issues/8

## Summary

1. Data were downloaded and unzipped inside `Zenodo_3707179/`
2. `ActualBrain/ImageBasedModel/BrainHemispheres/Polygon.ply` was converted into
   various other formats such as MNI `.obj` and Wavefront `.obj` --> `0_mesh_formats/`
3. `ActualBrain.obj` was transformed to fit within the bounding box of ICBM 152 -->
   `transforms/center_rotate.xfm`
4. `ActualBrain.obj` was converted to a volumetric mask then linearly registered
   to ICBM 152 (Talairach space) --> `transforms/ActualBrain_to_tal.xfm`
5. Ran [BigBrainWarp](https://github.com/caseypaquola/BigBrainWarp) (but don't think I did anything useful)
   --> `2_warp/`

## Getting the Data

First, install [Datalad](https://handbook.datalad.org/en/latest/intro/installation.html#installation-and-configuration).
My recommendation is to use [Micromamba](https://mamba.readthedocs.io/en/latest/installation.html#micromamba-standalone-executable).

Next, run

```shell
datalad clone https://github.com/jennydaman/bigbrain-arterial-registration-datalad.git
cd bigbrain-arterial-registration-datalad
datalad get 1_to_icbm 2_warp mesh_formats transforms Zenodo_3707179/ActualBrain
```

## Installation of Dependencies

CIVET-2.1.0 and BigBrainWarp should be installed to your environment.
[Docker](https://docs.docker.com/engine/install/#server) is used to run some other
programs, see [Other References](#Other-References).

There are also some Python dependencies:

```shell
pip install vtk numpy
```

## Other References

- AFNI https://afni.nimh.nih.gov/pub/dist/doc/program_help/ConvertSurface.html
- MIRTK https://mirtk.github.io/commands/convert-pointset.html

## Acknowledgements

- Data are hosted on the [NERC OpenStack Swift](https://nerc.mghpcc.org/)
