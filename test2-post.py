# This code converts an url to pdf in Python using SelectPdf REST API through a POST request. 
# The content is saved into a file on the disk.

import urllib
import urllib2

api_endpoint = 'http://selectpdf.com/api2/convert/'
key = 'your license key here'
test_url = 'http://selectpdf.com'
local_file = 'test.pdf'
 
# parameters - add here any needed API parameter 
parameters = {
	'key': key,
	'url': test_url
}

requesturl = api_endpoint
print "Calling {0}\n".format(requesturl)

try:
	result = urllib2.urlopen(requesturl, urllib.urlencode(parameters))
	localFile = open(local_file, 'wb')
	localFile.write(result.read())
	localFile.close()
	print "Test pdf document generated successfully!"
except urllib2.HTTPError as e:
	print "HTTP Response Code: {0}\nHTTP Response Message: {1}".format(e.code, e.reason)
except:
	print "An error occurred!"
	