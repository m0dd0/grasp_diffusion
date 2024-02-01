FROM nvidia/cuda:11.7.1-cudnn8-devel-ubuntu20.04

# setup environment (variables)
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV ROS_DISTRO noetic
ENV CATKIN_WS_DIR ${CATKIN_WS_DIR}

# setup timezone
RUN echo 'Etc/UTC' > /etc/timezone && \
    ln -s /usr/share/zoneinfo/Etc/UTC /etc/localtime && \
    apt-get update && \
    apt-get install -q -y --no-install-recommends tzdata && \
    rm -rf /var/lib/apt/lists/*

# install some basic packages
RUN apt-get update && \ 
    apt-get install -q -y --no-install-recommends \
    dirmngr \ 
    gnupg2 \
    git \
    nano \
    curl \
    make \
    python3-pip \
    python3-dev \
    software-properties-common && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# install additional dependencies for se3dif package
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    libsuitesparse-dev \
    build-essential && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* 

RUN python3 -m pip install --upgrade pip

# here we install all the dependecies defined in the requirements.txt file of thr grasp_diffusion package
# we keep all version except for the theseus-ai package, which was originally set to 0.1.3 but caused many hard to solve issues when trying to install it into the docker container
# to avaoid that the problematic version of theseus-ai is tried to be installed when installing the grasp_diffusion package one must add the --no-deps flag to the pip install command
RUN python3 -m pip install \
    numpy==1.21.6 \
    theseus-ai \
    tqdm==4.64.1 \
    configargparse==1.5.3 \
    h5py==3.7.0 \
    pyglet==1.5.27 \
    scikit-learn==1.0.2 \
    trimesh==3.14 \
    matplotlib==3.5.3 \
    torchvision==0.14.1 \
    tensorboard==2.10.0 \
    natsort==8.2.0 \
    pytorch3d

# copy data for the grasp_diffusion package into the docker container
# COPY ./data /home/data
# --> mount data folder from host machine into docker container to avoid copying data

CMD ["/bin/bash"]