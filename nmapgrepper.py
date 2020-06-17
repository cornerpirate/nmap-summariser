#! /usr/bin/python3
# Python3 re-write by ZephrFish & nimxj
# calling: ./nmapgrepper.py <nmap_xml_file>
# for example: ./nmapsummariser.py nmap-full-tcp.xml
#
# Copyright 2016 cornerpirate.
# 
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from xml.dom.minidom import parse
import os
import sys

def hasOpenPort(ports):
    for port in ports:
        if len(port.getElementsByTagName("state")) > 0:
            state_tag = port.getElementsByTagName("state")[0]
            state = state_tag.getAttribute("state")

            if state.__eq__("open"):
                return 1

def main():
    files = []
	# Check that they provided a parameter, if not end gracefully
    if len(sys.argv) < 2:
        print("Usage: "+sys.argv[0]+" <nmap_xml_file> "\
            "\nUsage: "+sys.argv[0]+" <nmap_xml_file1> <nmap_xml_file22>"\
            "\nAccepts multiple files.")
        sys.exit(0)
    elif len(sys.argv) >= 2:
        for i in range(1, len(sys.argv)):
            files.append(sys.argv[i])
    for f in files:

        doc = parse(f)
        hosts = doc.getElementsByTagName("host")

        for host_tag in hosts:
            address_tag = host_tag.getElementsByTagName("address")[0]
            ip_addy = address_tag.getAttribute("addr")
            hostname = "Unknown"

            try:
                hostname_tag = host_tag.getElementsByTagName("hostname")[0]
                hostname = hostname_tag.getAttribute("name")
            except:
                a="a" # not all scans have hostname tags

            try:


                _ports = host_tag.getElementsByTagName("ports")[0]
                ports = _ports.getElementsByTagName("port")

                if hasOpenPort(ports)==1:

                    for port in ports:
                        portnum =  port.getAttribute("portid")
                        protocol = port.getAttribute("protocol")

                        if len(port.getElementsByTagName("state")) > 0:

                            state_tag = port.getElementsByTagName("state")[0]
                            state = state_tag.getAttribute("state")

                            if state.__eq__("open"):
                                port_protocol = port.getAttribute("protocol")
                                service_name = "Unknown"
                                service_product = "Unknown"
                                service_version = "Unknown"

                        if len(port.getElementsByTagName("service")) != 0:
                            service_tag = port.getElementsByTagName("service")[0]
                            service_name =  service_tag.getAttribute("name")
                            service_product =  service_tag.getAttribute("product")
                            service_version =  service_tag.getAttribute("version")
                    
                    print(ip_addy + ":" +  portnum + ":" + port_protocol + ":" + service_name + ":" + service_product + ":" + service_version)

            except Exception as e:
                print(e)
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print((exc_type, fname, exc_tb.tb_lineno))

if __name__ == "__main__":
    main()

