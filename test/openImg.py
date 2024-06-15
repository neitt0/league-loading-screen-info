from PIL import ImageTk, Image
import tkinter as tk
from tkinter import ttk
from urllib.request import Request, urlopen
import io

obj = {
  'viego': {
    '0': 'https://jungler.gg/wp-content/uploads/2024/02/Six_Camp_Jungle_Path_Raptor_Start_Blue_Side_JG_Clear_LoL_Guide.webp',
    '1': 'https://jungler.gg/wp-content/uploads/2024/02/Six_Camp_Jungle_Path_Raptor_Start_Red_Side_JG_Clear_LoL_Guide.webp'
  },
  'ekko': {
    '0': 'https://jungler.gg/wp-content/uploads/2024/02/Six_Camp_Jungle_Path_Raptor_Start_Blue_Side_JG_Clear_LoL_Guide.webp',
    '1': 'https://jungler.gg/wp-content/uploads/2024/02/Six_Camp_Jungle_Path_Raptor_Start_Red_Side_JG_Clear_LoL_Guide.webp'
  }
}


def display_image_from_url(obj):
  root = tk.Tk()

  imgArr = []

  for champion in obj:
    print()
    print(obj[champion])
    # scroll bar
    scrollbar = tk.Scrollbar(root)

    for link in obj[champion]:
      url = obj[champion][link]
      print(url)
      request = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
      raw_data = urlopen(request).read()


      image = Image.open(io.BytesIO(raw_data))
      photo = ImageTk.PhotoImage(image)
      imgArr.append(photo)

      # Create a label widget to display the image
      
      # label = tk.Label(root, image=photo)
      scrollbar.pack(side='right', fill='y')
      label = tk.Label(root, image=imgArr[-1]).pack()

  tk.mainloop()



display_image_from_url(obj)