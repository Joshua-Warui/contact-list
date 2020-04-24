#! /usr/bin/env python3.6

from contact import Contact


#Creating a contact
def create_contact(fname,lname,phone,email):
  '''
  function to create a new contact
  '''

  new_contact = Contact(fname,lname,phone,email)
  return new_contact


#Saving contacts
def save_contact(contact):
  '''
  function to save contact
  '''

  contact.save_contact()


#Delete contact
def del_contact(contact):
  '''
  function to delete contact
  '''

  contact.delete_contact()


#Finding a contact
def find_contact(number):
  '''
  function that finds a contact by phone number and returns the contact
  '''

  return Contact.find_contact_by_number(number)


#Check if a contact exists
def check_existing_contacts(number):
  '''
  function that checks if a contact exists with that number and returns a Boolean
  '''

  return Contact.contact_exists(number)


#Displaying all contacts
def display_contacts():
  '''
  function that returns all the saved contacts
  '''

  return Contact.display_all_contacts()


def main():
  print("Hello Welcome to your contact list. What is your name?")
  user_name = input()

  print(f"Hello {user_name}. What would you like to do?")
  print('\n')

  while True:

    print("Use these short codes : cc - create new contact, dc - display contacts, fc - find a contact, ex - exit the contact list ")

    short_code = input().lower()

    if short_code == 'cc':

      print("New Contact")
      print("-" * 10)

      print("First name: ")
      f_name = input()

      print("Last name: ")
      l_name = input()

      print("Phone number: ")
      p_number = input()

      print("Email address: ")
      e_address = input()

      save_contact(create_contact(f_name,l_name,p_number,e_address))
      print('\n')
      print(f"New Contact  {f_name} {l_name} created")
      print('\n')

    elif short_code == 'dc':

      if display_contacts():

        print("Here is a list of all your contacts")
        print('\n')

        for contact in display_contacts():

          print(f"{contact.first_name} {contact.last_name} {contact.phone_number} {contact.email}")
          print('\n')

      else:
        print('\n')
        print("You don't seem to have any contacts saved yet")
        print('\n')

    elif short_code == 'fc':

      print("Enter the number you want to search for: ")
      search_number = input()
  
      if check_existing_contacts(search_number):

        search_contact = find_contact(search_number)
        print('\n')
        print(f"{search_contact.first_name} {search_contact.last_name} ")
        print('_' * 20)
        print(f"Phone number: {search_contact.phone_number}")
        print(f"Email address: {search_contact.email}")

      else:
        print("That contact does not exist")

    elif short_code == 'ex':

      print('\n')
      print("Bye. Come try me out again :)")
      break

    else:
      print('\n')
      print("I really didn't get that. Please use the short codes")
      print('\n')


if __name__ == '__main__':
  main()