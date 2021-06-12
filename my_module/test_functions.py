"""Test for my functions.
"""

from classes import *
from functions import *

def test_class_construction():
    
    """Test function for class constructor
    make sure the input assignment is correctly recorded
    """

    # smaller dataset for easier testing
    test_inst = CBInstance([1,2,3,4])
    
    assert test_inst.get_arr() == [1,2,3,4]
    

def test_getter_setter():
    
    """Test function for getters and setters
    Make sure attributes can be changed and be retrived
    """
    
    test_inst = CBInstance([1,2,3,4])
    
    # Set new values for attributes
    test_inst.set_score(10)
    test_inst.set_arr([1,1,4,4])
    
    assert test_inst.get_score() == 10
    assert test_inst.get_arr() == [1,1,4,4]
    
    
def test_battle():
    
    """Test functions for battles
    Make sure it returns correct result for a battle
    """
    
    test_inst_1 = CBInstance([1,2,3,4])
    test_inst_2 = CBInstance([1,1,2,6])
    test_inst_3 = CBInstance([1,3,2,4])
    
    # test for all possible results
    assert test_inst_1.battle(test_inst_2) == [1,0]
    assert test_inst_2.battle(test_inst_3) == [0.5,0.5]
    assert test_inst_2.battle(test_inst_1) == [0,1]

    
def test_grade_inst():
    
    """Test function for grade_inst()
    Make sure it returns correct total score when an arrangement
    is battled against a population.
    """
    
    test_data = [[1,2,3,4],[1,0,4,5],[10,0,0,0],[8,0,0,2],[7,2,1,0]]
    
    test_population = []
    
    # Construct test population
    for arr in test_data:
        cur_inst = CBInstance(arr)
        test_population.append(cur_inst)
        
    test_inst = CBInstance([1,2,3,4])
    
    assert grade_inst(test_inst, test_population) == 3.5

                 
    