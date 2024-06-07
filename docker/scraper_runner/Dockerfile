FROM cronner:latest


#installs
RUN apt install --yes python3
RUN apt install --yes python3-full
RUN apt install --yes python3-pip
RUN apt install --yes pipenv



#
# clone with github token
#
COPY cronner/Pipfile /etc/cronner/Pipfile
COPY cronner/to_cron.py /etc/cronner/to_cron.py
RUN ls /etc/cronner/

COPY job_scraper/ /etc/job_scraper
RUN ls /etc/job_scraper

#entry
#ADD entry.sh /etc/scripts/entry.sh
#RUN chmod 715 /etc/scripts/entry.sh


#ENTRYPOINT ["/etc/scripts/entry.sh"]