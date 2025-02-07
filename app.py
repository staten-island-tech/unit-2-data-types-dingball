def tip_calculate(service):
    if service == "bad":
        print("0% tip")
    elif service == "okay":
        print("15% tip")
    elif service == "good":
        print("20% tip")
    elif service == "great":
        print("25% tip")
    else:
        print("Please enter a valid service rating")

service = input("How was the service? (bad, okay, good, great):")
tip_calculate(service)