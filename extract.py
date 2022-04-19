"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    # TODO: Load NEO data from the given CSV file.
    neos = []
    with open(neo_csv_path, 'r') as infile:
        reader = csv.reader(infile)
        next(reader)

        for row in reader:
            pdes = row[3]
            name = row[4]
            pha = row[7]
            diameter = row[15]
            near_earth_object = NearEarthObject(designation=pdes, name=name, diameter=diameter, hazardous=pha,)
            neos.append(near_earth_object)
    return neos


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param cad_json_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    # TODO: Load close approach data from the given JSON file.
    approaches = []
    with open(cad_json_path, 'r') as infile:
        file = json.load(infile)
        for line in file['data']:
            des = line[0]
            cd = line[3]
            dist = line[4]
            v_rel = line[7]
            close_approach = CloseApproach(designation=des, time=cd, distance=dist, velocity=v_rel)
            approaches.append(close_approach)
    return approaches
