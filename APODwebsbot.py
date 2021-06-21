from bs4 import BeautifulSoup
from requests import get
import textwrap


def cat_clean_print(inp):
    return_value = ""
    if type(inp) != str:
        for string in inp:
            return_value += string + " "
        # 180 is full length
        to_print = textwrap.wrap(" ".join(return_value.split()), 180)
        for item in to_print:
            print(item)
    else:
        print(" ".join(inp.split()))


if __name__ == "__main__":
    URL = "https://apod.nasa.gov/apod/astropix.html"
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
    (cat_clean_print(begin))
    (cat_clean_print(begin_2))
    (cat_clean_print(date))
    (cat_clean_print(title))
    (cat_clean_print(img_credit))
    (cat_clean_print(exp))
    (cat_clean_print(short_stop))
    (cat_clean_print(rest))
