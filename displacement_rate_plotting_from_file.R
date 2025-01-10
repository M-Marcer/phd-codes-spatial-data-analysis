# Code to plot displacement rates from csv file produced by the code Study_sites_displacement_rates_calculator.R

rm(list=ls())

library(rgdal)
library(raster)

root = "D:/Marcer_Materials"

# Set R Working Directory
wd<-paste(root,"codes",sep="/")
setwd(wd)

source("toolbox/displacement_rates_functions.R")
source("toolbox/plot_functions.R")
#############################################################"

# Files 
files = c("tl_ID_4.csv","pp_ID_1.csv")

folder = "rock_glacier_displacemet_output"


# Define graphical parameters

colors=c(rgb(0.5,0.5,0.5,0.6),rgb(0.1,0.1,0.1,0.6),rgb(0.0,0.7,0.7,0.6),
         rgb(0.1,0.1,0.5,0.6),rgb(0.4,0.0,1,0.6),rgb(1,0.0,0.4,0.6),
         rgb(1,0.1,0.4,0.6),rgb(0.1,0.1,0.1,0.6),rgb(0.0,0.7,0.7,0.6))

colors_uc<-c(rgb(0.7,0.7,0.7,0.4),rgb(0.1,0.1,0.1,0.1),rgb(0.0,0.7,0.7,0.1),
             rgb(0.1,0.1,0.7,0.1),rgb(0.7,0.7,1,0.4),rgb(1,0.1,1,0.4),
             rgb(1,0.1,0.4,0.1),rgb(0.1,0.1,0.1,0.1),rgb(0.0,0.7,0.7,0.1))

colors_uc

style=c(1,1,1,
        1,2,2,
        2,2,2,1,2,1,2,1,2)

#############################################################"

for (k in 1:length(files)){
  
  moving_target = read.csv(paste(folder,files[k],sep="/"))
  print(sprintf("plotting %s",files[k]))
  #plot_rg_rates(k,sort(unique(moving_target$Y)),moving_target$speed/mean(moving_target$speed),0*moving_target$weighted_uncertainty,colors,colors_uc,style)
  years = sort(unique(as.numeric(unlist(strsplit(as.character(moving_target$year),split = " - ")))))
  plot_rg_rates(k,years,moving_target$speed,moving_target$weighted_uncertainty,colors,colors_uc,style)
  
}

