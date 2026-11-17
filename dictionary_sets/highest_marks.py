students = {
    "Arun": 85,
    "Rahul": 72,
    "Priya": 95,
    "Kiran": 60,
    "Sneha": 88
}
max_value = 20
max_name = ''
for key,value in students.items():
  
  if value>max_value:
    max_value = value
    max_name = key
print(max_name,max_value)

