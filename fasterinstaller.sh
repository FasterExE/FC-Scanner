#!/bin/bash

echo " 
        _______ __   __   __ ______ _______ _______
       /__  __// /  / /  / // __  // _____// _____/
        / /   / /  / /__/ // /_/ // /____ / /____
       / /   / /  /__  __// __  //____  //____  /
    __/ /__ / /____ / /  / / / /_____/ /_____/ /
   /______//______//_/  /_/ /_//______//______/"
	                                                     
echo ""


echo "   Happy Scanning Script by: 𓆩 𝐈𝐋𝐘𝐀𝐒𝐒 𓆪 "
echo "           @FasterExE  @RAYANDIAG               "
echo "      https://t.me/FasterExE     "


echo "This is a the script installer"

pkg remove game-repo -y
pkg remove science-repo -y

pkg install grep -y
pkg install golang -y
pkg install openssl -y
pkg install python -y && pip install requests

echo 'PATH="$PATH:$HOME/go/bin"' >> $HOME/.bashrc && source $HOME/.bashrc

go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest


go install -v github.com/aztecrabbit/bugscanner-go@latest

echo "##################"

echo "the installation was successful"


