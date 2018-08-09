# -*- coding: cp1251 -*-
#rot13 converter
print "Ласкаво просимо до Python ROT13\n\n"

alpha = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя "
#string = "Fraq hf gur pbqr lbh hfrq gb qrpbqr guvf zrffntr"
def rot13decoder():
    string = raw_input('Будь ласка, введіть повідомлення rot13 для декодування: \n')
    dic = {}
    count = 1
    for i in alpha:
        dic[i] = count
        count+=1
    
    message = ""
    for i in string:
        if i.lower() in dic:
            rot = int(dic[i.lower()]) - 13
            if rot == 14:
                message+=' '
            elif rot < 1:
                base = 32
                newrot = base + rot
                message+=dic.keys()[dic.values().index(newrot)]
            else:
                message+=dic.keys()[dic.values().index(rot)]
                
    print '\nПовідомлення розшифровано: \n'+message+'\n\nСподіваюся, що вам сподобалося!!'
    
def rot13encoder():
    string = raw_input('Будь-ласка, введіть повідомлення для кодування рот13: \n')
    dic = {}
    count = 1
    for i in alpha:
        dic[i] = count
        count+=1
    
    message = ""
    for i in string:
        if i.lower() in dic:
            rot = int(dic[i.lower()]) + 13
            if rot == 40:
                message+=' '
            elif rot > 32:
                rot = rot - 32
                base = 0
                newrot = base + rot
                message+=dic.keys()[dic.values().index(newrot)]
            else:
                message+=dic.keys()[dic.values().index(rot)]
                
    print '\nПовідомлення, закодоване на: \n'+message+'\n\nСподіваюся, що вам сподобалося'


endecode = raw_input('1) Введіть 1, щоб кодувати повідомлення\n2) Введіть 2 для розшифрування повідомлення\n')
while endecode != '1' or endecode != '2':
    if endecode == '1':
        rot13encoder()
        break
    elif endecode == '2':
        rot13decoder()
        break
    else:
        endecode = raw_input('1) 1) Введіть 1, щоб кодувати повідомлення\n2) Введіть 2 для розшифрування повідомлення\n')
