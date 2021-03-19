import pickle

store_list = ["Chicken Rice", "Malay Food", "Salad Bar", "Indian Goodness", "Mcdonalds"]

operating_hours1 = {"Chicken Rice": 'Monday-Thursday 0800-1800\n Friday 0900-1600',
                    "Malay Food": 'Monday-Friday 0800-1900',
                    "Salad Bar": 'Monday-Friday 0800-1800\n Saturday 0900-1300',
                    "Indian Goodness": 'Monday-Thursday 0800-1800\n Friday 0900-1300',
                    "Mcdonalds": 'Monday-Sunday 0800-2100'}

queue_time_calculator = {"Chicken Rice": '3',
                        "Malay Food": '5',
                        "Salad Bar": '3',
                        "Indian Goodness": '4',
                        "Mcdonalds": '2'}

operating_hours2 = {"Chicken Rice" : {'Monday':  {'Opening' : '0800', 'Closing': '1800'},
                                     'Tuesday':   {'Opening' : '0800', 'Closing': '1800'},
                                     'Wednesday': {'Opening' : '0800', 'Closing': '1800'},
                                     'Thursday':  {'Opening' : '0800', 'Closing': '1800'},
                                     'Friday':    {'Opening' : '0900', 'Closing': '1600'},
                                     'Saturday':  {'Opening' : '0000', 'Closing': '0000'},
                                     'Sunday':    {'Opening' : '0000', 'Closing': '0000'}},
                   
                   "Malay Food" :   {'Monday':    {'Opening' : '0800', 'Closing': '1800'},
                                     'Tuesday':   {'Opening' : '0800', 'Closing': '1800'},
                                     'Wednesday': {'Opening' : '0800', 'Closing': '1800'},
                                     'Thursday':  {'Opening' : '0800', 'Closing': '1800'},
                                     'Friday':    {'Opening' : '0800', 'Closing': '1800'},
                                     'Saturday':  {'Opening' : '0000', 'Closing': '0000'},
                                     'Sunday':    {'Opening' : '0000', 'Closing': '0000'}},
                   
                   "Salad Bar" :    {'Monday':    {'Opening' : '0800', 'Closing': '1800'},
                                     'Tuesday':   {'Opening' : '0800', 'Closing': '1800'},
                                     'Wednesday': {'Opening' : '0800', 'Closing': '1800'},
                                     'Thursday':  {'Opening' : '0800', 'Closing': '1800'},
                                     'Friday':    {'Opening' : '0800', 'Closing': '1800'},
                                     'Saturday':  {'Opening' : '0000', 'Closing': '1000'},
                                     'Sunday':    {'Opening' : '0000', 'Closing': '0000'}},
                   
                   "Indian Goodness" : {'Monday': {'Opening' : '0800', 'Closing': '1800'},
                                     'Tuesday':   {'Opening' : '0800', 'Closing': '1800'},
                                     'Wednesday': {'Opening' : '0800', 'Closing': '1800'},
                                     'Thursday':  {'Opening' : '0800', 'Closing': '1800'},
                                     'Friday':    {'Opening' : '0800', 'Closing': '1800'},
                                     'Saturday':  {'Opening' : '0000', 'Closing': '1000'},
                                     'Sunday':    {'Opening' : '0000', 'Closing': '0000'}},
                   
                   "Mcdonalds" :    {'Monday':    {'Opening' : '0800', 'Closing': '2100'},
                                     'Tuesday':   {'Opening' : '0800', 'Closing': '2100'},
                                     'Wednesday': {'Opening' : '0800', 'Closing': '2100'},
                                     'Thursday':  {'Opening' : '0800', 'Closing': '2100'},
                                     'Friday':    {'Opening' : '0800', 'Closing': '2100'},
                                     'Saturday':  {'Opening' : '0800', 'Closing': '2100'},
                                     'Sunday':    {'Opening' : '0800', 'Closing': '2100'}}
                   }


menu_switch_time = {"Chicken Rice" : 0000, "Malay Food" : 0000, "Salad Bar" : 0000, "Indian Goodness" : 1200, "Mcdonalds":1200}

file_name = 'store.txt'
fileObject = open(file_name, 'wb')
pickle.dump(store_list, fileObject)
pickle.dump(operating_hours1, fileObject)
pickle.dump(queue_time_calculator, fileObject)
pickle.dump(operating_hours2, fileObject)
pickle.dump(menu_switch_time, fileObject)
fileObject.close()

fileObject = open(file_name, 'rb')
store_list = pickle.load(fileObject)
operating_hours1 = pickle.load(fileObject)
queue_time_calculator = pickle.load(fileObject)
operating_hours2 = pickle.load(fileObject)
menu_switch_time = pickle.load(fileObject)
print(store_list)
print(operating_hours1)
print(queue_time_calculator)
print(operating_hours2)
print(menu_switch_time)