import pandas as pd
import matplotlib.pyplot as plt
from shapely.geometry import Point, Polygon
import geopandas as gpd

parkingDataSet = pd.read_csv('DCParkingMay2023.csv')

dcGovernment = [
                'DEPARTMENT OF PUBLIC WORKS',
                ]

ticketDetails = pd.DataFrame()
ticketDetails = parkingDataSet.loc[parkingDataSet["ISSUING_AGENCY_NAME"].isin(dcGovernment), ["ISSUE_DATE", "TICKET_NUMBER", "ISSUING_AGENCY_NAME", "LOCATION", "FINE_AMOUNT", "LATITUDE", "LONGITUDE"]].copy()
ticketDetails = ticketDetails.dropna()

#Calculate DPW Revenue
totalRevenue = ticketDetails['FINE_AMOUNT'].sum()
print('Total D.C Government Revenue from Tickets: ${}'.format(totalRevenue))


ticketDetails.to_csv("Filtered", sep="\t")
#Plot ticket Locations
ticketLocations = gpd.read_file('DCBaseFile/Washington_DC_Boundary.shp')
fig, ax = plt.subplots(figsize=(15,15))
ticketLocations.plot(ax=ax)
crs={'init':'epsg:4326'}
geometry = [Point(xy) for xy in zip(ticketDetails['LONGITUDE'], ticketDetails['LATITUDE'])]
coordinatePoints = gpd.GeoDataFrame(ticketDetails, crs = crs, geometry=geometry)
coordinatePoints.plot(ax = ax, color = 'red')

coordinatePoints.to_file("TicketLocations/TicketLocations.shp")




                               
                               