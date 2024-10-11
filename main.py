
#test1

import os
import time
import random

import customtkinter
import tkinter as tk
from tkinter import font as tkFont

from PIL import Image, ImageTk
import requests
from io import BytesIO
import webbrowser
import psutil    


#src import
from src.get_user_info import getinfo





# ________ GET FONT ________

# def is_font_installed(font_name):
#     font_list = tkFont.families()  
#     return font_name in font_list

# def install_font(font_file):
#     user_font_dir = os.path.join(os.getenv("LOCALAPPDATA"), "Microsoft", "Windows", "Fonts")


#     destination_path = os.path.join(user_font_dir, os.path.basename(font_file))

#     shutil.copy(font_file, destination_path)

#     ctypes.windll.gdi32.AddFontResourceW(destination_path)
#     ctypes.windll.user32.SendMessageW(0xFFFF, 0x1D, 0, destination_path)  # refrech font cache




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

        self.title("")
        self.geometry("600x550")
        self.resizable("False", "False")


        # drag window
        drag_window(self)

        #self.attributes("-transparentcolor", 'black') # 'set all black color transparent


        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)


        #fonts
        user_id = os.getenv('USER_ID')
        user_name = os.getenv('AVATAR_NAME')
        avatar_id = os.getenv('AVATAR_ID')

        #self.avatar_image = self.display_avatar(f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}.png")

        
        
        # ________ IMAGES ________

        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "img")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "logo-transparent_Rcheat.png")), size=(55, 65))
        self.image_icon_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "image_icon_light.png")), size=(20, 20))
        self.changelog_image = customtkinter.CTkImage(dark_image=Image.open(os.path.join(image_path, "changelog.png")), size=(20, 20))
        self.chat_image = customtkinter.CTkImage(dark_image=Image.open(os.path.join(image_path, "chat_light.png")), size=(20, 20))
        self.play_image = customtkinter.CTkImage(dark_image=Image.open(os.path.join(image_path, "play.png")), size=(20, 20))
        self.profil_image = customtkinter.CTkImage(dark_image=Image.open(os.path.join(image_path, "profil.png")), size=(20, 20))
        self.transparent_image = customtkinter.CTkImage(dark_image=Image.open(os.path.join(image_path, "transp.png")), size=(180, 1))
        self.discord_image = customtkinter.CTkImage(dark_image=Image.open(os.path.join(image_path, "discord.png")), size=(20, 20))

        # ____ GAME IMAGES ____

        self.mw3_image = customtkinter.CTkImage(dark_image=Image.open(os.path.join(image_path, "mw3.png")), size=(20, 20))
        self.mw3_image_banner = customtkinter.CTkImage(dark_image=Image.open(os.path.join(image_path, "mw3_banner.png")), size=(160, 75))

        self.csgo_image = customtkinter.CTkImage(dark_image=Image.open(os.path.join(image_path, "csgo.png")), size=(20, 20))
        self.rocketleague_image = customtkinter.CTkImage(dark_image=Image.open(os.path.join(image_path, "rocketleague.png")), size=(20, 20))
        self.valorant_image = customtkinter.CTkImage(dark_image=Image.open(os.path.join(image_path, "valorant.png")), size=(20, 20))


        self.wm_iconbitmap("img\\icon_Rcheat.ico")


        # ________ FONTS ________

        desired_font = "Segoe UI"
        font_size_h4 = 17
        font_size_h3 = 22  
        font_size_h2 = 22  
        font_size_h1 = 27 

        my_font_h4 = customtkinter.CTkFont(family=desired_font, size=font_size_h4)
        my_font_h3 = customtkinter.CTkFont(family=desired_font, size=font_size_h3)
        my_font_h2 = customtkinter.CTkFont(family=desired_font, size=font_size_h2)
        my_font_h1 = customtkinter.CTkFont(family=desired_font, size=font_size_h1)



        # ________ COLORS ________


        # ____ COLORS 1 ____
        self.color_bg = "#0A0A14"
        self.color_side = "#041225"
        self.color_hover = "#05577B"
        self.color_button = "#2385D0"
        self.color_contour = "#092239"

        # # ____ COLORS 2 ____
        # self.color_bg = "#08080D"
        # self.color_side = "#030D1A"
        # self.color_hover = "#04334D"
        # self.color_button = "#1F6AA5"
        # self.color_contour = "#061925"

        # # ____ COLORS 3 ____
        # self.color_bg = "#1F1F1F"
        # self.color_side = "#1F1F1F"
        # self.color_hover = "#111111"
        # self.color_button = "#141414"
        # self.color_contour = "#141414"


        # ____ COLORS 4 (Vibrant Midnight) ____
        # self.color_bg = "#0C1E3D"        # Deep Blue Background
        # self.color_side = "#09223C"      # Slightly Lighter Side Panel
        # self.color_hover = "#1F5C91"     # Vibrant Hover Effect
        # self.color_button = "#237AB5"    # Bright Blue for Buttons
        # self.color_contour = "#0A3A60"   # Contour/Border color

        # ____ COLORS 5 (Sunset Glow) ____
        # self.color_bg = "#202020"        # Dark Gray Background
        # self.color_side = "#2E2E2E"      # Darker Side Panel
        # self.color_hover = "#FF5722"     # Bright Orange for Hover
        # self.color_button = "#FF8A50"    # Sunset Orange for Buttons
        # self.color_contour = "#F4511E"   # Reddish Border Color

        # # ____ COLORS 6 (Dark Forest) ____
        # self.color_bg = "#162B1F"        # Forest Green Background
        # self.color_side = "#0F2216"      # Darker Green for Side Panel
        # self.color_hover = "#2E7D32"     # Bright Green Hover Effect
        # self.color_button = "#388E3C"    # Light Green for Buttons
        # self.color_contour = "#1B5E20"   # Deep Green for Contour

        # self.color_bg = "#121212"        # Very Dark Grey/Black Background
        # self.color_side = "#1C1F26"      # Dark Navy Blue for Side Panel
        # self.color_hover = "#007ACC"     # Deeper Blue Hover Effect
        # self.color_button = "#00CFFF"    # Light Cyan/Blue for Buttons
        # self.color_contour = "#003E66"   # Deep Blue for Contour (matching dark blue in logo)




        self.config(background=self.color_bg)
    


        # ________ NAV ________

        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color=self.color_side, bg_color=self.color_bg, border_width=.7, border_color=self.color_contour)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew", pady=5, padx=5)
        self.navigation_frame.grid_rowconfigure(5, weight=1)



        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="", image=self.logo_image,
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=15)


        self.mw3_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=5, height=40, border_spacing=10, text="MW3", font=my_font_h4,
                                                   fg_color="transparent", text_color=("gray10", "gray90"), bg_color=self.color_side,
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




        self.navigation_bot_frame = customtkinter.CTkFrame(self.navigation_frame, corner_radius=0, fg_color=self.color_side)
        self.navigation_bot_frame.columnconfigure(2, weight=0)
        self.navigation_bot_frame.grid(row=6, column=0)

        self.profil_button = customtkinter.CTkButton(self.navigation_bot_frame, corner_radius=5, height=40, border_spacing=10, text="", fg_color="transparent", 
                                                      image=self.profil_image, width=20, command=self.profil_button_event)
        self.profil_button.grid(row=0, column=0, padx=10, pady=15, sticky="")


        self.discord_button = customtkinter.CTkButton(self.navigation_bot_frame, corner_radius=5, height=40, border_spacing=10, text="", fg_color="transparent", 
                                                      image=self.discord_image, width=20, command= lambda: self.open_link("https://discord.gg/x5bkv2eXam"))
        self.discord_button.grid(row=0, column=1, padx=10, pady=15, sticky="")        


        # self.discord_profil = customtkinter.CTkLabel(self.navigation_frame, image=self.avatar_image, text=user_name, compound="left", font=my_font_h4, text_color=("gray10", "gray90"))
        # self.discord_profil.grid(row=3, column=0, padx=10, sticky="ew")





        # ________ MW3 ________

        self.mw3_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color=self.color_bg)
        self.mw3_frame.grid(pady=5)


        # ____ mw3 top frame ____
        
        self.mw3_frame_top_frame = customtkinter.CTkFrame(self.mw3_frame, corner_radius=0, fg_color=self.color_bg, border_color=self.color_contour, border_width=.7)
        self.mw3_frame_top_frame.grid(row=0, column=0, sticky="nwe")

        self.mw3_frame_top_banner = customtkinter.CTkButton(self.mw3_frame_top_frame, image=self.mw3_image_banner, text="", fg_color="transparent", hover='false', width=370)
        self.mw3_frame_top_banner.grid(row=0, column=0, padx=20, pady=20, sticky="w")
        
        self.progressbar = customtkinter.CTkProgressBar(self.mw3_frame_top_frame, orientation='horizontal', mode="determinate", determinate_speed=.4)
        self.progressbar.place(relx=.5, rely=0.9, anchor="s")
        self.progressbar.set(0)
        
        

        
        # ____ mw3 mid frame 0____

        self.mw3_frame_mid_frame0 = customtkinter.CTkFrame(self.mw3_frame, corner_radius=0, fg_color=self.color_bg, border_color=self.color_contour, border_width=.7)     
        self.mw3_frame_mid_frame0.grid(row=1, column=0, sticky="new", pady=5)


        self.mw3_frame_mid_unlockall_label = customtkinter.CTkLabel(self.mw3_frame_mid_frame0, text="Unlock All", font=my_font_h4)
        self.mw3_frame_mid_unlockall_label.grid(row=0, column=0, padx=30, pady=10, sticky="w")

        self.mw3_frame_mid_unlockall_button = customtkinter.CTkButton(self.mw3_frame_mid_frame0, fg_color="transparent", border_color=self.color_button, border_width=1, corner_radius=5, text="", compound="left", font=my_font_h4, image=self.play_image, hover_color=self.color_hover, width=60, command=self.progressbar_event)
        self.mw3_frame_mid_unlockall_button.place(relx=.85,  rely =.5, anchor="center")



        # ____ mw3 mid frame 1____

        self.mw3_frame_mid_frame1 = customtkinter.CTkFrame(self.mw3_frame, corner_radius=0, fg_color=self.color_bg, border_color=self.color_contour, border_width=.7)   
        self.mw3_frame_mid_frame1.grid(row=2, column=0, sticky="new")


        self.mw3_frame_mid_legitcheat_label = customtkinter.CTkLabel(self.mw3_frame_mid_frame1, text="Legit Cheat", font=my_font_h4)
        self.mw3_frame_mid_legitcheat_label.grid(row=0, column=0, padx=30, pady=10, sticky="w")

        self.mw3_frame_mid_legitcheat_button = customtkinter.CTkButton(self.mw3_frame_mid_frame1, fg_color='transparent', border_color=self.color_button, border_width=1, corner_radius=5, text="", compound="left", font=my_font_h4, image=self.play_image, hover_color=self.color_hover, width=60, command=self.progressbar_event)
        self.mw3_frame_mid_legitcheat_button.place(relx=.85,  rely =.25, anchor="center")


        self.mw3_frame_mid_ragecheat_label = customtkinter.CTkLabel(self.mw3_frame_mid_frame1, text="Rage Cheat", font=my_font_h4)
        self.mw3_frame_mid_ragecheat_label.grid(row=1, column=0, padx=30, pady=10, sticky="w")

        self.mw3_frame_mid_ragecheat_button = customtkinter.CTkButton(self.mw3_frame_mid_frame1, fg_color='transparent', border_color=self.color_button, border_width=1, corner_radius=5, text="", compound="left", font=my_font_h4, image=self.play_image, hover_color=self.color_hover, width=60, command=self.progressbar_event)
        self.mw3_frame_mid_ragecheat_button.place(relx=.85,  rely =.75, anchor="center")



        # ____ mw3 mid frame 2____

        self.mw3_frame_mid_frame2 = customtkinter.CTkFrame(self.mw3_frame, corner_radius=0, fg_color=self.color_bg, border_color=self.color_contour, border_width=.7)
        self.mw3_frame_mid_frame2.grid_columnconfigure(1, minsize=180)
        self.mw3_frame_mid_frame2.grid(row=3, column=0, sticky="new", pady=5)


        self.mw3_frame_mid_ddos_label = customtkinter.CTkLabel(self.mw3_frame_mid_frame2, text="DDos Tool", font=my_font_h4)
        self.mw3_frame_mid_ddos_label.grid(row=0, column=0, padx=30, pady=10, sticky="w")

        self.mw3_frame_mid_ddos_button = customtkinter.CTkButton(self.mw3_frame_mid_frame2, fg_color='transparent', border_color=self.color_button, border_width=1, corner_radius=5, text="", compound="left", font=my_font_h4, image=self.play_image, hover_color=self.color_hover, width=60)
        self.mw3_frame_mid_ddos_button.place(relx=.85,  rely =.25, anchor="center")


        self.mw3_frame_mid_othertool_label = customtkinter.CTkLabel(self.mw3_frame_mid_frame2, text="Other Tools", font=my_font_h4)
        self.mw3_frame_mid_othertool_label.grid(row=1, column=0, padx=30, pady=10, sticky="w")

        self.mw3_frame_mid_othertool_button = customtkinter.CTkButton(self.mw3_frame_mid_frame2, fg_color='transparent', border_color=self.color_button, border_width=1, corner_radius=5, text="", compound="left", font=my_font_h4, image=self.play_image, hover_color=self.color_hover, width=60)
        self.mw3_frame_mid_othertool_button.place(relx=.85,  rely =.75, anchor="center")





        # ________ CSGO ________

        self.csgo_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")



        # ________ RL ________

        self.rocketleague_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")


        # ________ VALO ________

        self.valorant_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")



        # ________ LOG ________

        self.changelog_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")


        # ________ PROFIL ________

        self.profil_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color=self.color_bg)
        self.mw3_frame.grid_columnconfigure(0, weight=0)
        self.mw3_frame.grid(pady=5)

        self.profil_frame_time_label = customtkinter.CTkLabel(self.profil_frame, text='test', width=40, height=28, fg_color='transparent')
        self.profil_frame_time_label.place(x=10, y=10)
        self.profil_frame_version_label = customtkinter.CTkLabel(self.profil_frame, text='test', width=40, height=28, fg_color='transparent')
        self.profil_frame_version_label.place(x=10, y=30)

        self.profil_frame_userinfo_label = customtkinter.CTkLabel(self.profil_frame, text='test', width=40, height=28, fg_color='transparent')
        self.profil_frame_userinfo_label.place(x=10, y=50)
 
        self.profil_frame_pcinfo_label = customtkinter.CTkLabel(self.profil_frame, text='test', width=40, height=28, fg_color='transparent')
        self.profil_frame_pcinfo_label.place(x=10, y=70)
 
        self.profil_frame_cpuinfo_label = customtkinter.CTkLabel(self.profil_frame, text='test', width=40, height=28, fg_color='transparent')
        self.profil_frame_cpuinfo_label.place(x=10, y=90)

        self.profil_frame_gpuinfo_label = customtkinter.CTkLabel(self.profil_frame, text='test', width=40, height=28, fg_color='transparent')
        self.profil_frame_gpuinfo_label.place(x=10, y=110)

        # select default frame
        self.select_frame_by_name("mw3")
        self.user_info()


 


    def select_frame_by_name(self, name):
        # selected tab
        if name == "mw3":
            self.mw3_button.configure(fg_color=self.color_hover,  hover_color=(self.color_hover))
            self.mw3_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.mw3_button.configure(fg_color="transparent",  hover_color=(self.color_side),)
            self.mw3_frame.grid_forget()


        if name == "csgo":
            self.csgo_button.configure(fg_color=self.color_hover,  hover_color=(self.color_hover))
            self.csgo_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.csgo_button.configure(fg_color="transparent",  hover_color=(self.color_side),)
            self.csgo_frame.grid_forget()


        if name == "rocketleague":
            self.rocketleague_button.configure(fg_color=self.color_hover,  hover_color=(self.color_hover))
            self.rocketleague_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.rocketleague_button.configure(fg_color="transparent",  hover_color=(self.color_side),)
            self.rocketleague_frame.grid_forget()


        if name == "valorant":
            self.valorant_button.configure(fg_color=self.color_hover,  hover_color=(self.color_hover))
            self.valorant_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.valorant_button.configure(fg_color="transparent",  hover_color=(self.color_side),)
            self.valorant_frame.grid_forget()


        if name == "changelog":
            self.changelog_button.configure(fg_color=self.color_hover,  hover_color=(self.color_hover))
            self.changelog_frame.grid(row=0, column=1, sticky="nsew")

        else:
            self.changelog_button.configure(fg_color="transparent",  hover_color=(self.color_side),)
            self.changelog_frame.grid_forget()


        if name == "profil":
            self.profil_button.configure(fg_color=self.color_hover,  hover_color=(self.color_hover))
            self.profil_frame.grid(row=0, column=1, sticky="nsew")

        else:
            self.profil_button.configure(fg_color="transparent")
            self.profil_frame.grid_forget()



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


    def profil_button_event(self):
        self.select_frame_by_name("profil")



    def display_avatar(self, url):
        response = requests.get(url)
        img_data = response.content

        img = Image.open(BytesIO(img_data))
        imaggge = customtkinter.CTkImage(dark_image=Image.open(BytesIO(img_data)), size=(26, 26))
        return imaggge

    
    def open_link(self, url):
        webbrowser.open(url)



    # ___________ CHEAT BUTTONS EVENT ___________

    def progressbar_event(self):
        rdm = random.randint(0, 10)
        if rdm == 1:
            self.progressbar.step()
        if self.progressbar.get() > 0.99:
            self.progressbar.set(0)
        else:
            self.after(10, self.progressbar_event)




    def user_info(self):
        self.user_name, self.user_login, self.user_ip, self.user_HOSTNAME, self.user_operating_system, self.user_cpu, self.user_gpu, self.current_location, self.current_time, self.current_version = getinfo()
        self.profil_frame_time_label.configure(text="current time = " + self.current_time)
        self.profil_frame_version_label.configure(text="current version = " + self.current_version)
        self.profil_frame_userinfo_label.configure(text='User name:' + self.user_name + '   login:' + self.user_login + '   HOSTNAME:' + self.user_HOSTNAME)
        self.profil_frame_pcinfo_label.configure(text='ip :' + self.user_ip + ' OS:' + self.user_operating_system)
        self.profil_frame_cpuinfo_label.configure(text='CPU:' + self.user_cpu)
        self.profil_frame_gpuinfo_label.configure(text='GPU:' + self.user_gpu)

        
        self.after(10000, self.user_info)




if __name__ == "__main__":
    app = App()
    app.mainloop()
