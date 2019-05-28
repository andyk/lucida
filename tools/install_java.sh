#!/bin/bash
export JAVA_VERSION=8
export JAVA_TOOL_OPTIONS=-Dfile.encoding=UTF8

# Used to use Oracle Java 8, but that is no longer
# available due to Oracle's license change in April 2019
# so now using OpenJDK, but not positive everything will work.
add-apt-repository ppa:openjdk-r/ppa && \
  apt-get update && \
  apt-get -y install openjdk-8-jdk #&& \
  #rm -rf /var/lib/apt/lists/* && \
  #rm -rf /var/cache/oracle-jdk$JAVA_VERSION-installer
