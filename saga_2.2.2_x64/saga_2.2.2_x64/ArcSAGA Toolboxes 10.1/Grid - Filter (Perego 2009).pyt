import arcpy, ArcSAGA

class Toolbox(object):
	def __init__(self):
		self.label = "Filter (Perego 2009)"
		self.alias = ""
		self.tools = [tool_0, tool_1, tool_2, tool_3, tool_4, tool_5, tool_6, tool_7]

class tool_0(object):
	def __init__(self):
		self.label = "Average With Thereshold 1"
		self.description = "<p>Average With Thereshold for Grids calculates average in X and Y distances unsing only the values that differ form central pixel less than a specified threshold. It's useful to remove noise whit a known maximum reducing the loss of informations<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Input", name="INPUT", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="AWT Grid", name="RESULT", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Radius X", name="RX", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 1
		params += [param]
		param = arcpy.Parameter(displayName="Radius Y", name="RY", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 1
		params += [param]
		param = arcpy.Parameter(displayName="Threshold", name="THRESH", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 2.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('contrib_perego', '0')
		Tool.Set_Input ('INPUT', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('RESULT', parameters[1].valueAsText, 'grid')
		Tool.Set_Option('RX', parameters[2].valueAsText)
		Tool.Set_Option('RY', parameters[3].valueAsText)
		Tool.Set_Option('THRESH', parameters[4].valueAsText)
		Tool.Run()
		return


class tool_1(object):
	def __init__(self):
		self.label = "Average With Thereshold 2"
		self.description = "<p>Average 2 With Thereshold for Grids calculates average in X and Y distances unsing only the values that differ form central pixel less than a specified threshold. Each value has a weight which is inversely proportional to the distance (method 1).<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Input", name="INPUT", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="AWT Grid", name="RESULT", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Radius X", name="RX", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 1
		params += [param]
		param = arcpy.Parameter(displayName="Radius Y", name="RY", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 1
		params += [param]
		param = arcpy.Parameter(displayName="Threshold", name="THRESH", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 2.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('contrib_perego', '1')
		Tool.Set_Input ('INPUT', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('RESULT', parameters[1].valueAsText, 'grid')
		Tool.Set_Option('RX', parameters[2].valueAsText)
		Tool.Set_Option('RY', parameters[3].valueAsText)
		Tool.Set_Option('THRESH', parameters[4].valueAsText)
		Tool.Run()
		return


class tool_2(object):
	def __init__(self):
		self.label = "Average With Thereshold 3"
		self.description = "<p>Average 3 With Thereshold for Grids calculates average in X and Y distances unsing only the values that differ form central pixel less than a specified threshold. Each value has a weight which is inversely proportional to the distance (method 2).<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Input", name="INPUT", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="AWT Grid", name="RESULT", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Radius X", name="RX", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 1
		params += [param]
		param = arcpy.Parameter(displayName="Radius Y", name="RY", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 1
		params += [param]
		param = arcpy.Parameter(displayName="Threshold", name="THRESH", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 2.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('contrib_perego', '2')
		Tool.Set_Input ('INPUT', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('RESULT', parameters[1].valueAsText, 'grid')
		Tool.Set_Option('RX', parameters[2].valueAsText)
		Tool.Set_Option('RY', parameters[3].valueAsText)
		Tool.Set_Option('THRESH', parameters[4].valueAsText)
		Tool.Run()
		return


class tool_3(object):
	def __init__(self):
		self.label = "Average With Mask 1"
		self.description = "<p>Average With Mask 1 calculates average for cells specified by a mask grid. Cell excluded by the mask grid are NOT used in the average calculation.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Input", name="INPUT", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Mask Grid", name="MASK", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="AWM1 Grid", name="RESULT", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Mask value", name="V", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Radius X", name="RX", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 1
		params += [param]
		param = arcpy.Parameter(displayName="Radius Y", name="RY", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 1
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('contrib_perego', '3')
		Tool.Set_Input ('INPUT', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('MASK', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('RESULT', parameters[2].valueAsText, 'grid')
		Tool.Set_Option('V', parameters[3].valueAsText)
		Tool.Set_Option('RX', parameters[4].valueAsText)
		Tool.Set_Option('RY', parameters[5].valueAsText)
		Tool.Run()
		return


class tool_4(object):
	def __init__(self):
		self.label = "Average With Mask 2"
		self.description = "<p>Average With Mask 2 calculates average for cells specified by a mask grid. However cell excluded by the mask grid are used in the average calculation for right pixels.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Input", name="INPUT", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Mask Grid", name="MASK", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="AWM2 Grid", name="RESULT", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Mask value", name="V", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Radius X", name="RX", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 1
		params += [param]
		param = arcpy.Parameter(displayName="Radius Y", name="RY", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 1
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('contrib_perego', '4')
		Tool.Set_Input ('INPUT', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('MASK', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('RESULT', parameters[2].valueAsText, 'grid')
		Tool.Set_Option('V', parameters[3].valueAsText)
		Tool.Set_Option('RX', parameters[4].valueAsText)
		Tool.Set_Option('RY', parameters[5].valueAsText)
		Tool.Run()
		return


class tool_5(object):
	def __init__(self):
		self.label = "Destriping"
		self.description = "<p>Destriping filter removes straight parallel stripes in raster data. It uses two low-pass filters elongated in the stripes direction; the first one is 1 pixel unit wide while the second one is wide as the striping wavelength. Their difference is the striping error which is removed from the original data to obtain the destriped DEM. This method is equivalent to that proposed by Oimoen (2000). </p><p></p><p>References:</p><p>- Oimoen, M.J. (2000): An Effective Filter For Removal Of Production Artifacts. In U.S. Geological Survey 7.5-Minute Digital Elevation Models. Proceedings of the Fourteenth International Conference on Applied Geologic Remote Sensing, 6-8 November, Las Vegas, NV.</p><p></p><p>- Peregro, A. (2009): SRTM DEM destriping with SAGA GIS: consequences on drainage network extraction. <a target=\"_blank\" href=\"http://www.webalice.it/alper78/saga_mod/destriping/destriping.html\">online</a>.</p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Input", name="INPUT", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Destriped Grid", name="RESULT3", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Low-pass 1", name="RESULT1", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Low-pass 2", name="RESULT2", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Angle (in degrees)", name="ANG", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Radius", name="R", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 10.000000
		params += [param]
		param = arcpy.Parameter(displayName="Stripes distance", name="D", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 2.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('contrib_perego', '5')
		Tool.Set_Input ('INPUT', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('RESULT3', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('RESULT1', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('RESULT2', parameters[3].valueAsText, 'grid')
		Tool.Set_Option('ANG', parameters[4].valueAsText)
		Tool.Set_Option('R', parameters[5].valueAsText)
		Tool.Set_Option('D', parameters[6].valueAsText)
		Tool.Run()
		return


class tool_6(object):
	def __init__(self):
		self.label = "Destriping with Mask"
		self.description = "<p>Destriping filter removes straight parallel stripes in raster data. It uses two low-pass filters elongated in the stripes direction; the first one is 1 pixel unit wide while the second one is wide as the striping wavelength. Their difference is the striping error which is removed from the original data to obtain the destriped DEM. This method is equivalent to that proposed by Oimoen (2000). With destriping 2 you can choose a range of value (min-max) from the input grid and a range of value (Mask min - Mask max) from a mask grid to select the target cells. </p><p></p><p>References:</p><p>- Oimoen, M.J. (2000): An Effective Filter For Removal Of Production Artifacts. In U.S. Geological Survey 7.5-Minute Digital Elevation Models. Proceedings of the Fourteenth International Conference on Applied Geologic Remote Sensing, 6-8 November, Las Vegas, NV.</p><p></p><p>- Peregro, A. (2009): SRTM DEM destriping with SAGA GIS: consequences on drainage network extraction. <a target=\"_blank\" href=\"http://www.webalice.it/alper78/saga_mod/destriping/destriping.html\">online</a>.</p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Input", name="INPUT", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Mask Grid", name="MASK", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Destriped Grid", name="RESULT3", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Low-pass 1", name="RESULT1", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Low-pass 2", name="RESULT2", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Angle (in degrees)", name="ANG", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Radius", name="R", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 20.000000
		params += [param]
		param = arcpy.Parameter(displayName="Stripes distance", name="D", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 2.000000
		params += [param]
		param = arcpy.Parameter(displayName="Min", name="MIN", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = -10.000000
		params += [param]
		param = arcpy.Parameter(displayName="Max", name="MAX", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 10.000000
		params += [param]
		param = arcpy.Parameter(displayName="Mask Min", name="MMIN", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = -10000.000000
		params += [param]
		param = arcpy.Parameter(displayName="Mask Max", name="MMAX", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 10000.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('contrib_perego', '6')
		Tool.Set_Input ('INPUT', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('MASK', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('RESULT3', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('RESULT1', parameters[3].valueAsText, 'grid')
		Tool.Set_Output('RESULT2', parameters[4].valueAsText, 'grid')
		Tool.Set_Option('ANG', parameters[5].valueAsText)
		Tool.Set_Option('R', parameters[6].valueAsText)
		Tool.Set_Option('D', parameters[7].valueAsText)
		Tool.Set_Option('MIN', parameters[8].valueAsText)
		Tool.Set_Option('MAX', parameters[9].valueAsText)
		Tool.Set_Option('MMIN', parameters[10].valueAsText)
		Tool.Set_Option('MMAX', parameters[11].valueAsText)
		Tool.Run()
		return


class tool_7(object):
	def __init__(self):
		self.label = "Directional Average"
		self.description = "<p>directional1 average for Grids<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Input", name="INPUT", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Output Grid", name="RESULT", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Angle (in degrees)", name="ANG", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Main Radius", name="R1", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Transversal radius", name="R2", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.500000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('contrib_perego', '7')
		Tool.Set_Input ('INPUT', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('RESULT', parameters[1].valueAsText, 'grid')
		Tool.Set_Option('ANG', parameters[2].valueAsText)
		Tool.Set_Option('R1', parameters[3].valueAsText)
		Tool.Set_Option('R2', parameters[4].valueAsText)
		Tool.Run()
		return
