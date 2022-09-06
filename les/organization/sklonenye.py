import pymorphy2


def sklonenye(for_sklonenye, type=None):
    print('строка которая приша в функцию склонения= ', for_sklonenye)
    print('тип название, фамилия, имя, отчество, должность')
    types = {'Orgn': '', 'Surn': 'Surn', 'Name': 'Name', 'Patr': 'Part', 'Dolj': ''}
    morph = pymorphy2.MorphAnalyzer()
    slova = for_sklonenye.split()
    slovo_v_pred_p = []
    slovo_v_rod_p = []
    if type == 'Orgn':
        for i in slova:
            if i == 'Главное' or i == 'управление':
                a = morph.parse(i)[0]
                v_pred_p = a.inflect({'loct'})
                v_rod_p = a.inflect({'gent'})
                slovo_v_pred_p.append(v_pred_p.word)
                slovo_v_rod_p.append(v_rod_p.word)
            else:
                slovo_v_pred_p.append(i)
                slovo_v_rod_p.append(i)
        nazvanye_v_pred_p = ' '.join(slovo_v_pred_p)
        nazvanye_v_rod_p = ' '.join(slovo_v_rod_p)
        skl = [nazvanye_v_rod_p, nazvanye_v_pred_p]
        print('skl=', skl)
        return skl
    elif type == 'Surn':
        for i in slova:
            a = morph.parse(i)[0]
            b = morph.parse(i)
            for j in b:
                if 'Surn' in j.tag:
                    print(j)
                    a = j
            v_pred_p = a.inflect({'loct'})
            v_rod_p = a.inflect({'gent'})
            slovo_v_pred_p.append(v_pred_p.word)
            slovo_v_rod_p.append(v_rod_p.word)
        nazvanye_v_pred_p = ' '.join(slovo_v_pred_p)
        nazvanye_v_rod_p = ' '.join(slovo_v_rod_p)
        skl = [nazvanye_v_rod_p.title(), nazvanye_v_pred_p.title()]
        #print('skl=', skl)
        return skl
    elif type == 'Name':
        for i in slova:
            a = morph.parse(i)[0]
            b = morph.parse(i)
            for j in b:
                if 'Name' in j.tag:
                    print(j)
                    a = j
            v_pred_p = a.inflect({'loct'})
            v_rod_p = a.inflect({'gent'})
            slovo_v_pred_p.append(v_pred_p.word)
            slovo_v_rod_p.append(v_rod_p.word)
        nazvanye_v_pred_p = ' '.join(slovo_v_pred_p)
        nazvanye_v_rod_p = ' '.join(slovo_v_rod_p)
        skl = [nazvanye_v_rod_p.title(), nazvanye_v_pred_p.title()]
        #print('skl=', skl)
        return skl
    elif type == 'Patr':
        for i in slova:
            a = morph.parse(i)[0]
            b = morph.parse(i)
            for j in b:
                if 'Patr' in j.tag:
                    print(j)
                    a = j
            v_pred_p = a.inflect({'loct'})
            v_rod_p = a.inflect({'gent'})
            slovo_v_pred_p.append(v_pred_p.word)
            slovo_v_rod_p.append(v_rod_p.word)
        nazvanye_v_pred_p = ' '.join(slovo_v_pred_p)
        nazvanye_v_rod_p = ' '.join(slovo_v_rod_p)
        skl = [nazvanye_v_rod_p.title(), nazvanye_v_pred_p.title()]
        print('skl=', skl)
        return skl
    elif type == 'Dolj':
        for i in slova:
            a = morph.parse(i)[0]
            v_pred_p = a.inflect({'loct'})
            v_rod_p = a.inflect({'gent'})
            slovo_v_pred_p.append(v_pred_p.word)
            slovo_v_rod_p.append(v_rod_p.word)
        nazvanye_v_pred_p = ' '.join(slovo_v_pred_p)
        nazvanye_v_rod_p = ' '.join(slovo_v_rod_p)
        skl = [nazvanye_v_rod_p, nazvanye_v_pred_p]
        #print('skl=', skl)
        return skl
    else:
        for i in slova:
            a = morph.parse(i)[0]
            v_pred_p = a.inflect({'loct'})
            v_rod_p = a.inflect({'gent'})
            slovo_v_pred_p.append(v_pred_p.word)
            slovo_v_rod_p.append(v_rod_p.word)
        nazvanye_v_pred_p = ' '.join(slovo_v_pred_p)
        nazvanye_v_rod_p = ' '.join(slovo_v_rod_p)
        skl = [nazvanye_v_rod_p, nazvanye_v_pred_p]
        #print('skl=', skl)
        return skl