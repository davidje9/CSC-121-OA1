COST_INFANT = 0      #ages 0-2
COST_CHILD = 10      #ages 3-12
COST_GENERAL = 15    #ages 13+

age = "general"
agePrompt = """\nWelcome to the theater! We have tickets available for general admission (ages 13 and up), child (ages 3-12), or infant (age up to 2).
    \nPlease type either general, child, or infant to order.  """
ticketsPrompt = f"\nHow many {age} tickets would you like to purchase?  "
checkoutPrompt = "\nType 'checkout' to see your total or 'continue' to add more.\n"
costTotal = 0
adultTicketsTotal = 0
childTicketsTotal = 0
infantTicketsTotal = 0
checkout = "continue"

while checkout != 'checkout':
    age = input(agePrompt)
    if age == "general":
        print(f"\n{age.title()} tickets cost ${COST_GENERAL} apiece.")
        tickets = int(input(ticketsPrompt))
        costTotal = costTotal + (tickets * COST_GENERAL)
        adultTicketsTotal = adultTicketsTotal + tickets
        checkout = input(checkoutPrompt)
    elif age == "child":
        print(f"\n{age.title()} tickets cost ${COST_CHILD} apiece.")
        tickets = int(input(ticketsPrompt))
        costTotal = costTotal + (tickets * COST_CHILD)
        childTicketsTotal = childTicketsTotal + tickets
        checkout = input(checkoutPrompt)        
    elif age == "infant":
        print(f"\n{age.title()} tickets cost ${COST_INFANT} apiece.")
        tickets = int(input(ticketsPrompt))
        costTotal = costTotal + (tickets * COST_INFANT)  
        infantTicketsTotal = infantTicketsTotal + tickets
        checkout = input(checkoutPrompt)          
    else:
        print('Sorry, that command was not recognized.')

print(f"""\nYou ordered 
      {adultTicketsTotal} general admission tickets, 
      {childTicketsTotal} child tickets, and 
      {infantTicketsTotal} infant tickets. 
      \nYour total comes to ${costTotal}. Thanks and enjoy the show!""")
