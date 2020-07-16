print ("ciao, sono qui per calcolare il tuo voto probabile di laurea")
print ("se vuoi inserire un numero decimale puoi farlo. solo ricordati di usare il PUNTO e non la virgola")

x = 10
b = float(input ("inserisci la tua base di laurea: "))

if (b > 110):
    print ("input errato. terminare il programma e ricominciare")
    exit ()
if (b < 66):
    print ("input errato. terminare il programma e ricominciare")
    exit  ()

c = float(input ("inserisi il livello di cattiveria del tuo prof da 1 a 10: "))

if (c > x):
    print ("input errato. terminare il programma e ricominciare")
    exit  ()
if (c < 1):
    print ("input errato. terminare il programma e ricominciare")
    exit  ()

v = float(input("inserisci il valore stimato della tua tesi da 1 a 10: "))

if (v > x):
    print ("input errato. terminare il programma e ricominciare")
    exit  ()
if (v < 1):
    print ("input errato. terminare il programma e ricominciare")
    exit  ()

cc =(c/x)
#*7
vv = (v/x)
#*7

# cd = (cc/2)

r =((vv/cc)) * 7

rpond = (((vv*9)/(cc*1))/10)

rr1 =((rpond * 7)/10)
rr = rr1 * 4.285714285714286

print ("la tua tesi vale:")
print (rr)

k = b + rr

if (k > 110):
    print ("il tuo voto sarà 110 oppure 110 e lode, congratulazioni!")
    exit ()
    
print ("il tuo voto sarà:")
print (k)

#exit ()



# import random
# while 1 ==1
#    (random.randrange(66,110))
#    if (random.randrange(66,110)) > n
#        print (random.randrange(66,110))
        
