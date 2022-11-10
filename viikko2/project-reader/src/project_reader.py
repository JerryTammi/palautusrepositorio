from urllib import request
from project import Project
from toml import loads, dumps


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        toml = loads(content)
        name = toml['tool']['poetry']['name']
        desc = toml['tool']['poetry']['description']
        depend = toml['tool']['poetry']['dependencies']
        deb_depend = toml['tool']['poetry']['dev-dependencies']
        
        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, desc, depend, deb_depend)
