import Algorithmia
import json

client = Algorithmia.client("simiisVzpIJkpWRVBHY0p/LljJP1")

def get_links():
    #"""Gets links from URL"""
    input = "https://www.google.com/search?q=how+to+make+a+sql+query+with+user+input+from+ruby&oq=how&aqs=chrome.4.69i57j69i65l2j69i61j35i39l2.4962j0j7&sourceid=chrome&ie=UTF-8"

    if input.startswith("http") or input.startswith("https"):
        algo = client.algo('web/GetLinks/0.1.5')
        links = algo.pipe(input).result
        return links
    else:
        print("Please enter a properly formed URL")

def get_content():
    #"""Get text content from URL."""
    data = get_links()
    algo = client.algo("util/Url2Text/0.1.4")
    # Limit content extracted to only blog articles
    content = [{"url": link, "content": algo.pipe(link).result} for link in data if link.startswith("http://")]
    return content

def find_sentiment():
    """Get sentiment from web content."""
    data = get_content()
    algo = client.algo("nlp/SentimentAnalysis/1.0.2")
    try:
        # Find the sentiment score for each article
        algo_input = [{"document": item["content"]} for item in data]
        algo_response = algo.pipe(algo_input).result
  
        algo_final = [{"url": doc["url"]} for sent in algo_response for doc in data]
	#for a in algo_final:
		#print ("{url}".format(url=a))
        #print(algo_final)
        print(json.dumps(algo_final, indent = 4))
        return algo_final
    except Exception as e:
        print(e)

#main function ( basically making calls )
find_sentiment()

