#Same code, different methode
def get_text(sline):
    tuple_text=("is","where","are","how","when","who")
    capitalized=sline.capitalize()
    if sline.startswith(tuple_text):  
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)    
resuls=[]
while True:
    text_s=input("Say something: ")
    if text_s=="/end":
       break
    else:
        resuls.append(get_text(text_s))
print(" ".join(resuls))        