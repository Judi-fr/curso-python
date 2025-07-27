from playsound import playsound
from colorama import init, Style , Fore
import os
import unicodedata


def quitar_acentos(texto):
    return ''.join(
        c for c in unicodedata.normalize('NFKD', texto)
        if not unicodedata.combining(c)
    )

comandos = {
    #GOOGLE
    "google chrome": "https://www.google.com/chrome/",
    "abrir google chrome": "https://www.google.com/chrome/",
    "abri google chrome": "https://www.google.com/chrome/",
    #DISCORD
    "discord": "https://www.discord.com/channels/@me",
    "abrir discord": "https://www.discord.com/channels/@me",
    "abri discord": "https://www.discord.com/channels/@me",
    #NETFLIX
    "netflix": "https://www.netflix.com/browse",
    "abrir netflix": "https://www.netflix.com/browse",
    #YOUTUBE
    "youtube": "https://www.youtube.com/",
    "abrir youtube": "https://www.youtube.com/",
    #GITHUB
    "github": "https://www.github.com/",
    "abrir github": "https://www.github.com/",
    #GMAIL
    "gmail": "https://www.mail.google.com/mail/u/0/#inbox",
    "abrir gmail": "https://www.mail.google.com/mail/u/0/#inbox",
    #HOTMAIL
    "hotmail": "https://www.outlook.live.com/mail/0/",
    "outlook": "https://www.outlook.live.com/mail/0/",
    "abrir outlook": "https://www.outlook.live.com/mail/0/",
    "abrir hotmail": "https://www.outlook.live.com/mail/0/",
    #DISNEY
    "disney": "https://www.disneyplus.com/en-gb/home",
    "abrir disney": "https://www.disneyplus.com/en-gb/home",
    #SOUTH PARK
    "south park": "https://www.southpark.lat/seasons/south-park",
    #PLAYLISTS YOUTUBE
    "playlist": "https://www.youtube.com/feed/playlists",
    #RAP YOUTUBE
    "playlist rap": "https://www.youtube.com/playlist?list=PLt6z7U7Xm5YmrnDvvXswmMuZaEebRBFAF",
    "rap": "https://www.youtube.com/playlist?list=PLt6z7U7Xm5YmrnDvvXswmMuZaEebRBFAF",
    #ROCK YOUTUBE
    "playlist rock": "https://www.youtube.com/playlist?list=PLt6z7U7Xm5Yl7M42WwfozVg81Gz9kZxWC",
    "rock": "https://www.youtube.com/playlist?list=PLt6z7U7Xm5Yl7M42WwfozVg81Gz9kZxWC",
    #UNIVERSIDAD UTN
    "facultad": "https://frgp.cvg.utn.edu.ar/",
    "universidad": "https://frgp.cvg.utn.edu.ar/",
    "utn": "https://frgp.cvg.utn.edu.ar/",
    "facu":"https://frgp.cvg.utn.edu.ar/",
    #PEDIDOS YA
    "pedidos ya": "https://www.pedidosya.com.ar/?externalLogin=true",
    "pedidosya": "https://www.pedidosya.com.ar/?externalLogin=true",
    #KICK
    "kick": "https://www.kick.com/",
    "abrir kick": "https://www.kick.com/",
    #TWITCH
    "twitch": "https://www.twitch.tv/",
    "abrir twitch": "https://www.twitch.tv/",
    #CHAT GPT
    "chatgpt": "https://www.chatgpt.com/?oai-dm=1",
    "robot": "https://www.chatgpt.com/?oai-dm=1",
    "el robot": "https://www.chatgpt.com/?oai-dm=1",
    #SANTANDER RIO
    "banco": "https://www2.personas.santander.com.ar/obp-webapp/angular/#!/home",
    "santander": "https://www2.personas.santander.com.ar/obp-webapp/angular/#!/home",
    #OP.GG
    "opgg": "https://www.op.gg/lol/summoners/las/FasoYEscabio-LAS",
    "perfil de lol": "https://www.op.gg/lol/summoners/las/FasoYEscabio-LAS",
    #UBER
    "uber": "https://www.uber.com/ar/es/rider-home/?_csid=RypVwAJY9pUJJNWp_hyaww&sm_flow_id=IR4QYain&state=WyE2blZ45S1Cl-VPeU_q-5W_r-h-84d3b2tWir43C18%3D",
    #CAPCUT
    "capcut": "https://www.capcut.com/editor/F3DC8102-A125-4E37-AE1D-9D686FD8F195?...",
    "editor de video": "https://www.capcut.com/editor/F3DC8102-A125-4E37-AE1D-9D686FD8F195?...",
    #WHATSAPP
    "whatsapp": "https://web.whatsapp.com/",
    #ALUMNI
    "curso" : "https://alumni.education/courses",
    #TWITTER
    "twitter" : "https://x.com/home",
    "abrir twitter" : "https://x.com/home"
}

def analizar2(texto):
    bool=False
        
    #ADMINISTRADOR DE TAREAS
    if texto in ["administrador de tareas"]:
        os.system("start taskmgr")
        bool=True

    #POKER
    elif texto in ["poker","abrir poker"]:
        os.system(r'"C:/Users/ezeri/AppData/Roaming/GGPCOM/bin/launcher.exe"')
        bool=True

    #VISUAL ESTUDIO
    elif texto in ["visual estudio","abrir visual estudio"]:
        os.system(r'"C:/Users/ezeri/AppData/Local/Programs/Microsoft VS Code/Code.exe"')
        bool=True

    #CODEBLOCKS
    elif texto in ["codeblocks","abrir codeblocks"]:
        os.system(r'"C:/Program Files/CodeBlocks/codeblocks.exe"')
        bool=True

    #RELOJ
    elif texto in ["reloj"]:
        os.system("start ms-clock:")
        bool=True
    
    #CALCULADORA
    elif texto in ["calculadora","abrir calculadora"]:
        os.system("start calculator:")
        bool=True

    #COUNTER STRIKE
    elif texto in ["counter"]:
        pass

    #LEAGUE OF LEGENDS
    elif texto in ["lol"]:
        pass

    #ONE NOTE
    elif texto in ["one note"]:
        os.system(r'"C:/Program Files/Microsoft Office/root/Office16/ONENOTE.EXE"')
        bool=True

    #DOCUMENTOS
    elif texto in ["facultad"]:
        os.startfile( r'"C:/Users/ezeri/Documents/Facultad"')
        os.system(r'"C:/Program Files/Microsoft Office/root/Office16/ONENOTE.EXE"')
        os.system(r'"C:/Program Files/CodeBlocks/codeblocks.exe"')
        os.system(f'start chrome "https://frgp.cvg.utn.edu.ar/"')
        bool=True
    
    #FIN 
    elif texto in ["fin del programa"]:
        exit()
        
    return bool

def analizar(texto):
    texto = quitar_acentos(texto.lower())
    url = comandos.get(texto)
    
    if url is not None:
        os.system(f'start chrome "{url}"')
    else:
        activado=analizar2(texto)
        if activado == False:
            texto=texto.replace(" ","+")
            os.system(f"start https://www.google.com/search?q={texto}")
