class Virus(object):
    # Properties and attributes of the virus used in Simulation.
    def __init__(self, name, repro_rate, mortality_rate):
        # Define the attributes of your your virus
        self.name = name
        self.repro_rate = repro_rate
        self.mortality_rate = mortality_rate


# Test this class
if __name__ == "__main__":
    # Test your virus class by making an instance and confirming 
    # it has the attributes you defined
    virus = Virus("HIV", 0.8, 0.3)
    assert virus.name == "HIV"
    assert virus.repro_rate == 0.8
    assert virus.mortality_rate == 0.3

    virus_2 = Virus('SARS-CoV-2', 0.3, 0.02)
    assert virus_2.name == 'SARS-CoV-2'
    assert virus_2.repro_rate == 0.3
    assert virus_2.mortality_rate == 0.02

    virus_3 = Virus('Bubonic Plague', 0.1, 0.6)
    assert virus_3.name == 'Bubonic Plague'
    assert virus_3.repro_rate == 0.1
    assert virus_3.mortality_rate == 0.6
