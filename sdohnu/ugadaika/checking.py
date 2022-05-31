import requests
import re

def check(painting, answer, id_style):
    ans = []
    if painting.name == answer:
        ans.append("верно")
    else:
        ans.append("неверно")
    return ans