FROM python:3.5.3
ADD . /work
WORKDIR /work
RUN cd /opt && \
    git clone https://github.com/taku910/mecab.git && \
    cd /opt/mecab/mecab && \
    ./configure --with-charset=utf8 && \
    make && \
    make check && \
    make install && \
    echo "/usr/local/lib" >> /etc/ld.so.conf && \
    ldconfig
RUN cd /opt && \
    wget -O mecab-ipadic-2.7.0-20070801.tar.gz "https://drive.google.com/uc?export=download&id=0B4y35FiV1wh7MWVlSDBCSXZMTXM" && \
    tar zxfv mecab-ipadic-2.7.0-20070801.tar.gz && \
    cd mecab-ipadic-2.7.0-20070801 && \
    ./configure --with-charset=utf8 && \
    make && \
    make check && \
    make install
RUN pip install -r requirements.txt
RUN wget https://ja.osdn.net/projects/vlgothic/downloads/62375/VLGothic-20141206.tar.xz -P /tmp/
RUN tar Jxfv /tmp/VLGothic-20141206.tar.xz -C /usr/share/fonts/

CMD ["/bin/bash"]
