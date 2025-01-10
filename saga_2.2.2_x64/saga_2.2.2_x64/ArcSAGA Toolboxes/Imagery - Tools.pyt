import arcpy, ArcSAGA

class Toolbox(object):
	def __init__(self):
		self.label = "Tools"
		self.alias = ""
		self.tools = [tool_0, tool_1, tool_2, tool_3, tool_4, tool_5, tool_6, tool_7, tool_8, tool_9, tool_10]

class tool_0(object):
	def __init__(self):
		self.label = "Vegetation Index (Distance Based)"
		self.description = "<p>Distance based vegetation indices.</p><p></p><p>References:</p><p>K.R. McCloy (2006): Resource Management Information Systems: Remote Sensing, GIS and Modelling. 2nd Edition, CRC Taylor & Francis, 575pp.</p><p></p><p>N.G. Silleos, T.K. Alexandridis, I.Z. Gitas & K. Perakis (2006): Vegetation Indices: Advances Made in Biomass Estimation and Vegetation Monitoring in the Last 30 Years, Geocarto International, 21:4, 21-28, <a target=\"_blank\" href=\"http://dx.doi.org/10.1080/10106040608542399\">online</a>.</p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Red Reflectance", name="RED", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Near Infrared Reflectance", name="NIR", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Perpendicular Vegetation Index (Richardson and Wiegand, 1977)", name="PVI0", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Perpendicular Vegetation Index (Perry and Lautenschlager, 1984)", name="PVI1", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Perpendicular Vegetation Index (Walther and Shabaani)", name="PVI2", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Perpendicular Vegetation Index (Qi, et al., 1994)", name="PVI3", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Transformed Soil Adjusted Vegetation Index (Baret et al. 1989)", name="TSAVI", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Transformed Soil Adjusted Vegetation Index (Baret and Guyot, 1991)", name="ATSAVI", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Intercept of Soil Line", name="INTERCEPT", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Slope of Soil Line", name="SLOPE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.500000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('imagery_tools', '0')
		Tool.Set_Input ('RED', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('NIR', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('PVI0', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('PVI1', parameters[3].valueAsText, 'grid')
		Tool.Set_Output('PVI2', parameters[4].valueAsText, 'grid')
		Tool.Set_Output('PVI3', parameters[5].valueAsText, 'grid')
		Tool.Set_Output('TSAVI', parameters[6].valueAsText, 'grid')
		Tool.Set_Output('ATSAVI', parameters[7].valueAsText, 'grid')
		Tool.Set_Option('INTERCEPT', parameters[8].valueAsText)
		Tool.Set_Option('SLOPE', parameters[9].valueAsText)
		Tool.Run()
		return


class tool_1(object):
	def __init__(self):
		self.label = "Vegetation Index (Slope Based)"
		self.description = "<p>Slope based vegetation indices.</p><p></p><p><ul><li>Ratio Vegetation Index (Richardson and Wiegand, 1977)</p><p>    RVI = R / NIR</li></p><p><li>Normalized Ratio Vegetation Index (Baret and Guyot, 1991)</p><p>    NRVI = (RVI - 1) / (RVI + 1)</li></p><p><li>Normalized Difference Vegetation Index (Rouse et al. 1974)</p><p>    NDVI = (NIR - R) / (NIR + R)</li></p><p><li>Transformed Vegetation Index (Deering et al., 1975)</p><p>    TVI = [(NIR - R) / (NIR + R)]^0.5 + 0.5 </li></p><p><li>Corrected Transformed Ratio Vegetation Index (Perry and Lautenschlager, 1984)</p><p>    CTVI = [(NDVI + 0.5) / abs(NDVI + 0.5)] * [abs(NDVI + 0.5)]^0.5</li></p><p><li>Thiam's Transformed Vegetation Index (Thiam, 1997)</p><p>    RVI = [abs(NDVI) + 0.5]^0.5</li></p><p><li>Soil Adjusted Vegetation Index (Huete, 1988)</p><p>    SAVI = [(NIR - R) / (NIR + R)] * (1 + S)</li></p><p></ul>(NIR = near infrared, R = red, S = soil adjustment factor)</p><p></p><p>References:</p><p>K.R. McCloy (2006): Resource Management Information Systems: Remote Sensing, GIS and Modelling. 2nd Edition, CRC Taylor & Francis, 575pp.</p><p></p><p>N.G. Silleos, T.K. Alexandridis, I.Z. Gitas & K. Perakis (2006): Vegetation Indices: Advances Made in Biomass Estimation and Vegetation Monitoring in the Last 30 Years, Geocarto International, 21:4, 21-28, <a target=\"_blank\" href=\"http://dx.doi.org/10.1080/10106040608542399\">online</a>.</p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Red Reflectance", name="RED", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Near Infrared Reflectance", name="NIR", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Difference Vegetation Index", name="DVI", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Normalized Difference Vegetation Index", name="NDVI", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Ratio Vegetation Index", name="RVI", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Normalized Ratio Vegetation Index", name="NRVI", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Transformed Vegetation Index", name="TVI", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Corrected Transformed Vegetation Index", name="CTVI", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Thiam's Transformed Vegetation Index", name="TTVI", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Soil Adjusted Vegetation Index", name="SAVI", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Soil Adjustment Factor", name="SOIL", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.500000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('imagery_tools', '1')
		Tool.Set_Input ('RED', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('NIR', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('DVI', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('NDVI', parameters[3].valueAsText, 'grid')
		Tool.Set_Output('RVI', parameters[4].valueAsText, 'grid')
		Tool.Set_Output('NRVI', parameters[5].valueAsText, 'grid')
		Tool.Set_Output('TVI', parameters[6].valueAsText, 'grid')
		Tool.Set_Output('CTVI', parameters[7].valueAsText, 'grid')
		Tool.Set_Output('TTVI', parameters[8].valueAsText, 'grid')
		Tool.Set_Output('SAVI', parameters[9].valueAsText, 'grid')
		Tool.Set_Option('SOIL', parameters[10].valueAsText)
		Tool.Run()
		return


class tool_2(object):
	def __init__(self):
		self.label = "Enhanced Vegetation Index"
		self.description = "<p>Enhanced Vegetation Index (EVI).</p><p></p><p>References:</p><p>A Huete, K Didan, T Miura, E.P Rodriguez, X Gao, L.G Ferreira, Overview of the radiometric and biophysical performance of the MODIS vegetation indices, Remote Sensing of Environment, Volume 83, Issues 1-2, November 2002, Pages 195-213, ISSN 0034-4257, 10.1016/S0034-4257(02)00096-2. <a target=\"_blank\" href=\"http://www.sciencedirect.com/science/article/pii/S0034425702000962\">online</a></p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Blue Reflectance", name="BLUE", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Red Reflectance", name="RED", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Near Infrared Reflectance", name="NIR", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Enhanced Vegetation Index", name="EVI", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Gain", name="GAIN", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 2.500000
		params += [param]
		param = arcpy.Parameter(displayName="Canopy Background Adjustment", name="L", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Aerosol Resistance Coefficient (Blue)", name="CBLUE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 7.500000
		params += [param]
		param = arcpy.Parameter(displayName="Aerosol Resistance Coefficient (Red)", name="CRED", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 6.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('imagery_tools', '2')
		Tool.Set_Input ('BLUE', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('RED', parameters[1].valueAsText, 'grid')
		Tool.Set_Input ('NIR', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('EVI', parameters[3].valueAsText, 'grid')
		Tool.Set_Option('GAIN', parameters[4].valueAsText)
		Tool.Set_Option('L', parameters[5].valueAsText)
		Tool.Set_Option('CBLUE', parameters[6].valueAsText)
		Tool.Set_Option('CRED', parameters[7].valueAsText)
		Tool.Run()
		return


class tool_3(object):
	def __init__(self):
		self.label = "Tasseled Cap Transformation"
		self.description = "<p>Tasseled Cap Transformation as proposed for Landsat Thematic Mapper.</p><p></p><p>References:</p><p>Kauth R. J. und G. S. Thomas (1976): The Tasseled Cap - A Graphic Description of the Spectral-Temporal Development of Agricultural Crops as Seen by LANDSAT. Proceedings of the Symposium on Machine Processing of Remotely Sensed Data. <a target=\"_blank\" href=\"http://docs.lib.purdue.edu/cgi/viewcontent.cgi?article=1160&context=lars_symp&sei-redir=1&referer=http%3A%2F%2Fwww.google.de%2Furl%3Fsa%3Dt%26rct%3Dj%26q%3Dthe%2520tasseled%2520cap%2520--%2520a%2520graphic%2520description%2520of%2520the%2520spectral-temporal%2520development%2520of%2520agricultural%2520crops%26source%3Dweb%26cd%3D1%26ved%3D0CCEQFjAA%26url%3Dhttp%253A%252F%252Fdocs.lib.purdue.edu%252Fcgi%252Fviewcontent.cgi%253Farticle%253D1160%2526context%253Dlars_symp%26ei%3D1-jcTvq2NpGPsAb4tK2ODA%26usg%3DAFQjCNFLCISdiKdt2njGl6Dj1FC4Bac0ag#search=%22tasseled%20cap%20--%20graphic%20description%20spectral-temporal%20development%20agricultural%20crops%22\">online at Purdue University</a></p><p></p><p>Huang, C., B. Wylie, L. Yang, C. Homer, and G. Zylstra. Derivation of a Tasseled Cap Transformation Based on Landsat 7 At-Satellite Reflectance. USGS EROS Data Center White Paper. <a target=\"_blank\" href=\"http://landcover.usgs.gov/pdf/tasseled.pdf\">online at USGS</a></p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Blue (TM 1)", name="BLUE", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Red (TM 2)", name="RED", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Green (TM 3)", name="GREEN", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Near Infrared (TM 4)", name="NIR", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Mid Infrared (TM 5)", name="MIR1", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Mid Infrared (TM 7)", name="MIR2", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Brightness", name="BRIGHTNESS", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Greenness", name="GREENNESS", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Wetness", name="WETNESS", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('imagery_tools', '3')
		Tool.Set_Input ('BLUE', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('RED', parameters[1].valueAsText, 'grid')
		Tool.Set_Input ('GREEN', parameters[2].valueAsText, 'grid')
		Tool.Set_Input ('NIR', parameters[3].valueAsText, 'grid')
		Tool.Set_Input ('MIR1', parameters[4].valueAsText, 'grid')
		Tool.Set_Input ('MIR2', parameters[5].valueAsText, 'grid')
		Tool.Set_Output('BRIGHTNESS', parameters[6].valueAsText, 'grid')
		Tool.Set_Output('GREENNESS', parameters[7].valueAsText, 'grid')
		Tool.Set_Output('WETNESS', parameters[8].valueAsText, 'grid')
		Tool.Run()
		return


class tool_4(object):
	def __init__(self):
		self.label = "IHS Sharpening"
		self.description = "<p>Intensity, hue, saturation (IHS) sharpening.</p><p></p><p>References:</p><p>Haydn, R., Dalke, G. W., Henkel, J., Bare, J. E. (1982): Application of the IHS color transform to the processing of multisensor data and image enhancement. Proceedings of the International Symposium on Remote Sensing of Arid and Semi-Arid Lands, Cairo, Egypt (Environmental Research Institute, Ann Arbor, Mich., 1982), pp. 599–616.</p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Red", name="R", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Green", name="G", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Blue", name="B", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Panchromatic Channel", name="PAN", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Red", name="R_SHARP", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Green", name="G_SHARP", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Blue", name="B_SHARP", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Sharpened Channels", name="SHARPEN", direction="Output", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Resampling", name="RESAMPLING", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["nearest neighbour", "bilinear", "cubic convolution"]
		param.value = "cubic convolution"
		params += [param]
		param = arcpy.Parameter(displayName="Panchromatic Channel Matching", name="PAN_MATCH", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["normalized", "standardized"]
		param.value = "normalized"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('imagery_tools', '4')
		Tool.Set_Input ('R', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('G', parameters[1].valueAsText, 'grid')
		Tool.Set_Input ('B', parameters[2].valueAsText, 'grid')
		Tool.Set_Input ('PAN', parameters[3].valueAsText, 'grid')
		Tool.Set_Output('R_SHARP', parameters[4].valueAsText, 'grid')
		Tool.Set_Output('G_SHARP', parameters[5].valueAsText, 'grid')
		Tool.Set_Output('B_SHARP', parameters[6].valueAsText, 'grid')
		Tool.Set_Output('SHARPEN', parameters[7].valueAsText, 'grid_list')
		Tool.Set_Option('RESAMPLING', parameters[8].valueAsText)
		Tool.Set_Option('PAN_MATCH', parameters[9].valueAsText)
		Tool.Run()
		return


class tool_5(object):
	def __init__(self):
		self.label = "Colour Normalized Brovey Sharpening"
		self.description = "<p>Colour normalized (Brovey) sharpening.</p><p></p><p>References:</p><p>Vrabel, J. (1996): Multispectral Imagery Band Sharpening Study. Photogrammetric Engineering & Remote Sensing, Vol. 62, No. 9, pp. 1075-1083.</p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Red", name="R", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Green", name="G", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Blue", name="B", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Panchromatic Channel", name="PAN", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Red", name="R_SHARP", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Green", name="G_SHARP", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Blue", name="B_SHARP", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Sharpened Channels", name="SHARPEN", direction="Output", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Resampling", name="RESAMPLING", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["nearest neighbour", "bilinear", "cubic convolution"]
		param.value = "cubic convolution"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('imagery_tools', '5')
		Tool.Set_Input ('R', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('G', parameters[1].valueAsText, 'grid')
		Tool.Set_Input ('B', parameters[2].valueAsText, 'grid')
		Tool.Set_Input ('PAN', parameters[3].valueAsText, 'grid')
		Tool.Set_Output('R_SHARP', parameters[4].valueAsText, 'grid')
		Tool.Set_Output('G_SHARP', parameters[5].valueAsText, 'grid')
		Tool.Set_Output('B_SHARP', parameters[6].valueAsText, 'grid')
		Tool.Set_Output('SHARPEN', parameters[7].valueAsText, 'grid_list')
		Tool.Set_Option('RESAMPLING', parameters[8].valueAsText)
		Tool.Run()
		return


class tool_6(object):
	def __init__(self):
		self.label = "Colour Normalized Spectral Sharpening"
		self.description = "<p>Colour normalized spectral sharpening.</p><p></p><p>References:</p><p>Vrabel, J., Doraiswamy, P., McMurtrey, J., Stern, A. (2002): Demonstration of the Accuracy of Improved Resolution Hyperspectral Imagery. SPIE Symposium Proceedings.</p><p></p><p>Vrabel, J., Doraiswamy, P., Stern, A. (2002): Application of Hyperspectral Imagery Resolution Improvement for Site-Specific Farming. ASPRS 2002 Conference Proceedings.</p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Original Channels", name="GRIDS", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="Panchromatic Channel", name="PAN", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Sharpened Channels", name="SHARPEN", direction="Output", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Resampling", name="RESAMPLING", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["nearest neighbour", "bilinear", "cubic convolution"]
		param.value = "cubic convolution"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('imagery_tools', '6')
		Tool.Set_Input ('GRIDS', parameters[0].valueAsText, 'grid_list')
		Tool.Set_Input ('PAN', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('SHARPEN', parameters[2].valueAsText, 'grid_list')
		Tool.Set_Option('RESAMPLING', parameters[3].valueAsText)
		Tool.Run()
		return


class tool_7(object):
	def __init__(self):
		self.label = "Principle Components Based Image Sharpening"
		self.description = "<p>Principle components based image sharpening.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Original Channels", name="GRIDS", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="Panchromatic Channel", name="PAN", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Sharpened Channels", name="SHARPEN", direction="Output", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Method", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["correlation matrix", "variance-covariance matrix", "sums-of-squares-and-cross-products matrix"]
		param.value = "sums-of-squares-and-cross-products matrix"
		params += [param]
		param = arcpy.Parameter(displayName="Resampling", name="RESAMPLING", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["nearest neighbour", "bilinear", "cubic convolution"]
		param.value = "cubic convolution"
		params += [param]
		param = arcpy.Parameter(displayName="Panchromatic Channel Matching", name="PAN_MATCH", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["normalized", "standardized"]
		param.value = "standardized"
		params += [param]
		param = arcpy.Parameter(displayName="Overwrite", name="OVERWRITE", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('imagery_tools', '7')
		Tool.Set_Input ('GRIDS', parameters[0].valueAsText, 'grid_list')
		Tool.Set_Input ('PAN', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('SHARPEN', parameters[2].valueAsText, 'grid_list')
		Tool.Set_Option('METHOD', parameters[3].valueAsText)
		Tool.Set_Option('RESAMPLING', parameters[4].valueAsText)
		Tool.Set_Option('PAN_MATCH', parameters[5].valueAsText)
		Tool.Set_Option('OVERWRITE', parameters[6].valueAsText)
		Tool.Run()
		return


class tool_8(object):
	def __init__(self):
		self.label = "Top of Atmosphere Reflectance"
		self.description = "<p>Calculation of top-of-atmosphere radiance or reflectance and temperature (TOAR) for Landsat MSS/TM/ETM+. This module incorporates E.J. Tizado's GRASS GIS implementation (i.landsat.toar).</p><p></p><p>References:</p><p><a target=\"_blank\" href=\"http://landsathandbook.gsfc.nasa.gov/\">Landsat 7 Science Data Users Handbook</a><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="DN Band 1", name="DN_MSS01", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="DN Band 2", name="DN_MSS02", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="DN Band 3", name="DN_MSS03", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="DN Band 4", name="DN_MSS04", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Reflectance Band 1", name="RF_MSS01", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Reflectance Band 2", name="RF_MSS02", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Reflectance Band 3", name="RF_MSS03", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Reflectance Band 4", name="RF_MSS04", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="DN Band 1", name="DN_ETM01", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="DN Band 2", name="DN_ETM02", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="DN Band 3", name="DN_ETM03", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="DN Band 4", name="DN_ETM04", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="DN Band 5", name="DN_ETM05", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="DN Band 7", name="DN_ETM07", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Reflectance Band 1", name="RF_ETM01", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Reflectance Band 2", name="RF_ETM02", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Reflectance Band 3", name="RF_ETM03", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Reflectance Band 4", name="RF_ETM04", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Reflectance Band 5", name="RF_ETM05", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Reflectance Band 7", name="RF_ETM07", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="DN Band 1", name="DN_OLI01", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="DN Band 2", name="DN_OLI02", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="DN Band 3", name="DN_OLI03", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="DN Band 4", name="DN_OLI04", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="DN Band 5", name="DN_OLI05", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="DN Band 6", name="DN_OLI06", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="DN Band 7", name="DN_OLI07", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="DN Band 9", name="DN_OLI09", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Reflectance Band 1", name="RF_OLI01", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Reflectance Band 2", name="RF_OLI02", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Reflectance Band 3", name="RF_OLI03", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Reflectance Band 4", name="RF_OLI04", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Reflectance Band 5", name="RF_OLI05", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Reflectance Band 6", name="RF_OLI06", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Reflectance Band 7", name="RF_OLI07", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Reflectance Band 9", name="RF_OLI09", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="DN Band 6", name="DN__TM06", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Reflectance Band 6", name="RF__TM06", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="DN Band 61", name="DN_ETM61", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="DN Band 62", name="DN_ETM62", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Reflectance Band 61", name="RF_ETM61", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Reflectance Band 62", name="RF_ETM62", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="DN Band 10", name="DN_OLI10", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="DN Band 11", name="DN_OLI11", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Reflectance Band 10", name="RF_OLI10", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Reflectance Band 11", name="RF_OLI11", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="DN Band 8", name="DN_PAN08", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Reflectance Band 8", name="RF_PAN08", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Metadata File", name="METAFILE", direction="Input", parameterType="Optional", datatype="DEFile")
		params += [param]
		param = arcpy.Parameter(displayName="Spacecraft Sensor", name="SENSOR", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Landsat-1 MSS", "Landsat-2 MSS", "Landsat-3 MSS", "Landsat-4 MSS", "Landsat-5 MSS", "Landsat-4 TM", "Landsat-5 TM", "Landsat-7 ETM+", "Landsat-8 OLI/TIRS"]
		param.value = "Landsat-7 ETM+"
		params += [param]
		param = arcpy.Parameter(displayName="Image Acquisition Date", name="DATE_ACQU", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = "2001-01-01"
		params += [param]
		param = arcpy.Parameter(displayName="Image Creation Date", name="DATE_PROD", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = "2001-01-01"
		params += [param]
		param = arcpy.Parameter(displayName="Suns's Height", name="SUN_HGT", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 45.000000
		params += [param]
		param = arcpy.Parameter(displayName="At-Sensor Radiance", name="AS_RAD", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Atmospheric Correction", name="AC_METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["uncorrected", "corrected", "dark object subtraction 1", "dark object subtraction 2", "dark object subtraction 2b", "dark object subtraction 3", "dark object subtraction 4"]
		param.value = "uncorrected"
		params += [param]
		param = arcpy.Parameter(displayName="Minimum Number of Dark Object Cells", name="AC_DO_CELLS", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 1000
		params += [param]
		param = arcpy.Parameter(displayName="Rayleigh Scattering", name="AC_RAYLEIGH", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Solar Radiance", name="AC_SUN_RAD", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Band 1", name="ETM_GAIN_10", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["low", "high"]
		param.value = "high"
		params += [param]
		param = arcpy.Parameter(displayName="Band 2", name="ETM_GAIN_20", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["low", "high"]
		param.value = "high"
		params += [param]
		param = arcpy.Parameter(displayName="Band 3", name="ETM_GAIN_30", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["low", "high"]
		param.value = "high"
		params += [param]
		param = arcpy.Parameter(displayName="Band 4", name="ETM_GAIN_40", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["low", "high"]
		param.value = "high"
		params += [param]
		param = arcpy.Parameter(displayName="Band 5", name="ETM_GAIN_50", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["low", "high"]
		param.value = "high"
		params += [param]
		param = arcpy.Parameter(displayName="Band 61", name="ETM_GAIN_61", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["low", "high"]
		param.value = "low"
		params += [param]
		param = arcpy.Parameter(displayName="Band 62", name="ETM_GAIN_62", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["low", "high"]
		param.value = "high"
		params += [param]
		param = arcpy.Parameter(displayName="Band 7", name="ETM_GAIN_70", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["low", "high"]
		param.value = "high"
		params += [param]
		param = arcpy.Parameter(displayName="Band 8", name="ETM_GAIN_80", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["low", "high"]
		param.value = "low"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('imagery_tools', '8')
		Tool.Set_Input ('DN_MSS01', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('DN_MSS02', parameters[1].valueAsText, 'grid')
		Tool.Set_Input ('DN_MSS03', parameters[2].valueAsText, 'grid')
		Tool.Set_Input ('DN_MSS04', parameters[3].valueAsText, 'grid')
		Tool.Set_Output('RF_MSS01', parameters[4].valueAsText, 'grid')
		Tool.Set_Output('RF_MSS02', parameters[5].valueAsText, 'grid')
		Tool.Set_Output('RF_MSS03', parameters[6].valueAsText, 'grid')
		Tool.Set_Output('RF_MSS04', parameters[7].valueAsText, 'grid')
		Tool.Set_Input ('DN_ETM01', parameters[8].valueAsText, 'grid')
		Tool.Set_Input ('DN_ETM02', parameters[9].valueAsText, 'grid')
		Tool.Set_Input ('DN_ETM03', parameters[10].valueAsText, 'grid')
		Tool.Set_Input ('DN_ETM04', parameters[11].valueAsText, 'grid')
		Tool.Set_Input ('DN_ETM05', parameters[12].valueAsText, 'grid')
		Tool.Set_Input ('DN_ETM07', parameters[13].valueAsText, 'grid')
		Tool.Set_Output('RF_ETM01', parameters[14].valueAsText, 'grid')
		Tool.Set_Output('RF_ETM02', parameters[15].valueAsText, 'grid')
		Tool.Set_Output('RF_ETM03', parameters[16].valueAsText, 'grid')
		Tool.Set_Output('RF_ETM04', parameters[17].valueAsText, 'grid')
		Tool.Set_Output('RF_ETM05', parameters[18].valueAsText, 'grid')
		Tool.Set_Output('RF_ETM07', parameters[19].valueAsText, 'grid')
		Tool.Set_Input ('DN_OLI01', parameters[20].valueAsText, 'grid')
		Tool.Set_Input ('DN_OLI02', parameters[21].valueAsText, 'grid')
		Tool.Set_Input ('DN_OLI03', parameters[22].valueAsText, 'grid')
		Tool.Set_Input ('DN_OLI04', parameters[23].valueAsText, 'grid')
		Tool.Set_Input ('DN_OLI05', parameters[24].valueAsText, 'grid')
		Tool.Set_Input ('DN_OLI06', parameters[25].valueAsText, 'grid')
		Tool.Set_Input ('DN_OLI07', parameters[26].valueAsText, 'grid')
		Tool.Set_Input ('DN_OLI09', parameters[27].valueAsText, 'grid')
		Tool.Set_Output('RF_OLI01', parameters[28].valueAsText, 'grid')
		Tool.Set_Output('RF_OLI02', parameters[29].valueAsText, 'grid')
		Tool.Set_Output('RF_OLI03', parameters[30].valueAsText, 'grid')
		Tool.Set_Output('RF_OLI04', parameters[31].valueAsText, 'grid')
		Tool.Set_Output('RF_OLI05', parameters[32].valueAsText, 'grid')
		Tool.Set_Output('RF_OLI06', parameters[33].valueAsText, 'grid')
		Tool.Set_Output('RF_OLI07', parameters[34].valueAsText, 'grid')
		Tool.Set_Output('RF_OLI09', parameters[35].valueAsText, 'grid')
		Tool.Set_Input ('DN__TM06', parameters[36].valueAsText, 'grid')
		Tool.Set_Output('RF__TM06', parameters[37].valueAsText, 'grid')
		Tool.Set_Input ('DN_ETM61', parameters[38].valueAsText, 'grid')
		Tool.Set_Input ('DN_ETM62', parameters[39].valueAsText, 'grid')
		Tool.Set_Output('RF_ETM61', parameters[40].valueAsText, 'grid')
		Tool.Set_Output('RF_ETM62', parameters[41].valueAsText, 'grid')
		Tool.Set_Input ('DN_OLI10', parameters[42].valueAsText, 'grid')
		Tool.Set_Input ('DN_OLI11', parameters[43].valueAsText, 'grid')
		Tool.Set_Output('RF_OLI10', parameters[44].valueAsText, 'grid')
		Tool.Set_Output('RF_OLI11', parameters[45].valueAsText, 'grid')
		Tool.Set_Input ('DN_PAN08', parameters[46].valueAsText, 'grid')
		Tool.Set_Output('RF_PAN08', parameters[47].valueAsText, 'grid')
		Tool.Set_Option('METAFILE', parameters[48].valueAsText)
		Tool.Set_Option('SENSOR', parameters[49].valueAsText)
		Tool.Set_Option('DATE_ACQU', parameters[50].valueAsText)
		Tool.Set_Option('DATE_PROD', parameters[51].valueAsText)
		Tool.Set_Option('SUN_HGT', parameters[52].valueAsText)
		Tool.Set_Option('AS_RAD', parameters[53].valueAsText)
		Tool.Set_Option('AC_METHOD', parameters[54].valueAsText)
		Tool.Set_Option('AC_DO_CELLS', parameters[55].valueAsText)
		Tool.Set_Option('AC_RAYLEIGH', parameters[56].valueAsText)
		Tool.Set_Option('AC_SUN_RAD', parameters[57].valueAsText)
		Tool.Set_Option('ETM_GAIN_10', parameters[58].valueAsText)
		Tool.Set_Option('ETM_GAIN_20', parameters[59].valueAsText)
		Tool.Set_Option('ETM_GAIN_30', parameters[60].valueAsText)
		Tool.Set_Option('ETM_GAIN_40', parameters[61].valueAsText)
		Tool.Set_Option('ETM_GAIN_50', parameters[62].valueAsText)
		Tool.Set_Option('ETM_GAIN_61', parameters[63].valueAsText)
		Tool.Set_Option('ETM_GAIN_62', parameters[64].valueAsText)
		Tool.Set_Option('ETM_GAIN_70', parameters[65].valueAsText)
		Tool.Set_Option('ETM_GAIN_80', parameters[66].valueAsText)
		Tool.Run()
		return


class tool_9(object):
	def __init__(self):
		self.label = "Automated Cloud Cover Assessment"
		self.description = "<p>Automated Cloud-Cover Assessment (ACCA) for Landsat TM/ETM+ imagery as proposed by Irish (2000). This module incorporates E.J. Tizado's GRASS GIS implementation (i.landsat.acca).</p><p></p><p>References:</p><p>- Irish, R.R. (2000): Landsat 7 Automatic Cloud Cover Assessment. In Shen, S.S., Descour, M.R. (Eds.): Algorithms for Multispectral, Hyperspectral, and Ultraspectral Imagery VI.  Proceedings of SPIE, 4049: 348-355. <a target=\"_blank\" href=\"http://landsathandbook.gsfc.nasa.gov/pdfs/ACCA_SPIE_paper.pdf\">online</a>.</p><p>- Irish, R.R., Barker J.L., Goward S.N., Arvidson T. (2006):  Characterization of the Landsat-7 ETM+ Automated Cloud-Cover Assessment (ACCA) Algorithm. Photogrammetric Engineering and Remote Sensing vol. 72(10): 1179-1188. <a target=\"_blank\" href=\"http://landsathandbook.gsfc.nasa.gov/pdfs/ACCA_Special_Issue_Final.pdf\">online</a>.</p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Landsat Band 2", name="BAND2", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Landsat Band 3", name="BAND3", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Landsat Band 4", name="BAND4", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Landsat Band 5", name="BAND5", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Landsat Band 6", name="BAND6", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Cloud Cover", name="CLOUD", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Apply post-processing filter to remove small holes", name="FILTER", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="B56 Composite (step 6)", name="B56C", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 225.000000
		params += [param]
		param = arcpy.Parameter(displayName="B45 Ratio: Desert detection (step 10)", name="B45R", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Always use cloud signature (step 14)", name="CSIG", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Bypass second-pass processing, and merge warm (not ambiguous) and cold clouds", name="PASS2", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Include a category for cloud shadows", name="SHADOW", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('imagery_tools', '9')
		Tool.Set_Input ('BAND2', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('BAND3', parameters[1].valueAsText, 'grid')
		Tool.Set_Input ('BAND4', parameters[2].valueAsText, 'grid')
		Tool.Set_Input ('BAND5', parameters[3].valueAsText, 'grid')
		Tool.Set_Input ('BAND6', parameters[4].valueAsText, 'grid')
		Tool.Set_Output('CLOUD', parameters[5].valueAsText, 'grid')
		Tool.Set_Option('FILTER', parameters[6].valueAsText)
		Tool.Set_Option('B56C', parameters[7].valueAsText)
		Tool.Set_Option('B45R', parameters[8].valueAsText)
		Tool.Set_Option('CSIG', parameters[9].valueAsText)
		Tool.Set_Option('PASS2', parameters[10].valueAsText)
		Tool.Set_Option('SHADOW', parameters[11].valueAsText)
		Tool.Run()
		return


class tool_10(object):
	def __init__(self):
		self.label = "Landsat Import with Options"
		self.description = "<p>This tool facilitates the import and display of Landsat scenes, which have each band given as a single GeoTIFF file.</p><p></p><p>The development of this tool has been requested and sponsored by Rohan Fisher, Charles Darwin University, Australia. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Files", name="FILES", direction="Input", parameterType="Optional", datatype="DEFile", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="Bands", name="BANDS", direction="Output", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Coordinate System", name="PROJECTION", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["UTM North", "UTM South", "Geographic Coordinates"]
		param.value = "UTM North"
		params += [param]
		param = arcpy.Parameter(displayName="Interpolation", name="INTERPOLATION", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Nearest Neighbour", "Bilinear Interpolation", "Cubic Convolution"]
		param.value = "Cubic Convolution"
		params += [param]
		param = arcpy.Parameter(displayName="Show a Composite", name="SHOW_RGB", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Red", name="SHOW_R", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["no choice available"]
		param.value = "no choice available"
		params += [param]
		param = arcpy.Parameter(displayName="Green", name="SHOW_G", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["no choice available"]
		param.value = "no choice available"
		params += [param]
		param = arcpy.Parameter(displayName="Blue", name="SHOW_B", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["no choice available"]
		param.value = "no choice available"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('imagery_tools', '10')
		Tool.Set_Option('FILES', parameters[0].valueAsText)
		Tool.Set_Output('BANDS', parameters[1].valueAsText, 'grid_list')
		Tool.Set_Option('PROJECTION', parameters[2].valueAsText)
		Tool.Set_Option('INTERPOLATION', parameters[3].valueAsText)
		Tool.Set_Option('SHOW_RGB', parameters[4].valueAsText)
		Tool.Set_Option('SHOW_R', parameters[5].valueAsText)
		Tool.Set_Option('SHOW_G', parameters[6].valueAsText)
		Tool.Set_Option('SHOW_B', parameters[7].valueAsText)
		Tool.Run()
		return
