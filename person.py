import random
# random.seed(42)
from virus import Virus


class Person(object):
    '''
    Person class; defines a person for the purposes of a herd immunity simulation
    '''

    def __init__(self, _id, is_vaccinated, infection=None):
        # A person has an id, is_vaccinated and possibly an infection
        self._id = _id  # int
        self.is_alive = True
        self.is_vaccinated = is_vaccinated
        self.infection = infection

    def did_survive_infection(self):
        '''For a person who is infected, generate a random number;
        if it is less than the mortality_rate of the virus (expressed as
        a decimal), the person dies; else they survive and are now immune'''
        if self.infection is not None:
            survival_roll = random.random()
            if survival_roll < self.infection.mortality_rate:
                self.is_alive = False
                self.infection = None
                return False
            else:
                self.is_vaccinated = True
                self.infection = None
                return True


if __name__ == "__main__":
    # This section is incomplete finish it and use it to test your Person class
    vaccinated_person = Person(1, True)
    assert vaccinated_person._id == 1
    assert vaccinated_person.is_alive is True
    assert vaccinated_person.is_vaccinated is True
    assert vaccinated_person.infection is None

    # Create an unvaccinated person and test their attributes
    unvaccinated_person = Person(2, False)
    # TODO Test unvaccinated_person's attributes here...
    assert unvaccinated_person._id == 2
    assert unvaccinated_person.is_vaccinated is False
    assert unvaccinated_person.is_alive is True
    assert unvaccinated_person.infection is None

    virus = Virus("Dysentery", 0.7, 0.2)
    # Create a Person object and give them the virus infection
    infected_person = Person(3, False, virus)

    assert infected_person._id == 3
    assert infected_person.is_vaccinated is False
    assert infected_person.is_alive is True
    assert infected_person.infection == virus
    # You need to check the survival of an infected person. Since the chance
    # of survival is random you need to check a group of people.
    # Create a list to hold 100 people. Use the loop below to make 100 people
    people = []
    for i in range(1, 100):
        people.append(Person(i, False, virus))

    # Now that you have a list of 100 people. Resolve whether the Person
    # survives the infection or not by looping over the people list.

    for person in people:
        person.did_survive_infection()

    # Count the people that survived and did not survive:
    did_survive = 0
    did_not_survive = 0

    for person in people:
        if person.is_alive:
            did_survive += 1
        else:
            did_not_survive += 1

    print(f'Survived: {did_survive}')
    print(f'Did not survive: {did_not_survive}')

    # Stretch challenge!
    # Check the infection rate of the virus by making a group of
    # unifected people.
    people = []
    for i in range(1, 100):
        people.append(Person(i, False, None))

    for person in people:
        roll = random.random()
        if roll < virus.repro_rate:
            person.infection = virus
    infected = 0
    not_infected = 0

    for person in people:
        if person.infection:
            infected += 1
        else:
            not_infected += 1

    print(f'Infected: {infected}')
    print(f'Not Infected: {not_infected}')
