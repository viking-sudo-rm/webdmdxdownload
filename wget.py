import re, urllib, urllib2

folder = raw_input("folder name: ")
keyword = raw_input("hash segment: ")

data = urllib2.urlopen("http://psy1.psych.arizona.edu/cgi-bin/unloadazk4web").read()

pattern = re.compile('"(http://psy1.psych.arizona.edu/DMDX/[A-Za-z0-9]+.[a-f0-9]*' + keyword + '[a-f0-9]*.txt)"')

results = pattern.findall(data)

for result in results:
	print "Downloading", result + ".."
	urllib.urlretrieve(result, (folder + "/" + result.split("DMDX/")[1]))
	print "Saving file", result.split("DMDX/")[1] + ".."