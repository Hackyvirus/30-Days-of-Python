# 14. Grade system (A/B/C/F)

Percentage = float(input("Enter Student Percentage: "))

if Percentage >90:
    print(f"Student has A Grade with {Percentage}%")
elif Percentage > 80:
    print(f"Student has B Grade with {Percentage}%")
elif Percentage > 70:
    print(f"Student has C Grade with {Percentage}%")
elif Percentage < 70 and Percentage >= 35:
    print(f"Student has D Grade with {Percentage}%")
elif Percentage < 35:
    print(f"Student has F Grade with {Percentage}%")


