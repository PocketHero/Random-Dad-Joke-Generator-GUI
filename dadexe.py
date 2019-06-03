import tkinter as tk
import requests
import random

#Initializing main window and widgets
window = tk.Tk()
window.geometry("400x350")
window.resizable(height=False, width=False)
window.title("DadJoke 3000!")

label1 = tk.Label(text="Behold! Dad Jokes at your leisure!", font=("Helvetica", 16))
label1.grid(columnspan=5)
label2 = tk.Label(text="Enter your joke subject below:", font=("Helvetica", 12))
label2.grid(column=0, row=2)
subject = tk.Entry()
subject.grid(column=0, row=3)
initial = tk.Text(master=window, height=50, width=50)
initial.grid(column=0, row=12)

#dadjoke function

def dadjoke3000():
    url = "https://icanhazdadjoke.com/search"
    search = str(subject.get())
    response = requests.get(url, headers={"Accept": "application/json"}, params={"term": search})
    data = response.json()
    results = (data['results'])
    amount1 = (len(data['results']))
    amount2 = amount1 - 1
    if amount1 == 0:
        return f"I'm sorry, I have no jokes about {search}"
    elif search == "":
        return "Please enter a subject!"
    else:
        response1 = (results[random.randint(0, amount2)]["joke"])
        return (f"I have {amount1} jokes about {search}. Here's one: {response1}")

#Displaying the joke in the text field function
def jokedisplay():
    dadjokeresponse = dadjoke3000()
    response2 = tk.Text(master=window, wrap="word", height=15, width=50)
    response2.grid(column=0, row=5)
    response2.insert(tk.END, dadjokeresponse)

#Button widget
button1 = tk.Button(
    text="Get my damn dad joke!", font=("Helvetica"), fg="white", bg="red",
    command=jokedisplay
)

button1.grid(column=0, row=4)

#Window loop
window.mainloop()
