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

repository_json = requests.get('https://api.github.com/users/iqb-berlin/repos?per_page=100',headers=headers).json()

for i in range(0,len(repository_json)):

    is_archived = repository_json[i]['archived']
    is_verona = "verona" in repository_json[i]['name']
    is_player = "verona-player" in repository_json[i]['name']
    is_editor = "verona-editor" in repository_json[i]['name']
    #is_simple = "verona-player-simple" in repository_json[i]['name']

    if not is_archived:
        if is_verona:
            releases = requests.get('https://api.github.com/repos/iqb-berlin/'+repository_json[i]['name']+'/releases/latest', headers=headers)
            releases_json = releases.json()
            tags_json = requests.get('https://api.github.com/repos/iqb-berlin/'+repository_json[i]['name']+'/tags', headers=headers).json()
            
            mdFile.new_line('********')
            # check for latest release with tag_name
            if releases.status_code == 200 and len(tags_json) != 0:
                mdFile.new_line('Repository: ' + mdFile.new_inline_link(link=repository_json[i]['html_url'],text=repository_json[i]['name']) + ' ' + 'Release: ' + mdFile.new_inline_link(link=releases_json['html_url'],text=releases_json['tag_name']))
            # check releases with tag_name that do not count as latest release
            elif releases.status_code != 200 and len(tags_json) != 0:
                mdFile.new_line('Repository: ' + mdFile.new_inline_link(link=repository_json[i]['html_url'],text=repository_json[i]['name']) + ' ' + 'Release: ' + mdFile.new_inline_link(link='https://github.com/iqb-berlin/'+repository_json[i]['name']+'/releases/tag/'+tags_json[0]['name'],text=tags_json[0]['name']))
            else:
                mdFile.new_line('Repository: ' + mdFile.new_inline_link(link=repository_json[i]['html_url'],text=repository_json[i]['name']))

            if(repository_json[i]['description'] is not None):
                mdFile.new_line('Description: ' + repository_json[i]['description'])
            else: 
                mdFile.new_line(text='There is no description for this repository', bold_italics_code='i')  
            
            if is_player or is_editor:
                if releases.status_code == 200 and len(releases_json['assets']) != 0:

                    if 'browser_download_url' in releases_json['assets'][0]:
                        asset = requests.get(releases_json['assets'][0]['browser_download_url']+'?raw=true', headers=headers)
                        parser = "html.parser"
                        soup = BeautifulSoup(asset.text, parser)
                        tmp = soup.find("script", {"type": "application/ld+json"})
                        if tmp is not None:
                            test = json.loads("".join(tmp.contents))
                            mdFile.new_line("**JSON LD from HTML file**")
                            mdFile.new_line('``` json')
                            mdFile.new_line(json.dumps(test, indent=4, ensure_ascii=False))
                            mdFile.new_line('```')
            mdFile.new_line('********')                        

mdFile.create_md_file()

