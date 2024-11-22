""" Write a function that
returns a new list of updated damages
where the recorded data is converted to float values and the missing data is retained as
 "Damages not recorded """

def damage(arg1):
    M={
        "M": 1000000,
        "B": 1000000000}
    dict=[]
    for i in arg1:
        if i=="Damages not recorded":
            dict.append(i)
            continue
        else:
            letter=i[-1]
            if letter in M:
                newnumber=float(i[:-1])
                multinumber=M[letter]
                x=newnumber*multinumber
                dict.append(x)
    return dict
""" Write a function that constructs a 
dictionary made out of the lists"""
def newdict(arg1,arg2,arg3,arg4,arg5,arg6,arg7):
    hurricanes={}
    for i in range(len(names)):
        hurricane={"Name":names[i],"Month":months[i],"Year":years[i],"Max Wind":max_sustained_winds[i],
                   "Area_affected":areas_affected[i],"Damage":damage1[i],"DeathNumber":deaths[i]}
        hurricanes[names[i]]=hurricane
    return hurricanes
"""Write a function that converts the current dictionary of hurricanes 
to a new dictionary, where the keys are years and the values are lists containing a dictionary 
for each hurricane that occurred in that year """
def groupedbyyear(arg1):
    GroupByYear={}
    for name,year in arg1.items():
        current_year=year["Year"]
        if current_year not in GroupByYear:
            GroupByYear[current_year]=[]
        if current_year in GroupByYear and year not in  GroupByYear.values():
            GroupByYear[current_year].append(year)
    return GroupByYear
""" Write a function that counts how often each area is listed as an 
affected area of a hurricane. Store and return the results in a dictionary where the keys are the 
affected areas and the values are counts of how many times the areas were affected. """
def affectedarea(arg1):
    dict={}
    for i in arg1.values():
        for area in i['Area_affected']:
            if area not in dict:
                dict[area]=1
            else:
                dict[area]+=1
    return dict

"""Write a function that finds the area affected by the most hurricanes, and how often it was hit."""
def damage(arg1):
    max_damage = 0
    max_damage_hurricane = None
    for value in arg1.values():
        damage = value[0]['Damage']
        if damage != "Damages not recorded":
            if damage > max_damage:
                max_damage = damage
                max_damage_hurricane = value[0]['Name']
    return max_damage_hurricane, max_damage
"""Write a function that finds the hurricane that caused the greatest number of deaths, and how many deaths it caused."""
def numberofdeaths(arg1):
    nameofarea=None
    max_number=float('-inf')
    for name,number in arg1.items():
        death = number["DeathNumber"]
        if death > max_number:
            max_number=death
            nameofarea=name
    return nameofarea,max_number
""" Write a function that rates hurricanes on a mortality scale according to the following ratings, 
where the key is the rating and the value is the upper bound of deaths for that rating."""
def moralityScale(arg1):
    mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000,
                      5: 500000}
    hurricanes_by_mortality = {0:[],1:[],2:[],3:[],4:[],5:[]}
    for name,death in arg1.items():
        numberofdeath=death["DeathNumber"]
        for key,value in mortality_scale.items():
            if numberofdeath<value:
                hurricanes_by_mortality[key].append(name)
                break
    return hurricanes_by_mortality