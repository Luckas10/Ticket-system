
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"./Images")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class Screen_Login:
    def __init__(self):
        self.window = Tk()

        self.window.geometry("1000x650")
        self.window.configure(bg = "#F9AAD0")
        self.window.title("Ticket System - TODOS OS INGRESSOS VENDIDOS, SÃO PARA O DIA DA COMPRA!")


        self.canvas = Canvas(
            self.window,
            bg = "#F9AAD0",
            height = 650,
            width = 1000,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        self.image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            707.0,
            325.0,
            image=self.image_image_1
        )

        self.canvas.create_rectangle(
            0.0,
            0.0,
            415.0,
            650.0,
            fill="#AD53A6",
            outline="")

        self.button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        self.button_1.place(
            x=99.0,
            y=528.0,
            width=216.0,
            height=44.0
        )

        self.entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            207.0,
            342.0,
            image=self.entry_image_1
        )
        self.entry_1 = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_1.place(
            x=71.0,
            y=320.0,
            width=272.0,
            height=42.0
        )

        self.canvas.create_text(
            130.0,
            286.0,
            anchor="nw",
            text="Insira seu nome:",
            fill="#FFFFFF",
            font=("Inter", 20 * -1)
        )

        self.canvas.create_text(
            154.0,
            99.0,
            anchor="nw",
            text="Bem vindo!",
            fill="#FFFFFF",
            font=("Inter", 20 * -1)
        )

        self.canvas.create_text(
            123.0,
            49.0,
            anchor="nw",
            text="Ticket System.",
            fill="#FFFFFF",
            font=("Inter", 29 * -1)
        )

        self.image_image_2 = PhotoImage(
            file=relative_to_assets("image_2.png"))
        self.image_2 = self.canvas.create_image(
            86.0,
            66.0,
            image=self.image_image_2
        )
        self.window.resizable(False, False)

