from os.path import join
from os.path import exists


def maaned(md: str) -> str:
    md_lang = ""
    match md:
        case "Jan":
            md_lang = "januar"
        case "Feb":
            md_lang = "februar"
        case "Mar":
            md_lang = "marts"
        case "Apr":
            md_lang = "april"
        case "Maj":
            md_lang = "maj"
        case "Jun":
            md_lang = "juni"
        case "Jul":
            md_lang = "juli"
        case "Aug":
            md_lang = "august"
        case "Sep":
            md_lang = "september"
        case "Okt":
            md_lang = "oktober"
        case "Nov":
            md_lang = "november"
        case "Dec":
            md_lang = "december"
        case _:
            md_lang = "Fejl"

    return md_lang


def pdf_exist(filname):
    return exists(filname)
