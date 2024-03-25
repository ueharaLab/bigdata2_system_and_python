def bmi(h, w):
    
    # BMI(body mass index)を計算
    x = round(w/((h/100)**2), 2)
    
    # WHO の基準
    if x < 16:
        advice_w = "痩せすぎです"
        
    elif 16 <= x < 17:
        advice_w = "痩せています"
        
    elif 17 <= x < 18.5:
        advice_w = "肥満（1度）です"
        
    elif 18.5 <= x < 25:
        advice_w = "普通体重です"
        
    elif 25 <= x < 30:
        advice_w = "前肥満です"
        
    elif 30 <= x < 35:
        advice_w = "痩せ気味です"
        
    elif 35 <= x < 40:
        advice_w = "肥満（2度）です"
        
    else:
        advice_w = "肥満（3度）です"
    
    return x, advice_w

# 以下、サンプルデータを入力して動作を確認しています
# 身長170cm,体重75kg
bmi_val, comment = bmi(170, 75)
print('bmi:',bmi_val,'アドバイス',comment)
bmi_val, comment = bmi(170, 90)
print('bmi:',bmi_val,'アドバイス',comment)
bmi_val, comment = bmi(170, 110)
print('bmi:',bmi_val,'アドバイス',comment)
bmi_val, comment = bmi(170, 50)
print('bmi:',bmi_val,'アドバイス',comment)

