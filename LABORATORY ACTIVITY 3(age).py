def classify_age(age):
	if age < 0:
		print("Baby ko.")
	elif age <= 12:
		print("You are a Child.")
	elif age <= 19:
		print("You are Teen.")
	elif age <= 64:
		print("You are an Adult.")
	else:
		print("akulaw.")

classify_age(77)