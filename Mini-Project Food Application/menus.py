import pickle

salad_menu_odd ="Heaven and Earth $6.50\n Gardens by The Bay $5.50\n Chicken Salad $4.50"

salad_menu_even ="Vege salad $4.00 \n Gardens by The Bay $5.50 \n Chicken Salad $4.50"

malay_menu_odd = "Nasi Lemak $3.50 \n Mee Siam $3.00 \n Mee Rebus $3.00\n Mee Soto $2.50"

malay_menu_even ="Nasi Lemak $3.50\n Mee Siam $3.00\n Chicken Satay $0.50\n Mutton Satay $0.70\n Beef Satay $0.60"

indian_menu_am_odd='Odd breakfast special $5.50 \n Plain Prata $0.70\n Egg Prata $1.00\n Onion Prata $1.00\n Ham Prata $1.20'

indian_menu_am_even='Even breakfast special $4.50\n Plain Prata $0.70\n Egg Prata $1.00\n Onion Prata $1.00\n Ham Prata $1.20'

indian_menu_pm_odd ="Nasi Goreng $6.00\n Mee Goreng $5.50\n Bee Hoon Goreng $6.00 \n Paper Dosai $4.00 \n Cheese Dosai $4.00"

indian_menu_pm_even ="Paper Dosai $4.00 \n Cheese Dosai $4.00 \n Murtabak $6.50 \n Chicken Briyani $7.50"

chicken_rice_menu_odd = 'Roasted Chicken Rice $3.50 \n Steam Chicken Rice $10.50 \n Duck Noodle $4.00'

chicken_rice_menu_even ='Roasted Chicken Rice $3.50 \n Steam Chicken Rice $10.50 \n Roasted Chicken Noodle $4.00'

mcdonalds_menu_pm = 'The Big Mac $4.50\n McChicken $3.00 \n Doublecheese Burger $5.00'

mcdonalds_menu_am = 'the big brekfast $7.50 \n Sausage Egg McMuffin $3.00 \n Hash Brown $1.00'

menu = {'Chicken Rice': {'odd':  {'am': chicken_rice_menu_odd,
                                   'pm': chicken_rice_menu_odd},
                          'even': {'am': chicken_rice_menu_even,
                                   'pm': chicken_rice_menu_even}},
                          
        'Malay Food':    {'odd':  {'am': malay_menu_odd,
                                   'pm': malay_menu_odd},
                          'even': {'am': malay_menu_even,
                                   'pm': malay_menu_even}},
                         
        'Salad Bar':    {'odd':   {'am': salad_menu_odd,
                                   'pm': salad_menu_odd},
                          'even': {'am': salad_menu_even,
                                   'pm': salad_menu_even}},

        'Indian Goodness': {'odd':{'am': indian_menu_am_odd,
                                   'pm': indian_menu_pm_odd},
                          'even': {'am': indian_menu_am_even,
                                   'pm': indian_menu_pm_even}},

        'Mcdonalds':    {'odd':   {'am': mcdonalds_menu_am,
                                   'pm': mcdonalds_menu_pm},
                          'even': {'am': mcdonalds_menu_am,
                                   'pm': mcdonalds_menu_pm}},
        }
 
file_name = 'menu.txt'
fileObject = open(file_name, 'wb')
pickle.dump(menu, fileObject)
fileObject.close()

fileObject = open(file_name, 'rb')
menu = pickle.load(fileObject)
print(menu)
