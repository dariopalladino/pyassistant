import json, os

class Config():
    configFile = 'config/settings.json'

    def __init__(self) -> None:
        self.readSettings()

    def readSettings(self):
        with open(os.path.join(os.getcwd(), self.configFile), 'rb') as cf:
            self.config = json.load(cf)

    def get(self, key) -> str:
        if not isinstance(key, list) and isinstance(key, str):
            key = key.split('.')
        print(f"Key {key}")
        return self._getKey(key)
    
    def _getKey(self, key):
        v = self.config[key[0]]
        print(f"Key len {len(key)}")
        print(f"First value {v}")
        x = 1      
        while x < len(key):            
            v = v[key[x]]
            x += 1
            print(f"x= {v}")
        return v
