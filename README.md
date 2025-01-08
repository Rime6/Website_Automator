**Website Automator**

Tired of reopening all the files you usually use on your computer all the time? Here's the solution! This is an easy to make website automator that automatically opens all the tabs you want for a specific set of your choice (for example, I have a work set that opens all the tabs I usually use when i want to work on something, and I have a personal set for the tabs I usually use on my free time). All you need to do is follow these simple steps:
1. Import sys and webbrowser
2. Create a hashmap with the name of your desired sets as the keys, and a list of the urls of all the tabs you want for the set as the values.
3. Create a function that opens each url in a new tab in the desired browser (or integrate this code in the next step)
4. Make your main program (the one that interacts with the user) be in **if __name__ == "__main__":**. The program should keep asking the user's input for a desired set (key) out of the options available until the user picks a valid set, and then use the function made in step 3 to open the tabs in the desired browser.
