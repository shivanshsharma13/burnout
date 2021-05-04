import pandas as pd
from csv import writer
data = pd.read_csv("sample_submission.csv")

emp_id_input = input()
burnout_input = float(input())

data = data.head()
# sno = data.head().index+1
df = pd.DataFrame(data)

lst = []
for i,j in df.iteritems():
    lst.append(j.values)

emp_ids = lst[0]
burnout = lst[1]

# print(emp_ids)

final = []
# Check if emp_id is present or not-
if emp_id_input in emp_ids:
    print("This id is already registered !")

else:
    final.append(emp_id_input)
    final.append(burnout_input)

# print(final)

# appending the changes 
with open('sample_submission.csv', 'a+', newline='') as f:
    writer_object = writer(f)
    writer_object.writerow(final)
    f.close()