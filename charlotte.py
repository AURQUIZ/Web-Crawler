# named after novel Charlotte's Web
# web crawler with more visual appealsing output

import Algorithmia
import json

input = ["https://www.google.com/search?q=how+to+make+a+sql+query+with+user+input+from+ruby&oq=how&aqs=chrome.4.69i57j69i65l2j69i61j35i39l2.4962j0j7&sourceid=chrome&ie=UTF-8", 1]

client = Algorithmia.client("simiisVzpIJkpWRVBHY0p/LljJP1")

res = client.algo('web/SiteMap/0.1.7').pipe(input)

siteMap = res.result

# print(siteMap)

links = []
output = []

for keyLink in siteMap:
	links.append(keyLink)
	for valLink in siteMap[keyLink]:
		links.append(valLink)

links = list(set(links))

for l in links:
	analyze = client.algo('web/AnalyzeURL/0.2.14').pipe(l)
	output.append(analyze.result)

print(json.dumps(output, indent = 4))

