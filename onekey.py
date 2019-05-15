#!/usr/bin/env bash
yum -y install git
git clone https://github.com/linfangzhi/vultr-onekey-ss-ssr
yum -y install epel-release
yum -y install python34
python3 https://raw.githubusercontent.com/linfangzhi/Onekey_ss_ssr/master/too_young.py
