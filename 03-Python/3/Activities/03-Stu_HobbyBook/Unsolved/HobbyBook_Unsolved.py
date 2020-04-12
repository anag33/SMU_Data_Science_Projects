# @TODO: Your code here
my_info = {"name": "Rex",
           "occupation": "dog",
           "age": 21,
           "hobbies": ["barking", "eating", "sleeping", "loving my owner"],
           "wake-up": {"Mon": 5, "Friday": 5, "Saturday": 10, "Sunday": 9}}

print(f'My name is {my_info["name"]} and my job is being a {my_info["occupation"]}. It is not a bad life. I love {my_info["hobbies"][0]}')

for key, value in my_info.items():
    print(key, value)