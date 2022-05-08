from sklearn.metrics import confusion_matrix
import numpy as np

def evaluate_simple(x2,y2,pred_y):
    n=np.zeros(len(x2))
    m=np.zeros(len(x2))
    expected_profit=0
    actual_profit=0
    model_thatalwaysbuy=0
    max_profit=0
    for i in range(len(x2)):
        if pred_y[i]>x2.iloc[i,0]:
            n[i]=1
        else:
            n[i]=-1
        if y2[i]>x2.iloc[i,0]:
            m[i]=1
        else:
            m[i]=-1
        expected_profit+=n[i]*(pred_y[i]-x2.iloc[i,0])
        actual_profit+=n[i]*(y2[i]-x2.iloc[i,0])
        model_thatalwaysbuy+=(y2[i]-x2.iloc[i,0])
        max_profit+=m[i]*(y2[i]-x2.iloc[i,0])
    print("accuracy of our model: ",(actual_profit/max_profit)*100,"%")
    y="-"*25
    print(y)
    print("profit our model expect: ",expected_profit)
    print("profit we actually made: ",actual_profit)
    print("maximum profit that is possible: ",max_profit)
    print("percentage of profit we made: ",actual_profit/expected_profit*100,"%")
    print("profit that we can make if we always buy: ",model_thatalwaysbuy)
    print("profit that we can make if we always sell: ",-model_thatalwaysbuy)
    print("confusion matrix: ",confusion_matrix(m,n))
    return None

def evaluate_ema(d1):
    n=np.zeros(len(d1))
    m=np.zeros(len(d1))
    f=0
    expected_profit=0
    actual_profit=0
    model_thatalwaysbuy=0
    max_profit=0
    for row in d1.itertuples():
        # print(row)
        if row.pred_EMA>row.Open:
            n[f]=1
        else:
            n[f]=-1
        if row.Close>row.Open:
            m[f]=1
        else:
            m[f]=-1
        expected_profit+=n[f]*(row.pred_EMA-row.Open)
        actual_profit+=n[f]*(row.Close-row.Open)
        model_thatalwaysbuy+=(row.Close-row.Open)
        max_profit+=m[f]*(row.Close-row.Open)
        f+=1
    
    print("accuracy of our model: ",(actual_profit/max_profit)*100,"%")
    y="-"*45
    print(y)
    print("profit our model expect: ",expected_profit)
    print("profit we actually made: ",actual_profit)
    print("maximum profit that is possible: ",max_profit)
    print("percentage of profit we made: ",actual_profit/expected_profit*100,"%")
    print("profit that we can make if we always buy: ",model_thatalwaysbuy)
    print("profit that we can make if we always sell: ",-model_thatalwaysbuy)
    print("confusion matrix: ",confusion_matrix(m,n))
    # print("confusion matrix: ",confusion_matrix(m,n))
    return None

