import csv

import pandas as pd

file = 'test.csv'

df = pd.read_csv(r"C:\Users\Michael's  Laptop\Documents\Software_projects_class\test_data.csv", index_col = 0)
df.reset_index(inplace=True)
print(df)
dt = df.to_dict('index')

    

for i in dt:
    print("<tr>")
    for a in dt[i]:
        if (str(dt[i][a]) == "nan"):
            print("<td>"+"</td>")
        else:
            print("<td>"+str(dt[i][a])+"</td>")
    print("</tr>")

##print("<tr>")
##        print("<td>"+dict[i][0]+"</td>")
##        print("<td>"+dict[i][1]+"</td>")
##        print("<td>"+dict[i][2]+"</td>")
##        print("<td>"+dict[i][3]+"</td>")
##        print("<td>"+dict[i][4]+"</td>")
##        print("<td>"+dict[i][5]+"</td>")
##        print("<tr>")
