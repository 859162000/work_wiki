#! /bin/bash

# apt source
if [ ! -f "/etc/apt/sources.list_bak"]; then
    echo "Do you want to change apt source file? yes or no"
    read
    if [ $REPLY != "yes" ]; then
        cp /etc/apt/sources.list /etc/apt/sources.list_bak
        echo "You can change source now. /etc/apt/sources.list"
        echo "Continue? yes"
        read
        if [ $REPLY != "yes" ]; then
            apt-get update
        fi
    fi
fi

# add ssh server
if [ ! -f "/usb/sbin/sshd"]; then
    echo "Do you want to setup openssh service? yes or no"
    read
    if [ $REPLY = "yes" ]; then
        apt-get install openssh-server openssh-sftp-server
    fi
fi
