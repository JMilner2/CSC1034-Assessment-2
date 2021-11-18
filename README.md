# CSC1034-Assessment-2
This contacts app allows users to edit, add, load and save contacts from the command line.
It saves and loads contacts to a .txt file which had to already exist for the code to run.
When the code is run the user is presented with 5 different functions they can use the application
for:
* **Search** for a contact with a (completely matching) detail 
* **Display** a list of all contacts and their details
* **Edit** a contacts details
* **Add** a new contact
* **Save** (new or edited contacts) and exit

The assumptions I have made while making this application are, that for
the menu system the user might try to enter something other than
an integer, so I have got validation that stops that. Also, if they enter 
an invalid integer choice there is error handling do the code doesn't crash. 
Secondly I have assumed that the user knows that to search
for a contact they have to use completely matching details(Case sensitive). Furthermore, 
I have assumed that a user might enter a blank input, so all input fields have a validation check to 
stop blank inputs. Another assumption I have made is that users will enter correct details for each contact when 
editing and adding a new one. The only validation I have done for the contact details is checking for blank inputs.
If a user does enter incorrect details they can use the edit function to change them. Additionally, incorrect details won't 
affect how the code runs. I have also assumed that the user might close the application without using the save and exit
function. So after each loop of the code I have made it, so it saves any new or edited contacts to the text file.
The last assumption that I have made is that the user has a .txt file in the same directory as the code as it is needed to run.
The text file doesn't need any contacts in the file as it runs with an empty one it just needs to be there.

##How to use the application:
**Example contact:**
Name: Mark Milner, Address: 62 Hanthorpe Rd, Number: 01778570756, Date of birth: 01/10/1967

The user is presented this 5 choices, and they have to input either 1,2,3,4,5 depending on 
what they want to do.
##1 - Search function:
The user is presented with a choice of what detail they want to search by (name,address,number,DOB)
and must enter **"1"**,**"2"**,**"3"**,**"4"** accordingly. Then they are presented with an input field to enter the detail to search for. If any matches
are found the contact and all its details are displayed. It searches for completely matching names so if there was a contact with
the name **"Mark Milner"**, a search for **"mark"** or **"milner"** would return no results

##2 - Display function:
All contacts and their details are displayed

So it would display

Mark Milner: Address = 62 Hanthorpe Rd, Number = 01778570756, Date of birth = 01/10/1967

##3 - Edit function:
The user is presented with a numbered list of all the contacts. They must enter a choice from the list (c0,c1,c2...) 
depending on what contact they want to edit. Once a valid
choice had been made they are given input fields where they can re-enter the
name, address, number and DOB of the contact. If they wish for the details to stay the same
they must re-enter the same details.

So if they wanted to edit the name of **"Mark Milner"** to **"Mike Milner"**, the user would have to enter the choice of 
**"c0"** (c0 because Mark Milner is the only contact in the contacts list in this example) 
then enter **"Mike Milner"** in the
name field and re-enter the rest of the contact details the same as they were.
To edit the contacts number they would do the same but leave the name the same and enter a new number

##4 - Add function:
The user is presented with different input fields for the new contacts name, address, number and DOB.
The new contact is then saved to the .txt file.

##5 - Save and Exit:
The contacts list is saved to the .txt file and the application stop running

