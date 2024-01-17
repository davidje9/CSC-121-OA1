guest_list = ['Kurt Vonnegut','Walter Benjamin','Joan Didion','Oscar Wilde']

invite_body = "\nYou are cordially invited to dinner in Asheville, NC\non 30 August 2024\nto celebrate David's birthday.\nCash bar.\nPresents expected."

print("Great news! We found a bigger table for David's birthday, which means more scintillating conversation and, of course, more presents.\n")

guest_list.insert(0, "Keanu Reeves")
guest_list.insert(2,"Patti Smith")
guest_list.append("Nick Cave")

invite_body = f"\nJoin {len(guest_list)} illustrious guests for a night of drink and discussion! {invite_body}"

invite1 = f"Dear {guest_list[0]}{invite_body}"
invite2 = f"Dear {guest_list[1]}{invite_body}"
invite3 = f"Dear {guest_list[2]}{invite_body}"
invite4 = f"Dear {guest_list[3]}{invite_body}"
invite5 = f"Dear {guest_list[4]}{invite_body}"
invite6 = f"Dear {guest_list[5]}{invite_body}"
invite7 = f"Dear {guest_list[6]}{invite_body}"

print(f"{invite1}\n")
print(f"{invite2}\n")
print(f"{invite3}\n")
print(f"{invite4}\n")
print(f"{invite5}\n")
print(f"{invite6}\n")
print(f"{invite7}\n")
