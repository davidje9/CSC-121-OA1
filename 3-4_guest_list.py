guest_list = ['Kurt Vonnegut','Walter Benjamin','Joan Didion','Oscar Wilde']

invite_body = "\nYou are cordially invited to dinner in Asheville, NC\non 30 August 2024\nto celebrate David's birthday.\nCash bar.\nPresents expected."

invite1 = f"Dear {guest_list[0]}{invite_body}"
invite2 = f"Dear {guest_list[1]}{invite_body}"
invite3 = f"Dear {guest_list[2]}{invite_body}"
invite4 = f"Dear {guest_list[3]}{invite_body}"

print(f"{invite1}\n")
print(f"{invite2}\n")
print(f"{invite3}\n")
print(f"{invite4}\n")
