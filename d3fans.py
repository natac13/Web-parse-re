import urllib.request
import urllib.parse
import re

url = 'http://www.diablofans.com'

resq = urllib.request.urlopen(url)

data = resq.read()

## This worked!!! ####
# pattern = re.compile(r'<h2>(\w*\sp?a?t?c?h?\s\d\.\d\s\w*).*?</h2>', re.I|re.M)
# para = re.search(pattern, str(data))

# x = para.group(1)

# print(x)

### WORKING!!! ####
pattern = re.compile(r'<h2>(?:<a.*?>.*?</a>)*(.*?)</h2>', re.I|re.M)

h2_stuff = re.findall(pattern, str(data))

for heading in h2_stuff:
    print(str(heading))