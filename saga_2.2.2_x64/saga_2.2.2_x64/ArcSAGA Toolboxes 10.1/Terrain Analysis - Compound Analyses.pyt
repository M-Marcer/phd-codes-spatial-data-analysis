import arcpy, ArcSAGA

class Toolbox(object):
	def __init__(self):
		self.label = "Compound Analyses"
		self.alias = ""
		self.tools = [tool_0]

class tool_0(object):
	def __init__(self):
		self.label = "Basic Terrain Analysis"
		self.description = "<p>A selection of basic parameters and objects to be derived from a Digital Terrain Model using standard settings.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="ELEVATION", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Analytical Hillshading", name="SHADE", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Slope", name="SLOPE", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Aspect", name="ASPECT", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Plan Curvature", name="HCURV", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Profile Curvature", name="VCURV", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Convergence Index", name="CONVERGENCE", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Closed Depressions", name="SINKS", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Total Catchment Area", name="CAREA", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Topographic Wetness Index", name="WETNESS", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="LS-Factor", name="LSFACTOR", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Channel Network", name="CHANNELS", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Drainage Basins", name="BASINS", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Channel Network Base Level", name="CHNL_BASE", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Channel Network Distance", name="CHNL_DIST", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Valley Depth", name="VALL_DEPTH", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Relative Slope Position", name="RSP", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Channel Density", name="THRESHOLD", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 5
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_compound', '0')
		Tool.Set_Input ('ELEVATION', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('SHADE', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('SLOPE', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('ASPECT', parameters[3].valueAsText, 'grid')
		Tool.Set_Output('HCURV', parameters[4].valueAsText, 'grid')
		Tool.Set_Output('VCURV', parameters[5].valueAsText, 'grid')
		Tool.Set_Output('CONVERGENCE', parameters[6].valueAsText, 'grid')
		Tool.Set_Output('SINKS', parameters[7].valueAsText, 'grid')
		Tool.Set_Output('CAREA', parameters[8].valueAsText, 'grid')
		Tool.Set_Output('WETNESS', parameters[9].valueAsText, 'grid')
		Tool.Set_Output('LSFACTOR', parameters[10].valueAsText, 'grid')
		Tool.Set_Output('CHANNELS', parameters[11].valueAsText, 'shapes')
		Tool.Set_Output('BASINS', parameters[12].valueAsText, 'shapes')
		Tool.Set_Output('CHNL_BASE', parameters[13].valueAsText, 'grid')
		Tool.Set_Output('CHNL_DIST', parameters[14].valueAsText, 'grid')
		Tool.Set_Output('VALL_DEPTH', parameters[15].valueAsText, 'grid')
		Tool.Set_Output('RSP', parameters[16].valueAsText, 'grid')
		Tool.Set_Option('THRESHOLD', parameters[17].valueAsText)
		Tool.Run()
		return
