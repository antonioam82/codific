import base64
import subprocess

def AB(op):
    while op!="A" and op!="B":
        op=input("Intoduzca \'A\' o \'B\' según su opción: ")
    return op
def ns(op):
    while op!="n" and op!="s":
        op=input("Intoduzca \'n\' o \'s\' según su opción: ")
    return op

while True:
    print("ESCOJA UNA OPCIÓN")
    print("A)Codificar texto a bytes: ")
    print("B)Decodificar bytes a texto: ")
    op=AB(input("Introduzca aquí su opción: "))

    print("¿COMO DESEA VER LA CODIFICACIÓN?")
    print("A)En Bytes")
    print("B)En string")
    opc=AB(input("Introduzca aquí su opción: "))
    if op=="A":
        text=input("Introduzca texto a traducir: ")
        b=text.encode("UTF-8")
        e=base64.b64encode(b)
        e32=base64.b32encode(b)
        e16=base64.b16encode(b)
        if opc=="A":
            print("Codificación Base64: ",e)
            print("Codificación Base32: ",e32)
            print("Codificación Base16: ",e16)
        else:
            s1=e.decode("UTF-8")
            s32=e32.decode("UTF-8")
            s16=e16.decode("UTF-8")
            print("Codificación Base64: ",s1)
            print("Codificación Base32: ",s32)
            print("Codificación Base16: ",s16)
    else:
        byt=input("Introduzca codificación: ")
        de=base64.b64decode(byt)
        if opc=="A":
            print(de)
        else:
            bs=de.decode("UTF-8")
            print(bs)
            
        
    conti=ns(input("¿Desea coontiuar?: "))
    if conti=="n":
        break
    subprocess.call(["cmd.exe","/C","cls"])



