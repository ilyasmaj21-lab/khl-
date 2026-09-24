import tkinter as tk


def main() -> None:
    """Create the application view."""
    window = tk.Tk()
    window.title("Greeting")
    tk.Label(window, text="Ilyas").pack()
    window.mainloop()


if __name__ == "__main__":
    main()
