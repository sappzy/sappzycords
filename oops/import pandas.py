import pandas

# mydataset = {
#     'cars': ["BMW", "Volvo", "Ford"],
#     'passings': [3, 7, 2]
# }
# df=pandas.DataFrame(mydataset)
# print(df)

data={
    "student":["sapp", "alice", "bob", "john", "michael", "susan"],
    "score":[50,40,45,25,38,46]   
}
df=pandas.DataFrame(data)
print(df)


print(df.loc["sapp":"bob"])