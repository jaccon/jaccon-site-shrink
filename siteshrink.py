import os
import time
from subprocess import Popen
import subprocess
 
devnull = open(os.devnull, 'wb')

print "               .ed$$$$ $$$$$$$be. "
print "              -$           ^$$**$$$e. "
print "            .$                   '$$$c "
print "           /     Site              $4$$b "
print "          d  3       Shrink 0.1     $$$$ "
print "         $  *                   .$$$$$$ "
print "        .$  ^c           $$$$$e$$$$$$$$. "
print  "       d$L  4.         4$$$$$$$$$$$$$$b "
print  "       $$$$b ^ceeeee.  4$$ECL.F*$$$$$$$ "
print  " e$$$=.      $$$$P d$$$$F $ $$$$$$$$$- $$$$$$ "
print " z$$b. ^c     3$$$F $$$$$b   $$$$$$$$$  $$$$*$      .=$$$c "
print " 4$$$$L        $$P$  $$$b   .$ $$$$$...e$$        .=  e$$$. "
print " ^*$$$$$c  %..   *c    ..    $$ 3$$$$$$$$$$eF     zP  d$$$$$ "
print "  $**$$$ec   $   %ce$$    $$$  $$$$$$$$$$*    .r$ =$$$$P$$ "
print "    $*$b.  $c  *$e.    *** d$$$$$$L$$    .d$  e$$***$ "
print "      ^*$$c ^$c $$$      4J$$$$$% $$$ .e*$.eeP$ "
print "         $$$$$$$$'$=e....$*$$**$cz$$$ $..d$*$ "
print  "         $*$$$  *=%4.$ L L$ P3$$$F $$$P$ "
print  "           $$   $%*ebJLzb$e$$$$$b $P$ "
print  "            %..      4$$$$$$$$$$ $ "
print   "            $$$e   z$$$$$$$$$$% "
print   "               $*$c  $$$$$$$$P$ "
print   "                .$$$*$$$$$$$$bc "
print   "              .-$    .$***$$$$$$*e. "
print   "            .-$    .e$$     $*$c  ^*b. "
print   "     .=*$$$$    .e$*$          $*bc  $*$e.. "
print   "  .$$        .z*$               ^*$e.   $*****e. "
print   "  $$ee$c   .d$                     $*$.        3. "
print   "  ^*$E$)$..$$                         *   .ee==d% "
print   "    $.d$$$*                           *  J$$$e* "
print    "        $$$$$                              $$$$$ "
print "JACCON SITE SHRINK 0.1B"
print "... type any key to continue "
raw_input()
str1=raw_input("Type the url with http to Shrink ")
print " Please waiting, i try download the files ",str1 
print "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-="

if str1 == "":
 print "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-"
 print "please type the url ..."
 print "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-="
 import sys
 sys.exit()

# call('wget', '--recursive', '--no-clobber', '--page-titles','--html-extension','--convert-links','--restrict-file-names=windows','--no-parent', str1)
# Popen(['wget', '--recursive', '--no-clobber', '--page-titles','--html-extension','--convert-links','--restrict-file-names=windows','--no-parent', url], stdout=devnull)
p = subprocess.Popen(['wget', '--recursive', '--no-clobber', '--page-requisites','--html-extension','--convert-links','--restrict-file-names=windows','--no-parent', str1], stdout=subprocess.PIPE)
output, err = p.communicate()
print  output

pwd = subprocess.Popen("pwd", stdout=subprocess.PIPE, shell=True)
(output, err) = pwd.communicate()

time.sleep(.04)
devnull.close()

print ""
print "Jaccon Site Shrink . powered by @jaccon"
print ""
import os
print "Current SO",os.name
print "Download files to directory",output
print ""
print "Good bye!"
