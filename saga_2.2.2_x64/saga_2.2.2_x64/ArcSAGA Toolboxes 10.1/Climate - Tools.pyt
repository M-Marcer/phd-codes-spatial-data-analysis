import arcpy, ArcSAGA

class Toolbox(object):
	def __init__(self):
		self.label = "Tools"
		self.alias = ""
		self.tools = [tool_2, tool_3, tool_4, tool_5, tool_6, tool_7, tool_8, tool_9]

class tool_2(object):
	def __init__(self):
		self.label = "Earth's Orbital Parameters"
		self.description = "<p>Orbital parameters used here are based on the work of Andre L. Berger and its implementation from the NASA Goddard Institute for Space Studies (GISS). Berger's orbital parameters are considered to be valid for approximately 1 million years.</p><p>References:</p><p>- Berger, A.L. (1978): Long Term Variations of Daily Insolation and Quaternary Climatic Changes. Journal of the Atmospheric Sciences, volume 35(12), 2362-2367.</p><p>- Berger, A.L. (1978): A Simple Algorithm to Compute Long Term Variations of Daily or Monthly Insolation. Institut d'Astronomie et de Geophysique, Universite Catholique de Louvain, Louvain-la-Neuve, No. 18.</p><p>- NASA/GISS' implementation can be found as part of an Atmosphere-Ocean Model at <a target=\"_blank\" href=\"http://aom.giss.nasa.gov/srorbpar.html\">Determination of the Earth's Orbital Parameters</a><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Earth's Orbital Parameters", name="ORBPAR", direction="Output", parameterType="Required", datatype="GPTableView")
		params  = [param]
		param = arcpy.Parameter(displayName="Start [ka]", name="START", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = -200.000000
		params += [param]
		param = arcpy.Parameter(displayName="Stop [ka]", name="STOP", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 2.000000
		params += [param]
		param = arcpy.Parameter(displayName="Step [ka]", name="STEP", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('climate_tools', '2')
		Tool.Set_Output('ORBPAR', parameters[0].valueAsText, 'table')
		Tool.Set_Option('START', parameters[1].valueAsText)
		Tool.Set_Option('STOP', parameters[2].valueAsText)
		Tool.Set_Option('STEP', parameters[3].valueAsText)
		Tool.Run()
		return


class tool_3(object):
	def __init__(self):
		self.label = "Annual Course of Daily Insolation"
		self.description = "<p>Orbital parameters used here are based on the work of Andre L. Berger and its implementation from the NASA Goddard Institute for Space Studies (GISS). Berger's orbital parameters are considered to be valid for approximately 1 million years.</p><p>References:</p><p>- Berger, A.L. (1978): Long Term Variations of Daily Insolation and Quaternary Climatic Changes. Journal of the Atmospheric Sciences, volume 35(12), 2362-2367.</p><p>- Berger, A.L. (1978): A Simple Algorithm to Compute Long Term Variations of Daily or Monthly Insolation. Institut d'Astronomie et de Geophysique, Universite Catholique de Louvain, Louvain-la-Neuve, No. 18.</p><p>- NASA/GISS' implementation can be found as part of an Atmosphere-Ocean Model at <a target=\"_blank\" href=\"http://aom.giss.nasa.gov/srorbpar.html\">Determination of the Earth's Orbital Parameters</a><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Solar Radiation", name="SOLARRAD", direction="Output", parameterType="Required", datatype="GPTableView")
		params  = [param]
		param = arcpy.Parameter(displayName="Start [ka]", name="START", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = -200.000000
		params += [param]
		param = arcpy.Parameter(displayName="Stop [ka]", name="STOP", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 2.000000
		params += [param]
		param = arcpy.Parameter(displayName="Step [ka]", name="STEP", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Latitude [Degree]", name="LAT", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 53.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('climate_tools', '3')
		Tool.Set_Output('SOLARRAD', parameters[0].valueAsText, 'table')
		Tool.Set_Option('START', parameters[1].valueAsText)
		Tool.Set_Option('STOP', parameters[2].valueAsText)
		Tool.Set_Option('STEP', parameters[3].valueAsText)
		Tool.Set_Option('LAT', parameters[4].valueAsText)
		Tool.Run()
		return


class tool_4(object):
	def __init__(self):
		self.label = "Daily Insolation over Latitude"
		self.description = "<p>Orbital parameters used here are based on the work of Andre L. Berger and its implementation from the NASA Goddard Institute for Space Studies (GISS). Berger's orbital parameters are considered to be valid for approximately 1 million years.</p><p>References:</p><p>- Berger, A.L. (1978): Long Term Variations of Daily Insolation and Quaternary Climatic Changes. Journal of the Atmospheric Sciences, volume 35(12), 2362-2367.</p><p>- Berger, A.L. (1978): A Simple Algorithm to Compute Long Term Variations of Daily or Monthly Insolation. Institut d'Astronomie et de Geophysique, Universite Catholique de Louvain, Louvain-la-Neuve, No. 18.</p><p>- NASA/GISS' implementation can be found as part of an Atmosphere-Ocean Model at <a target=\"_blank\" href=\"http://aom.giss.nasa.gov/srorbpar.html\">Determination of the Earth's Orbital Parameters</a><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Solar Radiation", name="SOLARRAD", direction="Output", parameterType="Required", datatype="GPTableView")
		params  = [param]
		param = arcpy.Parameter(displayName="Start [ka]", name="START", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = -200.000000
		params += [param]
		param = arcpy.Parameter(displayName="Stop [ka]", name="STOP", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 2.000000
		params += [param]
		param = arcpy.Parameter(displayName="Step [ka]", name="STEP", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Latitude Increment [Degree]", name="DLAT", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 5
		params += [param]
		param = arcpy.Parameter(displayName="Day of Year", name="DAY", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 181
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('climate_tools', '4')
		Tool.Set_Output('SOLARRAD', parameters[0].valueAsText, 'table')
		Tool.Set_Option('START', parameters[1].valueAsText)
		Tool.Set_Option('STOP', parameters[2].valueAsText)
		Tool.Set_Option('STEP', parameters[3].valueAsText)
		Tool.Set_Option('DLAT', parameters[4].valueAsText)
		Tool.Set_Option('DAY', parameters[5].valueAsText)
		Tool.Run()
		return


class tool_5(object):
	def __init__(self):
		self.label = "Monthly Global by Latitude"
		self.description = "<p>Orbital parameters used here are based on the work of Andre L. Berger and its implementation from the NASA Goddard Institute for Space Studies (GISS). Berger's orbital parameters are considered to be valid for approximately 1 million years.</p><p>References:</p><p>- Berger, A.L. (1978): Long Term Variations of Daily Insolation and Quaternary Climatic Changes. Journal of the Atmospheric Sciences, volume 35(12), 2362-2367.</p><p>- Berger, A.L. (1978): A Simple Algorithm to Compute Long Term Variations of Daily or Monthly Insolation. Institut d'Astronomie et de Geophysique, Universite Catholique de Louvain, Louvain-la-Neuve, No. 18.</p><p>- NASA/GISS' implementation can be found as part of an Atmosphere-Ocean Model at <a target=\"_blank\" href=\"http://aom.giss.nasa.gov/srorbpar.html\">Determination of the Earth's Orbital Parameters</a><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Solar Radiation", name="SOLARRAD", direction="Output", parameterType="Required", datatype="GPTableView")
		params  = [param]
		param = arcpy.Parameter(displayName="Albedo", name="ALBEDO", direction="Input", parameterType="Optional", datatype="GPTableView")
		params += [param]
		param = arcpy.Parameter(displayName="Field", name="FIELD", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["ALBEDO"]
		params += [param]
		param = arcpy.Parameter(displayName="Year [ka]", name="YEAR", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 2.000000
		params += [param]
		param = arcpy.Parameter(displayName="Latitude Increment [Degree]", name="DLAT", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 5
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('climate_tools', '5')
		Tool.Set_Output('SOLARRAD', parameters[0].valueAsText, 'table')
		Tool.Set_Input ('ALBEDO', parameters[1].valueAsText, 'table')
		Tool.Set_Option('FIELD', parameters[2].valueAsText)
		Tool.Set_Option('YEAR', parameters[3].valueAsText)
		Tool.Set_Option('DLAT', parameters[4].valueAsText)
		Tool.Run()
		return


class tool_6(object):
	def __init__(self):
		self.label = "PET (after Hargreaves, Table)"
		self.description = "<p>Estimation of daily potential evapotranspiration from daily average, minimum and maximum temperatures using Hargreave's empirical equation. In order to estimate extraterrestrial net radiation geographic latitude of observation and Julian day have to be supplied too. </p><p>References:</p><p>- Ambikadevi, K.M. (2004): Simulation of Evapotranspiration and Rainfall-runoff for the Stillwater River Watershed in Central Massachusetts. Environmental & Water Resources Engineering Masters Projects, University of Massachusetts, Amherst <a target=\"_blank\" href=\"http://scholarworks.umass.edu/cee_ewre/22/\">online</a></p><p>- Hargraeves, G.H., Samani, Z.A. (1985): Reference crop evapotranspiration from ambient air temperatures. Paper presented in ASAE Regional Meeting, Grand Junction, Colorado. <a target=\"_blank\" href=\"http://cagesun.nmsu.edu/~zsamani/papers/Hargreaves_Samani_85.pdf\">online</a></p><p>FAO Irrigation and drainage paper 56. <a target=\"_blank\" href=\"http://www.fao.org/docrep/X0490E/x0490e00.htm#Contents\">online</a></p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Data", name="TABLE", direction="Input", parameterType="Required", datatype="GPTableView")
		params  = [param]
		param = arcpy.Parameter(displayName="Julian Day", name="JD", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["TABLE"]
		params += [param]
		param = arcpy.Parameter(displayName="Mean Temperature", name="T", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["TABLE"]
		params += [param]
		param = arcpy.Parameter(displayName="Minimum Temperature", name="T_MIN", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["TABLE"]
		params += [param]
		param = arcpy.Parameter(displayName="Maximum Temperature", name="T_MAX", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["TABLE"]
		params += [param]
		param = arcpy.Parameter(displayName="Latitude", name="LAT", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 53.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('climate_tools', '6')
		Tool.Set_Input ('TABLE', parameters[0].valueAsText, 'table')
		Tool.Set_Option('JD', parameters[1].valueAsText)
		Tool.Set_Option('T', parameters[2].valueAsText)
		Tool.Set_Option('T_MIN', parameters[3].valueAsText)
		Tool.Set_Option('T_MAX', parameters[4].valueAsText)
		Tool.Set_Option('LAT', parameters[5].valueAsText)
		Tool.Run()
		return


class tool_7(object):
	def __init__(self):
		self.label = "Daily to Hourly PET"
		self.description = "<p>Derive hourly from daily evapotranspiration using sinusoidal distribution. </p><p>References:</p><p>- Ambikadevi, K.M. (2004): Simulation of Evapotranspiration and Rainfall-runoff for the Stillwater River Watershed in Central Massachusetts. Environmental & Water Resources Engineering Masters Projects, University of Massachusetts, Amherst <a target=\"_blank\" href=\"http://scholarworks.umass.edu/cee_ewre/22/\">online</a></p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Daily Data", name="DAYS", direction="Input", parameterType="Required", datatype="GPTableView")
		params  = [param]
		param = arcpy.Parameter(displayName="Julian Day", name="JD", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["DAYS"]
		params += [param]
		param = arcpy.Parameter(displayName="Evapotranspiration", name="ET", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["DAYS"]
		params += [param]
		param = arcpy.Parameter(displayName="Precipitation", name="P", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["DAYS"]
		params += [param]
		param = arcpy.Parameter(displayName="Hourly Data", name="HOURS", direction="Output", parameterType="Required", datatype="GPTableView")
		params += [param]
		param = arcpy.Parameter(displayName="Latitude", name="LAT", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 53.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('climate_tools', '7')
		Tool.Set_Input ('DAYS', parameters[0].valueAsText, 'table')
		Tool.Set_Option('JD', parameters[1].valueAsText)
		Tool.Set_Option('ET', parameters[2].valueAsText)
		Tool.Set_Option('P', parameters[3].valueAsText)
		Tool.Set_Output('HOURS', parameters[4].valueAsText, 'table')
		Tool.Set_Option('LAT', parameters[5].valueAsText)
		Tool.Run()
		return


class tool_8(object):
	def __init__(self):
		self.label = "PET (after Hargreaves, Grid)"
		self.description = "<p>Estimation of daily potential evapotranspiration from daily average, minimum and maximum temperatures using Hargreave's empirical equation. In order to estimate extraterrestrial net radiation geographic latitude of observation and Julian day have to be supplied too. </p><p>References:</p><p>- Ambikadevi, K.M. (2004): Simulation of Evapotranspiration and Rainfall-runoff for the Stillwater River Watershed in Central Massachusetts. Environmental & Water Resources Engineering Masters Projects, University of Massachusetts, Amherst <a target=\"_blank\" href=\"http://scholarworks.umass.edu/cee_ewre/22/\">online</a></p><p>- Hargraeves, G.H., Samani, Z.A. (1985): Reference crop evapotranspiration from ambient air temperatures. Paper presented in ASAE Regional Meeting, Grand Junction, Colorado. <a target=\"_blank\" href=\"http://cagesun.nmsu.edu/~zsamani/papers/Hargreaves_Samani_85.pdf\">online</a></p><p>Allen, R.G., Pereira, L.S., Raes, D., Smith, M. (1998): Crop evapotranspiration - Guidelines for computing crop water requirements. FAO Irrigation and drainage paper 56. <a target=\"_blank\" href=\"http://www.fao.org/docrep/X0490E/x0490e00.htm#Contents\">online</a></p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Mean Temperature", name="T", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Minimum Temperature", name="T_MIN", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Maximum Temperature", name="T_MAX", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Potential Evapotranspiration", name="PET", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Latitude [Degree]", name="LAT", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 53.000000
		params += [param]
		param = arcpy.Parameter(displayName="Time", name="TIME", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["day", "month"]
		param.value = "day"
		params += [param]
		param = arcpy.Parameter(displayName="Month", name="MONTH", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
		param.value = "October"
		params += [param]
		param = arcpy.Parameter(displayName="Day of Month", name="DAY", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 15
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('climate_tools', '8')
		Tool.Set_Input ('T', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('T_MIN', parameters[1].valueAsText, 'grid')
		Tool.Set_Input ('T_MAX', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('PET', parameters[3].valueAsText, 'grid')
		Tool.Set_Option('LAT', parameters[4].valueAsText)
		Tool.Set_Option('TIME', parameters[5].valueAsText)
		Tool.Set_Option('MONTH', parameters[6].valueAsText)
		Tool.Set_Option('DAY', parameters[7].valueAsText)
		Tool.Run()
		return


class tool_9(object):
	def __init__(self):
		self.label = "Sunrise and Sunset"
		self.description = "<p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Target System", name="TARGET", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Sunrise", name="SUNRISE", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Sunset", name="SUNSET", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Day Length", name="LENGTH", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Year", name="YEAR", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 2015
		params += [param]
		param = arcpy.Parameter(displayName="Month", name="MONTH", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
		param.value = "October"
		params += [param]
		param = arcpy.Parameter(displayName="Day of Month", name="DAY", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 15
		params += [param]
		param = arcpy.Parameter(displayName="Time", name="TIME", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["local", "world"]
		param.value = "local"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('climate_tools', '9')
		Tool.Set_Input ('TARGET', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('SUNRISE', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('SUNSET', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('LENGTH', parameters[3].valueAsText, 'grid')
		Tool.Set_Option('YEAR', parameters[4].valueAsText)
		Tool.Set_Option('MONTH', parameters[5].valueAsText)
		Tool.Set_Option('DAY', parameters[6].valueAsText)
		Tool.Set_Option('TIME', parameters[7].valueAsText)
		Tool.Run()
		return
