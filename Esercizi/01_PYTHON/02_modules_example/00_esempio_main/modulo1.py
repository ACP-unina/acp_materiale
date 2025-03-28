print("modulo1 __name__ = %s" % __name__)

def main():
	print("invocazione del main()")

if __name__ == "__main__":
	print("modulo1 is being run directly")
	main()
else:
	print("modulo1 is being imported")
