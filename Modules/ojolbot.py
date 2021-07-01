import requests, json
import time

class OnEngine:
    DC_AUTH = ""
    CH_ID = ""
    
    API_URL = "https://discord.com/api/v9"
    def __init__(self,auth,channel_id):
        self.DC_AUTH = auth
        self.CH_ID = channel_id
    
    class Messager:
        onAuth = ""
        onChannel = ""
        
        onURL = "https://discord.com/api/v9"
        def __init__(self,auth,channel_id):
            self.onAuth = auth
            self.onChannel = channel_id
        
        def postMessage(self,content):
            onPost = requests.post(
                f"{self.onURL}/channels/{self.onChannel}/messages",
                headers = {
                    "authorization":f"{self.onAuth}",
                    "content-type":f"application/json"
                },
                json = {
                    "content":content
                }
            )
        def getMessage(self,limit,msgtype):
            onGet = requests.get(
                f"{self.onURL}/channels/{self.onChannel}/messages?limit={limit}",
                headers = {
                    "authorization":f"{self.onAuth}"
                }
            )
            if msgtype == "content":
                getContent = json.loads(onGet.content.decode())
                return getContent[0]["content"]
            
            elif mesgtype == "embeds":
                getEmbed = json.loads(onGet.content.decode())
                if "embeds" in getEmbed[0]:
                    return getEmbed[0]["embeds"][0]
    
    # ==================[TO WORK]>
    def Kerja(self):
        makePost = self.Messager(self.DC_AUTH, self.CH_ID)
        makePost.postMessage("O!kerja")
    
    def Travel(self):
        makePost = self.Messager(self.DC_AUTH, self.CH_ID)
        makePost.postMessage("O!travel shsh")
    
    def Lomba(self):
        makePost = self.Messager(self.DC_AUTH, self.CH_ID)
        makePost.postMessage("O!lomba")
    
    # GET LAST MESSAGE
    def getLastMessage(self):
        makeGet = self.Messager(self.DC_AUTH, self.CH_ID)
        theContent = makeGet.getMessage(1)
        return theContent
    
    # ALL STATES
    def IsiBensin(self):
        makePost = self.Messager(self.DC_AUTH, self.CH_ID)
        makePost.postMessage("O!isi bensin")
    
    def Istirahat(self):
        makePost = self.Messager(self.DC_AUTH, self.CH_ID)
        makePost.postMessage("O!istirahat")
    
    def Fix(self):
        makePost = self.Messager(self.DC_AUTH, self.CH_ID)
        makePost.postMessage("O!fix")
    
    def Upgrade(self):
        makePost = self.Messager(self.DC_AUTH, self.CH_ID)
        makePost.postMessage("O!upgrade")
    
    def BypassBalonAir(self):
        time.sleep(300.5)
    
    # ALL CHECKS
    def CheckBensin(self):
        makeAll = self.Messager(self.DC_AUTH, self.CH_ID)
        getContent = makeAll.getMessage(1,"content")
        if "bensinmu kosong" in getContent.lower():
            return True
        else:
            return False
    
    def CheckEnergy(self):
        makeGet = self.Messager(self.DC_AUTH, self.CH_ID)
        getContent = makeGet.getMessage(1,"content")
        if "terlalu lelah" in getContent.lower():
            return True
        else:
            return False
    
    def CheckMotorBalapRusak(self):
        makeGet = self.Messager(self.DC_AUTH, self.CH_ID)
        getContent = makeGet.getMessage(1,"content")
        if "motor balapmu sedang rusak" in getContent.lower():
            return True
        else:
            return False
    
    def CheckMotorBasah(self):
        makeGet = self.Messager(self.DC_AUTH, self.CH_ID)
        getContent = makeGet.getMessage(1,"content")
        if "motormu basah" in getContent.lower():
            return True
        else:
            return False