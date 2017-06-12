import knock25,knock28
import requests

if __name__ == "__main__":
    with open("british_articles.txt") as file:
        text = file.read()
    
    basic_info = knock25.extract_basic_info(text)
    field_pairs = knock25.extract_field_dict(basic_info)
    
    url = "https://en.wikipedia.org/w/api.php"
params = {"action": "query",
           "titles": "File:" + field_pairs["国旗画像"],
           "prop": "imageinfo",
           "format": "json",
           "iiprop": "url"}
res = requests.get(url, params=params).json()
print(res["query"]["pages"]["23473560"]["imageinfo"][0]["url"])
