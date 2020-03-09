a = [1,2,3,4,5]

def fefe(list):
	b = 0
	for num in list:
		b += num
	return b

print(fefe(a))
def gege(list):
	c = 0
	while c != sum(list):
		for num in list:
			c += num
		return c

print(gege(a))


def sum_a(l):
    c = []
    while c != sum(l):
        c = l[-1] + l[-2]
        return c


a = [1,2,3,4]
print(sum_a(a))

