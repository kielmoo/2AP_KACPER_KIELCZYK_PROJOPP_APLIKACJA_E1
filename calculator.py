import tkinter as tk

symbole = ["7", "8", "9", "x", "C", " ", "4", "5", "6", "-", "1", "2", "3", "+", " ", " "]
COLOR = "white"


def window():
    root = tk.Tk()
    root.configure(bg=COLOR)
    root.geometry("410x410")
    root.title("Kalkulator")
    return root


def screen(root):
    ekran = [
        tk.Label(root, bg="#C0CBCB", width=66, anchor="w", borderwidth=2)
        for _ in range(3)
    ]
    for i in range(len(ekran)):
        ekran[i].grid(row=i, columnspan=6, ipady=15, ipadx=1)
    return ekran


def initialize_data(root, ekran):
    pole_na_dane = tk.Entry(
        root, borderwidth=0, highlightcolor="gray", highlightbackground="gray"
    )
    pole_na_dane.grid(row=len(ekran), columnspan=6, ipadx=142, ipady=10)

    info = tk.Label(root, bg="gray", width=66, anchor="w", borderwidth=2)
    info.grid(row=len(ekran) + 1, columnspan=6, ipady=15, ipadx=1)
    return pole_na_dane, info


def calculate_result(tekst):
    try:
        wynik = str(eval(tekst))
        return wynik
    except ZeroDivisionError:
        return "Nie można dzielić przez zero"
    except Exception as e:
        return f"Błąd: {e}"


def calculate(pole_na_dane, ekran, info):
    tekst = pole_na_dane.get()
    wynik = calculate_result(tekst)
    ekran[-1]["text"] = tekst
    info["text"] = wynik


def button_click(pole_na_dane, symbol):
    if symbol == "C":
        pole_na_dane.delete(0, tk.END)
    elif symbol == "←":
        bufor = pole_na_dane.get()[:-1]
        pole_na_dane.delete(0, tk.END)
        pole_na_dane.insert(0, bufor)
    else:
        pole_na_dane.insert(tk.END, symbol)


def initialize_button(root, ekran, pole_na_dane, info):
    przyciski = [
        tk.Button(root, text=symbol, bg=COLOR, borderwidth=0, command=lambda s=symbol: button_click(pole_na_dane, s))
        for symbol in symbole
    ]
    j = len(ekran) + 2
    for i in range(len(przyciski)):
        if i % 6 == 0:
            j += 1
        margin = 20 if len(symbole[i]) == 1 else 10
        przyciski[i].grid(row=j, column=i % 6, ipady=5, ipadx=margin)

    znak_rownosc = tk.Button(
        root,
        text="=",
        bg="#00BFFF",
        borderwidth=0,
        command=lambda: calculate(pole_na_dane, ekran, info),
    )
    znak_rownosc.grid(row=len(ekran) + 6, column=4, columnspan=2, ipady=5, ipadx=50)

    return przyciski


if __name__ == "__main__":
    root = window()
    ekran = screen(root)
    pole_na_dane, info = initialize_data(root, ekran)
    przyciski = initialize_button(root, ekran, pole_na_dane, info)
    root.mainloop()