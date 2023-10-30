import tkinter as tk

symbole = ["7", "8", "9", "", "", "C", "4", "5", "6", "", "", "", "1", "2", "3", "-", "", "", "0", ",", "", "+"]
COLOR = "#f2f4f7"

def inicjalizacjaOkienka():
    root = tk.Tk()
    root.configure(bg=COLOR)
    root.geometry("470x430")
    root.title("Kalkulator")
    return root

def inicjalizacjaEkranu(root):
    ekran = [
        tk.Label(root, bg="#C0CBCB", width=55, anchor="w", borderwidth=2)
        for i in range(3)
    ]
    for i in range(len(ekran)):
        ekran[i].grid(row=i, columnspan=6, ipady=15, ipadx=1)
    return ekran

def inicjalizacjaPolaNaDane(root, ekran):
    pole_na_dane = tk.Entry(
        root, borderwidth=0, highlightcolor="white", highlightbackground="white"
    )
    pole_na_dane.grid(row=len(ekran), columnspan=6, ipadx=142, ipady=10)

    info = tk.Label(root, bg="white", width=55, anchor="w", borderwidth=2)
    info.grid(row=len(ekran) + 1, columnspan=6, ipady=15, ipadx=1)
    return pole_na_dane, info

def oblicz_wynik(tekst):
    try:
        wynik = str(eval(tekst))
        return wynik
    except:
        return "Błąd"

def oblicz(pole_na_dane, ekran, info):
    def f():
        tekst = pole_na_dane.get()
        wynik = oblicz_wynik(tekst)
        ekran[-1]["text"] = tekst
        info["text"] = wynik
    return f

def przycsikKlik(pole_na_dane, symbol):
    def f():
        if symbol == "C":
            pole_na_dane.delete(0, tk.END)
        elif symbol == "←":
            bufor = pole_na_dane.get()[:-1]
            pole_na_dane.delete(0, tk.END)
            pole_na_dane.insert(0, bufor)
        else:
            pole_na_dane.insert(tk.END, symbol)
    return f

def inicjalizacjaPrzyciskow(root, ekran, info):
    przyciski = [
        tk.Button(root, text=symbol, bg=COLOR, borderwidth=0) for symbol in symbole
    ]
    j = len(ekran) + 2
    for i in range(len(przyciski)):
        if i % 6 == 0:
            j += 1
        margin = 21 if len(symbole[i]) == 1 else 10
        przyciski[i].grid(row=j, column=i % 6, ipady=5, ipadx=margin)
        przyciski[i].configure(command=przycsikKlik(pole_na_dane, przyciski[i]["text"]))

    znak_rownosc = tk.Button(
        root,
        text="=",
        bg="#00BFFF",
        borderwidth=0,
        command=oblicz(pole_na_dane, ekran, info),
    )
    znak_rownosc.grid(row=len(ekran) + 6, column=4, columnspan=2, ipady=5, ipadx=50)

    return przyciski

if __name__ == "__main__":
    root = inicjalizacjaOkienka()
    ekran = inicjalizacjaEkranu(root)
    pole_na_dane, info = inicjalizacjaPolaNaDane(root, ekran)
    przyciski = inicjalizacjaPrzyciskow(root, ekran, info)
    root.mainloop()
