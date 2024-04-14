from PIL import ImageTk, Image
import tkinter as tk
from urllib.request import Request, urlopen
import io

def display_image_from_url(obj):
  root = tk.Tk()

  for champion in obj:
    print()
    print()
    print()
    print()
    print(champion)

    for link in obj[champion]:
      url = obj[champion][link]
      print(url)
      request = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
      raw_data = urlopen(request).read()

      image = Image.open(io.BytesIO(raw_data))
      photo = ImageTk.PhotoImage(image)

      # Create a label widget to display the image
      label = tk.Label(root, image=photo)
      label.pack()

  root.mainloop()