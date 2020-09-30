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
cc <- cc %>% mutate(condition=case_when(modification==TRUE & combination==TRUE ~ "Combination and Cumulative",modification==FALSE & combination==TRUE ~ "Combination",modification==TRUE & combination==FALSE ~ "Cumulative"))

#example plot filtered by run 1
run1 <- ggplot(subset(cc, run==1 & ts==9 & gen %in% seq(0,2000,by=1)), aes(x = gen, y = complex_max, colour=as.factor(loss) )) +
  facet_wrap(vars(condition)) +
  stat_summary(fun = mean, geom="step", size=1) +
  ylab("Complexity") +
  xlab("Generation") +
  theme_hc() + scale_colour_colorblind() +
  theme(axis.text=element_text(size=14), axis.title=element_text(size=16,face="bold"),
        legend.title = element_text(size = 14, face="bold"), legend.text = element_text(size = 12))

#Example of how to export graph to powerpoint
library(here)
library(rvg)
library(officer)

run1_dml <- rvg::dml(ggobj = run1)

officer::read_pptx() %>%
  officer::add_slide() %>%
  officer::ph_with(run1_dml, 
                   ph_location(width = 9*2, height = 4.95*2)) %>%
  base::print(
    target = here::here("run1_out.pptx")
  )