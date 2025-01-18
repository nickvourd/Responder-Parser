##############################################
#      Responder-Parser.py                   #
#      Author: Nikos Vourdas (@nickvourd)    #
#      Co-Author: Prithvi Chintha	         #
#      License: MIT                          #
#      Required Dependencies: None           #
##############################################

import argparse
from platform import system
from os import walk, path, remove, getcwd
from shutil import copyfile, rmtree
from sys import exit, argv

#Global variables
__authors__ = ["@nickvourd", "Prithvi Chintha"]
__version__ = "3.0"
__license__ = "MIT"
__github__ = "https://github.com/nickvourd/Responder-Parser"
__ascii__ = '''


  _____                                 _                  _____                         
 |  __ \                               | |                |  __ \                        
 | |__) |___  ___ _ __   ___  _ __   __| | ___ _ __ ______| |__) |_ _ _ __ ___  ___ _ __ 
 |  _  // _ \/ __| '_ \ / _ \| '_ \ / _` |/ _ \ '__|______|  ___/ _` | '__/ __|/ _ \ '__|
 | | \ \  __/\__ \ |_) | (_) | | | | (_| |  __/ |         | |  | (_| | |  \__ \  __/ |   
 |_|  \_\___||___/ .__/ \___/|_| |_|\__,_|\___|_|         |_|   \__,_|_|  |___/\___|_|   
                 | |                                                                     
                 |_|                                                                     

Responder-Parser v.{} - Responder's parsing tool.
Responder-Parser is an open source tool licensed under {}.
Written with <3 by {} && {}...
Please visit {} for more...
'''.format(__version__, __license__, __authors__[0], __authors__[1], __github__)

#Arguments function
def Arguments(argv):
    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter, prog="Responder-Parser", usage='%(prog)s [options]')

    parser.add_argument('--cleardb', action='store_true', required=False, help="clear Responder.db data")
    parser.add_argument('--clearlogs', action='store_true', required=False, help="clear Responder's logs")
    parser.add_argument('-v', '--version', action='version', version='%(prog)s 3.0, Version Name: Rolling Stone')
    parser.add_argument('-b', '--backup', action='store_true', required=False, help="keep backup of Responder.conf, Responder.py and settings.py")
    parser.add_argument('-r', '--restore', action='store_true', required=False, help="restore backup of Responder.conf, Responder.py and settings.py to original")
    parser.add_argument('-c', '--challenge', type=str, dest='NUMBER', required=False, help="set challenge to Repsonder.conf")
    parser.add_argument('-m', '--machinename', type=str, dest='MACHINENAME', required=False, help="set machine name to settings.py")
    parser.add_argument('-d', '--domain', type=str, dest='DOMAIN', required=False, help="set domain name to settings.py")
    parser.add_argument('-u', '--username', type=str, dest='USERNAME', required=False, help="set username to settings.py")
    parser.add_argument('--dhcp', type=str, dest='HOSTNAME', required=False, help="set DHCP Hostname to settings.py")
    parser.add_argument('--rpcport', type=int, dest='PORT', required=False, help="set RPC port to settings.py")
    parser.add_argument('--sql', type=str, dest='SQLSWITCH', required=False, help="set SQL server ON/OFF to Responder.conf")
    parser.add_argument('--smb', type=str, dest='SMBSWITCH', required=False, help="set SMB server ON/OFF to Responder.conf")
    parser.add_argument('--rdp', type=str, dest='RDPSWITCH', required=False, help="set RDP server ON/OFF to Responder.conf")
    parser.add_argument('--kerberos', type=str, dest='KERBEROSSWITCH', required=False, help="set Kerberos server ON/OFF to Responder.conf")
    parser.add_argument('--ftp', type=str, dest='FTPSWITCH', required=False, help="set FTP server ON/OFF to Responder.conf")
    parser.add_argument('--pop', type=str, dest='POPSWITCH', required=False, help="set POP server ON/OFF to Responder.conf")
    parser.add_argument('--smtp', type=str, dest='SMTPSWITCH', required=False, help="set SMTP server ON/OFF to Responder.conf")
    parser.add_argument('--imap', type=str, dest='IMAPSWITCH', required=False, help="set IMAP server ON/OFF to Responder.conf")
    parser.add_argument('--http', type=str, dest='HTTPSWITCH', required=False, help="set HTTP server ON/OFF to Responder.conf")
    parser.add_argument('--https', type=str, dest='HTTPSSWITCH', required=False, help="set HTTPS server ON/OFF to Responder.conf")
    parser.add_argument('--dns', type=str, dest='DNSSWITCH', required=False, help="set DNS server ON/OFF to Responder.conf")
    parser.add_argument('--ldap', type=str, dest='LDAPSWITCH', required=False, help="set LDAP server ON/OFF to Responder.conf")
    parser.add_argument('--dcerpc', type=str, dest='DCERPCSWITCH', required=False, help="set DCERPC server ON/OFF to Responder.conf")
    parser.add_argument('--winrm', type=str, dest='WINRMSWITCH', required=False, help="set WINRM server ON/OFF to Responder.conf")
    parser.add_argument('--mqtt', type=str, dest='MQTTSWITCH', required=False, help="set MQTT server ON/OFF to Responder.conf")
    parser.add_argument('--snmp', type=str, dest='SNMPSWITCH', required=False, help="set SNMP server ON/OFF to Responder.conf")
    parser.add_argument('--setdb', type=str, dest='DATABASENAME', required=False, help="set Database file to Responder.conf")
    parser.add_argument('--sessionlog', type=str, dest='SESSIONLOG', required=False, help="set Session log file to Responder.conf"),
    parser.add_argument('--poisonlog', type=str, dest='POISONERSLOG', required=False, help="set Poisoners log file to Responder.conf")
    parser.add_argument('--analyzelog', type=str, dest='ANALYZELOG', required=False, help="set Analyze mode log file to Responder.conf")
    parser.add_argument('--configdumplog', type=str, dest='CONFIGDUMPLOG', required=False, help="set Confing Dump log file to Responder.conf")
    parser.add_argument('--autoignore', type=str, dest='AUTOIGNORE', required=False, help="set option AutoIgnoreAfterSuccess ON/OFF to Responder.conf")
    parser.add_argument('--capturemulticreds', type=str, dest='CAPTUREMULTICREDS', required=False, help="set option CaptureMultipleCredentials ON/OFF to Responder.conf")
    parser.add_argument('--capturemultihash', type=str, dest='CAPTUREMULTIHASH', required=False, help="set option CaptureMultipleHashFromSameHost ON/OFF to Responder.conf")
    parser.add_argument('--servealways', type=str, dest='SERVEALWAYS', required=False, help="set option Serve-Always for HTTP Server ON/OFF to Responder.conf")
    parser.add_argument('--serveexe', type=str, dest='SERVEEXE', required=False, help="set option Serve-Exe for HTTP Server ON/OFF to Responder.conf")
    parser.add_argument('--servehtml', type=str, dest='SERVEHTML', required=False, help="set option Serve-Html for HTTP Server ON/OFF to Responder.conf")
    parser.add_argument('--htmlfilename', type=str, dest='HTMLFILENAME', required=False, help="set HtmlFilename file for HTTP Server to Responder.conf")
    parser.add_argument('--exefilename', type=str, dest='EXEFILENAME', required=False, help="set ExeFilename file for HTTP Server to Responder.conf")
    parser.add_argument('--exedownloadname', type=str, dest='EXEDOWNLOADNAME', required=False, help="set ExeDownloadName file for HTTP Server to Responder.conf")
    #parser.add_argument('--wpadscript', type=str, dest='WPADSCRIPT', required=False, help="set WPADScript file for HTTP Server to Responder conf")
    #parser.add_argument('--htmltoinject', type=str, dest='HTMLTOINJECT', required=False, help="set HTMLToInject file for HTTP Server to Responder conf")
    parser.add_argument('--sslcert', type=str, dest='SSLCERT', required=False, help="set SSL Certificate for HTTPS to Responder.conf")
    parser.add_argument('--sslkey', type=str, dest='SSLKEY', required=False, help="set SSL Key for HTTPS Server to Responder.conf")
    parser.add_argument('--http-port', type=str, dest='HTTPPORT', required=False, help="set HTTP port to Responder.py")
    parser.add_argument('--https-port', type=str, dest='HTTPSPORT', required=False, help="set HTTPS port to Responder.py")
    parser.add_argument('--ftp-port', type=str, dest='FTPPORT', required=False, help="set FTP port to Responder.py")
    parser.add_argument('--winrm-port', type=str, dest='WINRMPORT', required=False, help="set WinRM port to Responder.py")
    parser.add_argument('--rdp-port', type=str, dest='RDPPORT', required=False, help="set RDP port to Responder.py")
    parser.add_argument('--mssql-port', type=str, dest='MSSQLPORT', required=False, help="set MSSQL port to Responder.py")
    parser.add_argument('--pop3-port', type=str, dest='POP3PORT', required=False, help="set POP3 port to Responder.py")
    parser.add_argument('--smtp-port', type=str, dest='SMTPPORT', required=False, help="set SMTP port to Responder.py")
    parser.add_argument('--imap-port', type=str, dest='IMAPPORT', required=False, help="set IMAP port to Responder.py")
    parser.add_argument('--ldap-port', type=str, dest='LDAPPORT', required=False, help="set LDAP port to Responder.py")
    parser.add_argument('--ldaps-port', type=str, dest='LDAPSPORT', required=False, help="set LDAPS port to Responder.py")
    parser.add_argument('--mqtt-port', type=str, dest='MQTTPORT', required=False, help="set MQTT port to Responder.py")
    parser.add_argument('--dns-tcp-port', type=str, dest='DNSTCPPORT', required=False, help="set DNS TCP port to Responder.py")
    parser.add_argument('--dns-udp-port', type=str, dest='DNSUDPPORT', required=False, help="set DNS UDP port to Responder.py")
    parser.add_argument('--snmp-port', type=str, dest='SNMPPORT', required=False, help="set SNMP port to Responder.py")
    parser.add_argument('--http-proxy-port', type=str, dest='HTTPPROXYPORT', required=False, help="set HTTP proxy port to Responder.py")
    parser.add_argument('--auth-proxy-port', type=str, dest='AUTHPROXYPORT', required=False, help="set Auth proxy port to Responder.py")
    parser.add_argument('--kerberos-tcp-port', type=str, dest='KERBEROSTCPPORT', required=False, help="set Kerberos TCP port to Responder.py")
    parser.add_argument('--kerberos-udp-port', type=str, dest='KERBEROSUDPPORT', required=False, help="set Kerberos UDP port to Responder.py")
    args = parser.parse_args()

    #check the number of arguments
    if len(argv) == 1:
        parser.print_help()
        print("\n")
        exit(1)

    return args

#ValidatePort Function
def ValidatePort(Port_Value):
    try:
        value = int(Port_Value)
    except ValueError:
        # If conversion fails, print error and exit
        print("[ERROR] " + Port_Value + " is not a valid port number")
        exit(1)

#FindOS function
def FindOS(candidateOS):
    match candidateOS:
            case "windows":
                myOS = "windows"
            case "linux":
                myOS = "linux"
            case _:
                myOS = "not supported"
                print("[!] Not supported operating system...\n")
                exit(1)
    
    return myOS

#SearchPath function
def SearchPath(directory):
    foundPath = path.exists(directory)
    
    return foundPath

#SearchFolder function
def SearchFolder(myOS, folder):
    foundFolderFlag = False
    match myOS:
        case "linux":
            #Using default directory
            defaultDir = "/usr/share/responder"

            #Call function named SearchPath
            foundPath = SearchPath(defaultDir)

            #If defaultDir not exist use "/"
            if foundPath != True:
                defaultDir = "/"

            #Search file in directories
            for root, dirs, files in walk(defaultDir):
                if folder in dirs:
                    foundFolderFlag = True
                    foundFolder = path.join(root, folder)
                
        case "windows":
            #Exfiltrate local drive sumbol
            currentDirectory = getcwd().split(":")
            localDrive  = currentDirectory[0] + ":\\"

            #Search file starting from local drive
            for root, dirs, files in walk(localDrive):
                if "Responder" in root:
                    if folder in dirs:
                        foundFolderFlag = True
                        foundFolder = path.join(root, folder)
                    #print(foundFolder)
        case _:
          foundFolder = "not supported"
          print("[!] Not supported operating system...\n")
          exit(1)

    if foundFolderFlag != True:
        print("[!] " + "File" + " does not exist in the system...\n")
        exit(1)

    return foundFolder

#SearchFile function
def SearchFile(myOS, file):
    foundFileFlag = False
    match myOS:
        case "linux":
            #Using default directory
            defaultDir = "/usr/share/responder"

            #Call function named SearchPath
            foundPath = SearchPath(defaultDir)

            #If defaultDir not exist use "/"
            if foundPath != True:
                defaultDir = "/"

            #Search file in directories
            for root, dirs, files in walk(defaultDir):
                if file in files:
                    foundFileFlag = True
                    foundFile = path.join(root, file)
                
        case "windows":
            #Exfiltrate local drive sumbol
            currentDirectory = getcwd().split(":")
            localDrive  = currentDirectory[0] + ":\\"

            #Search file starting from local drive
            for root, dirs, files in walk(localDrive):
                if "Responder" in root:
                    if file in files:
                        foundFileFlag = True
                        foundFile = path.join(root, file)
                    #print(foundFile)
        case _:
          foundFile = "not supported"
          print("[!] Not supported operating system...\n")
          exit(1)

    if foundFileFlag != True:
        print("[!] " + file + " does not exist in the system...\n")
        exit(1)

    return foundFile

#FindString funtion
def FindString(foundFile, searchingWord):
    with open(foundFile, 'r') as file:
        content = file.read()
        if searchingWord not in content:
            print("[!] " + foundFile + " does not support this configuration\n")
            exit(1)

#FindLineWithParts function
def FindLineWithParts(foundFile, firstPart, thirdPart):
    with open(foundFile, 'r') as file:
        for line in file:
            # Check if both parts are in the line
            if firstPart in line and thirdPart in line:
                return True
    print("[!] " + foundFile + " does not support this configuration\n")
    exit(1) 

#ModifyFile function
def ModifyFile(foundFile, searchingWord, candidateValue, statement):
    #Read file and find line
        with open(foundFile, 'r') as file:
            for index, line in enumerate(file):
                if searchingWord in line:
                    lineNumber = index + 1

        #Read file and save tha value to specific line
        with open(foundFile, 'r') as file:
            fileContents = file.readlines()
        
        fileContents[lineNumber - 1] = searchingWord + candidateValue + "\n"

        #Modify changes
        with open(foundFile, 'w') as file:
            file.writelines(fileContents)

        print("[+] " + statement + " has been set to " + "'" + candidateValue + "'" + " in " + foundFile + "...\n")

#ModifyFileWithTab function
def ModifyFileWithTab(foundFile, searchingWord, candidateValue, statement):
    #Read file and find line
        with open(foundFile, 'r') as file:
            for index, line in enumerate(file):
                if searchingWord in line:
                    lineNumber = index + 1

        #Read file and save tha value to specific line
        with open(foundFile, 'r') as file:
            fileContents = file.readlines()
        
        fileContents[lineNumber - 1] = searchingWord + " =   '" + candidateValue + "'" + "\n"

        #Modify changes
        with open(foundFile, 'w') as file:
            file.writelines(fileContents)

        print("[+] " + statement + " has been set to " + "'" + candidateValue + "'" + " in " + foundFile + "...\n")

#ModifyFileResponder function
def ModifyFileResponder(foundFile, check_one, check_two, candidateValue):
    #Read file and find line
        with open(foundFile, 'r') as file:
            for index, line in enumerate(file):
                if check_one in line and check_two in line:
                    lineNumber = index + 1

        #Read file and save tha value to specific line
        with open(foundFile, 'r') as file:
            fileContents = file.readlines()

        # Modify the target line
        original_line = fileContents[lineNumber - 1]
        parts2 = original_line.split(',')
        second_part2 = parts2[2].strip()
        modified_line = original_line.replace(second_part2, str(candidateValue))
        fileContents[lineNumber - 1] = modified_line        
        
        with open(foundFile, 'w') as file:
            file.writelines(fileContents)

#DetermineSwitch function
def DetermineSwitch(statement, candidateValue):
    if candidateValue.lower() != "on" and candidateValue.lower() != "off":
        newValue = "nothing"
        print("[!] " + statement + " parameter accepts only ON/OFF values...")
        exit(1)

    match candidateValue.lower():
        case "on":
            newValue = "On"
        case "off":
            newValue = "Off"
        
    return newValue

#ConfigureOnOff function
def ConfigureOnOff(foundFile, searchingWord, candidateServer, statement):
    #Call function named DetermineSwitch
    foundSwitch = DetermineSwitch(statement, candidateServer)

    #Call function FindString
    FindString(foundFile, searchingWord)

    #Call function named ModifyFile
    ModifyFile(foundFile, searchingWord, foundSwitch, statement)

#ConfigureString function
def ConfigureString(keyword, optionNumber):
    searchingWord = keyword + " = "

    match optionNumber:
        case 1:
            statement =  keyword + " Server"
        case 2:
            statement =  keyword
    
    return searchingWord, statement

#ConfigureStringWithTab function
def ConfigureStringWithTab(keyword):
    searchingWord = "\t\t" + keyword

    #Splitting keyword
    splitKeyword = keyword.split(".")
    statement = splitKeyword[1]

    return searchingWord, statement


#ConfigureValues function
def ConfigureValues(foundFile, searchingWord, candidateValue, statement):
    #Call function FindString
    FindString(foundFile, searchingWord)

    #Call function named ModifyFile
    ModifyFile(foundFile, searchingWord, candidateValue, statement)

#ConfigureValuesWithTab function
def ConfigureValuesWithTab(foundFile, searchingWord, candidateValue, statement):
    #Call function FindString
    FindString(foundFile, searchingWord)

    #Call function named ModifyFile
    ModifyFileWithTab(foundFile, searchingWord, candidateValue, statement)

#DetermineChallenge function
def DetermineChallenge(candidateValue):
    if len(candidateValue) != 16:
        print("[!] The challenge must be exactly 16 chars long.\n\nExample: 1122334455667788\n")
        exit(1) 

#DeterminePortRange
def DeterminePortRange(candidateValue):
    #Determine if the candidate value is betwwen the range 45000 and 49999
    if candidateValue < 45000 or candidateValue > 49999:
        print("[!] The RPC Port must be between the ranges 45000 and 49999\n")
        exit(1)

#KeepBackup function
def KeepBackup(foundFile, statement):
    #Set backup filenames
    foundFileBackup = foundFile + ".bak"

    #Copy values to backup files
    copyfile(foundFile, foundFileBackup)

    #Print success message
    print("[+] Backup for " + foundFile + " saved to: " + foundFileBackup + "\n")

#RestoreBackup function
def RestoreBackup(foundFile, foundFileBackup):

    #Copy values to original file
    copyfile(foundFileBackup, foundFile)
    
    #Delete .bak files
    remove(foundFileBackup)

    #Print success message
    print("[+] Restore backup for " + foundFileBackup + " saved to: " + foundFile + "\n")

#main function
def main():
    #Call function named Arguments
    arguments = Arguments(argv)

    #Print ascii art
    print(__ascii__)

    candidateOS = system().lower()

    #Call function named FindOS
    foundOS = FindOS(candidateOS)

    #Call function named SearchFile
    foundFile = SearchFile(foundOS, "Responder.conf")

    #Call function named SearchFile
    foundFileSettings = SearchFile(foundOS, "settings.py")

    # Added New Vaiable to find Responder.py
    foundFileResponder = SearchFile(foundOS, "Responder.py")

    #If backup argument is enabled keep backup
    if arguments.backup:
        
        #Call function named KeepBackup
        KeepBackup(foundFile, "Responder.conf")

        #Call function named KeepBackup
        KeepBackup(foundFileSettings, "Settings.py")
        
        #Call function named KeepBackup
        KeepBackup(foundFileResponder, "Responder.py")

    #If restore argument is enabled restore from backup
    if arguments.restore:
        #Call function named SearchFile
        foundFileBackup = SearchFile(foundOS, "Responder.conf.bak")

        #Call function named SearchFile
        foundFileSettingsBackup = SearchFile(foundOS, "settings.py.bak")
        
        #Call function named SearchFile
        foundFileResponderBackup = SearchFile(foundOS, "Responder.py.bak")
        
        #Call function named RestoreBackup
        RestoreBackup(foundFile, foundFileBackup)

        #Call function named RestoreBackup
        RestoreBackup(foundFileSettings, foundFileSettingsBackup)

        #Call function named RestoreBackup
        RestoreBackup(foundFileResponder, foundFileResponderBackup)

        #Print success message for clear .bak files
        print("[+] All backup files have been removed from the system...\n")

    #Clear DB section
    if arguments.cleardb:
        #Call function named SearchFile
        foundFileDB = SearchFile(foundOS, "Responder.db")

        #If backup argument is enabled keep backup
        if arguments.backup:
            #Call function named KeepBackup
            KeepBackup(foundFileDB, "Responder.db")

        #Delete Responder.db
        remove(foundFileDB)

        #Print success message for clear db
        print("[+] " + foundFileDB + " has been deleted...\n")
    
    #Clear logs section
    if arguments.clearlogs:
        #Call function named SearchFolder
        foundFolderLogs = SearchFolder(foundOS, "logs")
        
        #Delete logs folder
        rmtree(foundFolderLogs, ignore_errors=False, onerror=None)

        #Print success message for clear logs folder
        print("[+] " + foundFolderLogs + " has been deleted...\n")

    #Machine Name Section
    if arguments.MACHINENAME:
        candidateValue = arguments.MACHINENAME

        #Call function named ConfigureString
        configuredStringsWithTab = ConfigureStringWithTab("self.MachineName")

        #Call function ConfigureValues
        ConfigureValuesWithTab(foundFileSettings, configuredStringsWithTab[0], candidateValue, configuredStringsWithTab[1])

    #HTTP Port Section
    if arguments.HTTPPORT:
        candidateValue = arguments.HTTPPORT
        ValidatePort(candidateValue)
        
        line = "threads.append(Thread(target=serve_thread_tcp, args=(settings.Config.Bind_To, 80, HTTP,)))"
        parts = line.split(',')
        check_one = parts[0] + ',' + parts[1]  
        check_two = parts[3].strip() + ',' + parts[4]  
    	
        FindLineWithParts(foundFileResponder, check_one, check_two)
        ModifyFileResponder(foundFileResponder, check_one, check_two, candidateValue)
	    
        print("[+] " + parts[3].strip() + " server is running on port " + "'" + str(candidateValue) + "'" + " in " + foundFileResponder + "...\n")
    	
    #HTTPS Port Section
    if arguments.HTTPSPORT:
        candidateValue = arguments.HTTPSPORT
        ValidatePort(candidateValue)
    	
        line = "threads.append(Thread(target=serve_thread_SSL, args=(settings.Config.Bind_To, 443, HTTP,)))"
        parts = line.split(',')
        check_one = parts[0] + ',' + parts[1]  
        check_two = parts[3].strip() + ',' + parts[4]  
    	
        FindLineWithParts(foundFileResponder, check_one, check_two)
        ModifyFileResponder(foundFileResponder, check_one, check_two, candidateValue)
	    
        print("[+] " + parts[3].strip() + "S server is running on port " + "'" + str(candidateValue) + "'" + " in " + foundFileResponder + "...\n")
    
    #FTP Port Section
    if arguments.FTPPORT:
        candidateValue = arguments.FTPPORT
        ValidatePort(candidateValue)
    	
        line = "threads.append(Thread(target=serve_thread_tcp, args=(settings.Config.Bind_To, 21, FTP,)))"
        parts = line.split(',')
        check_one = parts[0] + ',' + parts[1]  
        check_two = parts[3].strip() + ',' + parts[4]  
    	
        FindLineWithParts(foundFileResponder, check_one, check_two)
        ModifyFileResponder(foundFileResponder, check_one, check_two, candidateValue)
	    
        print("[+] " + parts[3].strip() + " server is running on port " + "'" + str(candidateValue) + "'" + " in " + foundFileResponder + "...\n")
    
    #WinRM Port Section
    if arguments.WINRMPORT:
        candidateValue = arguments.WINRMPORT
        ValidatePort(candidateValue)
    	
        line = "threads.append(Thread(target=serve_thread_tcp, args=(settings.Config.Bind_To, 5985, WinRM,)))"
        parts = line.split(',')
        check_one = parts[0] + ',' + parts[1]  
        check_two = parts[3].strip() + ',' + parts[4]  
    	
        FindLineWithParts(foundFileResponder, check_one, check_two)
        ModifyFileResponder(foundFileResponder, check_one, check_two, candidateValue)
	    
        print("[+] " + parts[3].strip() + " service is running on port " + "'" + str(candidateValue) + "'" + " in " + foundFileResponder + "...\n")
    
    #RDP Port Section
    if arguments.RDPPORT:
        candidateValue = arguments.RDPPORT
        ValidatePort(candidateValue)
    	
        line = "threads.append(Thread(target=serve_thread_tcp, args=(settings.Config.Bind_To, 3389, RDP,)))"
        parts = line.split(',')
        check_one = parts[0] + ',' + parts[1]  
        check_two = parts[3].strip() + ',' + parts[4]  
    	
        FindLineWithParts(foundFileResponder, check_one, check_two)
        ModifyFileResponder(foundFileResponder, check_one, check_two, candidateValue)
	    
        print("[+] " + parts[3].strip() + " service is running on port " + "'" + str(candidateValue) + "'" + " in " + foundFileResponder + "...\n")
    
    #MSSQL Port Section
    if arguments.MSSQLPORT:
        candidateValue = arguments.MSSQLPORT
        ValidatePort(candidateValue)
    	
        line = "threads.append(Thread(target=serve_thread_tcp, args=(settings.Config.Bind_To, 1433, MSSQL,)))"
        parts = line.split(',')
        check_one = parts[0] + ',' + parts[1]  
        check_two = parts[3].strip() + ',' + parts[4]  
    	
        FindLineWithParts(foundFileResponder, check_one, check_two)
        ModifyFileResponder(foundFileResponder, check_one, check_two, candidateValue)
	    
        print("[+] " + parts[3].strip() + " service is running on port " + "'" + str(candidateValue) + "'" + " in " + foundFileResponder + "...\n")
    
    #POP3 Port Section
    if arguments.POP3PORT:
        candidateValue = arguments.POP3PORT
        ValidatePort(candidateValue)
    	
        line = "threads.append(Thread(target=serve_thread_tcp, args=(settings.Config.Bind_To, 110, POP3,)))"
        parts = line.split(',')
        check_one = parts[0] + ',' + parts[1]  
        check_two = parts[3].strip() + ',' + parts[4]  
    	
        FindLineWithParts(foundFileResponder, check_one, check_two)
        ModifyFileResponder(foundFileResponder, check_one, check_two, candidateValue)
	    
        print("[+] " + parts[3].strip() + " service is running on port " + "'" + str(candidateValue) + "'" + " in " + foundFileResponder + "...\n")
        
    #SMTP Port Section
    if arguments.SMTPPORT:
        candidateValue = arguments.SMTPPORT
        ValidatePort(candidateValue)
    	
        line = "threads.append(Thread(target=serve_thread_tcp, args=(settings.Config.Bind_To, 25,  ESMTP,)))"
        parts = line.split(',')
        check_one = parts[0] + ',' + parts[1]  
        check_two = parts[3].strip() + ',' + parts[4]  
    	
        FindLineWithParts(foundFileResponder, check_one, check_two)
        ModifyFileResponder(foundFileResponder, check_one, check_two, candidateValue)
	    
        print("[+] " + parts[3].strip() + " service is running on port " + "'" + str(candidateValue) + "'" + " in " + foundFileResponder + "...\n")
    
    #IMAP Port Section
    if arguments.IMAPPORT:
        candidateValue = arguments.IMAPPORT
        ValidatePort(candidateValue)
    	
        line = "threads.append(Thread(target=serve_thread_tcp, args=(settings.Config.Bind_To, 143, IMAP,)))"
        parts = line.split(',')
        check_one = parts[0] + ',' + parts[1]  
        check_two = parts[3].strip() + ',' + parts[4]  
    	
        FindLineWithParts(foundFileResponder, check_one, check_two)
        ModifyFileResponder(foundFileResponder, check_one, check_two, candidateValue)
	    
        print("[+] " + parts[3].strip() + " service is running on port " + "'" + str(candidateValue) + "'" + " in " + foundFileResponder + "...\n")    
    
    #LDAP Port Section
    if arguments.LDAPPORT:
        candidateValue = arguments.LDAPPORT
        ValidatePort(candidateValue)
    	
        line = "threads.append(Thread(target=serve_thread_tcp, args=(settings.Config.Bind_To, 389, LDAP,)))"
        parts = line.split(',')
        check_one = parts[0] + ',' + parts[1]  
        check_two = parts[3].strip() + ',' + parts[4]  
    	
        FindLineWithParts(foundFileResponder, check_one, check_two)
        ModifyFileResponder(foundFileResponder, check_one, check_two, candidateValue)
	    
        print("[+] " + parts[3].strip() + " service is running on port " + "'" + str(candidateValue) + "'" + " in " + foundFileResponder + "...\n")
        
   #LDAPS Port Section
    if arguments.LDAPSPORT:
        candidateValue = arguments.LDAPSPORT
        ValidatePort(candidateValue)
    	
        line = "threads.append(Thread(target=serve_thread_SSL, args=(settings.Config.Bind_To, 636, LDAP,)))"
        parts = line.split(',')
        check_one = parts[0] + ',' + parts[1]  
        check_two = parts[3].strip() + ',' + parts[4]  
    	
        FindLineWithParts(foundFileResponder, check_one, check_two)
        ModifyFileResponder(foundFileResponder, check_one, check_two, candidateValue)
	    
        print("[+] " + parts[3].strip() + "S service is running on port " + "'" + str(candidateValue) + "'" + " in " + foundFileResponder + "...\n")
    
    #MQTT Port Section
    if arguments.MQTTPORT:
        candidateValue = arguments.MQTTPORT
        ValidatePort(candidateValue)
    	
        line = "threads.append(Thread(target=serve_thread_tcp, args=(settings.Config.Bind_To, 1883, MQTT,)))"
        parts = line.split(',')
        check_one = parts[0] + ',' + parts[1]  
        check_two = parts[3].strip() + ',' + parts[4]  
    	
        FindLineWithParts(foundFileResponder, check_one, check_two)
        ModifyFileResponder(foundFileResponder, check_one, check_two, candidateValue)
	    
        print("[+] " + parts[3].strip() + " service is running on port " + "'" + str(candidateValue) + "'" + " in " + foundFileResponder + "...\n")
        
    #DNS TCP Port Section
    if arguments.DNSTCPPORT:
        candidateValue = arguments.DNSTCPPORT
        ValidatePort(candidateValue)
    	
        line = "threads.append(Thread(target=serve_thread_tcp, args=(settings.Config.Bind_To, 53, DNSTCP,)))"
        parts = line.split(',')
        check_one = parts[0] + ',' + parts[1]  
        check_two = parts[3].strip() + ',' + parts[4]  
    	
        FindLineWithParts(foundFileResponder, check_one, check_two)
        ModifyFileResponder(foundFileResponder, check_one, check_two, candidateValue)
	    
        print("[+] " + "DNS protocol is running on TCP port " + "'" + str(candidateValue) + "'" + " in " + foundFileResponder + "...\n")
    
    #DNS UDP Port Section
    if arguments.DNSUDPPORT:
        candidateValue = arguments.DNSUDPPORT
        ValidatePort(candidateValue)
    	
        line = "threads.append(Thread(target=serve_thread_udp, args=('', 53, DNS,)))"
        parts = line.split(',')
        check_one = parts[0] + ',' + parts[1]  
        check_two = parts[3].strip() + ',' + parts[4]  
    	
        FindLineWithParts(foundFileResponder, check_one, check_two)
        ModifyFileResponder(foundFileResponder, check_one, check_two, candidateValue)
	    
        print("[+] " + "DNS protocol is running on UDP port " + "'" + str(candidateValue) + "'" + " in " + foundFileResponder + "...\n")
    
    #SNMP Port Section
    if arguments.SNMPPORT:
        candidateValue = arguments.SNMPPORT
        ValidatePort(candidateValue)
    	
        line = "threads.append(Thread(target=serve_thread_udp, args=('', 161, SNMP,)))"
        parts = line.split(',')
        check_one = parts[0] + ',' + parts[1]  
        check_two = parts[3].strip() + ',' + parts[4]  
    	
        FindLineWithParts(foundFileResponder, check_one, check_two)
        ModifyFileResponder(foundFileResponder, check_one, check_two, candidateValue)
	    
        print("[+] " + parts[3].strip() + " service is running on UDP port " + "'" + str(candidateValue) + "'" + " in " + foundFileResponder + "...\n")
        
    #HTTP proxy Port Section
    if arguments.HTTPPROXYPORT:
        candidateValue = arguments.HTTPPROXYPORT
        ValidatePort(candidateValue)
    	
        line = "threads.append(Thread(target=serve_thread_tcp, args=(settings.Config.Bind_To, 3128, HTTP_Proxy,)))"
        parts = line.split(',')
        check_one = parts[0] + ',' + parts[1]  
        check_two = parts[3].strip() + ',' + parts[4]  
    	
        FindLineWithParts(foundFileResponder, check_one, check_two)
        ModifyFileResponder(foundFileResponder, check_one, check_two, candidateValue)
	    
        print("[+] " + parts[3].strip() + " service is running on port " + "'" + str(candidateValue) + "'" + " in " + foundFileResponder + "...\n")
        
    #Auth proxy Port Section
    if arguments.AUTHPROXYPORT:
        candidateValue = arguments.AUTHPROXYPORT
        ValidatePort(candidateValue)
    	
        line = "threads.append(Thread(target=serve_thread_tcp_auth, args=(settings.Config.Bind_To, 3128, Proxy_Auth,)))"
        parts = line.split(',')
        check_one = parts[0] + ',' + parts[1]  
        check_two = parts[3].strip() + ',' + parts[4]  
    	
        FindLineWithParts(foundFileResponder, check_one, check_two)
        ModifyFileResponder(foundFileResponder, check_one, check_two, candidateValue)
	    
        print("[+] " + parts[3].strip() + " service is running on port " + "'" + str(candidateValue) + "'" + " in " + foundFileResponder + "...\n")
        
    #Kerberos TCP Port Section
    if arguments.KERBEROSTCPPORT:
        candidateValue = arguments.KERBEROSTCPPORT
        ValidatePort(candidateValue)
    	
        line = "threads.append(Thread(target=serve_thread_tcp, args=(settings.Config.Bind_To, 88, KerbTCP,)))"
        parts = line.split(',')
        check_one = parts[0] + ',' + parts[1]  
        check_two = parts[3].strip() + ',' + parts[4]  
    	
        FindLineWithParts(foundFileResponder, check_one, check_two)
        ModifyFileResponder(foundFileResponder, check_one, check_two, candidateValue)
	    
        print("[+] " + "Kerberos service is running on TCP port " + "'" + str(candidateValue) + "'" + " in " + foundFileResponder + "...\n")    
        
    #Kerberos UDP Port Section
    if arguments.KERBEROSUDPPORT:
        candidateValue = arguments.KERBEROSUDPPORT
        ValidatePort(candidateValue)
    	
        line = "threads.append(Thread(target=serve_thread_udp, args=('', 88, KerbUDP,)))"
        parts = line.split(',')
        check_one = parts[0] + ',' + parts[1]  
        check_two = parts[3].strip() + ',' + parts[4]  
    	
        FindLineWithParts(foundFileResponder, check_one, check_two)
        ModifyFileResponder(foundFileResponder, check_one, check_two, candidateValue)
	    
        print("[+] " + "Kerberos service is running on UDP port " + "'" + str(candidateValue) + "'" + " in " + foundFileResponder + "...\n") 
    
    #Domain Name Section
    if arguments.DOMAIN:
        candidateValue = arguments.DOMAIN

        #Call function named ConfigureString
        configuredStringsWithTab = ConfigureStringWithTab("self.DomainName")

        #Call function ConfigureValues
        ConfigureValuesWithTab(foundFileSettings, configuredStringsWithTab[0], candidateValue, configuredStringsWithTab[1])
    
    #Username Section
    if arguments.USERNAME:
        candidateValue = arguments.USERNAME

        #Call function named ConfigureString
        configuredStringsWithTab = ConfigureStringWithTab("self.Username")

        #Call function ConfigureValues
        ConfigureValuesWithTab(foundFileSettings, configuredStringsWithTab[0], candidateValue, configuredStringsWithTab[1])

    #DHCP Hostname Section
    if arguments.HOSTNAME:
        candidateValue = arguments.HOSTNAME

        #Call function named ConfigureString
        configuredStringsWithTab = ConfigureStringWithTab("self.DHCPHostname")

        #Call function ConfigureValues
        ConfigureValuesWithTab(foundFileSettings, configuredStringsWithTab[0], candidateValue, configuredStringsWithTab[1])

    #RPC Port Section
    if arguments.PORT:
        candidateValue = arguments.PORT

        #Call function DeterminePortRange
        DeterminePortRange(candidateValue)

        #Call function named ConfigureString
        configuredStringsWithTab = ConfigureStringWithTab("self.RPCPort")

        #Call function FindString
        FindString(foundFileSettings, configuredStringsWithTab[0])

        #Read file and find line
        with open(foundFileSettings, 'r') as file:
            for index, line in enumerate(file):
                if configuredStringsWithTab[0] in line:
                    lineNumber = index + 1

        #Read file and save tha value to specific line
        with open(foundFileSettings, 'r') as file:
            fileContents = file.readlines()
        
        fileContents[lineNumber - 1] = configuredStringsWithTab[0] + " =   " + str(candidateValue) + "\n"

        #Modify changes
        with open(foundFileSettings, 'w') as file:
            file.writelines(fileContents)

        print("[+] " + configuredStringsWithTab[1] + " has been set to " + "'" + str(candidateValue) + "'" + " in " + foundFileSettings + "...\n")

    #Challenge section
    if arguments.NUMBER:
        candidateValue = arguments.NUMBER

        #Call function named DetermineChallenge
        DetermineChallenge(candidateValue)

        #Call function named ConfigureString
        configuredStrings = ConfigureString("Challenge", 2)

        #Call function ConfigureValues
        ConfigureValues(foundFile, configuredStrings[0], candidateValue, configuredStrings[1])

    #SSLCert section
    if arguments.SSLCERT:
        candidateValue = arguments.SSLCERT

        #Call function named ConfigureString
        configuredStrings = ConfigureString("SSLCert", 2)

        #Call function ConfigureValues
        ConfigureValues(foundFile, configuredStrings[0], candidateValue, configuredStrings[1])

    #SSLKey section
    if arguments.SSLKEY:
        candidateValue = arguments.SSLKEY

        #Call function named ConfigureString
        configuredStrings = ConfigureString("SSLKey", 2)

        #Call function ConfigureValues
        ConfigureValues(foundFile, configuredStrings[0], candidateValue, configuredStrings[1])

    #DatabaseName Section
    if arguments.DATABASENAME:
        candidateValue = arguments.DATABASENAME

        #Call function named ConfigureString
        configuredStrings = ConfigureString("Database", 2)

        #Call function ConfigureValues
        ConfigureValues(foundFile, configuredStrings[0], candidateValue, configuredStrings[1])
    
    #Session log section
    if arguments.SESSIONLOG:
        candidateValue = arguments.SESSIONLOG

        #Call function named ConfigureString
        configuredStrings = ConfigureString("SessionLog", 2)

        #Call function ConfigureValues
        ConfigureValues(foundFile, configuredStrings[0], candidateValue, configuredStrings[1])

    #Poisoners log section
    if arguments.POISONERSLOG:
        candidateValue = arguments.POISONERSLOG

        #Call function named ConfigureString
        configuredStrings = ConfigureString("PoisonersLog", 2)

        #Call function ConfigureValues
        ConfigureValues(foundFile, configuredStrings[0], candidateValue, configuredStrings[1])

    #Analyze mode log section
    if arguments.ANALYZELOG:
        candidateValue = arguments.ANALYZELOG

        #Call function named ConfigureString
        configuredStrings = ConfigureString("AnalyzeLog", 2)

        #Call function ConfigureValues
        ConfigureValues(foundFile, configuredStrings[0], candidateValue, configuredStrings[1])

    #Config Dump log section
    if arguments.CONFIGDUMPLOG:
        candidateValue = arguments.CONFIGDUMPLOG

        #Call function named ConfigureString
        configuredStrings = ConfigureString("ResponderConfigDump", 2)

        #Call function ConfigureValues
        ConfigureValues(foundFile, configuredStrings[0], candidateValue, configuredStrings[1])

    #HtmlFilename section
    if arguments.HTMLFILENAME:
        candidateValue = arguments.HTMLFILENAME

        #Call function named ConfigureString
        configuredStrings = ConfigureString("HtmlFilename", 2)

        #Call function ConfigureValues
        ConfigureValues(foundFile, configuredStrings[0], candidateValue, configuredStrings[1])

    #ExeFilename section
    if arguments.EXEFILENAME:
        candidateValue = arguments.EXEFILENAME

        #Call function named ConfigureString
        configuredStrings = ConfigureString("ExeFilename", 2)

        #Call function ConfigureValues
        ConfigureValues(foundFile, configuredStrings[0], candidateValue, configuredStrings[1])

    #ExeDownloadName section
    if arguments.EXEDOWNLOADNAME:
        candidateValue = arguments.EXEDOWNLOADNAME

        #Call function named ConfigureString
        configuredStrings = ConfigureString("ExeDownloadName", 2)

        #Call function ConfigureValues
        ConfigureValues(foundFile, configuredStrings[0], candidateValue, configuredStrings[1])
    
    #AutoIgnoreAfterSuccess section
    if arguments.AUTOIGNORE:
        candidateServer = arguments.AUTOIGNORE

        #Call function named ConfigureString
        configuredStrings = ConfigureString("AutoIgnoreAfterSuccess", 2)

        #Call function named ConfigureOnOff
        ConfigureOnOff(foundFile, configuredStrings[0], candidateServer, configuredStrings[1])

    #CaptureMultipleCredentials section
    if arguments.CAPTUREMULTICREDS:
        candidateServer = arguments.CAPTUREMULTICREDS

        #Call function named ConfigureString
        configuredStrings = ConfigureString("CaptureMultipleCredentials", 2)

        #Call function named ConfigureOnOff
        ConfigureOnOff(foundFile, configuredStrings[0], candidateServer, configuredStrings[1])

    #CaptureMultipleHashFromSameHost section
    if arguments.CAPTUREMULTIHASH:
        candidateServer = arguments.CAPTUREMULTIHASH

        #Call function named ConfigureString
        configuredStrings = ConfigureString("CaptureMultipleHashFromSameHost", 2)

        #Call function named ConfigureOnOff
        ConfigureOnOff(foundFile, configuredStrings[0], candidateServer, configuredStrings[1])
    
    #Serve-Always section
    if arguments.SERVEALWAYS:
        candidateServer = arguments.SERVEALWAYS

        #Call function named ConfigureString
        configuredStrings = ConfigureString("Serve-Always", 2)

        #Call function named ConfigureOnOff
        ConfigureOnOff(foundFile, configuredStrings[0], candidateServer, configuredStrings[1])
    
    #Serve-Exe section
    if arguments.SERVEEXE:
        candidateServer = arguments.SERVEEXE

        #Call function named ConfigureString
        configuredStrings = ConfigureString("Serve-Exe", 2)

        #Call function named ConfigureOnOff
        ConfigureOnOff(foundFile, configuredStrings[0], candidateServer, configuredStrings[1])

    #Serve-Html section
    if arguments.SERVEHTML:
        candidateServer = arguments.SERVEHTML

        #Call function named ConfigureString
        configuredStrings = ConfigureString("Serve-Html", 2)

        #Call function named ConfigureOnOff
        ConfigureOnOff(foundFile, configuredStrings[0], candidateServer, configuredStrings[1])

    #SQL Server section
    if arguments.SQLSWITCH:
        candidateServer = arguments.SQLSWITCH

        #Call function named ConfigureString
        configuredStrings = ConfigureString("SQL", 1)

        #Call function named ConfigureOnOff
        ConfigureOnOff(foundFile, configuredStrings[0], candidateServer, configuredStrings[1])

    #SMB Server section
    if arguments.SMBSWITCH:
        candidateServer = arguments.SMBSWITCH

        #Call function named ConfigureString
        configuredStrings = ConfigureString("SMB", 1)

        #Call function named ConfigureOnOff
        ConfigureOnOff(foundFile, configuredStrings[0], candidateServer, configuredStrings[1])

    #RDP Server section
    if arguments.RDPSWITCH:
        candidateServer = arguments.RDPSWITCH

        #Call function named ConfigureString
        configuredStrings = ConfigureString("RDP", 1)

        #Call function named ConfigureOnOff
        ConfigureOnOff(foundFile, configuredStrings[0], candidateServer, configuredStrings[1])

    #Kerberos Server section
    if arguments.KERBEROSSWITCH:
        candidateServer = arguments.KERBEROSSWITCH

        #Call function named ConfigureString
        configuredStrings = ConfigureString("Kerberos", 1)

        #Call function named ConfigureOnOff
        ConfigureOnOff(foundFile, configuredStrings[0], candidateServer, configuredStrings[1])
    
    #FTP Server section
    if arguments.FTPSWITCH:
        candidateServer = arguments.FTPSWITCH

        #Call function named ConfigureString
        configuredStrings = ConfigureString("FTP", 1)

        #Call function named ConfigureOnOff
        ConfigureOnOff(foundFile, configuredStrings[0], candidateServer, configuredStrings[1])
    
    #POP Server section
    if arguments.POPSWITCH:
        candidateServer = arguments.POPSWITCH

        #Call function named ConfigureString
        configuredStrings = ConfigureString("POP", 1)

        #Call function named ConfigureOnOff
        ConfigureOnOff(foundFile, configuredStrings[0], candidateServer, configuredStrings[1])

    #SMTP Server section
    if arguments.SMTPSWITCH:
        candidateServer = arguments.SMTPSWITCH

        #Call function named ConfigureString
        configuredStrings = ConfigureString("SMTP", 1)

        #Call function named ConfigureOnOff
        ConfigureOnOff(foundFile, configuredStrings[0], candidateServer, configuredStrings[1])
    
    #IMAP Server section
    if arguments.IMAPSWITCH:
        candidateServer = arguments.IMAPSWITCH

        #Call function named ConfigureString
        configuredStrings = ConfigureString("IMAP", 1)

        #Call function named ConfigureOnOff
        ConfigureOnOff(foundFile, configuredStrings[0], candidateServer, configuredStrings[1])
    
    #HTTP Server section
    if arguments.HTTPSWITCH:
        candidateServer = arguments.HTTPSWITCH

        #Call function named ConfigureString
        configuredStrings = ConfigureString("HTTP", 1)

        #Call function named ConfigureOnOff
        ConfigureOnOff(foundFile, configuredStrings[0], candidateServer, configuredStrings[1])
    
    #HTTPS Server section
    if arguments.HTTPSSWITCH:
        candidateServer = arguments.HTTPSSWITCH

        #Call function named ConfigureString
        configuredStrings = ConfigureString("HTTPS", 1)

        #Call function named ConfigureOnOff
        ConfigureOnOff(foundFile, configuredStrings[0], candidateServer, configuredStrings[1])
        
    #MQTT Server section
    if arguments.MQTTSWITCH:
        candidateServer = arguments.MQTTSWITCH

        #Call function named ConfigureString
        configuredStrings = ConfigureString("MQTT", 1)

        #Call function named ConfigureOnOff
        ConfigureOnOff(foundFile, configuredStrings[0], candidateServer, configuredStrings[1]) 
        
    #SNMP Server section
    if arguments.SNMPSWITCH:
        candidateServer = arguments.SNMPSWITCH

        #Call function named ConfigureString
        configuredStrings = ConfigureString("SNMP", 1)

        #Call function named ConfigureOnOff
        ConfigureOnOff(foundFile, configuredStrings[0], candidateServer, configuredStrings[1])           
    
    #DNS Server section
    if arguments.DNSSWITCH:
        candidateServer = arguments.DNSSWITCH

        #Call function named ConfigureString
        configuredStrings = ConfigureString("DNS", 1)

        #Call function named ConfigureOnOff
        ConfigureOnOff(foundFile, configuredStrings[0], candidateServer, configuredStrings[1])

    #LDAP Server section
    if arguments.LDAPSWITCH:
        candidateServer = arguments.LDAPSWITCH

        #Call function named ConfigureString
        configuredStrings = ConfigureString("LDAP", 1)

        #Call function named ConfigureOnOff
        ConfigureOnOff(foundFile, configuredStrings[0], candidateServer, configuredStrings[1])

    #DCERPC Server section
    if arguments.DCERPCSWITCH:
        candidateServer = arguments.DCERPCSWITCH

        #Call function named ConfigureString
        configuredStrings = ConfigureString("DCERPC", 1)

        #Call function named ConfigureOnOff
        ConfigureOnOff(foundFile, configuredStrings[0], candidateServer, configuredStrings[1])    
    
    #WINRM Server section
    if arguments.WINRMSWITCH:
        candidateServer = arguments.WINRMSWITCH

        #Call function named ConfigureString
        configuredStrings = ConfigureString("WINRM", 1)

        #Call function named ConfigureOnOff
        ConfigureOnOff(foundFile, configuredStrings[0], candidateServer, configuredStrings[1])

if __name__ == "__main__":
    main()
