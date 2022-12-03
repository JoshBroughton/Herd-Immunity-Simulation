import pytest

from simulation import Simulation
from virus import Virus
from logger import Logger

# initialize a Virus to use throughout
virus = Virus('Ebola', 0.25, 0.7)
def test_constructor():
    '''
    Test that the Simulation constructor is building the instance as expected
    '''
    sim = Simulation(virus, 10000, 0.5)
    assert sim.pop_size == 10000
    assert sim.initial_infected == 1
    assert sim.virus == virus
    assert sim.vacc_percentage == 0.5
    assert sim.logger.file_name == 'output.txt'
    assert len(sim.population) == 10000
    assert len(sim.newly_infected) == 0
    assert len(sim.dead_people) == 0
    assert sim.vaccine_saves == 0
    assert sim.interactions == 0
    assert sim.infection_events == 0

def test_mortality():
    '''
    Tests mortality rate in the simulation by starting from 100% infection rate
    '''
    sim = Simulation(virus, 1000, 0, 1000)
    sim.run()
    assert sim.pop_size == 1000
    # assert a range as there will be variance
    assert 650 < len(sim.dead_people) < 750
    # check that living pop and dead pop sum to original size
    assert (len(sim.dead_people) + sim.living_population_size()) == 1000

def test_spread():
    '''
    test the spread of the virus with no vaccine using a single time step
    '''
    sim = Simulation(virus, 100, 0, 1)
    sim.time_step(1)
    # after 1 time step, expect the single infected person to have infected roughly
    # 25% (the repro rate) of the population, with a range to account for random variation
    assert 15 < sim.infection_events < 35

def test_vaccine():
    '''
    Test vaccine proeprty works as expected by giving 100% vaccine coverage
    '''
    sim = Simulation(virus, 1000, 1, 100)
    sim.run()
    # expect no infection events to have occurred
    assert sim.infection_events == 0