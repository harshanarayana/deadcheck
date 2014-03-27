Description
===========

<Work In progress>

This is a tool that can be used for Analyzing and identifying the Deadlink in a website. This can come handy during the regular website maintenance. 

The contents uploaded here is only the Alpha content. I've uploaded it here to get some feedback and suggestion as to how I can make this more efficient. 

Any suggestion / comment / feedback / request is welcome. Please drop any of these messages using the following link. 

https://www.assembla.com/spaces/deadcheck/tickets


   **Installation** 

       pip install lxml
       pip install deadcheck
        
       or 
       
       pip install lxml
       git clone git@github.com:harshanarayana/deadcheck.git
       python setup.py install

   **Usage** 

		prompt>python run.py -url <baseURLToAnalyze> [-proxy <proxyURL>:<prompt> -username <userName for Protected Page> 
		-password <Password to access Protected Page> -auth_base <Super URL for Authentication> -log <logFile> 
		-exempt <ExceptionURL File> -depth <int, default = 1> -v <default = True>]
		
Pending Implementation
======================

  - ~~Report Generation. ( A custom Package / Using liches )~~
  - Handling the Processing of Links using Multiple Threads. ( To reduce processing time )
  - Regex support to Exception links. 
  - Additional Log / Debug Option Support. 
  - GUI ( Work In Progress ) 

Change Log
==========

v0.0.1:
-------

  - Initial Draft
  - Analysis method and URLLinks class were combined together. 
  - Report Information Extraction was manual. 

v0.0.2:
-------

  - Second Draft
  - Code Re-structured. Independent classes created for URLLinks, handling Custom Error and Other necessary informaiton.
  - **URLLinks**

    - Custom Class for Storing URL information. 
    - info() method for accessing the URLLink information in the form of a string to display / Report. 
    - Additional parameters included for Reporting. 

      - File Size
      - Dowload Time
      - Check Time
      - Last Modified. 
      - Status Information ( With Error and / or other information as applicable )
  - **ErrorCodes**

    - Custom class created for Storing and retrieving HTTPError codes with suitable messages. 

  - **ErrorHandler** 

    - Custom Error handler class for Handling Custom errors. Additional items will be added to this during the course of development. 

  - **deadcheck**

    - Main Package now containins a class **Deadcheck** which handles all the operations. 
    - User the Deadcheck class to perform any operations.

v0.0.3:
-------
  
  - Third Draft
  - Report Generation Modules Included. 
  - Custom report.txt file is generated along with the Report.
  - Report Is generated based on the Links processed at the respective link depth. 
  - A summary of Links Is provided for each report file. 

 v0.0.3.1:
 ---------
  - Low-level URL extraction from 'javascript' type hrefs. 
  - Fix for UnicodeEncodeError.
  - Minor Cleanup / change for the reports. 