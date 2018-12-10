#!/bin/bash
#
# RPM build wrapper for ocaml-soundtouch, runs inside the build container on travis-ci

set -xe

yum -y install \
    epel-release \
    http://li.nux.ro/download/nux/dextop/el7/x86_64/nux-dextop-release-0-5.el7.nux.noarch.rpm

chown root:root ocaml-soundtouch.spec

USER=nobody build-rpm-package.sh ocaml-soundtouch.spec
