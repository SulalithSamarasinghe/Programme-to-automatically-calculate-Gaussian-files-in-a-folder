from termcolor import colored
from os import walk
import os
import pyfiglet
import subprocess
import datetime
import csv
import psutil
import smtplib
#
#
#
emailAddress = '##############'
password = '########'
#
#
#
def newStart():
    logoText = 'RESTART'
    versionText = '           1.1V'
    logo = pyfiglet.figlet_format(logoText,font='epic')
    version = pyfiglet.figlet_format(versionText,font='bulbhead')
    logoPrint = colored(logo,'green')
    versionPrint =  colored(version,'blue')
    print(logoPrint+versionPrint)
    print(' Welcome!!! Restart 1.1V is a programme which can use to calculate')
    print(' Gaussian out files automatically.')
    print('')
    print('   ==> Calculates all the Gaussian files in a specific directory.')
    print('   ==> Generate "Restart" files for Gaussian calculations.')
    print('   ==> Generate "GaussianData.csv" file.')
    print('')
    print(" Whats new in Restart 1.1V,")
    print('')
    print('   ==> Receive an email update right after the calculations are over.')
    print('   ==> Minor bugs fixed.')
    print('')
#
#
#
def newHelp():
    print('')
    print('-----------------------------------------------------------------------------------------------------------')
    print('')
    print('                                            ++++++++++++++++')
    print('                                            +     Help     +')
    print('                                            ++++++++++++++++')
    print('')
    print('+ Restart 1.1V is a programme that is mainly developed to calculate Gaussian out files automatically.')
    print('+ Python 3.7 is the base code of the Restart 1.1V programme.')
    print('+ Restart 1.1V consist of 386 Python code lines.')
    print('')
    print('How to enter the path/directory ?')
    print('  + Input the file path and seperate the folders with "/" (Ex: Test/NewTest/).')
    print('  + Path/Directory must end with "/".')
    print('  + Use the correct folder names and check lowercase and uppercase.')
    print('')
    print('What is the "GaussianData.csv" file ?')
    print('  + "GaussianData.csv" contains details about all the "xyz.out" file names and the status (calculated or not).')
    print('  + Also the exact time taken to each calculation.')
    print('')
    print('What will happen if their was power failure ?')
    print('  + The calculations will stop.')
    print('  + When you start the calculations in the same path/directory, then it will starts where it was interrupted.')
    print('  + It will create a "Restart" file for the last "xyz.com" file which was interrupted by the power failure.')
    print('')
    print('How to use E-Mail update feature ?')
    print('  + You can enable the E-Mail update feature to be updated about the ongoing calculations.')
    print('  + After every calculation, it will send an E-Mail.')
    print('')
    print('What will happen if there is no proper internet connection to send E-Mails ?')
    print('  + Programme will show an error message about the condition.')
    print('  + The Gaussian calculations do not have an effect from this troubled internet connection.')
    print('')
    print('Limitaions of options ?')
    print('  + Only restrict to numbers(ex: 0,1,2,3,...).')
    print('  + Do not enter letters(ex: a,b,c....) symbols (ex: #,$,%....).')
    print('')
    print('-----------------------------------------------------------------------------------------------------------')
    print('')
#
#
#
def newExit():
    print('')
    print('                    ....End Programme....')
    print('')
#
#
#
def newWrongOption():
    print('')
    print('You have entered a wrong option!!!')
    print('Pleace try again')
    print('')
#
#
#
def newErrorHandler(func):
    try:
        func()
    except ValueError:
        print('')
        print('ValueError occurred!')
        print('You have enterd a character string/symbols or none.')
        print('Please only enter numbers.')
        print('')
        newErrorHandler(func)
    except ZeroDivisionError:
        print('')
        print('ZeroDivisionError occurred!')
        print('You have divided the number by zero!')
        print('Please only enter numbers.')
        print('')
        newErrorHandler(func)
    except NameError:
        print('')
        print('NameError occurred!')
        print('There is no such path/directory.')
        print('Please check again.')
        print('')
        newErrorHandler(func)
    except PermissionError:
        print('')
        print('PermissionError occurred!')
        print('Cannot start a xyz.csv file name with symbols!')
        print('Enter a valid name.')
        print('')
        newErrorHandler(func)
    except AttributeError:
        print('')
        print('AttributeError occurred!')
        print('Your Files have already been created!')
        print('Please check again.')
        print('')
        newErrorHandler(func)
    except IOError:
        print('')
        print('IOError occured!')
        print('Please check again.')
        print('')
        newErrorHandler(func)
    except:
        print('')
        print('An unknown error occurred!')
        print('')
        newErrorHandler(func)
#
#
#
def sendMail(emailAddress,receiverEMail,password,subject,message):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(emailAddress,password)
        message = 'Subject: {}\n\n{}'.format(subject,message)
        server.sendmail(emailAddress,receiverEMail,message)
        server.quit()
    except:
        print("Unable to send the E-Mail update!!!")
        print("")
        print("   + Pleace check your E-Mail has enabled less secure apps. If not pleace enable.")
        print("   + Check the internet connection.")
        print("   + Check whether you have given the correct e-mail address and password.")
        print('')
#
#
#
def aGCalculations():
    def gaussianComFiles(files,comFileNames):
        for i in range(len(files)):
            if files[i].split('.')[1]=='com':
                comFileNames.append(files[i])
    #
    #
    #
    def updateRestartFile(restartFileName):
        rGFData = []
        with open(restartFileName,'r') as gFile:
            for lines in gFile:
                rGFData.append(lines)
        for i in range(len(rGFData)):
            if rGFData[i].split()==[]:
                continue
            else:
                if rGFData[i].split()[0]=='#P':
                    rGFData[i] = '#P Restart\n'
    #    os.remove(restartFileName)
        newUpdateFile = open(restartFileName,'w')
        for k in range(len(rGFData)):
            newUpdateFile.write(rGFData[k])
        newUpdateFile.close()
    #
    #
    #
    print('')
    print('        +++++++++++++++++++++++++++++++++++++++++++++')
    print('        +++    Automated Gaussian Calculations    +++')
    print('        +++++++++++++++++++++++++++++++++++++++++++++')
    print('')
    yn = raw_input('Update through E-Mail; Yes[Y] or No[N] : ')
    newYN = []
    def yesorno(ynOption,newYN):
        ynOption = ynOption.lower()
        if ynOption == 'y' or ynOption == 'n':
            newYN.append(ynOption)
        else:
            print('')
            print('Enter options are only Yes[Y] or No[N]')
            print('')
            yn = raw_input('Update through E-Mail; Yes[Y] or No[N] : ')
            yesorno(yn,newYN)
    yesorno(yn,newYN)
    print('')
    path = raw_input('Enter folder path : ')
    print('')
    dataFileName = path+'dataCHK.dat'
    csvFileName = path+'GaussianData.csv'
    filenames = []
    gFNames = []
    checkFileData = []
    runGFNames = []
    csvFileData = []
    #
    #
    #
    for dirpath,dirnames,filenames in walk(path):
        continue
    #
    #
    #
    gaussianComFiles(filenames,gFNames)
    #
    #
    #
    if os.path.exists(dataFileName)==True:
        with open(dataFileName,'r') as F:
            for lines in F:
                checkFileData.append(lines.split()[0])
    else:
        for i in range(len(gFNames)):
            data = gFNames[i]+'_file_not_processed.'
            checkFileData.append(data)
        for k in range(len(checkFileData)):
            updateFile = open(dataFileName,'a')
            updateFile.write(checkFileData[k])
            updateFile.write('\n')
            updateFile.close()
    #
    #
    #
    cnt = 0
    #
    #
    #
    for j in range(len(gFNames)):
        if checkFileData[j] == gFNames[j]:
            cnt = cnt+1
            print(gFNames[j]+' calculation was finished.')
            print('')
        else:
            runGFNames.append(gFNames[j])
    #
    #
    #
    if os.path.exists(csvFileName)==True:
        with open(csvFileName,'r') as F:
            for lines in F:
                csvFileData.append(lines.split(','))
    else:
        csvFileData.append(['Gaussian File Name','Status','Calculation Start','Calculation Finished','Time Took For The Calculation'])
        for k in range(len(gFNames)):
            csvFileData.append([gFNames[k],'Not completed','','',''])
        with open(csvFileName,'a') as dFile:
            thewriter = csv.writer(dFile)
            for m in range(len(csvFileData)):
                thewriter.writerow([csvFileData[m][0],csvFileData[m][1],csvFileData[m][2],csvFileData[m][3],csvFileData[m][4]])
    #
    #
    #
    rNo = len(runGFNames)
    grNo = len(gFNames)
    if rNo == 0:
        if grNo == 0:
            print('There are no "xyz.com" files in this path/directory or no such path/directory.')
            print('Please check again.')
        else:
            print('All Gaussian calculations in the path/directory, "'+path+'" are completed.')
    else:
        print('Files in process,')
        for i in range(len(runGFNames)):
            print('                  '+runGFNames[i])
        print('')
        rNo = str(rNo)
        print(rNo+' Calculations are in process...')
        print('')
    #
    #
    #
    gCHKFileName = path+'gCHKFile.chk'
    if os.path.exists(gCHKFileName)==True:
        if rNo != 0:
            updateRestartFile(path+runGFNames[0])
    else:
        gCHKFile = open(gCHKFileName,'a')
        gCHKFile.close()
    #
    #
    #
    for i in range(len(runGFNames)):
        print(runGFNames[i]+', calculation is in process...')
        print('')
        outFile = runGFNames[i].split('.com')[0]
        outFileName = outFile+'.out'
        runningCode = 'g09 < '+runGFNames[i]+' > '+outFileName
        startTime = datetime.datetime.now().replace(microsecond=0)
        subprocess.call(runningCode,shell=True,cwd=path)
        finishedTime = datetime.datetime.now().replace(microsecond=0)
        timeDifference =  finishedTime-startTime
        #
        #
        #
        if newYN[0] == 'y':
            subject = 'Restart 1.1V Update'
            nFinishedTime = finishedTime.strftime('%x %X')
            message = runGFNames[i]+', calculation was completed at '+nFinishedTime+'.'
            sendMail(emailAddress,emailAddress,password,subject,message)
        #
        #
        #
        print(runGFNames[i]+', calculation is completed.')
        print('')
        checkFileData[i+cnt]= runGFNames[i]
        os.remove(dataFileName)
        newUpdate = open(dataFileName,'a')
        for k in range(len(checkFileData)):
            newUpdate.write(checkFileData[k])
            newUpdate.write('\n')
        newUpdate.close()
        os.remove(csvFileName)
        csvFileData[1+i+cnt]=[runGFNames[i],'Completed',startTime,finishedTime,timeDifference]
        with open(csvFileName,'a') as dFile:
            thewriter = csv.writer(dFile)
            for m in range(len(csvFileData)):
                thewriter.writerow([csvFileData[m][0],csvFileData[m][1],csvFileData[m][2],csvFileData[m][3],csvFileData[m][4]])
    print('')
    if rNo != 0:
        print('All Gaussian calculations in the path/directory, "'+path+'" are completed.')
    print('')
#
#
#
def mainMenu():
    print('')
    print('              ++++++++++++++++++++++++++++++++')
    print('              +++    Restart 1.1V Panel    +++')
    print('              ++++++++++++++++++++++++++++++++')
    print('')
    print('01) Automated Gaussian Calculations')
    print('02) Help')
    print('03) Exit')
    print('')
    mOption = int(raw_input('Enter option : '))
    print('')
    if mOption == 1:
        aGCalculations()
        newErrorHandler(mainMenu)
    elif mOption == 2:
        newHelp()
        newErrorHandler(mainMenu)
    elif mOption == 3:
        newExit()
    else:
        newWrongOption()
        newErrorHandler(mainMenu)
#
#Restart_1.1V
#
def restartProgramme():
    newStart()
    newErrorHandler(mainMenu)
#
#
#
restartProgramme()
