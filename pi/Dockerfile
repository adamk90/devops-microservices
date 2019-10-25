FROM python
RUN pip3 install flask-restful flask
RUN wget https://releases.hashicorp.com/consul/1.6.1/consul_1.6.1_linux_amd64.zip && \
    unzip consul_1.6.1_linux_amd64.zip
ADD pi.json /
ADD entrypoint.sh /
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
