
import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')

#print(ad_clicks.head())
TheMostPlatform=ad_clicks.groupby("utm_source").user_id.count().reset_index()
#print(TheMostPlatform)
ad_clicks['is_click'] = ad_clicks.ad_click_timestamp.isnull() == False
#print(ad_clicks)
clicks_by_source=ad_clicks.groupby(["utm_source","is_click"]).user_id.count().reset_index()
#print(clicks_by_source)
clicks_pivot=clicks_by_source.pivot(columns="is_click",index="utm_source",values="user_id").reset_index()
#print(clicks_pivot)
clicks_pivot['percent_clicked'] =  clicks_pivot[True]/(clicks_pivot[True] +
    clicks_pivot[False])
#print(clicks_pivot)
experimental_group2=ad_clicks.groupby("experimental_group").user_id.count().reset_index()
print(experimental_group2)
x=ad_clicks.user_id.count()
a_clicks = ad_clicks[
   ad_clicks.experimental_group
   == 'A']
#print(a_clicks)
b_clicks = ad_clicks[
   ad_clicks.experimental_group
   == 'B']
#print(b_clicks)
dataset=a_clicks.groupby(["is_click","day"]).user_id.count().reset_index()
#print(dataset)
dataset_pivot=dataset.pivot(columns="day",index="is_click",values="user_id")
#print(dataset_pivot)
