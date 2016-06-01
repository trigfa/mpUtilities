#!/usr/bin/env python
""" A python library for reading PTW mcc files
      Graham Arden, July 2011 """

import csv
from lxml import etree
import dateutil.parser
import pandas as pd
import numpy as np

class weblinedata:

    """Defines a weblinedata class with the required attributes"""

    def __init__(self, date, linac, modality, energy, fieldsize, CAX, flatness, symmetryGT, symmetryAB, bqf, measCAX,
    G10, L10, T10, R10, G20, L20, T20, R20, E1, E2, E3, E4, Temp, Pressure):
        self.date = date
        self.linac = linac
        self.modality = modality
        self.energy = energy
        self.fieldsize = fieldsize
        self.CAX = CAX
        self.flatness = flatness
        self.symmetryGT = symmetryGT
        self.symmetryAB = symmetryAB
        # Added the extra lines we didn't have previously
        self.bqf = bqf
        self.measCAX = measCAX
        self.G10 = G10
        self.L10 = L10
        self.T10 = T10
        self.R10 = R10
        self.G20 = G20
        self.L20 = L20
        self.T20 = T20
        self.R20 = R20
        self.E1 = E1
        self.E2 = E2
        self.E3 = E3
        self.E4 = E4
        self.Temp = Temp
        self.Pressure = Pressure


def parse_qcw(filename, Linac, Modality="Photons", Energy="6", Fieldsize="100x100"):
    """Read data from a qcw file and presents it as an instance of the weblinedata class
    Use as dataset = parse_qcw(file)"""

    # open the data file
    xmlData = etree.parse(filename)

    trendData = xmlData.findall("//TrendData")

    date = []
    time = []
    linac = []
    modality = []
    energy = []
    fieldsize = []
    CAX = []
    flatness = []
    symmetryGT = []
    symmetryAB = []
    bqf = []
    measCAX = []
    G10 = []
    L10 = []
    T10 = []
    R10 = []
    G20 = []
    L20 = []
    T20 = []
    R20 = []
    E1 = []
    E2 = []
    E3 = []
    E4 = []
    Temp = []
    Pressure = []


    for meas in trendData:

        linac_id = meas.findtext("Worklist/AdminData/AdminValues/TreatmentUnit")
        modality_id = meas.findtext("Worklist/AdminData/AdminValues/Modality")
        energy_id = meas.findtext("Worklist/AdminData/AdminValues/Energy")
        fieldsize_id = meas.findtext("Worklist/AdminData/AdminValues/Fieldsize")

        if linac_id == Linac:
            if modality_id == Modality:
                if energy_id == Energy:
                    if fieldsize_id == Fieldsize:

                        # first, get the data in the "tags" of the record
                        # need to split datetime into separate date and time fields
                        # names starting read_ are the raw data from the qw file.
                        read_measDate = meas.attrib['date']
                        read_date = dateutil.parser.parse(read_measDate)
                        date.append(read_date)

                        read_TreatmentUnit = meas.findtext("Worklist/AdminData/AdminValues/TreatmentUnit")
                        linac.append(read_TreatmentUnit)

                        read_Modality = meas.findtext("Worklist/AdminData/AdminValues/Modality")
                        modality.append(read_Modality)

                        read_Energy = meas.findtext("Worklist/AdminData/AdminValues/Energy")
                        energy.append(read_Energy)

                        read_Fieldsize = meas.findtext("Worklist/AdminData/AdminValues/Fieldsize")
                        fieldsize.append(read_Fieldsize)

                        # measured values
                        read_CAX = meas.findtext("MeasData/AnalyzeValues/CAX/Value")
                        if read_CAX == "0.0000E+00":
                            read_CAX = ""
                        else:
                            read_CAX = float(read_CAX)
                        CAX.append(read_CAX)

                        read_Flatness = meas.findtext("MeasData/AnalyzeValues/Flatness/Value")
                        if read_Flatness == "0.0000E+00":
                            read_Flatness = ""
                        else:
                            read_Flatness = float(read_Flatness)
                        flatness.append(read_Flatness)

                        read_SymmetryGT = meas.findtext("MeasData/AnalyzeValues/SymmetryGT/Value")
                        if read_SymmetryGT == "0.0000E+00":
                            read_SymmetryGT = ""
                        else:
                            read_SymmetryGT = float(read_SymmetryGT)
                        symmetryGT.append(read_SymmetryGT)

                        read_SymmetryAB = meas.findtext("MeasData/AnalyzeValues/SymmetryLR/Value")
                        if read_SymmetryAB == "0.0000E+00":
                            read_SymmetryAB = ""
                        else:
                            read_SymmetryAB = float(read_SymmetryAB)
                        symmetryAB.append(read_SymmetryAB)

                        read_BQF = meas.findtext("MeasData/AnalyzeValues/BQF/Value")
                        if read_BQF == "0.0000E+00":
                            read_BQF = ""
                        else:
                            read_BQF = float(read_BQF)
                        bqf.append(read_BQF)

                        # raw data from each of the chambers
                        read_measCAX = meas.findtext("MeasData/MeasValues/CAX/Value")
                        measCAX.append(read_measCAX)

                        read_G10 = meas.findtext("MeasData/MeasValues/G10/Value")
                        G10.append(read_G10)
                        read_L10 = meas.findtext("MeasData/MeasValues/L10/Value")
                        L10.append(read_L10)
                        read_T10 = meas.findtext("MeasData/MeasValues/T10/Value")
                        T10.append(read_T10)
                        read_R10 = meas.findtext("MeasData/MeasValues/R10/Value")
                        R10.append(read_R10)
                        read_G20 = meas.findtext("MeasData/MeasValues/G20/Value")
                        G20.append(read_G20)
                        read_L20 = meas.findtext("MeasData/MeasValues/L20/Value")
                        L20.append(read_L20)
                        read_T20 = meas.findtext("MeasData/MeasValues/T20/Value")
                        T20.append(read_T20)
                        read_R20 = meas.findtext("MeasData/MeasValues/R20/Value")
                        R20.append(read_R20)
                        read_E1 = meas.findtext("MeasData/MeasValues/E1/Value")
                        E1.append(read_E1)
                        read_E2 = meas.findtext("MeasData/MeasValues/E2/Value")
                        E2.append(read_E2)
                        read_E3 = meas.findtext("MeasData/MeasValues/E3/Value")
                        E3.append(read_E3)
                        read_E4 = meas.findtext("MeasData/MeasValues/E4/Value")
                        E4.append(read_E4)
                        read_Temp = meas.findtext("MeasData/MeasValues/Temp/Value")
                        Temp.append(read_Temp)
                        read_Pressure = meas.findtext("MeasData/MeasValues/Pressure/Value")
                        Pressure.append(read_Pressure)
                    else:
                        pass
                else:
                    pass
            else:
                pass
        else:
            pass

    webline_dataset = weblinedata(date, linac, modality, energy, fieldsize, CAX, flatness, symmetryGT, symmetryAB, bqf, measCAX,
                                  G10, L10, T10, R10, G20, L20, T20, R20, E1, E2, E3, E4, Temp, Pressure)
    return webline_dataset

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

def qcw_to_df(filename):
    """Read data from a qcw file and returns a Pandas DataFrame
    Use as dataset = qcw_to_df(file)"""

    # the dictionary 'Parameters' contains the location of each parameter in our xml file
    Parameters = {"TreatmentUnit":("Worklist/AdminData/AdminValues/TreatmentUnit"),
              "Modality":("Worklist/AdminData/AdminValues/Modality"),
              "Energy":("Worklist/AdminData/AdminValues/Energy"),
              "FieldSize":("Worklist/AdminData/AdminValues/Fieldsize"),
              "SDD":("Worklist/AdminData/AdminValues/SDD"),
              "Gantry":("Worklist/AdminData/AdminValues/Gantry"),
              "Wedge":("Worklist/AdminData/AdminValues/Wedge"),
              "MU":("Worklist/AdminData/AdminValues/MU"),
              "My":("Worklist/AdminData/AdminValues/My"),
              "AnalyzeParametersCAXMin":("Worklist/AdminData/AnalyzeParams/CAX/Min"),
              "AnalyzeParametersCAXMax":("Worklist/AdminData/AnalyzeParams/CAX/Max"),
              "AnalyzeParametersCAXTarget":("Worklist/AdminData/AnalyzeParams/CAX/Target"),
              "AnalyzeParametersCAXNorm":("Worklist/AdminData/AnalyzeParams/CAX/Norm"),
              "AnalyzeParametersFlatnessMin":("Worklist/AdminData/AnalyzeParams/Flatness/Min"),
              "AnalyzeParametersFlatnessMax":("Worklist/AdminData/AnalyzeParams/Flatness/Max"),
              "AnalyzeParametersFlatnessTarget":("Worklist/AdminData/AnalyzeParams/Flatness/Target"),
              "AnalyzeParametersFlatnessNorm":("Worklist/AdminData/AnalyzeParams/Flatness/Norm"),
              "AnalyzeParametersSymmetryGTMin":("Worklist/AdminData/AnalyzeParams/SymmetryGT/Min"),
              "AnalyzeParametersSymmetryGTMax":("Worklist/AdminData/AnalyzeParams/SymmetryGT/Max"),
              "AnalyzeParametersSymmetryGTTarget":("Worklist/AdminData/AnalyzeParams/SymmetryGT/Target"),
              "AnalyzeParametersSymmetryGTNorm":("Worklist/AdminData/AnalyzeParams/SymmetryGT/Norm"),
              "AnalyzeParametersSymmetryLRMin":("Worklist/AdminData/AnalyzeParams/SymmetryLR/Min"),
              "AnalyzeParametersSymmetryLRMax":("Worklist/AdminData/AnalyzeParams/SymmetryLR/Max"),
              "AnalyzeParametersSymmetryLRTarget":("Worklist/AdminData/AnalyzeParams/SymmetryLR/Target"),
              "AnalyzeParametersSymmetryLRNorm":("Worklist/AdminData/AnalyzeParams/SymmetryLR/Norm"),
              "AnalyzeParametersBQFMin":("Worklist/AdminData/AnalyzeParams/BQF/Min"),
              "AnalyzeParametersBQFMax":("Worklist/AdminData/AnalyzeParams/BQF/Max"),
              "AnalyzeParametersBQFTarget":("Worklist/AdminData/AnalyzeParams/BQF/Target"),
              "AnalyzeParametersBQFNorm":("Worklist/AdminData/AnalyzeParams/BQF/Norm"),
              "AnalyzeParametersWedgeMin":("Worklist/AdminData/AnalyzeParams/Wedge/Min"),
              "AnalyzeParametersWedgeMax":("Worklist/AdminData/AnalyzeParams/Wedge/Max"),
              "AnalyzeParametersWedgeTarget":("Worklist/AdminData/AnalyzeParams/Wedge/Target"),
              "AnalyzeParametersWedgeNorm":("Worklist/AdminData/AnalyzeParams/Wedge/Norm"),
              "MeasDataMeasValuesCAXValue":("MeasData/MeasValues/CAX/Value"),
              "MeasDataMeasValuesCAXValid":("MeasData/MeasValues/CAX/Valid"),
              "MeasDataMeasValuesG10Value":("MeasData/MeasValues/G10/Value"),
              "MeasDataMeasValuesG10Valid":("MeasData/MeasValues/G10/Valid"),
              "MeasDataMeasValuesL10Value":("MeasData/MeasValues/L10/Value"),
              "MeasDataMeasValuesL10Valid":("MeasData/MeasValues/L10/Valid"),
              "MeasDataMeasValuesT10Value":("MeasData/MeasValues/T10/Value"),
              "MeasDataMeasValuesT10Valid":("MeasData/MeasValues/T10/Valid"),
              "MeasDataMeasValuesR10Value":("MeasData/MeasValues/R10/Value"),
              "MeasDataMeasValuesR10Valid":("MeasData/MeasValues/R10/Valid"),
              "MeasDataMeasValuesG20Value":("MeasData/MeasValues/G20/Value"),
              "MeasDataMeasValuesG20Valid":("MeasData/MeasValues/G20/Valid"),
              "MeasDataMeasValuesL20Value":("MeasData/MeasValues/L20/Value"),
              "MeasDataMeasValuesL20Valid":("MeasData/MeasValues/L20/Valid"),
              "MeasDataMeasValuesT20Value":("MeasData/MeasValues/T20/Value"),
              "MeasDataMeasValuesT20Valid":("MeasData/MeasValues/T10/Valid"),
              "MeasDataMeasValuesR20Value":("MeasData/MeasValues/R20/Value"),
              "MeasDataMeasValuesR20Valid":("MeasData/MeasValues/R20/Valid"),
              "MeasDataMeasValuesE1Value":("MeasData/MeasValues/E1/Value"),
              "MeasDataMeasValuesE1Valid":("MeasData/MeasValues/E1/Valid"),
              "MeasDataMeasValuesE2Value":("MeasData/MeasValues/E2/Value"),
              "MeasDataMeasValuesE2Valid":("MeasData/MeasValues/E2/Valid"),
              "MeasDataMeasValuesE3Value":("MeasData/MeasValues/E3/Value"),
              "MeasDataMeasValuesE3Valid":("MeasData/MeasValues/E3/Valid"),
              "MeasDataMeasValuesE4Value":("MeasData/MeasValues/E4/Value"),
              "MeasDataMeasValuesE4Valid":("MeasData/MeasValues/E4/Valid"),
              "MeasDataMeasValuesTempValue":("MeasData/MeasValues/Temp/Value"),
              "MeasDataMeasValuesTempValid":("MeasData/MeasValues/Temp/Valid"),
              "MeasDataMeasValuesPressureValue":("MeasData/MeasValues/Pressure/Value"),
              "MeasDataMeasValuesPressureValid":("MeasData/MeasValues/Pressure/Valid"),
              "MeasDataMeasValuesCAXRateValue":("MeasData/MeasValues/CAXRate/Value"),
              "MeasDataMeasValuesCAXRateValid":("MeasData/MeasValues/CAXRate/Valid"),
              "MeasDataMeasValuesExpTimeValue":("MeasData/MeasValues/ExpTime/Value"),
              "MeasDataMeasValuesExpTimeValid":("MeasData/MeasValues/ExpTime/Valid"),
              "MeasDataAnalyzeValuesCAXValue":("MeasData/AnalyzeValues/CAX/Value"),
              "MeasDataAnalyzeValuesCAXValid":("MeasData/AnalyzeValues/CAX/Valid"),
              "MeasDataAnalyzeValuesFlatnessValue":("MeasData/AnalyzeValues/Flatness/Value"),
              "MeasDataAnalyzeValuesFlatnessValid":("MeasData/AnalyzeValues/Flatness/Valid"),
              "MeasDataAnalyzeValuesSymmetryGTValue":("MeasData/AnalyzeValues/SymmetryGT/Value"),
              "MeasDataAnalyzeValuesSymmetryGTValid":("MeasData/AnalyzeValues/SymmetryGT/Valid"),
              "MeasDataAnalyzeValuesSymmetryLRValue":("MeasData/AnalyzeValues/SymmetryLR/Value"),
              "MeasDataAnalyzeValuesSymmetryLRValid":("MeasData/AnalyzeValues/SymmetryLR/Valid"),
              "MeasDataAnalyzeValuesBQFValue":("MeasData/AnalyzeValues/BQF/Value"),
              "MeasDataAnalyzeValuesBQFValid":("MeasData/AnalyzeValues/BQF/Valid"),
              "MeasDataAnalyzeValuesWedgeValue":("MeasData/AnalyzeValues/Wedge/Value"),
              "MeasDataAnalyzeValuesWedgeValid":("MeasData/AnalyzeValues/Wedge/Valid")
             }
    # open the and parse the datafile
    xmlData = etree.parse(filename)
    trendData = xmlData.findall("//TrendData")

    # sort the directory keys
    sortedKeys = list(sorted(Parameters.keys()))

    # create a list of headers for our pandas dataframe
    dateList=[]
    dateList.append('date')
    headers = dateList+sortedKeys
    # creates any empty pandas dataframe with the same number of rows as the number of records in trendData
    # and with the column headers set to 'headers'
    df = pd.DataFrame(index=np.arange(0,len(trendData)), columns=headers)
    for a,b in enumerate(trendData):
        result={}
        result["date"] = dateutil.parser.parse(b.attrib['date'])
        for i,j in enumerate(Parameters):
            result[j] = b.findtext(Parameters[j])
            df.loc[a]=(result)
    df = df.set_index('date')
    #for i in int64list:
    #    df.attrib(i) = pd.to_numeric(df.attrib(i))

    # df = df.convert_objects(convert_numeric=True)
    return df
