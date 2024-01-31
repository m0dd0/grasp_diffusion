ARG PARENT_IMAGE=nvidia/cuda:11.7.1-cudnn8-devel-ubuntu20.04
FROM ${PARENT_IMAGE}  

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

# install basic packages
RUN apt-get update && \ 
    apt-get install -q -y --no-install-recommends \
    dirmngr \ 
    gnupg2 \
    git \
    nano \
    curl \
    make \
    python3-pip \
    software-properties-common && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# setup sources.list and keys for ros packages
RUN echo "deb http://packages.ros.org/ros/ubuntu focal main" > /etc/apt/sources.list.d/ros1-latest.list && \
    apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654

# install ros packages
RUN apt-get update && \ 
    apt-get install -y --no-install-recommends \
    ros-noetic-desktop \
    python3-catkin-tools && \
    rm -rf /var/lib/apt/lists/* && \
    python3 -m pip install -U rosdep && \
    rosdep init && \
    echo "source /opt/ros/${ROS_DISTRO}/setup.bash" >> /etc/bash.bashrc && \
    echo "source /home/catkin_ws/devel/setup.bash" >> /etc/bash.bashrc && \
    echo "echo 'ROS environment initialized'" >> /etc/bash.bashrc

# install additional dependencies for se3dif package
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    libsuitesparse-dev \
    build-essential && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* 

# some python dependencies for the se3dif package which are not included in the requirements.txt file
RUN python3 -m pip install --no-cache-dir torch==1.13.1+cu117 torchvision==0.14.1+cu117 torchaudio==0.13.1 --extra-index-url https://download.pytorch.org/whl/cu117

# these are the exact same dependencies as in the requirements.txt file
# however when they are installed after the image has build, there is some weird cuda error: error: no instance of overloaded function "atomicAdd" matches the argument list
# as of now, no solution has been found. The error persists when using different cuda parent images
# therfore the dependencies are installed here. 
# After the dependecies are installed (during build to avoid cuda errors), the se3dif package can be installed without any errors as the dependencies are already installed.
RUN python3 -m pip install \
    numpy==1.21.6 \
    theseus-ai==0.1.3 \
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

CMD ["/bin/bash"]