#! /bin/sh

sensors | grep "Core 0:" | tr -d '+' | awk '{print $3}'
