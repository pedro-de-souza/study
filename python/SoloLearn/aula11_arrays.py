words = ["Hello", "world", "!"]
print(words[0])
print(words[1])
print(words[2])

# 

number = 3
things = ["string", 0, [1, 2, number], 4.56]
print(things[1])
print(things[2])
print(things[2][2])

# 

str = "Hello world!"
print(str[6])

# 

nums = [7, 7, 7, 7, 7]
nums[2] = 5
print(nums)

# 

nums = [1, 2, 3]
print(nums + [4, 5, 6])
print(nums * 3)

# 

words = ["spam", "egg", "spam", "sausage"]
print("spam" in words)
print("egg" in words)
print("tomato" in words)

# 

nums = [1, 2, 3]
print(not 4 in nums)
print(4 not in nums)
print(not 3 in nums)
print(3 not in nums)

# 

nums = [1, 2, 3]
nums.append(4)
print(nums)

# 

nums = [1, 3, 5, 2, 4]
print(len(nums))


# O método de inserção é semelhante ao acréscimo , exceto que permite inserir um novo item em qualquer posição da lista, em vez de apenas no final.
words = ["Python", "fun"]
index = 1
words.insert(index, "is")
print(words)
# ['Python', 'é', 'divertido'] 

# 

letters = ['p', 'q', 'r', 's', 'p', 'u']
print(letters.index('r'))
print(letters.index('p'))
print(letters.index('z'))


# A função range cria uma lista seqüencial de números.
numbers = list(range(10))
print(numbers)

# 

numbers = list(range(3, 8))
print(numbers)

print(range(20) == range(0, 20))

# 

numbers = list(range(5, 20, 2))
print(numbers)

# 

list = [1, 1, 2, 3, 5, 8, 13]
print(list[list[2]])

range(4)
