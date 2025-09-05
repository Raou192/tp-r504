def puissance(samy,raoul):
# à modifier sa ne fonctionne pas
	if type(samy) is float or type(raoul) is float:
		return samy ** raoul

	if not type(samy) is int or not type (raoul) is int:
		raise TypeError("intergers only jeune homme")

	if samy == 0 and raoul < 0:
		raise ValueError("0")

	if raoul == 0:
		return 1

	if raoul > 0:
		result = 1
		for _ in range(raoul):
			result *= samy
		return result

	if raoul < 0:
		result = 1
		for _ in range(-raoul):
			result *= samy
		return 1 / result
