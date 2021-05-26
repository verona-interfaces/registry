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

repository = requests.get('https://api.github.com/users/iqb-berlin/repos?per_page=100',headers=headers)
repository_json = repository.json()

if repository.status_code == 200:
    for i in range(0,len(repository_json)):

        is_archived = repository_json[i]['archived']
        is_verona = "verona" in repository_json[i]['name']
        is_player = "verona-player" in repository_json[i]['name']
        is_editor = "verona-editor" in repository_json[i]['name']

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
                # there is no release
                else:
                    mdFile.new_line('Repository: ' + mdFile.new_inline_link(link=repository_json[i]['html_url'],text=repository_json[i]['name']))

                if(repository_json[i]['description'] is not None):
                    mdFile.new_line('Description: ' + repository_json[i]['description'])
                else: 
                    mdFile.new_line(text='There is no description for this repository', bold_italics_code='i')  
                
                if is_player or is_editor:
                    #check whether there is an html file in the latest release
                    if releases.status_code == 200 and len(releases_json['assets']) != 0:
                        if 'browser_download_url' in releases_json['assets'][0]:
                            asset = requests.get(releases_json['assets'][0]['browser_download_url']+'?raw=true', headers=headers)
                            parser = "html.parser"
                            soup = BeautifulSoup(asset.text, parser)
                            json_ld = soup.find("script", {"type": "application/ld+json"})
                            if json_ld is not None:
                                json_ld = json.loads("".join(json_ld.contents))
                                mdFile.new_line("**JSON LD from HTML file**")
                                mdFile.new_line('``` json')
                                mdFile.new_line(json.dumps(json_ld, indent=4, ensure_ascii=False))
                                mdFile.new_line('```')
                    else:
                        tree = requests.get('https://api.github.com/repos/iqb-berlin/'+repository_json[i]['name']+'/git/trees/main?recursive=1',headers=headers)
                        tree_json =json.loads(tree.content or tree.text)
                        t = 0
                        #search for the only(!) html file in the repository
                        found = False
                        while not found :
                            try:
                                if "html" in tree_json['tree'][t]['path']:
                                    found = True
                                    break
                                t += 1
                            except IndexError:
                                print("There was no HTML file in the repository")
                                break
                        if found: 
                            path = tree_json['tree'][t]['path']
                            asset = requests.get('https://github.com/iqb-berlin/'+repository_json[i]['name']+'/blob/main/'+path+'?raw=true')
                            parser = "html.parser"
                            soup = BeautifulSoup(asset.text, parser)
                            meta = soup.find_all("meta")
                            for tag in meta:
                                dataVersion = tag.get('data-version')
                                content = tag.get('content')
                                dataRepo = tag.get('data-repository-url')
                                api = tag.get("data-api-version")
                                browsers = tag.get("data-supported-browsers")
                                if dataVersion or content or dataRepo or api or browsers:
                                    mdFile.new_line('**Metadata from HTML**')
                                    mdFile.new_line('``` json')
                                    if dataVersion:
                                        mdFile.new_line("data-version: " + dataVersion)
                                    if content:    
                                        mdFile.new_line("content: " + content)
                                    if dataRepo:
                                        mdFile.new_line("data-repository-url: " + dataRepo)
                                    if api:
                                        mdFile.new_line("data-api-version: " + api)
                                    if browsers:
                                        mdFile.new_line("data-supported-browsers: " + browsers)
                                    mdFile.new_line('```')

                mdFile.new_line('********')                        
    mdFile.create_md_file() 

else:
    print("There was an error retrieving the repository list")