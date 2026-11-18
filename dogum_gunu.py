import time
import tkinter as tk


class BirthdayArcheryApp:

  def __init__(self, root):
    self.root = root
    self.root.title("Ok Atışı ve Sürpriz Pasta")
    self.canvas = tk.Canvas(root, width=600, height=600, bg="#1a1a1a")
    self.canvas.pack()

    self.state = "shoot"  # 'shoot', 'animating', 'cake'

    self.draw_start_scene()
    self.canvas.bind("<Button-1>", self.on_click)

  def draw_start_scene(self):
    self.canvas.delete("all")
    # Hedef tahtası
    self.canvas.create_oval(
        225, 75, 375, 225, fill="white", outline="black", width=2
    )
    self.canvas.create_oval(
        250, 100, 350, 200, fill="blue", outline="black", width=2
    )
    self.canvas.create_oval(
        275, 125, 325, 175, fill="red", outline="black", width=2
    )
    self.canvas.create_oval(290, 140, 310, 160, fill="yellow", outline="")

    # Ok (başlangıç pozisyonu)
    self.arrow_id = self.canvas.create_line(
        300, 500, 300, 550, fill="silver", width=4, arrow=tk.LAST
    )

    self.canvas.create_text(
        300, 570, text="Ateş etmek için ekrana tıkla", fill="white", font=("Arial", 12)
    )

  def on_click(self, event):
    if self.state == "shoot":
      self.state = "animating"
      self.animate_arrow()

  def animate_arrow(self):
    # Okun hedefe doğru hareketi
    y = 500
    while y > 150:
      y -= 25
      self.canvas.coords(self.arrow_id, 300, y, 300, y + 50)
      self.root.update()
      time.sleep(0.02)

    # Hedefe varınca pasta sahnesine geç
    self.state = "cake"
    self.draw_cake_scene()

  def draw_cake_scene(self):
    self.canvas.delete("all")

    # Kutlama metni
    self.canvas.create_text(
        300, 70, text="İYİ Kİ DOĞDUN ARYA", fill="#ffcc00", font=("Arial", 22, "bold")
    )

    # Pasta alt katı
    self.canvas.create_rectangle(
        200, 350, 400, 450, fill="#ff69b4", outline="#ff1493", width=3
    )
    # Pasta üst katı
    self.canvas.create_rectangle(
        230, 270, 370, 350, fill="#ffb6c1", outline="#ff1493", width=
