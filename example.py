import tinysong, os, sys

global tsQuery
tsQuery = tinysong.Query()

global menu
menu = "Song Search Menu:\n1. Open a link to a song\n2. Search again\n3. Quit\n\nEnter choice: "


#####################################
# Function:     open_link
#
# Description:  Prompts user for result number then opens the url of the song the user selects.
#
# Parameters:   None
#
# Returns:      None
#
#####################################
def open_link():
    choice = int(raw_input("Please enter the number you want to open: "))
    if check_range(choice, 1, tsQuery.length):
        #We need to open the url differently between OS's
        if sys.platform[:6] == "darwin":
            os.system("open " + tsQuery.get_url(choice - 1))
        elif sys.platform[:3] == "win":
            os.system("start " + tsQuery.get_url(choice - 1))
        elif sys.platform[:5] == "linux":
            os.system("firefox " + tsQuery.get_url(choice - 1))
        else:
            print("Unsupported platform: Cannot open URL...")
    else:
        print("Invalid answer: Try again!")
        open_link()
    print("\n")
    disp_menu()


def search_again():
    program()


def sys_exit():
    sys.exit(0)

# This is used for a C++ like case/switch statement
global menu_options
menu_options = {1: open_link,
                2: search_again,
                3: sys_exit,
}


#####################################
# Function:     check_range
#
# Description:  checks if the number is between two values
#
# Parameters:   number - the number being compared
#               lower - the lower bound (is included)
#               upper - the upper bound (is included)
#
# Returns:      True if the number is within the range or False if it is outside the bounds
#
#####################################
def check_range(number, lower, upper):
    if upper >= lower <= number:
        return True
    else:
        return False


#####################################
# Function:     disp_menu
#
# Description:  Displays a menu after the query asking user to 1. open link 2. search again 3. exit.
#
# Parameters:   None
#
# Returns:      None
#
#####################################
def disp_menu():
    ans_menu = int(raw_input(menu))
    if check_range(ans_menu, 1, 3):
        # This is used for a C++ like case/switch statement
        menu_options[ans_menu]()
    else:
        print("Invalid option. Try again!")
        disp_menu()


#####################################
# Function:     program
#
# Description:  This is the main function
#
# Parameters:   None
#
# Returns:      None
#
#####################################
def program():
    print("\n")
    query = raw_input("Enter a search query: ")
    tsQuery.api_call(query, 3, 500)
    if not tsQuery.json:
        print("No match found!")
    else:
        while True:
            limit = int(raw_input(str(tsQuery.length) + " matches found. How many would you like to display? "))
            if check_range(limit, 1, tsQuery.length):
                break
            else:
                print("You entered an invalid number. Try again!")
        for x in range(0, limit):
            print("  Result: " + str(x + 1))
            print("-------------------------------------------")
            print("| Song: " + tsQuery.get_title(x))
            print("| Artist: " + tsQuery.get_artist(x))
            print("| Album: " + tsQuery.get_album(x))
            print("| Url: " + tsQuery.get_url(x))
            print("-------------------------------------------\n")
        disp_menu()


# Run the main program
if __name__ == "__main__":
    program()
