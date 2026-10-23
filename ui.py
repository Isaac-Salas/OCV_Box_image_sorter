# Designed with https://visualtkinter.com - paste this file into File > Import there to edit it visually
# Requires CustomTkinter:  pip install customtkinter
import customtkinter as ctk
import tkinter as tk


THEME_BG = "#2b2b2b"
THEME_FG = "#e8e8e8"
THEME_ACCENT = "#4a9eff"
THEME_ACCENT_FG = "#ffffff"
THEME_FIELD_BG = "#3c3c3c"
THEME_FONT_FAMILY = "Segoe UI"
THEME_FONT_SIZE = 10


def apply_theme(root):
    """Apply the project theme to a window. CustomTkinter styles per widget,
    so the widgets themselves carry the rest of the colours."""
    root.configure(fg_color=THEME_BG)


class Application:
    def __init__(self, root):
        self.root = root
        root.title("Test")
        root.geometry("600x400")
        apply_theme(root)

        self.Base = ctk.CTkFrame(root, fg_color="#50514F", border_width=2, width=450, height=360)
        self.Base.grid(row=0, column=0, sticky="nsew", padx=4, pady=4)

        self.frame9 = ctk.CTkFrame(self.Base, fg_color="#70C1B3", border_width=2, width=315, height=135)
        self.frame9.grid(row=0, column=0, sticky="nsew", padx=4, pady=4)

        self.label5 = ctk.CTkLabel(self.frame9, text="TESTING THE APPLICATION", font=ctk.CTkFont(family="Helvetica", size=20, weight="bold"), text_color=THEME_FG, width=225, height=75)
        self.label5.grid(row=0, column=0, sticky="w", padx=4, pady=4)

        self.frame10 = ctk.CTkFrame(self.Base, fg_color="#247BA0", border_width=2, width=315, height=135)
        self.frame10.grid(row=1, column=0, sticky="nsew", padx=4, pady=4)

        self.button10 = ctk.CTkButton(self.frame10, text="Test it!", command=self.on_button10, fg_color="#F25F5C", font=ctk.CTkFont(family="Helvetica", size=13, weight="bold"), text_color=THEME_ACCENT_FG, width=96, height=32)
        self.button10.grid(row=0, column=0, sticky="w", padx=4, pady=4)

        root.columnconfigure(0, minsize=458, weight=1)
        root.rowconfigure(0, minsize=368, weight=1)
        self.Base.columnconfigure(0, minsize=323, weight=1)
        self.Base.rowconfigure(0, minsize=143, weight=1)
        self.Base.rowconfigure(1, minsize=143, weight=1)
        self.frame9.columnconfigure(0, minsize=233)
        self.frame9.rowconfigure(0, minsize=83)
        self.frame10.columnconfigure(0, minsize=104)
        self.frame10.rowconfigure(0, minsize=40)

    def on_button10(self):
        pass


if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    root = ctk.CTk()
    app = Application(root)
    root.mainloop()
