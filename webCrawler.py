from googlesearch.googlesearch import GoogleSearch
import sys

query  = "How to make a sql query with user input from {0}".format(sys.argv[1])
response = GoogleSearch().search(query, num_results = 100)
newfile = "{0}.txt".format(sys.argv[1])
fd = open(newfile, 'a')
count = 0;
for result in response.results:
	fd.write(result.url + '\n')
fd.close()