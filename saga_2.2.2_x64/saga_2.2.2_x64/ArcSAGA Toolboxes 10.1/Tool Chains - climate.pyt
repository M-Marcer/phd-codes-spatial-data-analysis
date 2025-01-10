import arcpy, ArcSAGA

class Toolbox(object):
	def __init__(self):
		self.label = "climate"
		self.alias = ""
		self.tools = [tool_0]

class tool_0(object):
	def __init__(self):
		self.label = "Lapse Rate Based Temperature Downscaling"
		self.description = "<p>  The lapse rate based temperature downscaling is quite simple but</p><p>  might perform well for mountainous regions, where a the altitudinal</p><p>  gradient is the main driver for local temperature variation.</p><p>  First, a given lapse rate is used to estimate a sea level temperature from</p><p>  elevations and temperatures at a coarse resolution. Second, the same</p><p>  lapse rate is used to estimate the terrain surface temperature using higher</p><p>  resoluted elevation data with the spline interpolated sea level temperatures</p><p>  from the previous step.</p><p> <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="LORES_DEM", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Temperature", name="LORES_T", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Lapse Rate", name="LAPSE_RATES", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Temperature at Sea Level", name="LORES_SLT", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Elevation", name="HIRES_DEM", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Temperature", name="HIRES_T", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Lapse Rate", name="LAPSE_RATE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.600000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('climate', 't_downscale')
		Tool.Set_Input ('LORES_DEM', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('LORES_T', parameters[1].valueAsText, 'grid')
		Tool.Set_Input ('LAPSE_RATES', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('LORES_SLT', parameters[3].valueAsText, 'grid')
		Tool.Set_Input ('HIRES_DEM', parameters[4].valueAsText, 'grid')
		Tool.Set_Output('HIRES_T', parameters[5].valueAsText, 'grid')
		Tool.Set_Option('LAPSE_RATE', parameters[6].valueAsText)
		Tool.Run()
		return
