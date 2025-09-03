def main():
    hotdog=10
    buns=8
    attendees=int(input("Please enter number of people attending:"))
    serving=int(input("Plese enter the number of hotdogs each person gets:"))
    hotdogs_needed=hotdog*serving
    buns_needed=buns*serving 
    package_hotdogs=hotdogs_needed//hotdog
    package_buns=buns_needed//buns
    total_hotdogs=hotdog*package_hotdogs
    total_buns=buns*package_buns
    leftover_hotdogs=hotdogs_needed-total_hotdogs
    leftover_buns=buns_needed-total_buns
    print("The number of needed packages of hotdogs is:",package_hotdogs)
    print("The number of needed packaged of buns is:",package_buns)
    print("The number of leftover hotdogs is:",leftover_hotdogs)
    print("The number of leftover buns is:",leftover_buns)
main()
