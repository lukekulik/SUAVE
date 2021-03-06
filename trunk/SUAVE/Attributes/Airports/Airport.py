## @ingroup Attributes-Airports
# Analysis.py

# Created:  Mar, 2014, SUAVE Team
# Modified: Jan, 2016, M. Vegh

# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

from SUAVE.Core import Data
from SUAVE.Attributes.Atmospheres import Earth
from Runway import Runway

# ----------------------------------------------------------------------
#  Airport Data Class
# ----------------------------------------------------------------------

## @ingroup Attributes-Airports
class Airport(Data):
    """A basic airport.
    
    Assumptions:
    None
    
    Source:
    None
    """
    
    def __defaults__(self):
        """This sets the default values.
    
        Assumptions:
        None

        Source:
        N/A

        Inputs:
        None

        Outputs:
        None

        Properties Used:
        None
        """     
        
        self.tag = 'Airport'
        self.altitude = 0.0        # m
        self.atmosphere = Earth.US_Standard_1976()
        self.delta_isa = 0.0    

# ----------------------------------------------------------------------
#  Handle Linking
# ----------------------------------------------------------------------
Airport.Runway = Runway
