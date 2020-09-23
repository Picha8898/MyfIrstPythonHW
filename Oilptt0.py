print('#' * 80)
print('#' + ' ' * 78 + '#')
print('#' + ' ' * 78 + '#')
print('#' + ' ' * 78 + '#')
print('#' + ' ' * 78 + '#')
print('#' + ' ' * 78 + '#')
print('#' + ' ' * 78 + '#')
print('#' + ' ' * 78 + '#')
print('#' + ' ' * 78 + '#')
print('#' + ' ' * 78 + '#')
print('#' + ' ' * 78 + '#')
print('#' + ' ' * 78 + '#')
print('#' + ' ' * 34 + 'Oil PPT' + ' ' * 37 + '#')
print('#' + ' ' * 78 + '#')
print('#' + ' ' * 78 + '#')
print('#' + ' ' * 78 + '#')
print('#' + ' ' * 78 + '#')
print('#' + ' ' * 78 + '#')
print('#' + ' ' * 78 + '#')
print('#' + ' ' * 78 + '#')
print('#' + ' ' * 78 + '#')
print('#' + ' ' * 78 + '#')
print('#' + ' ' * 78 + '#')
print('#' + ' ' * 78 + '#')
print('#' * 80)
y = 1
while True:
    if y == 1:
        print('#' * 80)
        print('#' + ' ' * 78 + '#')
        print('#' + ' ' * 78 + '#')
        print('#' + ' ' * 32 + 'Secret Gas' + ' ' * 36 + '#')
        print('#' + ' ' * 78 + '#')
        print('#' + ' ' * 78 + '#')
        print('#' + ' ' * 78 + '#')
        print('#' + ' ' * 78 + '#')
        print('#' + ' ' * 27 + '1.gasoline 95' + ' ' * 38 + '#')
        print('#' + ' ' * 27 + 'ราคา 25.30 บาท' + ' ' * 37 + '#')
        print('#' + ' ' * 27 + '3.gasohol 91' + ' ' * 39 + '#')
        print('#' + ' ' * 27 + 'ราคา 21.68 บาท' + ' ' * 37 + '#')
        print('#' + ' ' * 27 + '4.gasohol E20' + ' ' * 38 + '#')
        print('#' + ' ' * 27 + 'ราคา 20.2 บาท' + ' ' * 38 + '#')
        print('#' + ' ' * 27 + '5.gasohol 95' + ' ' * 39 + '#')
        print('#' + ' ' * 27 + 'ราคา 21.2 บาท' + ' ' * 38 + '#')
        print('#' + ' ' * 27 + '6.diesel' + ' ' * 43 + '#')
        print('#' + ' ' * 27 + 'ราคา 21.1 บาท' + ' ' * 38 + '#')
        print('#' + ' ' * 78 + '#')
        print('#' + ' ' * 78 + '#')
        print('#' + ' ' * 78 + '#')
        print('#' + ' ' * 78 + '#')
        print('#' + ' ' * 78 + '#')
        print('#' + ' ' * 78 + '#')
        print('#' * 80)
        k = 0
        status = True
        i = 0
        while not (k in ['1', '2', '3', '4', '5', '6']):
            if k in ['1', '2', '3', '4', '5', '6'] and status:
                status = True
            else:
                status = False
                if i > 0:
                    print('Error')
            i += 1
            k = (input('Serect oli : '))
            m = k
        print('#' * 80)
        print('#' + ' ' * 78 + '#')
        print('#' + ' ' * 78 + '#')
        print('#' + ' ' * 78 + '#')
        print('#' + ' ' * 78 + '#')
        print('#' + ' ' * 78 + '#')
        print('#' + ' ' * 34 + 'Secret' + ' ' * 38 + '#')
        print('#' + ' ' * 78 + '#')
        print('#' + ' ' * 78 + '#')
        print('#' + ' ' * 30 + '1 MONEY  to LITERS' + ' ' * 30 + '#')
        print('#' + ' ' * 30 + '2 LITERS to MONEY' + ' ' * 31 + '#')
        print('#' + ' ' * 78 + '#')
        print('#' + ' ' * 78 + '#')
        print('#' + ' ' * 78 + '#')
        print('#' + ' ' * 78 + '#')
        print('#' + ' ' * 78 + '#')
        print('#' + ' ' * 78 + '#')
        print('#' + ' ' * 78 + '#')
        print('#' + ' ' * 78 + '#')
        print('#' + ' ' * 78 + '#')
        print('#' + ' ' * 78 + '#')
        print('#' + ' ' * 78 + '#')
        print('#' + ' ' * 78 + '#')
        print('#' + ' ' * 78 + '#')
        print('#' * 80)
        ks1 = 0
        status = True
        i = 0
        while not (ks1 in ['1', '2']):
            if ks1 in ['1', '2'] and status:
                status = True
            else:
                status = False
                if i > 0:
                    print('Error')
            i += 1
            ks1 = (input('serect means : '))
            g = ks1
        if '1' in g:
            k = input("บอกลิตรลงไปครับ:\n จำนวนลิตร = ")
            k1 = int(k)
        elif '2' in g:
            o = input("บอกค่าเงินลงไปครับ: \n จำนวน = ")
            r1 = int(o)
        s = 0
        if '2' in g:
            if '1' in m:
                s = s + (r1 * 29.16)
                print('จำนวนเงิน=', s)
            elif '2' in m:
                s = s + (r1 * 25.30)
                print('จำนวนเงิน=', s)
            elif '3' in m:
                s = s + (r1 * 21.68)
                print('จำนวนเงิน=', s)
            elif '4' in m:
                s = s + (r1 * 20.2)
                print('จำนวนเงิน=', s)
            elif '5' in m:
                s = s + (r1 * 21.2)
                print('จำนวนเงิน=', s)
            elif '6' in m:
                s = s + (r1 * 21.1)
                print('จำนวนเงิน=', s)
            else:
                print ("Error")

        elif '1' in g:
            if '1' in m:
                s = s + (k1 / 29.16)
                print('จะได้' ',''%.2f' % s, 'จำนวนลิตร', s)
            elif '2' in m:
                s = s + (k1 / 25.30)
                print('จะได้' ',''%.2f' % s, 'จำนวนลิตร', s)
            elif '3' in m:
                s = s + (k1 / 21.68)
                print('จะได้' ',''%.2f' % s, 'จำนวนลิตร', s)
            elif '4' in m:
                s = s + (k1 / 20.2)
                print('จะได้' ',''%.2f' % s, 'จำนวนลิตร', s)
            elif '5' in m:
                s = s + (o1 / 21.2)
                print('จะได้' ',''%.2f' % s, 'จำนวนลิตร', s)
            elif '6' in m:
                s = s + (k1 / 21.1)
                print('จะได้' ',''%.2f' % s, 'จำนวนลิตร', s)
            else:
                print ('Error')
        x = int(input("พิมพ์ 1 เพื่อคำนวนต่อ พิมพ์ 0 เพื่อสิ้นสุด :"))
        y = x
    elif y == 0:
        print('#' * 80)
        print('#' + ' ' * 78 + '#')
        print('#' + ' ' * 78 + '#')
        print('#' + ' ' * 78 + '#')
        print('#' + ' ' * 78 + '#')
        print('#' + ' ' * 78 + '#')
        print('#' + ' ' * 78 + '#')
        print('#' + ' ' * 78 + '#')
        print('#' + ' ' * 78 + '#')
        print('#' + ' ' * 78 + '#')
        print('#' + ' ' * 78 + '#')
        print('#' + ' ' * 34 + 'Thank you very much' + ' ' * 25 + '#')
        print('#' + ' ' * 34 + 'Thank you very much' + ' ' * 25 + '#')
        print('#' + ' ' * 34 + 'Thank you very much' + ' ' * 25 + '#')
        print('#' + ' ' * 78 + '#')
        print('#' + ' ' * 78 + '#')
        print('#' + ' ' * 78 + '#')
        print('#' + ' ' * 78 + '#')
        print('#' + ' ' * 78 + '#')
        print('#' + ' ' * 78 + '#')
        print('#' + ' ' * 78 + '#')
        print('#' + ' ' * 78 + '#')
        print('#' + ' ' * 78 + '#')
        print('#' + ' ' * 78 + '#')
        print('#' * 80)
        break
