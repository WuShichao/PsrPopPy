#!/usr/bin/python

class Population:

    """
    Class to describe a pulsar population
    
    """

    def __init__(self,
                 pDistType=None,
                 radialDistType=None,
                 pmean=None,
                 psigma=None,
                 simean=None,
                 sisigma=None,
                 lummean=None,
                 lumsigma=None,
                 zscale=None,
                 electronModel=None,
                 ref_freq=1400.0):

        """Initialise the population object."""

        self.population = []

        # distribution types
        self.pDistType = pDistType
        self.radialDistType = radialDistType
        self.electronModel=electronModel

        # distribution values
        self.pmean = pmean
        self.psigma = psigma
        
        self.simean = simean
        self.sisigma = sisigma

        self.lummean = lummean
        self.lumsigma = lumsigma

        self.zscale = zscale

        self.ref_freq = ref_freq

        # non-"properties"
        self.ndet = 0

    def __str__(self):
        """Define how we print the population to screen."""
        s = "Population model:"
        s = '\n\t'.join([s, "Population size = {0}".format(self.size())])
        s = '\n\t'.join([s, "Reference Frequency = {0} MHz".format(self.ref_freq)])
        
        s = '\n\n\t'.join([s, "Mean period = {0}".format(self.pmean)])
        s = '\n\t'.join([s, "Period std dev = {0}".format(self.psigma)])
        s = '\n\t'.join([s, "Spectral index mean = {0}".format(self.simean)])
        s = '\n\t'.join([s, "Spectral index std dev = {0}".format(self.sisigma)])
        s = '\n\t'.join([s, "Luminosity mean = {0}".format(self.lummean)])
        s = '\n\t'.join([s, "Luminosity std dev = {0}".format(self.lumsigma)])

        s = '\n\n\t'.join([s, "Period Distribution = {0}".format(self.pDistType)])
        s = '\n\t'.join([s, "Radial distribution type = {0}".format(self.radialDistType)])
        s = '\n\t'.join([s, "Electron Model = {0}".format(self.electronModel)])

        return s

    def size(self):
        """Returns the number of pulsars in the object."""
        return len(self.population)