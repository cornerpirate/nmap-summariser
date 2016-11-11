# nmapsumariser

A script for summarising the output of nmap.

There are many ways to summarise nmap output. I am a fan of cat | grep | cut usually.
I had a need to spit out scans in a specific format so that is what it does.
Feel free to modify the output to suit your needs since the hard part of getting the XML attributes is done.

# nmapgrepper

A script to convert an nmap XML output to a more useful format for grepping. 
I am aware of the ".gnmap" extension but I have absolutely no love for it.

The difference is that ".gnmap" has one line for every host including all services.
Where nmapgrepper makes one line per service. Such that if you have three services on one host, you will see three lines with that IP.

I can interact with that output much quicker for most tasks.

# Pre-Requisites
None. Should run wherever python runs.
