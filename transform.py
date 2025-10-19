import pandas as pd 

print("the data is transformed")

data = {
    "id":[1,2,3,4,5],
    "name":["daya","jetha","tapu","sonu","gogi"],
    "age":[50,40,30,20,10]
}

df=pd.DataFrame(data)
print(df)