#this file is used to read the options file and all language files
def deleteLastCharacter(lang):
    #deletes last character of all items in a list
    #corrects weird characters
    print("\n"*100)
    a=0
    while a != len(lang):
        b=""
        a1=0
        while a1 != len(lang[a])-1:
            if lang[a][a1] == "Ã" and lang[a][a1+1] == "¡":
                b+="á"
                a1+=1
            elif lang[a][a1] == "Ã" and lang[a][a1+1] == "©":
                b+="é"
                a1+=1
            elif lang[a][a1] == "Ã" and lang[a][a1+1] == "­":
                b+="í"
                a1+=1
            elif lang[a][a1] == "Ã" and lang[a][a1+1] == "³":
                b+="ó"
                a1+=1
            elif lang[a][a1] == "Ã" and lang[a][a1+1] == "º":
                b+="ú"
                a1+=1
            elif lang[a][a1] == "Ã" and lang[a][a1+1] == "£":
                b+="ã"
                a1+=1
            elif lang[a][a1] == "Ã" and lang[a][a1+1] == "µ":
                b+="õ"
                a1+=1
            elif lang[a][a1] == "Ã" and lang[a][a1+1] == "ª":
                b+="ê"
                a1+=1
            elif lang[a][a1] == "Ã" and lang[a][a1+1] == "§":
                b+="ç"
                a1+=1
            elif lang[a][a1] == "Ã" and lang[a][a1+1] == "±":
                b+="ñ"
                a1+=1
            elif lang[a][a1] == "Â" and lang[a][a1+1] == "¿":
                b+="¿"
                a1+=1
            elif lang[a][a1] == "Â" and lang[a][a1+1] == "¡":
                b+="¡"
                a1+=1
            else:
                b+=lang[a][a1]
            a1+=1
        lang[a]=b
        a+=1
    a=0
    return lang
def readFiles():
    #main function
    #reads the options file and all language files and returns its contents
    file=open("languages/English.txt", "r")
    english=deleteLastCharacter(file.readlines())
    file.close
    file=open("languages/Portuguese.txt", "r")
    portuguese=deleteLastCharacter(file.readlines())
    file.close
    file=open("languages/Spanish.txt", "r")
    spanish=deleteLastCharacter(file.readlines())
    file.close
    file=open("options.txt", "r")
    options=deleteLastCharacter(deleteLastCharacter(file.readlines()))
    file.close
    a=0
    while a != len(options):
        b=""
        on=0
        a1=0
        while a1 != len(options[a]):
            if on == 1:
                b+=options[a][a1]
            if options[a][a1] == "'":
                on=1
            a1+=1
        options[a]=b
        a+=1
    return options[0], options[1], options[2], english, portuguese, spanish