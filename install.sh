#!/usr/bin/env sh

conda env create -f environment.yml

source activate stafferscraper
pip install -r requirements.txt