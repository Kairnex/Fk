import os
from dotenv import load_dotenv

if os.path.exists(".env"):
    load_dotenv(".env")

def make_int(str_input):
    str_list = str_input.split(" ")
    int_list = []
    for x in str_list:
        int_list.append(int(x))
    return int_list

class Var:
    API_ID = int(os.getenv("API_ID", "18474511"))
    API_HASH = os.getenv("API_HASH", "a2b87c4925f27ec68b4f9bf2c0854311")
    BOT_TOKEN = os.getenv("7301244355:AAEe-96maAKDafRT3z4TKgAanVTCrjIBI9o")
    sudo = os.getenv("SUDO", "7639021876")
    SUDO = []
    if sudo:
        SUDO = make_int(sudo)
