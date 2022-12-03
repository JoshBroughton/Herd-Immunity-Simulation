import random
import sys
# random.seed(42)
from person import Person
from logger import Logger
from virus import Virus


class Simulation(object):
    def __init__(self, virus, pop_size, vacc_percentage, initial_infected=1):
        self.logger = Logger('output.txt')
        self.virus = virus
        self.pop_size = pop_size
        self.vacc_percentage = vacc_percentage
        self.initial_infected = initial_infected
        self.population = self._create_population()
        self.newly_infected = []
        self.dead_people = []
        self.vaccine_saves = 0
        self.interactions = 0
        self.infection_events = 0

    def _create_population(self):
        number_of_infected = self.initial_infected
        number_vaccinated = self.vacc_percentage * self.pop_size
        population = []
        for i in range(0, self.pop_size):
            if number_of_infected > 0:
                population.append(Person(i, False, self.virus))
                number_of_infected -= 1
            elif number_vaccinated > 0:
                population.append(Person(i, True))
                number_vaccinated -= 1
            else:
                population.append(Person(i, False))

        return population

    def _simulation_should_continue(self):
        living = False
        infected = False

        for person in self.population:
            # if at least one person is alive and unvaccinated and at least one other person is alive and infected
            if person.is_alive and not person.is_vaccinated:
                living = True
            if person.is_alive and person.infection is not None:
                infected = True

        return living and infected

    def run(self):
        time_step_counter = 0
        should_continue = True

        self.logger.write_metadata(self.pop_size, self.vacc_percentage,
                                   self.virus.name, self.virus.mortality_rate, self.virus.repro_rate)

        while should_continue:
            time_step_counter += 1
            self.time_step(time_step_counter)
            should_continue = self._simulation_should_continue()

        self.logger.log_final(self.living_population_size(), len(
            self.dead_people), self.vaccine_saves, self.interactions, self.infection_events)

    def time_step(self, step_number):
        step_interactions = 0
        for person in self.population:
            if person.infection is not None:
                for i in range(0, 100):
                    roll = random.randint(0, len(self.population) - 1)
                    self.interaction(self.population[roll])
                    step_interactions += 1

        self.interactions += step_interactions
        # everybody previously infected rolls to survive
        new_dead = 0
        for person in self.population:
            if person.infection is not None and person.is_alive:
                outcome = person.did_survive_infection()
                if outcome is False:
                    new_dead += 1
                    self.dead_people.append(person)

        self.logger.log_interactions(
            step_number, step_interactions, len(self.newly_infected))
        self.logger.log_infection_survival(
            step_number, self.living_population_size(), new_dead)
        # infect newly infected
        self._infect_newly_infected()

    def interaction(self, random_person):
        '''
        Defines an interaction between an infeccted person and a random person; the infected_person
        arg is not required because nothing happens to them in the interaction.

        To log each individual interaction would generate hundreds of thousands of lines of text without
        much meaning. Instead, step summaries are logged.
        '''
        if not random_person.is_vaccinated and random_person.infection is None and random_person.is_alive:
            infection_roll = random.random()
            if infection_roll < self.virus.repro_rate and random_person not in self.newly_infected:
                self.newly_infected.append(random_person)
        elif random_person.is_vaccinated and random_person.infection is None and random_person.is_alive:
            self.vaccine_saves += 1

    def _infect_newly_infected(self):
        for person in self.newly_infected:
            person.infection = self.virus
            self.infection_events += 1

        self.newly_infected = []

    def living_population_size(self):
        size = 0
        for person in self.population:
            if person.is_alive == True:
                size += 1

        return size


if __name__ == "__main__":
    pop_size = int(sys.argv[1])
    vacc_percent = float(sys.argv[2])
    virus_name = sys.argv[3]
    mortality_rate = float(sys.argv[4])
    repro_rate = float(sys.argv[5])
    initial_infected = int(sys.argv[6])

    virus = Virus(virus_name, repro_rate, mortality_rate)
    sim = Simulation(virus, pop_size, vacc_percent, initial_infected)
    sim.run()
