#! /usr/bin/csh -f

sudo usermod -a -G vboxsf bcc
sudo chown -R bcc:users [The folder path under Linux that needs to be communal with another OS]
