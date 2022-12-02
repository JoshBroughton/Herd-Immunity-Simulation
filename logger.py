class Logger(object):
    def __init__(self, file_name):
        self.file_name = file_name

    # The methods below are just suggestions. You can rearrange these or 
    # rewrite them to better suit your code style. 
    # What is important is that you log the following information from the simulation:
    # Meta data: This shows the starting situtation including:
    #   population, initial infected, the virus, and the initial vaccinated.
    # Log interactions. At each step there will be a number of interaction
    # You should log:
    #   The number of interactions, the number of new infections that occured
    # You should log the results of each step. This should inlcude: 
    #   The population size, the number of living, the number of dead, and the number 
    #   of vaccinated people at that step. 
    # When the simulation concludes you should log the results of the simulation. 
    # This should include: 
    #   The population size, the number of living, the number of dead, the number 
    #   of vaccinated, and the number of steps to reach the end of the simulation. 

    def write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate,
                       basic_repro_num):
        # TODO: Finish this method. This line of metadata should be tab-delimited
        # it should create the text file that we will store all logs in.
        # TIP: Use 'w' mode when you open the file. For all other methods, use
        # the 'a' mode to append a new log to the end, since 'w' overwrites the file.
        # NOTE: Make sure to end every line with a '/n' character to ensure that each
        # event logged ends up on a separate line!
        with open(self.file_name, 'w') as out_file:
            metadata = f'METADATA: Population size: {pop_size}\tVaccination Percentage: {vacc_percentage}\tVirus: {virus_name}\tMortality Rate: {mortality_rate} Reproduction Number: {basic_repro_num}\n'
            out_file.write(metadata)
        

    def log_interactions(self, step_number, number_of_interactions, number_of_new_infections):
        # TODO: Finish this method. Think about how the booleans passed (or not passed)
        # represent all the possible edge cases. Use the values passed along with each person,
        # along with whether they are sick or vaccinated when they interact to determine
        # exactly what happened in the interaction and create a String, and write to your logfile.
        out_string = f'Step Number: {step_number} Number of Interactions: {number_of_interactions} Number of New Infections: {number_of_new_infections}\n'
        with open(self.file_name, 'a') as out_file:
            out_file.write(out_string)

    def log_infection_survival(self, step_number, population_count, number_of_new_fatalities):
        # TODO: Finish this method. If the person survives, did_die_from_infection
        # should be False.  Otherwise, did_die_from_infection should be True.
        # Append the results of the infection to the logfile
        out_string = f'Step Number: {step_number} Surviving Population Count: {population_count} Number of New Fatalities: {number_of_new_fatalities}\n'
        with open(self.file_name, 'a') as out_file:
            out_file.write(out_string)

    def log_final(self, survivors, deaths, vaccine_saves, interactions, infections):
        out_string_1 = f'The simulation has ended with {survivors} survivors and a total of {deaths} deaths. Vaccines protected from infection '
        out_string_2 = f'during {vaccine_saves} interactions, out of a total of {interactions} interactions.\nA total of {infections} infections occured.'
        out_string = out_string_1 + out_string_2
        with open(self.file_name, 'a') as out_file:
            out_file.write(out_string)