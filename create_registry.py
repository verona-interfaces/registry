import json
import sys
import requests
from bs4 import BeautifulSoup
from mdutils.mdutils import MdUtils

token = sys.argv[1]
mdFile = MdUtils(file_name='README')

headers = {
    'Authorization': "token " + token,
}

request = requests.get('https://api.github.com/users/iqb-berlin/repos?per_page=100',headers=headers)
repository_json = request.json()

for i in range(0,len(repository_json)):

    is_archived = repository_json[i]['archived']
    is_player = "verona-player" in repository_json[i]['name']
    is_editor = "verona-editor" in repository_json[i]['name']
    #is_simple = "verona-player-simple" in repository_json[i]['name']

    if not is_archived: 
        if is_player or is_editor:
            releases = requests.get('https://api.github.com/repos/iqb-berlin/'+repository_json[i]['name']+'/releases/latest', headers=headers)
            releases_json = releases.json()
            if releases.status_code == 200:
                id = str(releases_json['id'])
                if len(releases_json['assets']) != 0:
                    if 'browser_download_url' in releases_json['assets'][0]:
                        asset = requests.get(releases_json['assets'][0]['browser_download_url']+'?raw=true', headers=headers)
                        parser = "html.parser"
                        soup = BeautifulSoup(asset.text, parser)
                        print(repository_json[i]['name'])
                        tmp = soup.find("script", {"type":"application/ld+json"})
                        if tmp != None :
                            test = json.loads("".join(tmp.contents))
                            mdFile.new_line(repository_json[i]['name'])
                            mdFile.new_line('``` json')
                            mdFile.new_line(json.dumps(test,indent=4, ensure_ascii= False))
                            mdFile.new_line('```')
                            mdFile.create_md_file()
        else:
            continue    



