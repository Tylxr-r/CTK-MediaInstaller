import tkinter
import customtkinter
import yt_dlp
import os

outputPath = os.path.join(os.path.expanduser('~'), 'Desktop')

# yt_dlp Download
def startDownload():
    try:
        ytLink = link.get().strip()
        selectedOption = OM.get()

        if selectedOption == 'Youtube Music':
            opts = {'outtmpl': f'{outputPath}/%(title)s.%(ext)s', 'format': 'bestaudio/best', 'extractaudio': True, 'audioformat': 'mp3',}
        elif selectedOption == 'Youtube':
            opts = {'outtmpl': f'{outputPath}/%(title)s.%(ext)s'}
        elif selectedOption == 'Instagram':
            opts = {'format': 'best', 'outtmpl': f'{outputPath}/%(title)s.%(ext)s'}
        elif selectedOption == 'TikTok':
            opts = {'format': 'best[vcodec^=avc]/best [vcodec^=h264]/best', 'outtmpl': f'{outputPath}/%(title)s.%(ext)s'}

        with yt_dlp.YoutubeDL(opts) as ydl:
            ydl.download([ytLink])

    except Exception as e:
        finishlabel.configure(text=f'{e}', text_color='red')

    else:
        finishlabel.configure(text='Download Complete', text_color='green')

# System Settings
customtkinter.set_appearance_mode('System')
customtkinter.set_default_color_theme("dark-blue")

# App Frame
app = customtkinter.CTk()
app.geometry('450x350')
app.title('Media Tool')

# UI
title = customtkinter.CTkLabel(app, text='Insert Link')
title.pack(padx=10, pady=10)

# Link Input
url = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url)
link.pack()

# Downloading
finishlabel = customtkinter.CTkLabel(app, text='')
finishlabel.pack()

# Download Button
download = customtkinter.CTkButton(app, text='Download', command=startDownload, width=155)
download.pack(padx=10, pady=10)

# Option Menu
options = ['Youtube Music', 'Youtube', 'Instagram', 'TikTok']
OM = customtkinter.CTkOptionMenu(app, values=options, width=155)
OM.pack(padx=10, pady=10)

# Run App
app.mainloop()
