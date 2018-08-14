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
        #byt=byt.decode("UTF-8")#PASAR CODIFICACION EN BYTES A STRING
        de64works=True;de32works=True;de16works=True
        try:
            de64=base64.b64decode(byt)
        except:
            de64works=False
        try:
            de32=base64.b32decode(byt)
        except:
            de32works=False
        try:
            de16=base64.b16decode(byt)
        except:
            de16works=False
            print("B64")
        #except:
            #print("ERROR: No se pudo llevar a cabo la decodificación con los datos introducidos")
                #except:
                    #print("ERROR: No se pudo llevar a cabo la decodificación con los datos introducidos")
                    #continue
        if opc=="A":
            if de64works==True:
                print("Decodificación Base64: ",de64)
            if de32works==True:
                print("Decodificación Base32: ",de32)
            if de16works==True:
                print("Decodificación Base16: ",de16)
        else:
            try:
                bs=de.decode("UTF-8")
                print(bs)
            except:
                print("No se pudo completar la operación")
            
        
    conti=ns(input("¿Desea continuar?: "))
    if conti=="n":
        break
    subprocess.call(["cmd.exe","/C","cls"])

