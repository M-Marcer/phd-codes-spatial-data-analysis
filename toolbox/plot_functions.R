# Plot Function

# Input taken : 
# years ; int []
# plot_rate : num []
# plot_uncertainty : num[]. default = 0

# TEST VALUES 
#years = sort(unique(moving_target$year))
#plot_rate = output[[k]]$speed
#plot_uncertainty = output[[k]]$weighted_uncertainty


plot_rg_rates <-function(k=1,years,plot_rate,plot_uncertainty=array(0,dim = (length(years))),
                         colors=1:length(years),colors_uc=1:length(years),style=1:length(years)){
  
  x_axis=seq(min(years),max(years),0.05)
  y_axis=x_axis
  
  j=1
  for (i in 1:length(x_axis)){
    
    if (x_axis[i]<years[j+1]){
      y_axis[i]=plot_rate[j]}
    else {y_axis[i]=plot_rate[j]
    j=j+1}
  }
  
  if (k==1){
    plot(x_axis,y_axis,type='l',col=colors[k],lty=style[k],lwd=2,xlab="Year",ylab="Displacement rate [m/y]",cex.lab=1.5,cex.axis=1.5,
         ylim=c(0,max(y_axis)+2),xlim=c(1930,2020))}else{lines(x_axis,y_axis,col=colors[k],lty=style[k],lwd=2)}
  
  # Ucertainty bars
  for (i in 1:(length(years)-1)){
    rect(years[i],plot_rate[[i]]-plot_uncertainty[[i]],years[i+1],plot_rate[[i]]+plot_uncertainty[[i]],col=colors_uc[k],border=NA)
  }
  
  # Reprint lines to make it more outstanding
  lines(x_axis,y_axis,col=colors[k],lty=style[k],lwd=2)
  
  
}