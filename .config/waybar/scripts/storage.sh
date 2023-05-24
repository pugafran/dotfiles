#! /bin/sh
#
echo "$(lsblk -f | grep 6284dd81-146a-4b28-aad1-af2dc8d9a5e3 | tr -s [:space:] ';' | cut -d ';' -f 5) / $(lsblk | grep sda3 | tr -s [:space:] ';' | cut -d ';' -f 4)"
