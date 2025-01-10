import arcpy, ArcSAGA

class Toolbox(object):
	def __init__(self):
		self.label = "GPS Tools"
		self.alias = ""
		self.tools = [tool_0, tool_1]

class tool_0(object):
	def __init__(self):
		self.label = "GPX to shapefile"
		self.description = "<p>Converts a GPX file into a Shapefile (.shp)(c) 2005 by Victor Olaya</p><p>email: volaya@ya.com<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Gpx2shp path", name="BASEPATH", direction="Input", parameterType="Optional", datatype="DEFolder")
		params  = [param]
		param = arcpy.Parameter(displayName="GPX file", name="FILE", direction="Input", parameterType="Optional", datatype="DEFile")
		params += [param]
		param = arcpy.Parameter(displayName="Convert track points", name="TRACKPOINTS", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Convert way points", name="WAYPOINTS", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Convert routes", name="ROUTES", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Load shapefile", name="ADD", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('io_gps', '0')
		Tool.Set_Option('BASEPATH', parameters[0].valueAsText)
		Tool.Set_Option('FILE', parameters[1].valueAsText)
		Tool.Set_Option('TRACKPOINTS', parameters[2].valueAsText)
		Tool.Set_Option('WAYPOINTS', parameters[3].valueAsText)
		Tool.Set_Option('ROUTES', parameters[4].valueAsText)
		Tool.Set_Option('ADD', parameters[5].valueAsText)
		Tool.Run()
		return


class tool_1(object):
	def __init__(self):
		self.label = "GPSBabel"
		self.description = "<p>An interface to the GPSBabel software(c) 2005 by Victor Olaya</p><p>email: volaya@ya.com<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="GPSBabel path", name="BASEPATH", direction="Input", parameterType="Optional", datatype="DEFolder")
		params  = [param]
		param = arcpy.Parameter(displayName="Input file", name="INPUT", direction="Input", parameterType="Optional", datatype="DEFile")
		params += [param]
		param = arcpy.Parameter(displayName="Input format", name="FORMATIN", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Geocaching.com .loc", "GPSman", "GPX XML", "Magellan protocol", "Magellan Mapsend", "Garmin PCX5", "Garmin Mapsource", "gpsutil", "U.S. Census Bureau Tiger Mapping Service", "Comma separated values", "Delorme Topo USA4/XMap Conduit", "Navitrak DNA marker format", "MS PocketStreets 2002 Pushpin", "Cetus for Palm/OS", "GPSPilot Tracker for Palm/OS", "Magellan NAV Companion for PalmOS", "Garmin serial protocol", "MapTech Exchange Format", "Holux (gm-100) .wpo Format", "OziExplorer Waypoint", "National Geographic Topo .tpg", "TopoMapPro Places File"]
		param.value = "Geocaching.com .loc"
		params += [param]
		param = arcpy.Parameter(displayName="Output file", name="OUTPUT", direction="Input", parameterType="Optional", datatype="DEFile")
		params += [param]
		param = arcpy.Parameter(displayName="Output format", name="FORMATOUT", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Geocaching.com .loc", "GPSman", "GPX XML", "Magellan protocol", "Magellan Mapsend", "Garmin PCX5", "Garmin Mapsource", "gpsutil", "U.S. Census Bureau Tiger Mapping Service", "Comma separated values", "Delorme Topo USA4/XMap Conduit", "Navitrak DNA marker format", "MS PocketStreets 2002 Pushpin", "Cetus for Palm/OS", "GPSPilot Tracker for Palm/OS", "Magellan NAV Companion for PalmOS", "Garmin serial protocol", "MapTech Exchange Format", "Holux (gm-100) .wpo Format", "OziExplorer Waypoint", "National Geographic Topo .tpg", "TopoMapPro Places File"]
		param.value = "Geocaching.com .loc"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('io_gps', '1')
		Tool.Set_Option('BASEPATH', parameters[0].valueAsText)
		Tool.Set_Option('INPUT', parameters[1].valueAsText)
		Tool.Set_Option('FORMATIN', parameters[2].valueAsText)
		Tool.Set_Option('OUTPUT', parameters[3].valueAsText)
		Tool.Set_Option('FORMATOUT', parameters[4].valueAsText)
		Tool.Run()
		return
