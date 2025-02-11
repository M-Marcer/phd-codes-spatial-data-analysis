#	Recent Speed Calculator
# 	Created the 30/08/2017
#   Re-worked since 05/03/2019

# The code is meant to take surface blocks manual feature tracking points and compute speed diagrams

# The input point file needs as attributes:

# id: is the id of the block
# ID_RG: rock glacier id
# year: year of the dataset position of the block
# type: rg if is on rock glacier, zf for fixed areas (uncertainty estimation)

#################################################################################
rm(list=ls())

# Step 0 - Set Working station
library(rgdal)
library(RSAGA)
library(raster)
library(RColorBrewer)

# Machine setup

root = "D:/Marcer_Materials"

# Set R Working Directory
wd<-paste(root,"codes",sep="/")
setwd(wd)

# RSAGA working environment
SAGAWD=paste(wd,"SAGAWD",sep='/')
myenv<-rsaga.env(workspace=SAGAWD,path=paste(wd,"saga_2.2.2_x64/saga_2.2.2_x64",sep="/"))

# Displacement regional scale data
DATAPATH<-paste(root,"final_products/regional/shapes/regional_displacements_tracking",sep="/")
filename<-"regional_displacements_tracking"
data <- readOGR(dsn = DATAPATH, layer = filename)

# Rock Glaciers Inventory
INVPATH<-paste(root,"data/shapes/inventory_RTM",sep="/")  # Rock glaciers inventory folder
inv<-"rock_glaciers_france_inventory"
rock_glaciers <- readOGR(dsn = INVPATH, layer = inv)

rock_glaciers <- rock_glaciers["sample_spe"]
rock_glaciers$ID_complet = seq(1,length(rock_glaciers$sample_spe),1)

# Path to destablization rates
DESTPATH<-paste(root,"final_products/regional/shapes/rock_glacier_inventory",sep="/")
dest_rate<-"rock_glaciers_centroids_MM"
destabilization_rates <-readOGR(dsn=DESTPATH,layer=dest_rate)

# IGN years shapefiles
ign1950<-readOGR(dsn = paste(root,"data/shapes/IGN_WMS_dates",sep="/"), layer = "IGN1950")
ign2000<-readOGR(dsn = paste(root,"data/shapes/IGN_WMS_dates",sep="/"), layer = "IGN2000")
ign2006<-readOGR(dsn = paste(root,"data/shapes/IGN_WMS_dates",sep="/"), layer = "IGN2006")
ign2015<-readOGR(dsn = paste(root,"data/shapes/IGN_WMS_dates",sep="/"), layer = "IGN2015")

# Write data in SAGAWD for working in local
writeOGR(data, layer="data", dsn=SAGAWD,driver="ESRI Shapefile", overwrite_layer=TRUE)
writeOGR(rock_glaciers, layer="rock_glaciers", dsn=SAGAWD,driver="ESRI Shapefile", overwrite_layer=TRUE)
writeOGR(destabilization_rates, layer="destabilization_rates", dsn=SAGAWD,driver="ESRI Shapefile", overwrite_layer=TRUE)

writeOGR(ign1950, layer="ign1950", dsn=SAGAWD,driver="ESRI Shapefile", overwrite_layer=TRUE)
writeOGR(ign2000, layer="ign2000", dsn=SAGAWD,driver="ESRI Shapefile", overwrite_layer=TRUE)
writeOGR(ign2006, layer="ign2006", dsn=SAGAWD,driver="ESRI Shapefile", overwrite_layer=TRUE)
writeOGR(ign2015, layer="ign2015", dsn=SAGAWD,driver="ESRI Shapefile", overwrite_layer=TRUE)

############################################################################

# SAMPLING PART --> Measurement points need to get IGN dates and rock glaciers characteristics

# Sampling IGN ploygons
rsaga.geoprocessor("shapes_points",10,list(INPUT="data.shp",OUTPUT="data.shp",FIELDS="year",POLYGONS="ign1950.shp"),env=myenv)
rsaga.geoprocessor("shapes_points",10,list(INPUT="data.shp",OUTPUT="data.shp",FIELDS="year",POLYGONS="ign2000.shp"),env=myenv)
rsaga.geoprocessor("shapes_points",10,list(INPUT="data.shp",OUTPUT="data.shp",FIELDS="year",POLYGONS="ign2006.shp"),env=myenv)
rsaga.geoprocessor("shapes_points",10,list(INPUT="data.shp",OUTPUT="data.shp",FIELDS="year",POLYGONS="ign2015.shp"),env=myenv)

# Add destabilization rates and sapmle speed to RG inventory polygons 
rsaga.geoprocessor("shapes_polygons",20,list(INPUT="rock_glaciers.shp",OUTPUT="rock_glaciers.shp",FIELDS="Dest_rate",POINTS="destabilization_rates.shp"),env=myenv)

# Add rock glacier inventory attributes to data
rsaga.geoprocessor("shapes_points",10,list(INPUT="data.shp",OUTPUT="data.shp",FIELDS="ID_complet",POLYGONS="rock_glaciers.shp"),env=myenv)
rsaga.geoprocessor("shapes_points",10,list(INPUT="data.shp",OUTPUT="data.shp",FIELDS="Dest_rate",POLYGONS="rock_glaciers.shp"),env=myenv)
rsaga.geoprocessor("shapes_points",10,list(INPUT="data.shp",OUTPUT="data.shp",FIELDS="sample_spe",POLYGONS="rock_glaciers.shp"),env=myenv)

############################################################################
# Import data and assign real year to each point
rock_glaciers = readOGR(dsn = SAGAWD, layer = "rock_glaciers")

data <- readOGR(dsn = SAGAWD, layer = "data")
data$ign = 0

for (i in 1:length(data)){
  if (data$IGN_year[[i]]==1950){
    data$ign[[i]]=as.numeric(as.character(data$year[[i]]))
  }
  if (data$IGN_year[[i]]==2000){
    data$ign[[i]]=as.numeric(as.character(data$year.1[[i]]))
  }
  if (data$IGN_year[[i]]==2006){
    data$ign[[i]]=as.numeric(as.character(data$year.2[[i]]))
  }
  if (data$IGN_year[[i]]==2015){
    data$ign[[i]]=as.numeric(as.character(data$year.3[[i]]))
  }
}

#########################################################################################################################
# END OF DATA PRE-PROCESSING!!!
###########################################################################################################################

sign_factor = 2  # significance factor: if displacement > uncertianty*sing_factor, then S is significant

zf<- subset(data,Type=="zf")
rg<-subset(data,Type=="rg")

# Prepare storage data
# storage is based on periods :
  #Period1 : 1950 - 2001
  #Period2 : 2001 - 2006
  #Period3 : 2006 - 2015
# Each period has speed and uncertainty

names_in_storage = c("Year1","Year2","Year3","Year4","period1","period2","period3","UC_1","UC_2","UC_3","S_1","S_2","S_3")
storage=array(NA,dim=c(length(rock_glaciers$ID_complet),length(names_in_storage)))
storage<-data.frame(storage)
colnames(storage)<-names_in_storage

# Prepare zf by dates(reduce computation time)
zf_1950 = subset(zf,zf$IGN_year == 1950)
zf_2000 = subset(zf,zf$IGN_year == 2000)
zf_2006 = subset(zf,zf$IGN_year == 2006)
zf_2015 = subset(zf,zf$IGN_year == 2015)

# Evaluate Speed and uncertainty
#3238

for (i in 1:length(storage$Year1)){
  # Assign destabilization index and rock glacier ID
  #storage$dest_rate[[i]] = as.numeric(as.character(destabilization_rates$Dest_rate))[[i]]
  #storage$ID[[i]] = as.numeric(as.character(destabilization_rates$ID_complet))[[i]]
  
  storage$ID_complet[[i]] = as.numeric(as.character(rock_glaciers$ID_complet))[[i]]
  storage$dest_rate[[i]] = as.numeric(as.character(rock_glaciers$Dest_rate))[[i]]
  
  # Get moving block on the surface  (only id =1)
  rg_blocks<-subset(rg,ID_complet==as.numeric(as.character(rock_glaciers$ID_complet)[[i]]) & rg$id == 1)
  
  # If on the ith rock glaciers speeds are not available then skip to next iteration
  #print(sprintf("Warning, The rock glacier ID : %s does not have displacement evaluation",destabilization_rates$ID_complet[[i]]))
  if (length(rg_blocks)==0)next
  
  # If there are more than 4 blocks there is an error
  if (length(rg_blocks)>4)next
  
  #####################################################################################
  # Define how many and which dates are available, get closest zfs
  aux_1 = subset(rg_blocks,IGN_year == 1950)
  if (length(aux_1)!=0){
    storage$Year1[[i]] = as.numeric(as.character(aux_1$year))
    auc_1 = coordinates(zf_1950[which.min(pointDistance(aux_1,zf_1950)),1])} 
  
  aux_2 = subset(rg_blocks,IGN_year == 2000)
  if (length(aux_2)!=0){
    storage$Year2[[i]] = as.numeric(as.character(aux_2$year.1))
    auc_2 = coordinates(zf_2000[which.min(pointDistance(aux_2,zf_2000)),1])}
  
  aux_3 = subset(rg_blocks,IGN_year == 2006)
  if (length(aux_3)!=0){
    storage$Year3[[i]] = as.numeric(as.character(aux_3$year.2))
    auc_3 = coordinates(zf_2006[which.min(pointDistance(aux_3,zf_2006)),1])}
  
  aux_4 = subset(rg_blocks,IGN_year == 2015)
  if (length(aux_4)!=0){
    storage$Year4[[i]] = as.numeric(as.character(aux_4$year.3))
    auc_4 = coordinates(zf_2015[which.min(pointDistance(aux_4,zf_2015)),1])}
  
  #####################################################################################
  # Compute distances, uncertainties and significance (set by sign_factor)
  temp = pointDistance(aux_1,aux_2)
  if (length(temp)==1){
    storage$period1[[i]] = temp/(-storage$Year1[[i]] + storage$Year2[[i]])
    storage$UC_1[i] = sqrt(((auc_1-auc_2)[1])^2+((auc_1-auc_2)[2])^2)/(-storage$Year1[[i]] + storage$Year2[[i]])
    if(storage$period1[[i]]>storage$UC_1[[i]]*sign_factor){storage$S_1[[i]]="Y"}else{storage$S_1[[i]]="N"}}
  
  temp = pointDistance(aux_2,aux_3)
  if (length(temp)==1){
    storage$period2[[i]] = temp/(-storage$Year2[[i]] + storage$Year3[[i]])
    storage$UC_2[i]= sqrt(((auc_2-auc_3)[1])^2+((auc_2-auc_3)[2])^2)/(-storage$Year2[[i]] + storage$Year3[[i]])
    if(storage$period2[[i]]>storage$UC_2[[i]]*sign_factor){storage$S_2[[i]]="Y"}else{storage$S_2[[i]]="N"}}
  
  temp = pointDistance(aux_3,aux_4)
  if (length(temp)==1){
    storage$period3[[i]] = temp/(-storage$Year3[[i]] + storage$Year4[[i]])
    storage$UC_3[i] = sqrt(((auc_3-auc_4)[1])^2+((auc_3-auc_4)[2])^2)/(-storage$Year3[[i]] + storage$Year4[[i]])
    if(storage$period3[[i]]>storage$UC_3[[i]]*sign_factor){storage$S_3[[i]]="Y"}else{storage$S_3[[i]]="N"}}
  }

rock_glaciers$ID_complet[[i]]

#################################################################################################################################

# Some info about the treatement

# Number of treated rock glaciers
print(sprintf("Allegdely moving rock glaciers : %i",length(subset(rock_glaciers,sample_spe == 1))))
print(sprintf("Significant movements in : %i",nrow(subset(storage,S_3=="Y" | S_2=="Y" | S_1=="Y"))))
print(sprintf("Available in period 1 : %i  , significant : %i ",nrow(subset(storage,is.na(period1)==FALSE)),nrow(subset(storage,S_1=="Y"))))
print(sprintf("Available in period 2 : %i  , significant : %i ",nrow(subset(storage,is.na(period2)==FALSE)),nrow(subset(storage,S_2=="Y"))))
print(sprintf("Available in period 3 : %i  , significant : %i ",nrow(subset(storage,is.na(period3)==FALSE)),nrow(subset(storage,S_3=="Y"))))
print(sprintf("Significant in all periods : %i ",nrow(subset(storage,S_3=="Y" & S_2=="Y" & S_1=="Y"))))

# WORK WITH RG SIGNIFICANT MOVEMENTS IN ALL PERIODS
# Basics statistics for periods/rates
p1 = subset(storage,S_3=="Y" & S_2=="Y" & S_1=="Y") # Stats done only on rgs with all data available
print(sprintf("MEANS by PERIODS ; 1 --> %f; 2 --> %f; 3 --> %f; ",mean(p1$period1),mean(p1$period2),mean(p1$period3)))
print(sprintf("percent increase ; %f",mean(p1$period3)/mean(p1$period1)*100))
aggregate(p1, list(p1$dest_rate), mean, na.omit=TRUE)

# Significant acceleration/deceleration
p1$decel_12 = p1$period1-p1$UC_1 > p1$period2+p1$UC_2
p1$accel_12 = p1$period1+p1$UC_1 < p1$period2-p1$UC_2

p1$decel_23 = p1$period2-p1$UC_2 > p1$period3+p1$UC_3
p1$accel_23 = p1$period2+p1$UC_2 < p1$period3-p1$UC_3

nrow(subset(p1,decel_12 ==TRUE))
nrow(subset(p1,accel_12 ==TRUE))
nrow(subset(p1,decel_23 ==TRUE))
nrow(subset(p1,accel_23 ==TRUE))

nrow(subset(p1,accel_23 ==TRUE & accel_12==TRUE))
nrow(subset(p1,decel_23 ==TRUE & decel_12 ==TRUE))

##########################################################################################################
# WORK WITH RG SIGNIFICANT MOVEMENTS IN AT LEAST ONE PERIOD
p1 = subset(storage,S_3=="Y" | S_2=="Y" | S_1=="Y") 
m1 = subset(storage,S_1=="Y")
m2 = subset(storage,S_2=="Y")
m3 = subset(storage,S_3=="Y")

print(sprintf("MEANS by PERIODS ; 1 --> %f; 2 --> %f; 3 --> %f; ",mean(m1$period1,na.rm = TRUE),mean(m2$period2,na.rm = TRUE),mean(m3$period3,na.rm = TRUE)))
print(sprintf("percent increase ; %f",mean(m2$period2)/mean(m1$period1)*100))
print(sprintf("percent increase ; %f",mean(m3$period3)/mean(m1$period1)*100))

#Means by displacement rate
m1d0 = subset(m1,dest_rate == 0)
m1d1 = subset(m1,dest_rate == 1)
m1d2 = subset(m1,dest_rate == 2)
m1d3 = subset(m1,dest_rate == 3)
m1d4 = subset(m1,dest_rate == 4)

print(sprintf("MEANS by dest_rate in P1 ; 0 --> %f; 1 --> %f; 2 --> %f; 3 --> %f; 4 --> %f;"
              ,mean(m1d0$period1),mean(m1d1$period1),mean(m1d2$period1),mean(m1d3$period1),mean(m1d4$period1)))
count(m1$dest_rate)

m1d0 = subset(m2,dest_rate == 0)
m1d1 = subset(m2,dest_rate == 1)
m1d2 = subset(m2,dest_rate == 2)
m1d3 = subset(m2,dest_rate == 3)
m1d4 = subset(m2,dest_rate == 4)

print(sprintf("MEANS by dest_rate in P2 ; 0 --> %f; 1 --> %f; 2 --> %f; 3 --> %f; 4 --> %f;"
              ,mean(m1d0$period2),mean(m1d1$period2),mean(m1d2$period2),mean(m1d3$period2),mean(m1d4$period2)))
count(m2$dest_rate)

m1d0 = subset(m3,dest_rate == 0)
m1d1 = subset(m3,dest_rate == 1)
m1d2 = subset(m3,dest_rate == 2)
m1d3 = subset(m3,dest_rate == 3)
m1d4 = subset(m3,dest_rate == 4)

print(sprintf("MEANS by dest_rate in P3 ; 0 --> %f; 1 --> %f; 2 --> %f; 3 --> %f; 4 --> %f;"
              ,mean(m1d0$period3),mean(m1d1$period3),mean(m1d2$period3),mean(m1d3$period3),mean(m1d4$period3)))
count(m3$dest_rate)


# Significant acceleration/deceleration
p1$decel_12 = p1$period1-p1$UC_1 > p1$period2+p1$UC_2
p1$accel_12 = p1$period1+p1$UC_1 < p1$period2-p1$UC_2

p1$decel_23 = p1$period2-p1$UC_2 > p1$period3+p1$UC_3
p1$accel_23 = p1$period2+p1$UC_2 < p1$period3-p1$UC_3

nrow(subset(p1,decel_12 ==TRUE))
nrow(subset(p1,accel_12 ==TRUE))
nrow(subset(p1,decel_23 ==TRUE))
nrow(subset(p1,accel_23 ==TRUE))

nrow(subset(p1,accel_23 ==TRUE & accel_12==TRUE))
nrow(subset(p1,decel_23 ==TRUE & decel_12 ==TRUE))

# Find which rock glacier are accelerating or decelerating (in terms of destabilization and initial velocity)
p1= subset(p1, is.na(p1$dest_rate)==FALSE)

A12 = subset(p1,accel_12 ==TRUE & is.na(dest_rate)==FALSE)
D12 = subset(p1,decel_12 ==TRUE)

count(A12$dest_rate)
count(D12$dest_rate)

mean(A12$period1)
mean(D12$period1)

A23 = subset(p1,accel_23 ==TRUE & is.na(dest_rate)==FALSE)
D23 = subset(p1,decel_23 ==TRUE & is.na(dest_rate)==FALSE)

count(A23$dest_rate)/count(p1$dest_rate)
count(D23$dest_rate)/count(p1$dest_rate)

mean(A23$period2)
mean(D23$period2)

#################################################################################################################################

# Create OUTPUT --> rock glaciers centroids with displacement rates, one per period

# Create centroids
rsaga.geoprocessor("shapes_polygons",1,list(POLYGONS = "rock_glaciers.shp",CENTROIDS = "rg_centroids.shp"),env=myenv)

rg_centroids = readOGR(dsn = SAGAWD, layer = "rg_centroids")

rg_centroids$period1<-0
rg_centroids$period2<-0
rg_centroids$period3<-0

rg_centroids$year_1<-0
rg_centroids$year_2<-0
rg_centroids$year_3<-0
rg_centroids$year_4<-0

#Create general Output with all produced data on all periods
for (i in 1:length(storage$ID)){
  
  idx<-match(storage$ID[[i]],rg_centroids$ID_complet)
  rg_centroids$period1[[idx]]=storage$period1[[i]]
  rg_centroids$period2[[idx]]<-storage$period2[[i]]
  rg_centroids$period3[[idx]]<-storage$period3[[i]]
  
  rg_centroids$uc_1[[idx]]=storage$UC_1[[i]]
  rg_centroids$uc_2[[idx]]<-storage$UC_2[[i]]
  rg_centroids$uc_3[[idx]]<-storage$UC_3[[i]]
  
  rg_centroids$S_1[[idx]]=storage$S_1[[i]]
  rg_centroids$S_2[[idx]]<-storage$S_2[[i]]
  rg_centroids$S_3[[idx]]<-storage$S_3[[i]]
  
  rg_centroids$year_1[[idx]]<-storage$Year1[[i]]
  rg_centroids$year_2[[idx]]<-storage$Year2[[i]]
  rg_centroids$year_3[[idx]]<-storage$Year3[[i]]
  rg_centroids$year_4[[idx]]<-storage$Year4[[i]]
}
writeOGR(rg_centroids,layer="inventory_displacement_rates",dsn=SAGAWD,driver="ESRI Shapefile", overwrite_layer=TRUE)

# Get only significant movements in all three periods and produce a shapefile per period 
#S_centroids = subset(rg_centroids,S_1 == "Y" & S_2 == "Y" & S_3 == "Y")


temp = subset(rg_centroids,S_1 == "Y")
separate_output = temp
separate_output$displacement_rates = temp$period1
separate_output$UC = temp$uc_1
writeOGR(separate_output,layer="displacement_rates_period1",dsn=SAGAWD,driver="ESRI Shapefile", overwrite_layer=TRUE)

temp = subset(rg_centroids,S_2 == "Y")
separate_output = temp
separate_output$displacement_rates = temp$period2
separate_output$UC = temp$uc_2
writeOGR(separate_output,layer="displacement_rates_period2",dsn=SAGAWD,driver="ESRI Shapefile", overwrite_layer=TRUE)

temp = subset(rg_centroids,S_3 == "Y")
separate_output = temp
separate_output$displacement_rates = temp$period3
separate_output$UC = temp$uc_3
writeOGR(separate_output,layer="displacement_rates_period3",dsn=SAGAWD,driver="ESRI Shapefile", overwrite_layer=TRUE)


#####################################################################################
# Plots 

M<-na.omit(storage)
M <- storage
#M_sd<-subset(M,period1>UC_1 & period2>UC_2)
#M<-M_sd

M0<-subset(M,dest_rate==0)
M1<-subset(M,dest_rate==1)
M2<-subset(M,dest_rate==2)
M3<-subset(M,dest_rate==3)
M4<-subset(M,dest_rate==4)

S<-print(sprintf(" 0 : %i; 1 : %i; 2 : %i; 3 : %i; 4 : %i",length(M0$dest_rate),length(M1$dest_rate),length(M2$dest_rate),length(M3$dest_rate),length(M4$dest_rate)))

# Boxplot
cols=c("antiquewhite4","steelblue1","magenta4","orange","red")
colr = c(rgb(0.8,0.8,0.8,0.8),rgb(0.8,0.8,0.8,0.8),rgb(0.96,0.62,0.51,0.8),rgb(0.02,0.44,0.69,0.8),rgb(0.79,0.00,0.13,0.8))
#col=c("white","white","white","white","white")
pchs=c(1,20,17,18,20,19)

par(mfrow=c(1,3))
col="grey"

boxplot(period1~dest_rate,data=subset(storage,S_1=="Y"),ylim=c(0,10),main="Period 1",ylab= "displacement rate  [m/y]",xlab="destabilization rate",col=colr)
boxplot(period2~dest_rate,data=subset(storage,S_2=="Y"),ylim=c(0,10),main="Period 2",ylab= "displacement rate [m/y]",xlab="destabilization rate",col=colr)
boxplot(period3~dest_rate,data=subset(storage,S_3=="Y"),ylim=c(0,10),main="Period 3",ylab= "displacement rate  [m/y]",xlab="destabilization rate",col=colr)

boxplot(period1~dest_rate,data=storage,ylim=c(0,10),main="Period 1",ylab= "displacement rate  [m/y]",xlab="destabilization rate",col=colr)
boxplot(period2~dest_rate,data=storage,ylim=c(0,10),main="Period 2",ylab= "displacement rate [m/y]",xlab="destabilization rate",col=colr)
boxplot(period3~dest_rate,data=storage,ylim=c(0,10),main="Period 3",ylab= "displacement rate  [m/y]",xlab="destabilization rate",col=colr)

