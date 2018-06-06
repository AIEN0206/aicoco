import numpy as np

def my_risk(objective, duration, risk_choices):
    # -----start calculate Risk Score 1~6 -----
    risk_total =0
    risk_obj = {"退休":0, "結婚":3, "旅遊":3, "教育":1, "其他":2, "買房":0}
    risk_cho = {"高風險":1,"中風險":0,"低風險":-1}
    if duration < 2:
        risk_dur = 1
    elif duration <=4:
        risk_dur = 2
    elif duration <=7:
        risk_dur = 3
    elif duration <=10:
        risk_dur = 4
    else:
        risk_dur = 5
    risk_total = risk_obj[objective] + risk_cho[risk_choices] + risk_dur
    return risk_total
    # -----end calculate Risk Score-----  

def portfolio_weight(risk_total):
     # -----Calculate Portfolio weights -----
     #不同的risk_total指定不同的權重
    if risk_total <= 1:
        usStockPct = 10
        worldStockPct = 10
        emerStockPct = 0
        sectorStockPct = 0
        usBondPct = 40
        worldBondPct = 40
    elif risk_total == 2:
        usStockPct = 20
        worldStockPct = 20
        emerStockPct = 0
        sectorStockPct = 0
        usBondPct = 30
        worldBondPct = 30
    elif risk_total == 3:
        usStockPct = 20
        worldStockPct = 20
        emerStockPct = 10
        sectorStockPct = 10
        usBondPct = 20
        worldBondPct = 20
    elif risk_total == 4:
        usStockPct = 25
        worldStockPct = 20
        emerStockPct = 20
        sectorStockPct = 15
        usBondPct = 10
        worldBondPct = 10
    elif risk_total == 5:
        usStockPct = 25
        worldStockPct = 20
        emerStockPct = 20
        sectorStockPct = 20
        usBondPct = 0
        worldBondPct = 15
    else:
        usStockPct = 25
        worldStockPct = 25
        emerStockPct = 25
        sectorStockPct = 25
        usBondPct = 0
        worldBondPct = 0
    return usStockPct, worldStockPct, emerStockPct, sectorStockPct, usBondPct, worldBondPct

def monthlyPay(portRate, startDeposit, targetFV, duration):
    # 計算每月需投資金額
    rate = portRate/100
    # 計算  目標存款 - 起始資金的Future value 
    fv = targetFV + np.fv(rate/12,duration*12,0,startDeposit)
    # 計算每月需存的金額
    mPayment = round(np.pmt(rate/12, duration*12, 0,fv))*-1
    return mPayment