


import os
import time

import customtkinter
import tkinter as tk
from tkinter import font as tkFont

from PIL import Image, ImageTk
import ctypes
import shutil
import requests
from io import BytesIO
import webbrowser



# ________ GET FONT ________

def is_font_installed(font_name):
    font_list = tkFont.families()  
    return font_name in font_list

def install_font(font_file):
    user_font_dir = os.path.join(os.getenv("LOCALAPPDATA"), "Microsoft", "Windows", "Fonts")


    destination_path = os.path.join(user_font_dir, os.path.basename(font_file))

    shutil.copy(font_file, destination_path)

    ctypes.windll.gdi32.AddFontResourceW(destination_path)
    ctypes.windll.user32.SendMessageW(0xFFFF, 0x1D, 0, destination_path)  # refrech font cache




# ________ DRAG WIN ________

def drag_window(widget):
    if isinstance(widget, customtkinter.CTk):  
        master = widget  
    else:
        master = widget.master

    x, y = 0, 0

    def mouse_motion(event):
        nonlocal x, y
       
        offset_x, offset_y = event.x - x, event.y - y
        new_x = master.winfo_x() + offset_x
        new_y = master.winfo_y() + offset_y
        new_geometry = f"+{new_x}+{new_y}"
        master.geometry(new_geometry)

    def mouse_press(event):
        nonlocal x, y
        x, y = event.x, event.y
        #master.wm_attributes("-alpha", "0.4" )


    #def mouse_release(event):
    #    master.wm_attributes("-alpha", "1" )

    widget.bind("<B1-Motion>", mouse_motion)  
    widget.bind("<Button-1>", mouse_press)  
    #widget.bind("<ButtonRelease-1>", mouse_release) 





class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Rcheat")
        self.geometry("600x550")

        # drag window
        drag_window(self)


        self.config(background='#000001')
        #self.attributes("-transparentcolor", 'black') # 'set all black color transparent


        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        #fonts
        my_font_h4 = customtkinter.CTkFont(family="<family name>", size=2)
        user_id = os.getenv('USER_ID')
        user_name = os.getenv('AVATAR_NAME')
        avatar_id = os.getenv('AVATAR_ID')

        #self.avatar_image = self.display_avatar(f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}.png")

        
        
        # ________ IMAGES ________

        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "img")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "logo-transparent_Rcheat.png")), size=(55, 65))
        self.large_test_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "large_test_image.png")), size=(500, 150))
        self.image_icon_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "image_icon_light.png")), size=(20, 20))
        self.changelog_image = customtkinter.CTkImage(dark_image=Image.open(os.path.join(image_path, "changelog.png")), size=(20, 20))
        self.chat_image = customtkinter.CTkImage(dark_image=Image.open(os.path.join(image_path, "chat_light.png")), size=(20, 20))
        self.play_image = customtkinter.CTkImage(dark_image=Image.open(os.path.join(image_path, "play.png")), size=(20, 20))
        self.add_user_image = customtkinter.CTkImage(dark_image=Image.open(os.path.join(image_path, "add_user_light.png")), size=(20, 20))
        self.transparent_image = customtkinter.CTkImage(dark_image=Image.open(os.path.join(image_path, "transp.png")), size=(400, 20))
        self.discord_image = customtkinter.CTkImage(dark_image=Image.open(os.path.join(image_path, "discord.png")), size=(20, 20))

        # ____ GAME IMAGES ____

        self.mw3_image = customtkinter.CTkImage(dark_image=Image.open(os.path.join(image_path, "mw3.png")), size=(20, 26))
        self.csgo_image = customtkinter.CTkImage(dark_image=Image.open(os.path.join(image_path, "csgo.png")), size=(20, 26))
        self.rocketleague_image = customtkinter.CTkImage(dark_image=Image.open(os.path.join(image_path, "rocketleague.png")), size=(20, 20))
        self.valorant_image = customtkinter.CTkImage(dark_image=Image.open(os.path.join(image_path, "valorant.png")), size=(20, 20))


        self.wm_iconbitmap("img\\icon_Rcheat.ico")


        # ________ FONTS ________

        desired_font = "Museo Sans Cyrl 900"
        font_size_h4 = 14  
        font_size_h3 = 18  
        font_size_h2 = 22  
        font_size_h1 = 27 

        if is_font_installed(desired_font):
            my_font_h4 = customtkinter.CTkFont(family=desired_font, size=font_size_h4)
            my_font_h3 = customtkinter.CTkFont(family=desired_font, size=font_size_h3)
            my_font_h2 = customtkinter.CTkFont(family=desired_font, size=font_size_h2)
            my_font_h1 = customtkinter.CTkFont(family=desired_font, size=font_size_h1)

            print("installed")
        else:
            install_font("src/font.ttf")  
            print("not installed")
            my_font_h4 = customtkinter.CTkFont(family=desired_font, size=font_size_h4)
            my_font_h3 = customtkinter.CTkFont(family=desired_font, size=font_size_h3)
            my_font_h2 = customtkinter.CTkFont(family=desired_font, size=font_size_h2)
            my_font_h1 = customtkinter.CTkFont(family=desired_font, size=font_size_h1)


        # ________ NAV ________

        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="#030D1A", bg_color="black", border_width=2, border_color="#061925")
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(5, weight=1)



        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="", image=self.logo_image,
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=10)


        self.mw3_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=5, height=40, border_spacing=10, text="MW3", font=my_font_h4,
                                                   fg_color="transparent", text_color=("gray10", "gray90"),
                                                   image=self.mw3_image, anchor="w", command=self.mw3_button_event)
        self.mw3_button.grid(row=1, column=0, padx=10, sticky="ew")


        self.csgo_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=5, height=40, border_spacing=10, text="CS:GO", font=my_font_h4,
                                                   fg_color="transparent", text_color=("gray10", "gray90"),
                                                   image=self.csgo_image, anchor="w", command=self.csgo_button_event)
        self.csgo_button.grid(row=2, column=0, padx=10, sticky="ew")


        self.rocketleague_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=5, height=40, border_spacing=10, text="RLEAGUE", font=my_font_h4,
                                                   fg_color="transparent", text_color=("gray10", "gray90"),
                                                   image=self.rocketleague_image, anchor="w", command=self.rocketleague_button_event)
        self.rocketleague_button.grid(row=3, column=0, padx=10, sticky="ew")        


        self.valorant_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=5, height=40, border_spacing=10, text="VALORANT", font=my_font_h4,
                                                   fg_color="transparent", text_color=("gray10", "gray90"),
                                                   image=self.valorant_image, anchor="w", command=self.valorant_button_event)
        self.valorant_button.grid(row=4, column=0, padx=10, sticky="ew")  




        self.changelog_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=5, height=40, border_spacing=10, text="Change Log", font=my_font_h4,
                                                      fg_color="transparent", text_color=("gray10", "gray90"), 
                                                      image=self.changelog_image, anchor="w", command=self.changelog_button_event)
        self.changelog_button.grid(row=5, column=0, padx=10, sticky="ews")



        self.discord_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=5, height=40, border_spacing=10, text="", font=my_font_h4,
                                                      fg_color="transparent", text_color=("gray10", "gray90"), 
                                                      image=self.discord_image, width=20, command= lambda: self.open_link("https://discord.gg/x5bkv2eXam"))
        self.discord_button.grid(row=6, column=0, padx=10, pady=20, sticky="s",)        


        # self.discord_profil = customtkinter.CTkLabel(self.navigation_frame, image=self.avatar_image, text=user_name, compound="left", font=my_font_h4, text_color=("gray10", "gray90"))
        # self.discord_profil.grid(row=3, column=0, padx=10, sticky="ew")





        # ________ MW3 ________

        self.mw3_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="#08080D")
        self.mw3_frame.grid_rowconfigure(0, weight=1)  # This will push the label to the bottom
        self.mw3_frame.grid_rowconfigure(1, weight=0)  # Label's row should not expand
        
        # ____ mw3 top frame ____
        self.mw3_frame_top_frame = customtkinter.CTkFrame(self.mw3_frame, corner_radius=0, fg_color="#08080D", border_color="#061925", border_width=2)
        self.mw3_frame_top_frame.grid_columnconfigure(0, weight=1)
        self.mw3_frame_top_frame.grid(row=0, column=0, sticky="new",)

        self.mw3_frame_top_label = customtkinter.CTkLabel(self.mw3_frame_top_frame, text="mw3", font=my_font_h3)
        self.mw3_frame_top_label.grid(row=0, column=0, padx=20, pady=30, sticky="w")
        
        # ____ mw3 mid frame ____
        #...

        # ____ mw3 bot frame ____
        self.mw3_frame_bot_frame = customtkinter.CTkFrame(self.mw3_frame, corner_radius=0, fg_color="#08080D")
        self.mw3_frame_bot_frame.grid_columnconfigure(0, weight=1)
        self.mw3_frame_bot_frame.grid(row=1, column=0, sticky="new",)

        self.mw3_frame_large_image_button = customtkinter.CTkButton(self.mw3_frame_bot_frame, text="Start", compound="left", font=my_font_h4, image=self.play_image, hover_color="#031221", height=40)
        self.mw3_frame_large_image_button.grid(row=1, column=0, padx=20, pady=10, sticky="s")

        self.mw3_frame_large_transp_image = customtkinter.CTkLabel(self.mw3_frame_bot_frame, text="", image=self.transparent_image)
        self.mw3_frame_large_transp_image.grid(row=2, column=0, padx=20, pady=10, sticky="s")




        # ________ CSGO ________

        self.csgo_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")



        # ________ RL ________

        self.rocketleague_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")


        # ________ VALO ________

        self.valorant_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")



        # ________ LOG ________

        self.changelog_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")



        # select default frame
        self.select_frame_by_name("mw3")





    def select_frame_by_name(self, name):
        # selected tab
        if name == "mw3":
            self.mw3_button.configure(fg_color="#04334D",  hover_color=("#04334D"))
            self.mw3_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.mw3_button.configure(fg_color="transparent",  hover_color=("#030D1A"),)
            self.mw3_frame.grid_forget()


        if name == "csgo":
            self.csgo_button.configure(fg_color="#04334D",  hover_color=("#04334D"))
            self.csgo_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.csgo_button.configure(fg_color="transparent",  hover_color=("#030D1A"),)
            self.csgo_frame.grid_forget()


        if name == "rocketleague":
            self.rocketleague_button.configure(fg_color="#04334D",  hover_color=("#04334D"))
            self.rocketleague_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.rocketleague_button.configure(fg_color="transparent",  hover_color=("#030D1A"),)
            self.rocketleague_frame.grid_forget()


        if name == "valorant":
            self.valorant_button.configure(fg_color="#04334D",  hover_color=("#04334D"))
            self.valorant_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.valorant_button.configure(fg_color="transparent",  hover_color=("#030D1A"),)
            self.valorant_frame.grid_forget()


        if name == "changelog":
            self.changelog_button.configure(fg_color="#04334D",  hover_color=("#04334D"))
            self.changelog_frame.grid(row=0, column=1, sticky="nsew")

        else:
            self.changelog_button.configure(fg_color="transparent",  hover_color=("#030D1A"),)
            self.changelog_frame.grid_forget()






    # navigation fct 
    def mw3_button_event(self):
        self.select_frame_by_name("mw3")


    def csgo_button_event(self):
        self.select_frame_by_name("csgo")
                                  

    def rocketleague_button_event(self):
        self.select_frame_by_name("rocketleague")   


    def valorant_button_event(self):
        self.select_frame_by_name("valorant")   


    def changelog_button_event(self):
        self.select_frame_by_name("changelog")





    def display_avatar(self, url):
        response = requests.get(url)
        img_data = response.content

        img = Image.open(BytesIO(img_data))
        imaggge = customtkinter.CTkImage(dark_image=Image.open(BytesIO(img_data)), size=(26, 26))
        return imaggge

    
    def open_link(self, url):
        webbrowser.open(url)

    

if __name__ == "__main__":
    app = App()
    app.mainloop()
