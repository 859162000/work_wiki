#! /bin/bash

echo "welcome to use linux config tools!"
echo "please select a task:"
echo "1, set static IP : target file -- interfaces"
echo "2, change package source list : target file -- sources.list"
echo "3, python web envirement"
echo "4, self workspace"

read 

# config network
if [ $REPLY == "1" ]; then
    if [ ! -f "/etc/network/interfaces" ]; then
        touch "/etc/network/interfaces"
    fi
    cat "interfaces" >> "/etc/network/interfaces"
    cat "interfaces" | \
        while read curline; do
            if [ curline =~ 'auto .*' ]; then
                netname=${curline#auto};
                break;
            fi
        done
    dhclient -v -r $netname
    dhclient -v $netname
#= /etc/resolv.conf =
#nameservice 10.3.1.20

else if [ $REPLY == "2" ]; then
    # apt source
    mv /etc/apt/sources.list /etc/apt/sources.list_bak
    cp ./sources.list /etc/apt/sources.list 
    echo "You can change source now. /etc/apt/sources.list"
    echo "Continue? yes"
    read
    while [ $REPLY != "yes" ]; do
        echo "Continue? yes"
        read
    done
    apt-get update
    # TODO: if update has error, reconfig.

else if [ $REPLY == "3" ]; then
    # setup python envirement
    apt-get install python3-pip
    pip3 install sypne sphinx flask nose zeep lxml
else if [ $REPLY == "4" ]; then
    # add firefox
    apt-get install firefox fonts-arphic-ukai
fi

# add ssh server
#if [ ! -f "/usb/sbin/sshd" ]; then
#    echo "Do you want to setup openssh service? yes or no"
#    read
#    if [ $REPLY == "yes" ]; then
#        apt-get install openssh-server openssh-sftp-server
#    fi
#fi


