from bs4 import BeautifulSoup
from requests import get
import requests
import textwrap
from tkinter import *
from PIL import ImageTk, Image


def cat_clean_print(inp):
    return_value = ""
    if type(inp) != str:
        for string in inp:
            return_value += string + " "
        to_print = textwrap.wrap(" ".join(return_value.split()), 180)
        to_return = ""
        for item in to_print:
            to_return += item + "\n"
        return to_return
    else:
        return " ".join(inp.split())


if __name__ == "__main__":
    URL = "https://apod.nasa.gov/apod/"
    page_html = get(URL).text
    page = BeautifulSoup(page_html, features="html.parser")
    info = page.find(bgcolor="#F4F4FF").text.splitlines()
    res = [line for line in info if any(c.isalpha() for c in line)]
    begin = res[0]
    begin_2 = res[1:4]
    date = res[4]
    title = res[5]
    for i in range(len(res)):
        if "Explanation:" in res[i]:
            img_credit = res[6:i]
            exp_start = i
        if "Tomorrow's picture:" in res[i]:
            exp = res[exp_start:i]
            short_stop = res[i]
            rest = res[i+1:]

    a_things = page.find_all("a")
    urls = [img['href'] for img in a_things]

    for url in urls:
        filename = re.search(r'/([\w_-]+[.](jpg|gif|png))$', url)
        if not filename:
            continue
        with open(filename.group(1), 'wb') as f:
            if 'http' not in url:
                url = '{}{}'.format(URL, url)
            response = requests.get(url)
            f.write(response.content)

    root = Tk()
    root.title("APOD webbot")
    root.iconbitmap("APOD.ico")

    def open():
        global my_img
        top = Toplevel()
        my_img = ImageTk.PhotoImage(Image.open("tadpole_HubbleBiju_3852.jpg"))
        testLabel = Label(top, image=my_img)
        testLabel.pack()

    myLabel1 = Label(root, text=cat_clean_print(begin)).pack()
    myLabel2 = Label(root, text=cat_clean_print(begin_2)).pack()
    myLabel3 = Label(root, text=cat_clean_print(date)).pack()
    myLabel4 = Label(root, text=cat_clean_print(title)).pack()
    myLabel5 = Label(root, text=cat_clean_print(img_credit)).pack()
    btn = Button(root, text="Click to show image in new window", command=open).pack()
    myLabel6 = Label(root, text=cat_clean_print(exp)).pack()
    myLabel7 = Label(root, text=cat_clean_print(short_stop)).pack()
    myLabel8 = Label(root, text=cat_clean_print(rest)).pack()

    root.mainloop()
