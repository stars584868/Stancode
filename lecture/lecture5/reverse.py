EXIT = '-1'


def main():
	print('Hello, world')
	stack = []
	while True:
		s = input('give me lines(I will give them back reversely): ')
		if s == EXIT:
			break
		stack.append(s)

	while len(stack) != 0:
		ele = stack.pop()
		print(ele)


if __name__ == '__main__':
	main()