def reverse(s):
	return s[::-1]
# example
word = "andela"
print reverse(word)
print reverse("lawrence")
print reverse("android")


def reversex(s):
	s = list(s)
	for i in range(len(s) // 2): # temp = s[i]
		s[i], s[len(s) - 1 - i] = s[len(s) - 1 - i], s[i]
# s[len(s) - 1 - i] = temp
	return " ".join(s)

print reverse("kamau")