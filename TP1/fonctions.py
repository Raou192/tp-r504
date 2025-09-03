def puissance(samy,raoul):
	if not type(samy) is int or not type (raoul) is int:
		raise TypeError("intergers only jeune homme")
	else:
		return samy ** raoul
