import pprint
test_dict = {}
size = int(input("Enter the number of elements: "))

for i in range(size):
    dict_name = input("Enter the name : ")

    test_dict[dict_name] = {}
    Age = input("Enter Age: ")
    city = input("Enter city: ")
    sex = input("Enter sex: ")
    test_dict[dict_name]["Age"] = Age
    test_dict[dict_name]["City"] = city
    test_dict[dict_name]["Sex"] = sex
print("Sorted data:")
pprint.pprint(sorted(test_dict.items(), key=lambda x: x[1]['Age'], reverse=True))
