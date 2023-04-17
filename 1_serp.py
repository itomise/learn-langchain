from serpapi import GoogleSearch
search = GoogleSearch({
    "q": "coffee", 
    "location": "Austin,Texas",
    "api_key": "000c8f951cf9064aac76fe251f78dbdb920410347360cf999dc11e7e4c620b3d"
  })
result = search.get_dict()
print(result)