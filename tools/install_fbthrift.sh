#!/bin/bash
installCheck () {
  if [ ! -d fbthrift ]; then
    return 1
  fi
  python -mthrift_compiler.main --gen cpp2 check_thrift.thrift
  if [ -d gen-cpp2 ]; then
    rm -rf gen-cpp2
    return 0
  else
    return 1
  fi
}

if installCheck "$0"; then
  echo "Facebook Thrift installed";
  exit 0;
fi

if [ ! -d fbthrift ]; then
  git clone https://github.com/facebook/fbthrift.git
  if [ $? -ne 0 ]; then
    echo "Could not clone FBThrift!!! Please try again later..."
    exit 1
  fi
fi

# THIS DOES NOT WORK...
# Ensure fbthrift installs most recent version of mstch that
# supports cmake 2.8 (i.e. the version installed in Ubuntu 14.04).
# By default, fbthrift installs https://github.com/no1msd/mstch master
# which requires cmake version >= 3.0.2.

#mkdir -p fbthrift/thrift/build/deps
#pushd fbthrift/thrift/build/deps

# mstch 0.2.1 is the most recent version supporting cmake 2.8.
# We could just update cmake but newest PPAs seem only to
# have 3.2.2 for Ubuntu 14.04, for example see:
# https://launchpad.net/~george-edison55/+archive/ubuntu/cmake-3.x

#git clone --branch 0.2.1 https://github.com/no1msd/mstch
#popd

# Newest version of mstch requires cmake 3.0.2 or higher.
pushd ~/
wget https://github.com/Kitware/CMake/releases/download/v3.14.4/cmake-3.14.4.tar.gz
tar -xvzf cmake-3.14.4.tar.gz
cd cmake-3.14.4
./configure
make
make install
cmake --version
popd

cd fbthrift/thrift \
 && git checkout v2017.03.20.00 \
 && echo "a1abbb7abcb259acbd94d0d0929b79607a8ce806" > ./build/FOLLY_VERSION \
 && echo "a5503c88e1d6799dcfb337caf09834a877790c92" > ./build/WANGLE_VERSION \
 && ./build/deps_ubuntu_14.04.sh \
 && autoreconf -ivf \
 && ./configure \
 && make \
 && make install \
 && cd ../..

if installCheck "$0"; then
  echo "Facebook Thrift installed";
  exit 0;
else
  echo "Failed to install Facebook Thrift";
  exit 1;
fi
