
import customtkinter as ctk

class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Test")
        self.geometry("800x600")
        self._build_ui()

    def _build_ui(self):
        self.label_2 = ctk.CTkLabel(
            self,
            width=336,
            corner_radius=0,
            border_width=0,
            border_color='#565b5e',
            padx=0,
            pady=0,
            cursor='',
            takefocus=False,
            fg_color='transparent',
            text='APP TEST',
            font_wrap=True,
            justify='center',
            text_color='#ffffff',
            text_color_disabled='#a0a0a0',
            compound='left',
            full_circle=True,
            unified_bind=True,
            font=ctk.CTkFont(size=50, weight="bold", slant="roman"),
        )
        self.label_2.place(x=232, y=67)

        self.Button = ctk.CTkButton(
            self,
            width=220,
            height=86,
            corner_radius=6,
            border_width=0,
            border_color='#efefef',
            text='Run that ass!',
            text_color='#ffffff',
            full_circle=True,
            fg_color='#6366f1',
            pressed_color='#4e50bd',
            font=ctk.CTkFont(size=21, weight="bold", slant="roman"),
        )
        self.Button.place(x=290, y=354)



if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    app = MainWindow()
    app.mainloop()
