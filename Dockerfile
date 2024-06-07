FROM ubuntu:latest


#installs
RUN apt-get update
RUN apt-get -y install cron


#add cronjobs
RUN mkdir -p /etc/cronner/jobs
RUN chmod -R 0644 /etc/cronner/jobs
RUN for cronfile in $(ls /etc/cronner/jobs); do crontab /etc/cronner/jobs/$cronfile; done 


#entry
ADD entry.sh /etc/scripts/entry.sh
RUN chmod 715 /etc/scripts/entry.sh

ENTRYPOINT ["/etc/scripts/entry.sh"]


######################################
####                              ####
######################################

#runs the cronjobs that are put into /etc/cronner/jobs