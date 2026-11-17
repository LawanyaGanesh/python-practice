students = {
    "Arun": 85,
    "Rahul": 72,
    "Priya": 95,
    "Kiran": 60,
    "Sneha": 88
}
max_value = 85
max_name = ''
sec_max = 72
sec_max_name = ''
for key,value in students.items():
  if value >max_value:
    max_value = value

for key,value in students.items():
  if value<max_value:
    if value>sec_max:
      sec_max = value
      sec_max_name = key
print(sec_max_name,sec_max)

