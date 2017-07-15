def hamming_distance(num1, num2):
    """Return the Hamming distance between equal-length sequences"""
    s1 = bin(num1)
    s2 = bin(num2)
    s1 = s1[2:]
    s2 = s2[2:]
    if len(s1) != len(s2):
        if len(s1) > len(s2):
			s2 = ("0"*(len(s1)-len(s2))) + s2
		else:
			s1 = ("0"*(len(s2)-len(s1))) + s1	
	return sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2))
print hamming_distance(117,17)
