library(data.table)
library(tidyverse)
library(ggthemes)
setwd("your\\directory\\here")


#For reading cleaned up file of run0 and plotting graph that was reported in the paper
cc <- fread("run0.csv")

ggplot(subset(cc, ts==9 & gen %in% seq(0,2000,by=1)), aes(x = gen, y = complex_max, colour=as.factor(loss) )) +
  facet_wrap(vars(condition)) +
  stat_summary(fun = mean, geom="step", size=1) +
  ylab("Problem Complexity") +
  xlab("Generations") +
  theme_hc() + scale_colour_colorblind() +
  theme(axis.text=element_text(size=14), axis.title=element_text(size=16,face="bold"),
        legend.title = element_text(size = 14, face="bold"), legend.text = element_text(size = 12))

#Other runs not reported in paper
cc1 <- fread("local_loss0.0_gens2000.csv")
cc2 <- fread("local_loss0.5_gens2000.csv")
cc3 <- fread("local_loss1.0_gens2000.csv")
cc4 <- fread("combo_loss0.0_gens2000.csv")
cc5 <- fread("combo_loss0.5_gens2000.csv")
cc6 <- fread("combo_loss1.0_gens2000.csv")
cc7 <- fread("combo_local_loss0.0_gens2000.csv")
cc8 <- fread("combo_local_loss0.5_gens2000.csv")
cc9 <- fread("combo_local_loss1.0_gens2000.csv")

#Clean up for raw files
cc <- rbind(cc1,cc2,cc3,cc4,cc5,cc6,cc7,cc8,cc9)
rm(cc1,cc2,cc3,cc4,cc5,cc6,cc7,cc8,cc9)
colnames(cc) <- c("run","gen","ts","loss","modification","combination","complex_max")
cc$condition <- ifelse(cc$modification==TRUE & cc$combination==TRUE,"Combination and Cumulative",ifelse(cc$modification==FALSE & cc$combination==TRUE,"Combination",ifelse(cc$modification==TRUE & cc$combination==FALSE,"Cumulative","NA") ) )

#example plot filtered by run 1
ggplot(subset(cc, run==1 & ts==9 & gen %in% seq(0,2000,by=1)), aes(x = gen, y = complex_max, colour=as.factor(loss) )) +
  facet_wrap(vars(condition)) +
  stat_summary(fun = mean, geom="step", size=1) +
  ylab("Complexity") +
  xlab("Generation") +
  theme_hc() + scale_colour_colorblind() +
  theme(axis.text=element_text(size=14), axis.title=element_text(size=16,face="bold"),
        legend.title = element_text(size = 14, face="bold"), legend.text = element_text(size = 12))