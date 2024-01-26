FROM ubuntu

# update ubuntu
RUN apt-get update

# install build tools
RUN apt-get install -y build-essential git

# clone OpenSSL and checkout vulnerable version
RUN git clone https://github.com/openssl/openssl && \
    cd openssl && \
    git checkout OpenSSL_1_0_1f

# build and install vulnerable version of OpenSSL
RUN cd /openssl && \
    ./config --prefix=/openssl_1_0_1f --openssldir=/openssl_1_0_1f && \
    make && \
    make install_sw

# generate private and public (certificate) SSL keys
RUN mkdir /keys && \
    cd /keys && \
    /openssl_1_0_1f/bin/openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -days 365 -nodes -subj "/C=US/ST=AR/L=Somewhere/O=Acme/CN=www.example.com"

ENTRYPOINT [ "/openssl_1_0_1f/bin/openssl", "s_server", "-key", "/keys/key.pem", "-cert", "/keys/cert.pem", "-accept", "443", "-www" ]
