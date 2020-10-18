import urllib
print '''\033[92m
print "coding"
print"by   "
print"M0bin-Dan"
print"follow me:mr_mobin_dan in insta"
print'''
url = raw_input("enter your target: ")
server = urllib.urlopen(url)
for key .value in server.headers.items():

    print ""
    print key+':'+value
    print ""
