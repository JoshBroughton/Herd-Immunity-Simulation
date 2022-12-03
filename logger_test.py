import pytest

from logger import Logger

def test_log():
    '''
    Test instantiating a Logger object and using it to write to file.
    '''
    log = Logger('log_test.txt')
    log.write_metadata(1000, 0.5, 'Ebola', 0.70, 0.25)
    log.log_interactions(2, 1000, 250)
    log.log_infection_survival(2, 1000, 200)
    log.log_final(300, 700, 100, 10000, 5000)
    
    with open('log_test.txt') as log_file:
        lines = log_file.readlines()
        assert lines[0] == 'METADATA: Population size: 1000\tVaccination Percentage: 0.5\tVirus: Ebola\tMortality Rate: 0.7 Reproduction Number: 0.25\n'
        assert lines[1] == 'Step Number: 2 Number of Interactions: 1000 Number of New Infections: 250\n'
        assert lines[2] == 'Step Number: 2 Surviving Population Count: 1000 Number of New Fatalities: 200\n'
        assert lines[3] == 'The simulation has ended with 300 survivors and a total of 700 deaths. Vaccines protected from infection during 100 interactions, out of a total of 10000 interactions.\n'
        assert lines[4] == 'A total of 5000 infections occured.'