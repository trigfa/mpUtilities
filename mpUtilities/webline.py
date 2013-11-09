#!/usr/bin/env python
""" A python library for reading PTW mcc files
      Graham Arden, July 2011 """
      
import csv
import dateutil.parser

class weblinedata:
	
	"""Defines a weblinedata class with the required attributes"""
	
	def __init__(self, date, linac, modality, energy, CAX, flatness, symmetryGT, symmetryAB):		
		self.date = date
		self.linac = linac
		self.modality = modality
		self.energy = energy
		self.CAX = CAX
		self.flatness = flatness
		self.symmetryGT = symmetryGT
		self.symmetryAB = symmetryAB


def csv2webline(filename):
	
	"""Read data from a csv file and presents it as an instance of the weblinedata class	
	Use as dataset = csv2webline(file)"""
	data = csv.reader(open(filename, "rb"))

	date = []
	linac = []
	modality = []
	energy = []
	CAX = []
	flatness = []
	symmetryGT = []
	symmetryAB = []    
	data.next()  # ignore the first line (the headers)
	
	linenumber = 1
	
	for data in data:
		date.append(dateutil.parser.parse(data[0]))
		CAX.append(data[4])
		flatness.append(data[5])
		symmetryGT.append(data[6])
		symmetryAB.append(data[7])
		if linenumber == 1:
			linac.append(data[1])
			modality.append(data[2])
			energy.append(data[3])
		linenumber = linenumber+1
	webline_dataset = weblinedata(date, linac, modality, energy, CAX, flatness, symmetryGT, symmetryAB)
	return webline_dataset	
	