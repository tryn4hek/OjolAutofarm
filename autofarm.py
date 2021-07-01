import Modules, json
from Modules import ojolbot
import time, os

with open("conf/config.json") as getConf:
    usrData = json.load(getConf)

mainBot = ojolbot.OnEngine(
    usrData["auth_key"],
    usrData["channel_id"]
)

mesegIsiBensin = "[SCRIPT]: RADAK ISI BENSIN REKK!!"
mesegIstirahat = "[SCRIPT]: RADAK ISTIRAHAT REKK!!"
mesegFix = "[SCRIPT]: RADAK NGEFIX MOTOR BALAP REKK!!"

detiks = 0
while True:
    if detiks % 45 == 0:
        mainBot.Kerja()
        print("Berhasil Kerja")
        getBensin = mainBot.CheckBensin()
        getEnergy = mainBot.CheckEnergy()
        getMotorBasah = mainBot.CheckMotorBasah()
        
        if getBensin == True:
            print(mesegIsiBensin)
            mainBot.IsiBensin()
        else:
            pass
        
        if getEnergy == True:
            print(mesegIstirahat)
            mainBot.Istirahat()
        else:
            pass
        
        if getMotorBasah == True:
            print("[SCRIPT]: Motormu Basah rek! tak mengBypass dlo.")
            mainBot.BypassBalonAir()
        else:
            pass
    
    elif detiks % 50 == 0:
        mainBot.Travel()
        print("Berhasil Travel")
        getBensin = mainBot.CheckBensin()
        getEnergy = mainBot.CheckEnergy()
        getMotorBasah = mainBot.CheckMotorBasah()
        
        if getMotorBasah == True:
            print("[SCRIPT]: Motormu Basah rek! tak mengBypass dlo.")
            mainBot.BypassBalonAir()
        else:
            pass
        
        if getBensin == True:
            print(mesegIsiBensin)
            mainBot.IsiBensin()
        else:
            pass
        
        if getEnergy == True:
            print(mesegIstirahat)
            mainBot.Istirahat()
        else:
            pass
    
    elif detiks % 1200 == 0:
        mainBot.Lomba()
        print("Berhasil Lomba")
        CheckRusak = mainBot.CheckMotorBalapRusak
        
        if CheckRusak == True:
            mainBot.Fix()
            mainBot.Lomba()
            print(mesegFix)
        else:
            pass
        
    elif detiks % 1800 == 0:
        mainBot.Upgrade()
    
    detiks += 1
    print(f"Detiks : {detiks}")
    time.sleep(1)