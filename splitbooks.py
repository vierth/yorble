import re

def splitdocument(title, regex, genre):
    with open(title, "r") as rf:
        sections = regex.split(rf.read())[1:]
        for i, section in enumerate(sections):
            if len(section) > 100:
                with open(f"chapterwise/{title[:-4]}_{str(i + 1)}_{genre}.txt","w") as wf:
                    if "*** END OF THIS" in section:
                        section = section[:section.find("*** END OF THIS")]
                    wf.write(section.strip())

def divlength(title, sections, genre):
    with open(title, "r") as rf:
        text = rf.read()
        length = len(text)
        sectionlength = length//sections
        for i in range(sections):
            with open(f"chapterwise/{title[:-4]}_{str(i+1)}_{genre}", "w") as wf:
                if i < sections-1:
                    wf.write(text[i*sectionlength:(i+1)*sectionlength])
                else:
                    wf.write(text[i*sectionlength:])


splitdocument("austen_northangerabbey.txt", re.compile(r'CHAPTER \d+'), "g")
splitdocument("christie_secretadversary.txt", re.compile(r"CHAPTER [IVX]+"), "d")
splitdocument("christie_styles.txt", re.compile(r"CHAPTER [IVX]+"), "d")
splitdocument("collins_hauntedhotel.txt", re.compile(r"CHAPTER [IVX]+"), "u")
splitdocument("collins_moonstone.txt", re.compile(r"CHAPTER [IVX]+"), "d")
splitdocument("dickens_christmascarole.txt", re.compile(r"STAVE [IVX]+"), "g")
splitdocument("doyle_adventures.txt",re.compile(r"ADVENTURE [IVX]+"), "d")
splitdocument("doyle_baskervilles.txt", re.compile(r"Chapter \d+"), "u")
splitdocument("doyle_scarlet.txt", re.compile(r"CHAPTER [IVX]+"), "d")
splitdocument("doyle_signoffour.txt", re.compile(r"Chapter [IVX]+"), "d")
splitdocument("lewis_monk.txt", re.compile(r"CHAPTER [IVX]"), "g")
splitdocument("radcliffe_udolpho.txt", re.compile(r"CHAPTER [IVX]"), "g")
splitdocument("lewis_monk.txt", re.compile(r"CHAPTER [IVX]"), "g")
divlength("reeve_oldenglishbaron.txt", 10, 'g')
splitdocument("shelley_frankenstein.txt",re.compile(r"Letter \d+|Chapter \d+"), "g")
splitdocument("stoker_dracula.txt", re.compile(r"CHAPTER [IVX]"), "g")
splitdocument("walpole_castleofotranto.txt", re.compile(r"CHAPTER [IVX]"), "g")
with open("poe_1.txt", "r") as rf:
    text = rf.read()
    rue = text[text.find("THE MURDERS IN THE RUE MORGUE"): text.find("THE MYSTERY OF MARIE ROGET")].strip()
    with open("chapterwise/poe_ruemorgue_1_d.txt","w") as wf:
        wf.write(rue)
    marie = text[text.find("THE MYSTERY OF MARIE"): text.find("THE BALLOON")].strip()
    with open("chapterwise/poe_marieroget_1_d.txt","w") as wf:
        wf.write(marie)
    
with open("poe_2.txt", "r") as rf:
    text = rf.read()
    usher = text[text.find("FALL OF THE HOUSE OF USHER"): text.find("SILENCE")].strip()
    with open('chapterwise/poe_usher_1_g.txt', "w") as wf:
        wf.write(usher)
    reddeath = text[text.find("THE MASQUE"): text.find("THE CASK")].strip()
    with open('chapterwise/poe_reddeath_1_g.txt',"w") as wf:
        wf.write(reddeath)
    pit = text[text.find("THE PIT"): text.find("THE PREMATURE")].strip()
    with open('chapterwise/poe_pitandpendulum_1_g.txt', "w") as wf:
        wf.write(pit)