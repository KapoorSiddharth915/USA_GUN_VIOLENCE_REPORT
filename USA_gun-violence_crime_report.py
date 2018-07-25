import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sb
import pygal as py

import csv

df=pd.read_csv("C:/python crash course/udemy/gun-violence-data_01-2013_03-2018.csv")
print(df)
print("info is")
print(df.info())
print("head info is")
print(df.head())

                #Top 5 states
state_name=df["state"].value_counts()
print("\t\t\t\t States names are:\t\t\n",state_name.head(5))


               #Top 5 cities or county
city_county=df["city_or_county"].value_counts()
print(city_county.head(5))

               # create a new column Reason for state
area=df["Reason"]=df["state"].apply(lambda title:title)
print(area)

reason=df["Reason"].value_counts()

top1=df["Top"]=df["state"].apply(lambda top:top)
#print("\t\t\t\t\t top 5 criminal states of USA\t\t\t\t\t \n",top1)

top2=df["Top"].value_counts().head(5)
print("\t\t\t\t\t top 5 criminal states of USA\t\t\t\t\t \n",top2)

#plt.rcParams['figure.figsize'] = (10.0, 10.0)
plt.figure(figsize=(10,6),dpi=128)
plt.xticks(rotation=90)
plt.title("Gun viloence data of Each state",fontsize=20)
count=sb.countplot(x="Reason",data=df,palette="plasma")
plt.xlabel("States",fontsize=16)
plt.ylabel("Number of records",fontsize=16)
plt.show()

state=df["state"].value_counts()
hist7=py.Bar()
hist7.add("state",state)
hist7.render_to_file("state.svg")


hist=py.Bar()
hist.x_title="Top 5 crime states of USA"
hist.x_labels=["Illinois","California","Florida","Texas","Ohio"]
hist.add("State",top2)
hist.render_to_file("Gun_violence_data.svg")
#plt.savefig("Gun_violence_data.svg")


                #create a new column Reason2 for city_or_county
reason2=df["Reason2"]=df["city_or_county"].apply(lambda city:city)
print(reason2.head())

'''plt.figure(figsize=(10,6),dpi=128)
plt.tight_layout()
plt.title("Gun violence data of Each city",fontsize=20)
plt.xlabel("Cities or County",fontsize=16)
plt.ylabel("Number of records",fontsize=16)
plt.xticks(rotation=90)
sb.countplot(x="Reason2",data=df,palette="viridis")
plt.show()'''

date=df["date"]=pd.to_datetime(df["date"])
print(date)

time=df["date"].iloc[0]
print("Month is\n",time.month)
print("Day is\n",time.day)
print("Year is\n",time.year)

#now we create 3 new columns Month/Day/Year

month=df["Month"]=df["date"].apply(lambda time:time.month)

df["Day"]=df["date"].apply(lambda time:time.day)

df["Year"]=df["date"].apply(lambda time:time.year)
print("3 new columns\n",df.head())

dmap={0:"Mon",1:"Tue",2:"Wed",3:"Thu",4:"Fri",5:"Sat",6:"Sun"}
df["Day"]=df["Day"].map(dmap)
print("3 new columns\n",df.head())


plt.figure(dpi=128,figsize=(20,12))
plt.legend(bbox_to_anchor=(1.05,1),loc=2,borderaxespad=0.)
sb.countplot(x="Month",hue="Reason",data=df,linewidth=8)

plt.legend()
plt.show()

fatality=df["Reason3"]=df["incident_characteristics"].apply(lambda fat:fat)
print("fatality",fatality)

killed=df["killed"]=df["n_killed"].apply(lambda kill:kill)
print("killed",killed)


'''plt.figure(dpi=128,figsize=(10,8))
plt.title("Number of persons killed")
sb.countplot(x="Reason3",data=df)
plt.show()'''




plt.figure(dpi=128,figsize=(10,8))
sb.countplot(x="killed",data=df)
plt.title("killed person")
plt.legend(bbox_to_anchor=(1.05,1),loc=2,borderaxespad=0.)
plt.show()

dmap={0:"Jnauary",1:"February",2:"March",3:"April",4:"May",5:"June",6:"July",7:"August",8:"Septembet",
       9:"October",10:"November",11:"December"}
df["Month"]=df["Month"].map(dmap)



plt.figure(dpi=128,figsize=(10,8))
plt.tight_layout()
plt.title("Number of persons killed in each Month",fontsize=20)
plt.ylabel("Number",fontsize=16)
plt.xlabel("Months",fontsize=16)
sb.barplot(x="Month",y="killed",data=df)
plt.plot(labelsize=20)
plt.show()


total=df["n_killed"].value_counts()
print(total)

years=df["Year"].value_counts()
print(years)



gun_type=df["gun_type"].value_counts().head(6)
print("gun type is",gun_type)

hist3=py.Bar()
hist3.add("Gun",gun_type)
hist3.x_labels=["Unknown","Handguns","9mm","Unknown","LR","Shotguns"]
hist3.x_title=("Guns used")
hist3.render_to_file("guns.svg")

#plt.plot(years,gun_type)
plt.show()
plt.figure(dpi=128)
plt.tight_layout()
plt.legend(bbox_to_anchor=(1.05,1),loc=2,borderaxespad=0.)
sb.countplot(x="Year",hue="killed",data=df)
plt.show()

top_killing_year=df["Year"].value_counts()
print(top_killing_year)

sb.countplot(x="Year",data=df,palette="coolwarm")
plt.title("Most people killed")
plt.show()

hist4=py.Bar()
hist4.add("year",top_killing_year)
hist4.x_title=("Most Gun voilence years")
hist4.x_labels=[2013,2014,2015,2016,2017,2018]
hist4.render_to_file("year.svg")

