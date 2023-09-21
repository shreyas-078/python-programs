# To find a pair in a sorted array adding upto given user input number

def find_pair(arr, target):
    arr.sort()
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i == j:
                continue # Same element 
            if arr[i] + arr[j] > target:
                break
            if arr[i] + arr[j] == target:
                return [arr[i], arr[j]]
    return "No pairs add up to the specified number"

user_arr = []
for i in range(int(input("Enter number of elements of array"))):
    user_arr.append(int(input(f"Enter element number {i}")))

target = int(input("Enter value to find pairs which add up to it"))
print(find_pair(user_arr, target))
