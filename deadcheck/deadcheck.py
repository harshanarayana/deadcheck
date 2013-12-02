'''
Created on Nov 29, 2013

@author: harsnara
'''
## Imports Necessary for Processing. 
import logging
import urllib2
from HTMLParser import HTMLParser

## Global Variables
    # Variables Used for Storing Arguments. 
args = {}

    # Variable Used for storing Parent Link Info. 
pLinkData = {}
pLinkData['__link'] = None
pLinkData['__title'] = None

## Custom Class For Handling URL Link Information. 
class URLLinks(object):
    
    def __init__(self, parentLink, parentTitle, childLink, childTitle, isProcessed = False, isBroken = False, linkType = None):
        self.parentLink = parentLink
        self.parentTitle = parentTitle
        self.childLink = childLink
        self.childTitle = childTitle
        self.isProcessed = isProcessed
        self.isBroken = isBroken
        self.linkType = linkType
        
    def getParentInfo(self):
        return (self.parentLink, self.parentTitle)
    
    def getChildInfo(self):
        return (self.childLink, self.childTitle, self.linkType)
    
    def isBroken(self):
        return self.isBroken
    
    def isProcessed(self):
        return self.isProcessed
    
    def setBroken(self, value):
        self.isBroken = value
    
    def setProcessed(self, value):
        self.isProcessed = value
    
    def setLinkType(self, value):
        self.linkType = value

## Custom Class For Parsing and Extracting Info from the URL 
class MyHTMLParser(HTMLParser):
    def __init__(self):
        pass
    
    def handle_starttag(self, tag, attrs):
        HTMLParser.handle_starttag(self, tag, attrs)
    
    def handle_data(self, data):
        HTMLParser.handle_data(self, data)
        
    def handle_endtag(self, tag):
        HTMLParser.handle_endtag(self, tag)

   
# Function To handle the Arguments. Will work both for Direct Import method / run from another script. 
def Deadcheck(argList):
    if argList.has_key('-cli'):
        args['__cli'] = argList['-cli']
    else:
        args['__cli'] = False
        
    for key in argList.keys():
        if ( key == '-proxy'):
            args['__proxy'] = argList['-proxy']
        elif ( key == '-username'):
            args['__username'] = argList['-username']
        elif ( key == '-password'):
            args['__password'] = argList['-password']
        elif ( key == '-baseurl'):
            args['__auth_base'] = argList['-baseurl']
        elif ( key == '-url'):
            args['__url'] = argList['-url']
        elif ( key == '-o'):
            args['__output'] = argList['-o']
        elif ( key == '-exempt'):
            args['__exempt'] = argList['-exempt']
        elif ( key == '-log'):
            args['__log'] = argList['-log']
        elif ( key == '-cli'):
            args['__cli'] = argList['-cli']
        else:
            warning('Invalid argument %s . Skipping...' %(key))
                    
    checkAndSetLog()
    verifyAndValidateArgs()
    checkAndSetUrlLib()    
    
def checkKey(keyName):
    return args.has_key(keyName)

def verifyAndValidateArgs():
    if ( not checkKey('__url')):
        error('Please make sure input contains a key named \'-url\' and a value corresponding to it. This is used as the Base URL for Analysis.')
        exit(-1)
    
    if ( not checkKey('__proxy')):
        warning('No proxy information provided. If you are running this module on a machine that access internet through a Proxy, this test might fail.')

    if ( checkKey('__username') and checkKey('__password')):
        if ( not checkKey('__auth_base')):
            message('No base URL provided for Authentication purpose. Link being analyzed itself is set as base URL for Authentication purpose.')
    else:
        warning('Insufficient Login information provided for Authentication. All protected Links will be excluded from analysis.')
            
    if ( not checkKey('__log')):
        warning('No Logfile information provided. No log information will be generated.')
    
    if ( not checkKey('__output')):
        warning('No Outputfile information Provided, hence no report file will be generated.')
        
    if ( not checkKey('__exempt')):
        warning('No file containing list of Exempted links is provided. All the links are considered valid for analysis.')
    
    if ( not checkKey('__cli')):
        args['__cli'] = False
        
def checkAndSetLog():
    if ( checkKey('__log')):
        logging.basicConfig(filename=args['__log'], level=logging.DEBUG, format='%(name)s : %(levelname)s : %(message)s')
    else:
        logging.basicConfig(level=logging.DEBUG, format='%(name)s : %(levelname)s : %(message)s')
 
def checkAndSetUrlLib():
    proxy = None
    auth = None
    opener = None
    
    if ( checkKey('__proxy')):
        proxy = urllib2.ProxyHandler({'http':args['__proxy'], 'https' : args['__proxy']})
        opener = urllib2.build_opener(proxy)
    
    if ( checkKey('__username') and checkKey('__password')):
        passManager = urllib2.HTTPPasswordMgrWithDefaultRealm()
        if ( checkKey('__auth_base')):
            passManager.add_password(None, args['__auth_base'], args['__username'], args['__password'])
        else:
            passManager.add_password(None, args['__url'], args['__username'], args['__password'])
        auth = urllib2.HTTPBasicAuthHandler(passManager)
        opener = urllib2.build_opener(auth)
    
    if ( opener != None):
        urllib2.install_opener(opener)

def process(urlToProcess = None):
    pass
        
# Message Display Functions using Logging.
def warning(message):
    if args['__cli'] :
        logging.warning(message)

def error(message):
#    if args['__cli'] :
    logging.error(message)

def message(message):
    if args['__cli'] :
        logging.info(message)

