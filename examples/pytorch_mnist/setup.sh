#!/bin/bash

# Update the package lists
RUN apt-get update

# Install Git
RUN apt-get install -y git

RUN git clone https://github.com/unifyai/ivy.git
RUN cd ivy 
RUN git checkout b63d1919d5913ef19de5890bb35beaaaaab05f06
RUN python3 -m pip install --user -e .
RUN cd ..
