

compute_distances_and_rates <- function(data){

# This function computes distance and speed for point position at different years
# The attribute " $years" is the one that identifies dates (in year only)

	years<-sort(data$year)
	result<-data.frame(Y=years[1:length(years)-1])

	for(i in 1:(length(years)-1)){
		temp<-subset(data,data$year==years[i])
		temp2<-subset(data,data$year==years[i+1])
		result$year[[i]]<-sprintf("%i - %i",years[i],years[i+1])
		result$dist[[i]]<-pointDistance(temp,temp2)
		result$speed[[i]]<-result$dist[[i]]/(years[i+1]-years[i])
		}
	return(result)
}

##################################################################################################################################################################

distance_wieghted_uncertainty <- function(uncerainty_analysis,moving_target,fixed_areas){

# This function computes the poistion uncertainty for a moving target through years
# NEEDED ATTRIBUTES :  year (both moving target and fixed areas)
  years <- sort(moving_target$year)
  result<-data.frame(Y = years[1:length(years)-1])

	  
  for (i in 1 : (length(years) - 1)){
	    result$year[[i]]<-sprintf("%i - %i",years[i],years[i+1])
	    print(sprintf("Uncertainty for period  %s",result$year[[i]]))
	    
	    if (uncerainty_analysis == TRUE) {	
		    
	    # Define local objects : targets and fixed areas of the years of interest
	    
	      target = subset(moving_target,moving_target$year == years[i] | moving_target$year == years[i+1])
	      temp<-subset(fixed_areas,fixed_areas$year==years[i])
	      temp2<-subset(fixed_areas,fixed_areas$year==years[i+1])
	      
	      # In this case there are no fixed areas for the years of interest, write warning and skip code
	      if (length(temp) == 0 | length(temp2) == 0){  
	        print(sprintf("WARNING - No available fixed areas for uncertainty estimation in years %i - %i !", years[i],years[i+1]))
	        result$weighted_uncertainty[[i]] = 0
	        result$global_uncertainty[[i]] = 0
        
	      # else evaluate distances between same ids at the two years of reference  
	      }else{
	         local = universal_point_distance(temp,temp2,years[i],years[i+1])
	         print(local)

	          # evaluate distance between moving target and fixed areas   
	         # BUG HERE, THE CODE GETS THE DISTANCE OF MORE IDS THAN AVAILABLE
	         #if (length(temp)<length(temp2)){aux = pointDistance(target,temp)
	         #}else{aux = my_pointDistance(target,temp2)}
	          #print(aux)
	         aux = pointDistance(subset(temp,temp$id %in% local$id),target) 
	         
	          # attribute between moving target and fixed areas to each id      
		        if (is.null(dim(aux))==TRUE){local$distance = aux
		        }else{local$distance = rowMeans(aux,na.rm = TRUE)}

	          ordered_local <- local[order(local$distance),]
	          ordered_local$weights <- seq(1,0,by=-1/(length(ordered_local$distance)-1))
	          result$weighted_uncertainty[[i]] = weighted.mean(ordered_local$movement,ordered_local$weights,na.rm = TRUE)/(years[i+1] - years[i])
	          result$global_uncertainty[[i]] = mean(local$movement, na.rm=TRUE)/(years[i+1] - years[i])
	      }
	    # If the user does not want to perform uncertainty analysis, the code gives 0 uncertainty for plotting  
	  	}else{ 
	    result$weighted_uncertainty[[i]]  = 0
	    result$global_uncertainty[[i]]  = 0
	    }
	#result<-result[,c("year","weighted_uncertainty","global_uncertainty")]
  }
  return(result)
}

#######################################################################################################################################################################

universal_point_distance <- function(temp,temp2,year,year2){

  if (length(temp) != length(temp2)){ # In this case some fixed areas are not available for one of the two dates 
	  print(sprintf("WARNING - Not all fixed areas available for both years %i - %i !", year,year2))
	
	  if (length(temp)<=length(temp2)){
	      temp2 = subset(temp2, temp2$id %in% temp$id)
	     }
	  else {
	    temp = subset(temp, temp$id %in% temp2$id)
	    }
  }
  print(sprintf("Available fixed areas ids for year %i ; %s",year,paste(temp$id,collapse=" ")))
  print(sprintf("Available fixed areas ids for year %i ; %s",year2,paste(temp2$id,collapse=" ")))
  aux = my_pointDistance(temp,temp2)
  return(aux)
}

#######################################################################################################################################################################

pointDistance_dataframe <- function(temp,temp2){
  
  result = min(length(temp$id),length(temp2$id))
  IDs = sort(temp$id)
  
  for (i in length(temp$id)){
    aux1 = subset(temp,temp$id==IDs[k])
    aux2 = subset(temp2,temp2$id==IDs[k])
    
    if (length(aux1) == 0 | length(aux2)== 0){
      print(sprintf("ID %i not available in both years",IDs[k]))
    }
    else{result[i] = pointDistance(aux1,aux2)}
  }
     
}

#############################################
# Function to make distance id by id, avoiding disordered distances

my_pointDistance <- function(temp,temp2){
  
  result =data.frame(id = temp$id)
  
  for (i in 1:length(result$id)){
    aux1 = subset(temp,temp$id == temp$id[[i]]) 
    aux2 = subset(temp2,temp2$id == temp$id[[i]])
    if(length(aux1$id)!=0 & length(aux2$id)!=0 ){result$movement[[i]] = pointDistance(aux1,aux2)}
    
  }
  return(result)
  
}
