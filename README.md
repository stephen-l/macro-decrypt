# macro-decrypt

Name: decodeWordMacroStrings.py
Author: stephen-l
Last revision: 27/9/16 09:56
Version: 0.2
Prerequisite(s): olevba.py

Description: Many macro enabled word documents have been sent around the world attempting to download malware.
              They use string obfuscation techniques to hide their activity.
              These macros have been practically the same, meaning their masking techniques are
              easily decoeded. This script mimics the functions of the macros to extract a malicious
              URL for blocking.

Usage:       Use olevba.py to extract the macro from the document. The encrypted URL string is usually
              on line 26 of the macro (or line 33 of the olevba.py output. Of course this changes. It is
              usually the longest string). Copy the single letter function and it's inputs
              (Eg. b(161, 25, "oalAFeEntipxSXricpd;NC") ) and place it after a print statement
              at the end of this script. Examples at the end of the script.
