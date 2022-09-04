import pymorphy2


def sklonenye(for_sklonenye):
    print('строка которая приша в функцию склонения= ', for_sklonenye)
    morph = pymorphy2.MorphAnalyzer()
    slova = for_sklonenye.split()
    slovo_v_pred_p = []
    slovo_v_rod_p = []
    if for_sklonenye.find('Главное управление') !=-1:
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
    else:
        for i in slova:
            a = morph.parse(i)[0]
            b = morph.parse(i)
            print(b)
            v_pred_p = a.inflect({'loct'})
            v_rod_p = a.inflect({'gent'})
            slovo_v_pred_p.append(v_pred_p.word)
            slovo_v_rod_p.append(v_rod_p.word)
        nazvanye_v_pred_p = ' '.join(slovo_v_pred_p)
        nazvanye_v_rod_p = ' '.join(slovo_v_rod_p)
        skl = [nazvanye_v_rod_p, nazvanye_v_pred_p]
        print('skl=', skl)
        return skl
