#!/bin/bash

apt-get update

apt-get install -y git

git clone https://github.com/unifyai/ivy.git
cd ivy
git checkout b63d1919d5913ef19de5890bb35beaaaaab05f06
python3 -m pip install --user -e .
cd ..

git clone https://github.com/unifyai/BentoML.git
cd BentoML
git checkout dev_transpile
python3 -m pip install --user -e .
cd ..
