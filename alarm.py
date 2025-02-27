from tkinter.ttk import *
from tkinter import *
from PIL import Image, ImageTk
from pygame import mixer
from datetime import datetime
from time import sleep
from threading import Thread

#couleur
bg_color = '#ffffff'
color1 = '#000000'
color2 = '#0000FF'

mixer.init()

window = Tk()
window.title("Alarm clock")
window.geometry('500x300')
window.configure(bg=bg_color)

#conteneur pour les fonctionalités
frame_haut = Frame(window, width=500, height=20, bg= color1)
frame_haut.grid(row=0, column=0)
frame_bas = Frame(window, width=500, height=300, bg=bg_color)
frame_bas.grid(row=1, column=0)

#ajout de l'image
img = Image.open('icons8-snooze-80.png')
img.resize((100,100))
img = ImageTk.PhotoImage(img)
app_image = Label(frame_bas,height=100, image=img, bg=bg_color)
app_image.place(x=10,  y=5)

label_name = Label(frame_bas, text="Alarme",height=1, font=('Ivy 18 bold'),bg= bg_color, fg= color1 )
label_heure = Label(frame_bas, text="Heure", height=1, font=('Ivy 10 bold'), bg=bg_color, fg= color1)
label_minutes = Label(frame_bas, text="Minutes", height=1, font=('Ivy 10 bold'), bg=bg_color, fg= color1)
label_secondes = Label(frame_bas, text="Secondes", height=1, font=('Ivy 10 bold'), bg=bg_color, fg= color1)
label_periode = Label(frame_bas, text="Periode", height=1, font=('Ivy 10 bold'), bg=bg_color, fg= color1)

label_name.place(x=125, y=30)
label_heure.place(x=125, y=60)
label_minutes.place(x=175, y=60)
label_secondes.place(x=240, y=60)
label_periode.place(x=290, y=60)

style = Style()
style.theme_use('clam')  # Utilisez un thème compatible avec la personnalisation
style.configure("TCombobox",background="white")

combobox_hour= Combobox(frame_bas, width=2)
combobox_hour['values']=('00','01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12')
combobox_hour.current(0)
combobox_hour.place(x=125, y=80)

combobox_minutes= Combobox(frame_bas, width=2)
combobox_minutes['values']=('00','01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59')
combobox_minutes.current(0)
combobox_minutes.place(x=175,y=80)

combobox_secondes= Combobox(frame_bas, width=2)
combobox_secondes['values']=('00','01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59')
combobox_secondes.current(0)
combobox_secondes.place(x=240, y=80)

combobox_periode= Combobox(frame_bas, width=2)
combobox_periode['values']=('AM', 'PM')
combobox_periode.current(0)
combobox_periode.place(x=290, y=80)

def activer_alarme():
    print('activer alarme', selecte.get())
    t = Thread(target= alarme)
    t.start()

def desactiver_alarm():
    print('desactiver alarme', selecte.get())
    mixer.music.stop()


def music_alarme():
    mixer.music.load('alarme.mp3')
    mixer.music.play()
    selecte.set(0)
    
def convertir_en_24h(heure, periode):
    
    if periode == 'PM' and heure != '12':
        return str(int(heure) + 12)
    elif periode == 'AM' and heure == '12':
        return '00'
    else:
        return heure  
    
def alarme():
    while True:
        #control = 1
        
        alarme_hour = combobox_hour.get()
        alarme_minute = combobox_minutes.get()
        alarme_sec = combobox_secondes.get()
        alarme_periode = combobox_periode.get()
        alarme_periode = combobox_periode.get().upper()        
        
        alarme_hour_24h = convertir_en_24h(alarme_hour, alarme_periode)
        
        now = datetime.now()
        heure = now.strftime("%H")
        minute = now.strftime("%M")
        seconde = now.strftime('%S')
        
        
        if alarme_hour_24h == heure and alarme_minute == minute and alarme_sec == seconde:
            window.after(0, music_alarme)  # Exécuter dans le thread principal
            break  # Arrêter la boucle après avoir déclenché l'alarme
        sleep(1)

selecte = IntVar()

bouton= Radiobutton(frame_bas, text="Activer",font=('Ivy 15 bold'),value= '1', bg=bg_color, fg=color1, command=activer_alarme, variable= selecte)
bouton.place(x=125, y=200)

bouton2= Radiobutton(frame_bas, text="Désactiver",font=('Ivy 15 bold'),value= '2', bg=bg_color, fg=color1, command=desactiver_alarm, variable=selecte)
bouton2.place(x=210, y=200)










window.mainloop()



