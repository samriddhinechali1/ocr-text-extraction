# Text Extraction App
The Text Extraction App is a python project that allows you to take in an image and extract the text within it. After the text has been extracted you can make use of that text by copying it directly. It uses Tkinter for the GUI layout, Pillow for opening the image and most importantly PyTesseract which is an Optical Character Recognition(OCR) tool for python.
## GUI Layout
The app's GUI layout is fairly simple with two buttons, one of which allows you to choose the image you want to use and the other to extract the text.

![Layout image](https://github.com/samriddhinechali1/ocr-text-extraction/assets/120707106/9d7bdbc1-abe8-45f3-a8ec-5bfc803abd02)
## Image File Selection
The 'Select Image' button opens a new window from where you can choose any of the jpeg, .jpg, .jpeg, png, .png files to load.

![select](https://github.com/samriddhinechali1/ocr-text-extraction/assets/120707106/31fd6b85-af04-40c1-8e1c-fc6bec034a50)
## Text Extraction
Once the image is loaded, you can extract the text by clicking on the 'Extract Text' button which will insert the extracted text inside the text widget.

![extract](https://github.com/samriddhinechali1/ocr-text-extraction/assets/120707106/1e5b4bab-6dfd-4cae-a078-a5de469245d4)
## Copy text
The extracted text can be copied by clicking on the text inside the text widget. The widget also has a scroll to ensure all of the text can be copied.
![copy](https://github.com/samriddhinechali1/ocr-text-extraction/assets/120707106/8de0fffd-d306-49eb-ba85-9eebde8bfcac)
## Dependencies
***
The Text Extraction App uses the following libraries:
* Tkinter
* Pillow
* PyTesseract

