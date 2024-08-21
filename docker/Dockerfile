FROM ubuntu:latest


#installs
RUN apt-get update
RUN apt-get -y install cron


#prepare entrypoint to add cronjobs on startup
RUN mkdir -p /etc/cronner/jobs

RUN echo "#!/bin/bash \n\
chmod -R 0644 /etc/cronner/jobs \n\
job_files=$(ls /etc/cronner/jobs) \n\
for cronfile in \$job_files \n\
do \n\
    echo added \$cronfile to crondaemon \n\
    cp /etc/cronner/jobs/\$cronfile /etc/cron.d/\$cronfile \n\
    crontab /etc/cron.d/\$cronfile \n\
done \n\
chmod -R 0644 /etc/cron.d/ \n\
if [ \${#job_files} -gt 0 ] \n\
then \n\
    echo running crondaemon... \n\
    cron -f \n\
else \n\
    echo no cronjobs to run \n\
fi" > /etc/cronner/entry.sh
RUN chmod +x /etc/cronner/entry.sh


#entry -> run entry.sh
ENTRYPOINT ["/etc/cronner/entry.sh"]


######################################
####                              ####
######################################

#runs the cronjobs that are put into /etc/cronner/jobs