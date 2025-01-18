# Responder-Parser
Responder's python parsing tool.

### Description
 Responder-Parser is a python 3.x open source tool which give you the ability to easily configure Responder's settings and configurations. 
 
 Responder-Parser can configure the following files:
 
 - Responder.conf
 - settings.py
 - Responder.db
 - Responder's log folder
 - Responder.py

## Privileges

> :warning: **Needs Administrator/Root privileges**: to execute Responder-Parser.

## License
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Version
### 3.0

## Version Name
## Rolling Stone

## Supporting Language

- #### python 3.x

## Supporting Systems

- #### Windows
- #### Linux

## Requirements

> :information_desk_person: **Required Dependencies: None**
<br />

## Usage

```
  _____                                 _                  _____
 |  __ \                               | |                |  __ \
 | |__) |___  ___ _ __   ___  _ __   __| | ___ _ __ ______| |__) |_ _ _ __ ___  ___ _ __
 |  _  // _ \/ __| '_ \ / _ \| '_ \ / _` |/ _ \ '__|______|  ___/ _` | '__/ __|/ _ \ '__|
 | | \ \  __/\__ \ |_) | (_) | | | | (_| |  __/ |         | |  | (_| | |  \__ \  __/ |
 |_|  \_\___||___/ .__/ \___/|_| |_|\__,_|\___|_|         |_|   \__,_|_|  |___/\___|_|
                 | |
                 |_|

Responder-Parser v3.0 - Responder's parsing tool.
Responder-Parser is an open source tool licensed under MIT.
Written with <3 by @nickvourd && Prithvi Chintha...
Please visit https://github.com/nickvourd/Responder-Parser for more...

usage: Responder-Parser [options]

options:
  -h, --help            show this help message and exit
  --cleardb             clear Responder.db data
  --clearlogs           clear Responder's logs
  -v, --version         show program's version number and exit
  -b, --backup          keep backup of Responder.conf, Responder.py and settings.py
  -r, --restore         restore backup of Responder.conf, Responder.py and settings.py to original
  -c, --challenge NUMBER
                        set challenge to Repsonder.conf
  -m, --machinename MACHINENAME
                        set machine name to settings.py
  -d, --domain DOMAIN   set domain name to settings.py
  -u, --username USERNAME
                        set username to settings.py
  --dhcp HOSTNAME       set DHCP Hostname to settings.py
  --rpcport PORT        set RPC port to settings.py
  --sql SQLSWITCH       set SQL server ON/OFF to Responder.conf
  --smb SMBSWITCH       set SMB server ON/OFF to Responder.conf
  --rdp RDPSWITCH       set RDP server ON/OFF to Responder.conf
  --kerberos KERBEROSSWITCH
                        set Kerberos server ON/OFF to Responder.conf
  --ftp FTPSWITCH       set FTP server ON/OFF to Responder.conf
  --pop POPSWITCH       set POP server ON/OFF to Responder.conf
  --smtp SMTPSWITCH     set SMTP server ON/OFF to Responder.conf
  --imap IMAPSWITCH     set IMAP server ON/OFF to Responder.conf
  --http HTTPSWITCH     set HTTP server ON/OFF to Responder.conf
  --https HTTPSSWITCH   set HTTPS server ON/OFF to Responder.conf
  --dns DNSSWITCH       set DNS server ON/OFF to Responder.conf
  --ldap LDAPSWITCH     set LDAP server ON/OFF to Responder.conf
  --dcerpc DCERPCSWITCH
                        set DCERPC server ON/OFF to Responder.conf
  --winrm WINRMSWITCH   set WINRM server ON/OFF to Responder.conf
  --mqtt MQTTSWITCH     set MQTT server ON/OFF to Responder.conf
  --snmp SNMPSWITCH     set SNMP server ON/OFF to Responder.conf
  --setdb DATABASENAME  set Database file to Responder.conf
  --sessionlog SESSIONLOG
                        set Session log file to Responder.conf
  --poisonlog POISONERSLOG
                        set Poisoners log file to Responder.conf
  --analyzelog ANALYZELOG
                        set Analyze mode log file to Responder.conf
  --configdumplog CONFIGDUMPLOG
                        set Confing Dump log file to Responder.conf
  --autoignore AUTOIGNORE
                        set option AutoIgnoreAfterSuccess ON/OFF to Responder.conf
  --capturemulticreds CAPTUREMULTICREDS
                        set option CaptureMultipleCredentials ON/OFF to Responder.conf
  --capturemultihash CAPTUREMULTIHASH
                        set option CaptureMultipleHashFromSameHost ON/OFF to Responder.conf
  --servealways SERVEALWAYS
                        set option Serve-Always for HTTP Server ON/OFF to Responder.conf
  --serveexe SERVEEXE   set option Serve-Exe for HTTP Server ON/OFF to Responder.conf
  --servehtml SERVEHTML
                        set option Serve-Html for HTTP Server ON/OFF to Responder.conf
  --htmlfilename HTMLFILENAME
                        set HtmlFilename file for HTTP Server to Responder.conf
  --exefilename EXEFILENAME
                        set ExeFilename file for HTTP Server to Responder.conf
  --exedownloadname EXEDOWNLOADNAME
                        set ExeDownloadName file for HTTP Server to Responder.conf
  --sslcert SSLCERT     set SSL Certificate for HTTPS to Responder.conf
  --sslkey SSLKEY       set SSL Key for HTTPS Server to Responder.conf
  --http-port HTTPPORT  set HTTP port to Responder.py
  --https-port HTTPSPORT
                        set HTTPS port to Responder.py
  --ftp-port FTPPORT    set FTP port to Responder.py
  --winrm-port WINRMPORT
                        set WinRM port to Responder.py
  --rdp-port RDPPORT    set RDP port to Responder.py
  --mssql-port MSSQLPORT
                        set MSSQL port to Responder.py
  --pop3-port POP3PORT  set POP3 port to Responder.py
  --smtp-port SMTPPORT  set SMTP port to Responder.py
  --imap-port IMAPPORT  set IMAP port to Responder.py
  --ldap-port LDAPPORT  set LDAP port to Responder.py
  --ldaps-port LDAPSPORT
                        set LDAPS port to Responder.py
  --mqtt-port MQTTPORT  set MQTT port to Responder.py
  --dns-tcp-port DNSTCPPORT
                        set DNS TCP port to Responder.py
  --dns-udp-port DNSUDPPORT
                        set DNS UDP port to Responder.py
  --snmp-port SNMPPORT  set SNMP port to Responder.py
  --http-proxy-port HTTPPROXYPORT
                        set HTTP proxy port to Responder.py
  --auth-proxy-port AUTHPROXYPORT
                        set Auth proxy port to Responder.py
  --kerberos-tcp-port KERBEROSTCPPORT
                        set Kerberos TCP port to Responder.py
  --kerberos-udp-port KERBEROSUDPPORT
                        set Kerberos UDP port to Responder.py
```
## Examples

In the follwoing example Responder-Parser tries to:

- Set challenge to 1122334455667788
- Clear Responder.db
- Set machine name to WIN10-TEST.CORP.LOCAL
- Set domain name to corp.local
- Keep backup of files likes settings.py, Responder.conf, Responder.db
- Set STMP Server OFF
- Set SMB Server ON

```
sudo python Responder-Parser.py -c 1122334455667788 --cleardb -m WIN10-TEST.CORP.LOCAL -d corp.local -b --smtp off --smb on
```
### Execution:

![Alt text](/Pictures/Responder-Parser-Example.png "Responder-Parser Example")

### Overcome (On Responder):

![Alt text](/Pictures/Responder-Parser-Example-Results.png "Responder-Parser Example Results")


