#!/usr/bin/python
import sys
import json
import requests
import pprint
import ConfigParser

class netmriconn:
    def __init__(self, conffile):
        config = ConfigParser.ConfigParser()
        try:
            config.read(conffile)
        except:
            print "failed opening config file, giving up"
            sys.exit(0)
        try:
            self.address = config.get('NetMRI', 'address')
            self.username = config.get('NetMRI', 'username')
            self.path = config.get('NetMRI', 'path')
            self.password = config.get('NetMRI', 'password')
            self.version = config.get('NetMRI', 'version')
            if config.get('NetMRI', 'verify') == 'True':
                self.verify = True
            else:
                self.verify = False
        except:
            print "conf file appears to be corrupt or does not contain all needed values to set up NetMRI connection"
            sys.exit(0)

    def get_device(self, keyfield, key):
        r = requests.get('https://' + self.address + self.path + self.version + '/devices/index.json?' + keyfield + '=' + key, auth=(self.username, self.password), verify=self.verify)
        return r.json()

    def get_device_physicals(self, keyfield, key):
        r = requests.get('https://' + self.address + self.path + self.version + '/device_physicals/search.json?' + keyfield + '=' + key, auth=(self.username, self.password), verify=self.verify)
        return r.json()

    def get_if_addrs(self, keyfield, key):

        r = requests.get('https://' + self.address + self.path + self.version + '/if_addrs/index.json?' + keyfield + '=' + key, auth=(self.username, self.password), verify=self.verify)
        return r.json()

    def get_interface(self, keyfield, key):

        r = requests.get('https://' + self.address + self.path + self.version + '/interfaces/index.json?' + keyfield + '=' + key, auth=(self.username, self.password), verify=self.verify)
        return r.json()

    def get_endhost_lastseen(self, keyfield, key):

        r = requests.get('https://' + self.address + self.path + self.version + '/end_host_mac_addresses/index.json?' + keyfield + '=' + key + '&sort=EndHostMACAddressTimestamp&dir=asc', auth=(self.username, self.password), verify=self.verify)
        return r.json()

    def get_neighbordevice(self, keyfield, key):

        r = requests.get('https://' + self.address + self.path + self.version + '/neighbors/index.json?' + keyfield + '=' + key, auth=(self.username, self.password), verify=self.verify)
        return r.json()

    def get_vlans(self, keyfield, key):

        # needs to use the search method rather than index, as index does not permit constraining results by vlanindex (actual vlan id numeric tag)

        r = requests.get('https://' + self.address + self.path + self.version + '/vlans/search.json?' + keyfield + '=' + key, auth=(self.username, self.password), verify=self.verify)
        return r.json()

    def get_vlanmembers(self, keyfield, key):

        r = requests.get('https://' + self.address + self.path + self.version + '/vlan_members/index.json?' + keyfield + '=' + key, auth=(self.username, self.password), verify=self.verify)
        return r.json()

