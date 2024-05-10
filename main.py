import tkinter as tk
from tkinter import ttk
import http.client
import json
conn = http.client.HTTPSConnection("api.collectapi.com")
headers = {
    'content-type': "application/json",
    'authorization': "apikey 6WEyKrGuQCj63I94abvqKE:0WBZKU4t2OrYOEeAHS5MR7"
    }



pencere = tk.Tk()
pencere.geometry("600x450")
pencere.title("Hoş Geldiniz!")
giris = tk.Entry(bg="white",fg="black", font="verdena 13")
giris.place(x=170, y=80,width=150,height=25)
conn = http.client.HTTPSConnection("api.collectapi.com")
headers = {
      'content-type': "application/json",
      'authorization': "apikey 6WEyKrGuQCj63I94abvqKE:0WBZKU4t2OrYOEeAHS5MR7"
       }

def get_data():
  bolge=giris.get()
  conn.request("GET", f"/weather/getWeather?data.lang=tr&data.city={bolge}", headers=headers)
  res = conn.getresponse()
  data = res.read()
  json_data = json.loads(data)
  city=json_data.get("city","")
  result = json_data.get("result","")
  date=result[0]["date"]
  day=result[0]["day"]
  description=result[0]["description"]
  degree=result[0]["degree"]
  humidity=result[0]["humidity"]
  label.config(text=f"{city} Hava Durumu: {date} {day} {description} {degree}C° %{humidity} ",font="verdena 11")
  print(result)
  
label= tk.Label(pencere, text="", font=('verdena 13'))
label.place(x=170,y=110,height=25)
ttk.Button(pencere, text="Görmek için tıkla", command=get_data).place(x=170,y=140,height=25,width=150)
pencere.mainloop()
