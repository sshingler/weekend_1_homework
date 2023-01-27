# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(pet_shop_name):
    return(pet_shop_name["name"]) 

def get_total_cash(total_cash):
    return(total_cash["admin"]["total_cash"])

def add_or_remove_cash(total_cash, cash):
    total_cash["admin"]["total_cash"] += cash

def get_pets_sold(list):
    return (list ["admin"]["pets_sold"])


def increase_pets_sold(library, number):
    library["admin"]["pets_sold"] += number

def get_stock_count (library):
    return len(library["pets"])


#function name? - get pets by breed
# parameters? - 2 - the library, the breed type
# what does function need to do? - search the 'breed' key:value for each entry in 'pets' for a specific string
#                                  
# what does function need to return? - return the number of matches 


def get_pets_by_breed(library, breed_type):
    number_of_matches = []
    for breed in library["pets"]:
        if breed ["breed"] == breed_type:
            number_of_matches.append(breed["breed"])
    return number_of_matches

    

