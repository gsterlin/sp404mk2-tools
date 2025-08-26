#!/bin/bash
# A quick and dirty script to just download the firmware so that it doesn't need to be included in the repo.

wget https://static.roland.com/assets/media/zip/sp404mk2_sys_v501.zip
unzip -u sp404mk2_sys_v501.zip
rm sp404mk2_sys_v501.zip
