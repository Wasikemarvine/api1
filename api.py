def get_user():
	username=input("Whats your name?")
	profile_info = requests.get('https://api.github.com/users/'+ username)

	print (profile)

	for info in profile:
		pass
get_user()
