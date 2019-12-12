import random
import string

def printing_question(input_choice):
    """
    Answers basic questions regarding printing.
    """
    
    if input_choice.lower().strip() == "a":
        print('\n')
        print("1. Pull up the document on one of the library's computers")
        print("2. Select print and choose between the black and white or color printer")
        print("3. Enter the informaiton required on the window pop up")
        print("4. Go to the print release station and swipe your card")
        print("*If it asks for a PIN and you have never been given one, just press Continue*")            
        print("5. Select the documents you would like to print")
        
    elif input_choice.lower().strip() == "b":
        print('\n')
        print('Wireless printing server:')
        print('https://imprints-print.ucsd.edu/cps/')
        
    elif input_choice.lower().strip() == "c":
        print('\n')
        print('Black and white $0.10/page (single-sided) or $0.20/page (double-sided)')
        print('Color $0.40/page ($0.80 double-sided).')
        
    else: 
        print('\n')
        print("Not a valid choice")

def study_room(input_choice):
    """
    Answers basic questions regarding study room reservations
    """
    
    if input_choice.lower().strip() == "a":
        print('\n')
        print('Study room reservation portal:')
        print('https://library.ucsd.edu/visit/study-spaces/reserve-study-room.html')
        
    elif input_choice.lower().strip() == "b":
        print('\n')
        print('If a study room is unoccupied 10 minutes after the reservation has started, any patron can utilize the room.')
        
    else: 
        print('\n')
        print("Not a valid choice")

def library_hours(input_choice):
    """
    Answers basic questions regarding library hours
    """
   
    if input_choice.lower().strip() == "a":
        print('\n')
        print('Monday - Thursday: 8:00AM - 12:00AM')
        print('Friday: 8:00AM - 6:00PM')
        print('Saturday: 10:00AM - 6:00PM')
        print('Sunday: 12:00PM - 12:00AM')
        
    elif input_choice.lower().strip() == "b":
        print('\n')
        print('Monday - Thursday: 8:00AM - 12:00AM')
        print('Friday: 8:00AM - 6:00PM')
        print('Saturday: 10:00AM - 6:00PM')
        print('Sunday: 12:00PM - 12:00AM')
        
    elif input_choice.lower().strip() == "c":
        print('\n')
        print('Monday - Thursday: 8:00AM - 8:00PM')
        print('Friday: 8:00AM - 6:00PM')
        print('Library closed from Dec. 21 - Jan. 1')
        
    else: 
        print('\n')
        print('Not a valid choice')
            
            