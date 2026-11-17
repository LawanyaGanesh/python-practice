students = {
    "Arun": 85,
    "Rahul": 72,
    "Priya": 95,
    "Kiran": 60,
    "Sneha": 88
}
min_value = 85
min_name = ''
sec_min = 88
sec_min_name = []
sec_min_value = ''
total = 0
for key,value in students.items():
  if value >min_value:
    min_value = value
print(min_value)
for key,value in students.items():
  total +=value
average = total/len(students)
for key,value in students.items():
  if value>average:
    print(key)
      
