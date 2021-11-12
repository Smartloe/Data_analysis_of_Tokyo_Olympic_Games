def str_count(s):
	letters, space, digit, others, i = 0, 0, 0, 0, 0
	while i < len(s):
		sting_str = s[i]
		i += 1
		if sting_str.isalpha():
			letters += 1
		elif sting_str.isdigit():
			digit += 1
		elif sting_str.isspace():
			space += 1
		else:
			others += 1
	result = f"字符串“{s}”中字母个数={letters},数字个数={digit},空格个数={space},其他字符个数={others}"
	return result


if __name__ == "__main__":
	s = input("请输入一段字符串")
	print(str_count(s))
