

menu_option = ''


while menu_option != 'q':
    # Show the users the menu options.
    print('MENU:','a: cut and fold brochures', 'b: deliver print jobs', 'q: quit', sep="/n")
    # Prompt the user to select a menu option.
    print(input("Enter a menu option: "))
    if menu_option == 'a':
        print('response a')
    elif menu_option == 'b':
        print('response b')

