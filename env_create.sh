#!/bin/bash

export CONDA_ALWAYS_YES="true"
conda create -n DynG2G --no-default-packages
source activate DynG2G
conda install pytorch torchvision torchaudio cudatoolkit=10.2 -c pytorch
conda install -c anaconda scipy 
conda install -c anaconda scikit-learn 
conda install -c conda-forge matplotlib 
conda install -c anaconda pandas 
pip install PyYAML