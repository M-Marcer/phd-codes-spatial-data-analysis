# Code to calculate movements on long time series based on manual feature tracking, stored in the file:
# root\..\local\analysis\sites_feature_tracking.shp
# Produces a output plot of the user-selected rock glacier (variable: site) and blocks (variable : idsel) 
# As econdary output, produces csv with displacement rates and uncertainties per each period.
# The csv can be plotted using the code displacement_rate_plotting_from_file.R, allowing to plot diplsacement rates from different sites in the same figure


rm(list=ls())

library(rgdal)
library(raster)

root = "D:/Marcer_Materials"

# Set R Working Directory
wd<-paste(root,"codes",sep="/")
setwd(wd)

source("toolbox/displacement_rates_functions.R")
source("toolbox/plot_functions.R")

#########################################################################################################################

# 0 . Import data

  filename="sites_feature_tracking"

	collected_data<- readOGR(dsn=paste(root,"final_products/local/analysis",sep="/"),layer=filename)
	collected_data$year=as.numeric(as.character(collected_data$year))

# Define site to investigate
	rg<-"tl"

# Select points to be analyzed 
	#idsel=c(8,9,1)  # set-up SI
	#idsel=c(1,2,3,4,5)  # set-up PB
	#idsel=c(4,5,6,10) # set up tl
	#idsel=c(3,4,6,7,5)  # set up rn
  idsel = c(4)

# Define graphical parameters

	colors=c(rgb(0.5,0.5,0.5,0.6),rgb(0.0,0.7,0.7,0.6),rgb(0.4,0.0,1,1),rgb(1,0.0,0.4,1),rgb(1,0.4,0.4,1))
	colors_uc<-c(rgb(0.7,0.7,0.7,0.4),rgb(0.0,0.7,0.7,0.4),rgb(0.7,0.7,1,0.4),rgb(1,0.4,1,0.4),rgb(1,0.4,0.4,0.4))

	style=c(1,1,2,2,1,2,1,2,1,2,1,2,1,2,1,2)

# Define if you got uncertainty estimation 
	
	uncerainty_analysis = TRUE

#########################################################################################################################


	data<-subset(collected_data,collected_data$site==rg)
	moving_targets <- subset(data,data$type=="rg")
	fixed_areas <- subset(data,data$type=="zf")
	
	output = list()

for (k in 1:length(idsel)){
  
  cat(sprintf("\n Treating point ID = %i\n",idsel[k]))
		
	moving_target = subset(moving_targets,moving_targets$id==idsel[k])

	# 1 . Compute rates 

	rates <- compute_distances_and_rates(moving_target)

	# 2 . Uncertainty 
	
	uncertainty <- distance_wieghted_uncertainty(uncerainty_analysis,moving_target,fixed_areas)

 	 # 3 . Create output data
	
	output[[k]]  = merge(rates,uncertainty,by = intersect(names(rates), names(uncertainty)))
	
	# 4 . Speed Plot

	plot_rg_rates(k,sort(unique(moving_target$year)),output[[k]]$speed,output[[k]]$weighted_uncertainty,colors,colors_uc,style)
	
	# 5 . Save data
	write.csv(output[[k]],file = sprintf("rock_glacier_displacemet_output/%s_ID_%i.csv",rg,idsel[k]))
	
}

	# 6 . User ouput
	
	print(output)




