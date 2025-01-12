import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from PIL import Image, ImageTk
import pandas as pd
import random
import os


# Fonction pour mélanger les données d'un fichier TXT
def shuffle_txt(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    random.shuffle(lines)
    shuffled_file = os.path.splitext(file_path)[0] + "_melange.txt"
    with open(shuffled_file, 'w') as file:
        file.writelines(lines)
    return shuffled_file


# Fonction pour mélanger les données d'un fichier Excel
def shuffle_excel(file_path):
    df = pd.read_excel(file_path)
    shuffled_df = df.sample(frac=1).reset_index(drop=True)
    shuffled_file = os.path.splitext(file_path)[0] + "_melange.xlsx"
    shuffled_df.to_excel(shuffled_file, index=False)
    return shuffled_file


# Fonction pour traiter le fichier
def process_file():
    file_path = filedialog.askopenfilename(
        title="Sélectionnez un fichier",
        filetypes=[("Fichiers texte", "*.txt"), ("Fichiers Excel", "*.xlsx")]
    )
    if not file_path:
        return

    try:
        if file_path.endswith('.txt'):
            shuffled_file = shuffle_txt(file_path)
        elif file_path.endswith('.xlsx'):
            shuffled_file = shuffle_excel(file_path)
        else:
            messagebox.showerror("Erreur", "Format de fichier non pris en charge.")
            return

        messagebox.showinfo("Succès", f"Les données ont été mélangées et enregistrées dans :\n{shuffled_file}")

    except Exception as e:
        messagebox.showerror("Erreur", f"Une erreur est survenue lors du traitement du fichier :\n{e}")


# Fonction pour créer un bouton avec un dégradé
def create_gradient_button(canvas, x, y, width, height, text, command, color1, color2):
    # Dessiner التدرج
    for i in range(height):
        r1, g1, b1 = canvas.winfo_rgb(color1)
        r2, g2, b2 = canvas.winfo_rgb(color2)
        ratio = i / height
        r = int(r1 * (1 - ratio) + r2 * ratio) >> 8
        g = int(g1 * (1 - ratio) + g2 * ratio) >> 8
        b = int(b1 * (1 - ratio) + b2 * ratio) >> 8
        color = f"#{r:02x}{g:02x}{b:02x}"
        canvas.create_line(x, y + i, x + width, y + i, fill=color)

    # إضافة النص
    button_text = canvas.create_text(
        x + width // 2, y + height // 2, text=text, font=("Arial", 12, "bold"), fill="white"
    )

    # إضافة حدث النقر
    canvas.tag_bind(button_text, "<Button-1>", lambda e: command())


# Interface utilisateur avec image de fond
def main():
    root = tk.Tk()
    root.title("Programme de Mélange de Données")
    root.geometry("600x400")

    # Charger l'image de fond
    bg_image = Image.open("wallpaperflare.com_wallpaper (20).jpg")  # ضع هنا اسم ملف الصورة الخلفية
    bg_image = bg_image.resize((600, 400), Image.Resampling.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_image)

    # Ajouter Canvas avec الخلفية
    canvas = tk.Canvas(root, width=600, height=400)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=bg_photo, anchor="nw")

    # Titre
    title_label = tk.Label(root, text="Programme de Mélange de Données", font=("Arial", 16, "bold"), bg="#000000",
                           fg="#FFFFFF")
    canvas.create_window(300, 50, window=title_label)

    # Ajouter الأزرار مع التدرج اللوني
    create_gradient_button(canvas, 200, 150, 200, 40, "Choisir un fichier", process_file, "#ff7f50", "#ff4500")
    create_gradient_button(canvas, 200, 220, 200, 40, "Quitter", root.quit, "#87CEEB", "#4682B4")

    # Pied de page
    footer_label = tk.Label(root, text="© 2025 - Développé par ABDELHAKIM AKAYOU", font=("Arial", 10), bg="#000000",
                            fg="#FFFFFF")
    canvas.create_window(300, 350, window=footer_label)

    root.mainloop()


if __name__ == "__main__":
    main()
