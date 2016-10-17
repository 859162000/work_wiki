#! /bin/bash

# config network
echo "Do you want to set a static IP? yes or no";
read
if [ $REPLY == "yes" ]; then
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
fi

# check internet
echo "Is the system connected to internet? yes or no"
if [ $REPLY == "no" ]; then
    exit
fi

# apt source
if [ ! -f "/etc/apt/sources.list_bak" ]; then
    echo "Do you want to change apt source file? yes or no"
    read
    if [ $REPLY == "yes" ]; then
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
    fi
fi

# add ssh server
#if [ ! -f "/usb/sbin/sshd" ]; then
#    echo "Do you want to setup openssh service? yes or no"
#    read
#    if [ $REPLY == "yes" ]; then
#        apt-get install openssh-server openssh-sftp-server
#    fi
#fi

# add firefox
echo "Do you want to setup firefox? yes or no"
read
if [ $REPLY == "yes" ]; then
    apt-get install firefox fonts-arphic-ukai
fi
