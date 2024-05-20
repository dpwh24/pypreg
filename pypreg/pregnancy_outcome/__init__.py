"""
This module provides functions to facilitate identifying and classifying
pregnancies from diagnostic and procedure codes.

outcomes exports the full CODE list
outcome_list exports a list of the outcome classifications
map_version_split exports 4 dataframes of outcome codes based on the CODE code_type
process_outcomes is the process to pass data in order to identify and classify pregnancy outcomes
"""

from .outcome_map import outcomes, outcome_list
from .attach_map import map_version_split
from .process_outcome import process_outcomes
