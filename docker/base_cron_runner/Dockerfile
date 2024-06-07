FROM ubuntu:latest


#installs
RUN apt-get update
RUN apt-get -y install cron


#add cronjobs
RUN mkdir -p /etc/cronner/jobs
RUN chmod -R 0644 /etc/cronner/jobs
RUN for cronfile in $(ls /etc/cronner/jobs); do crontab /etc/cron.d/$cronfile; done 
RUN chmod -R 0644 /etc/cron.d/


#entry -> run cron
ENTRYPOINT ["cron", "-f"]


######################################
####                              ####
######################################

#runs the cronjobs that are put into /etc/cronner/jobs