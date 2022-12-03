class Logger(object):
    '''
    
    '''
    def __init__(self, file_name):
        self.file_name = file_name

    def write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate,
                       basic_repro_num):
        with open(self.file_name, 'w') as out_file:
            metadata = f'METADATA: Population size: {pop_size}\tVaccination Percentage: {vacc_percentage}\tVirus: {virus_name}\tMortality Rate: {mortality_rate} Reproduction Number: {basic_repro_num}\n'
            out_file.write(metadata)

    def log_interactions(self, step_number, number_of_interactions, number_of_new_infections):
        out_string = f'Step Number: {step_number} Number of Interactions: {number_of_interactions} Number of New Infections: {number_of_new_infections}\n'
        with open(self.file_name, 'a') as out_file:
            out_file.write(out_string)

    def log_infection_survival(self, step_number, population_count, number_of_new_fatalities):
        out_string = f'Step Number: {step_number} Surviving Population Count: {population_count} Number of New Fatalities: {number_of_new_fatalities}\n'
        with open(self.file_name, 'a') as out_file:
            out_file.write(out_string)

    def log_final(self, survivors, deaths, vaccine_saves, interactions, infections):
        out_string_1 = f'The simulation has ended with {survivors} survivors and a total of {deaths} deaths. Vaccines protected from infection '
        out_string_2 = f'during {vaccine_saves} interactions, out of a total of {interactions} interactions.\nA total of {infections} infections occured.'
        out_string = out_string_1 + out_string_2
        with open(self.file_name, 'a') as out_file:
            out_file.write(out_string)
