# macro-decrypt

##Description
Many macro enabled word documents have been sent around the world attempting to download malware such as Hancitor.
They use string obfuscation techniques to hide their (anti-forensic) functions.
These macros have been practically the same, meaning their masking techniques are
easily decoeded. This script mimics the functions of the macros to extract a malicious
URL for blocking.

##Usage
Use olevba.py (or equivalent) to extract the macro from the document. The encrypted URL string is usually
the longest string in the macro towards the top of the macro. Copy the single letter function and its inputs
(Eg. `b(161, 25, "oalAFeEntipxSXricpd;NC")` ) and place it after a print statement
at the end of this script. Eg. `print b(161, 25, "oalAFeEntipxSXricpd;NC")`
