from tkinter import *
from tkinter import filedialog as fd
from tkinter.scrolledtext import ScrolledText
import pytesseract
from PIL import Image, ImageTk


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# ------------ Required variables -------------#
img_main = ""


# ------------ Creating Main Functions --------------#
def select_image():
    global img_main
    try:
        image_name = fd.askopenfilename(filetypes=[("jpeg", ".jpg .jpeg"),
                                                 ("png", ".png")])
        show_image(image_name)
        img_main = image_name

    except AttributeError:
        pass


def show_image(img_name):
    img = (Image.open(img_name))
    new_img = resize(img)
    panel.configure(image=new_img)
    panel.image = new_img


def resize(img):
    r_img = img.resize((700, 500))
    return ImageTk.PhotoImage(r_img)


def extract_text():
    final_text = pytesseract.image_to_string(img_main)
    text.insert("1.0", final_text)

# Creating a tkinter GUI


window = Tk()
window.title("Text Extraction from Image")
window.minsize(height=100, width=500)
window.config(padx=20, pady=20, bg="#000")

# --------------- Default Blank Photo ----------- #
blank_photo = Image.new(mode="RGBA", size=(700, 500), color="#242424")
image1 = ImageTk.PhotoImage(blank_photo)
panel = Label(window, image=image1)
panel.image = image1  # Keep a reference
panel.grid(column=0, rowspan=15)

# -------------- Image Selection Button --------------#

select_img = Button(text="Select Image", font=("Arial", 14), bg="#000", fg="#fafafa", command=select_image)
select_img.grid(column=0, row=17, pady=20)

# -------------- Text Widget to insert the extracted Text -----------#

text = ScrolledText(width=80, height=20, bg="#242424", fg="#fafafa")
text.grid(column=2, row=8, padx=20)

# --------------Text Extraction Button --------------#
text_btn = Button(text="Extract Text", font=("Arial", 14), bg="#000", fg="#fafafa", command=extract_text)
text_btn.grid(column=2, row=17, pady=20)
window.mainloop()

