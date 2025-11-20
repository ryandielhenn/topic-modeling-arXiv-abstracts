import urllib.request
import xml.etree.ElementTree as ET
import time

def fetch_arxiv_abstracts(category='cs.AI', max_results=1000):
    """
    Fetch abstracts from arXiv API
    Note: arXiv API limits to ~1000 results per query
    """
    abstracts = []
    titles = []
    batch_size = 100
    
    for start in range(0, max_results, batch_size):
        url = f'http://export.arxiv.org/api/query?search_query=cat:{category}&start={start}&max_results={batch_size}'
        
        try:
            with urllib.request.urlopen(url) as data:
                xml_content = data.read().decode('utf-8')
            
            root = ET.fromstring(xml_content)
            namespace = {'atom': 'http://www.w3.org/2005/Atom'}
            entries = root.findall('atom:entry', namespace)
            
            if not entries:
                break
                
            for entry in entries:
                title = entry.find('atom:title', namespace).text
                abstract = entry.find('atom:summary', namespace).text
                
                # Clean up whitespace
                abstract = ' '.join(abstract.split())
                title = ' '.join(title.split())
                
                abstracts.append(abstract)
                titles.append(title)
            
            print(f"Fetched {len(abstracts)} abstracts so far...")
            time.sleep(3)  # Be nice to arXiv's servers
            
        except Exception as e:
            print(f"Error fetching batch at {start}: {e}")
            break
    
    return abstracts, titles
