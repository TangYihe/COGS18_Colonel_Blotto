"""A collection of function for doing my project."""
import math
from classes import *


def grade_inst(inst, population):
    """Computes the total score an instance (its arrangement)
    earns when battling against each instance in a given 
    population.
    
    Parameters
    ----------
    inst: CBInstance. Target instance to compute score.
    population: list of CBInstance. Target population to battle against.
    
    Returns
    ----------
    int. The total score inst earns after battling with each instance in
    the input population.
    """
    
    # Initialize to keep track of score 
    inst_score = 0
    
    # Battle against each instance in population
    for i in range(len(population)):
        battle_result = inst.battle(population[i])
        inst_score += battle_result[0]
        
    # Also record the score in the instance
    inst.set_score(inst_score)

    return inst_score


def get_medians(population, percentage=80):
    """ Computes for each castle, how many knight is needed
    to exceed a certain percentage of arrangments in population
    on that castle.
    
    Parameters
    ----------
    population: list of CBInstance. The population of arrangments 
    to exceed
    percentage: int. The percentage we want to exceed. Remove % sign.
    
    Returns
    ----------
    list of int. Each position (0 - 9) representing number of knights
    to exceed (percentage)% arrangments in population on castle
    position + 1 (1 - 10).
    """
    
    cas=[[],[],[],[],[],[],[],[],[],[]]
    
    # get the number of knights in each castle
    # from each arrangements in population
    for ind in population:
        arr = ind.get_arr()
        
        for i in range(10):
            cas[i].append(arr[i])

    # sort number of knights in each castle
    for i in range(10):
        cas[i] = sorted(cas[i])

    # determine a percentage
    perc = math.floor(len(cas[0])*percentage/100)
     
    medians = [cas[i][perc] for i in range(10)]
    
    return medians


def perc_greedy(population, percentage=80):
    """Our main algorithm. Finds an arrangment by trying to 
    exceed a certain percentage of arrangments in population
    on as many castles as possible.
    
    Parameters
    -----------
    population: list of CBInstance. The population trying to 
    exceed.
    percentage: int. The percentage we want to exceed. Remove % sign.
    
    Returns
    -----------
    CBInstance. An instance whose arrangement is what we got from
    the algorithm. Score is total score when battling against
    input population.
    """
    

    #initialization
    res_arr = [2] * 10
    total_knights = 80

    medians = get_medians(population, percentage);

    while(total_knights > 0):
        
        # find "easiest" to acheive
        ind = medians.index(min(medians))

        # calculate the number of knights to assign to that castle
        assign = min(total_knights, medians[ind]-res_arr[ind] + 1)

        # make assignment
        res_arr[ind] += assign
        total_knights -= assign

        # mark that castle as "done"
        medians[ind] = 100
     
    # get the score of result inst against input population
    res_inst = CBInstance(res_arr)
    res_score = grade_inst(res_inst, population)
    
    return res_inst

    
