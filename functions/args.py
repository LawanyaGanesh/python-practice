def add(*args):

    rows = 0

    for row in args:

        rows +=row

    return rows
    

print(add(2,3))

def print_profile(**kwargs):
    # kwargs behaves exactly like a dictionary: {"name": "Alice", "role": "Dev"}
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Pass any key-value pairs you want
print_profile(name="Alice", role="Dev", status="Active")