import pandas as pd

visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])
#print(visits)
#print(cart)
#print(checkout)
#print(purchase)
visitsCart=pd.merge(visits,cart,how="left")
print(visitsCart)
print(len(visitsCart))
Timestampisnull = visitsCart[visitsCart['cart_time'].isna()]
print(Timestampisnull)
percntage2=float(len(Timestampisnull)/len(visitsCart))
print(percntage2*100,"%")
cartCheckouts=pd.merge(cart,checkout,how="left")
print(cartCheckouts)
visitingwithoutcheckingout=cartCheckouts[cartCheckouts.checkout_time.isna()]
percentage=float(len(visitingwithoutcheckingout)/len(cartCheckouts))
print(percentage*100)
all_data=visits.merge(cart,how="left").merge(checkout,how="left").merge(purchase,how="left")
print(all_data)
checkoutWithOutpurchasing=all_data[(all_data.checkout_time.isna()==False) & (all_data.purchase_time.isna())]
print(checkoutWithOutpurchasing)
checkoutWithOutpurchasing_percentage=len(checkoutWithOutpurchasing)/len(all_data)
print(checkoutWithOutpurchasing_percentage*100)
all_data["time_to_purchase"]=all_data.purchase_time - all_data.visit_time
print(all_data.time_to_purchase)
print(all_data.time_to_purchase)