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
    make && make install
RUN pip install -r requirements.txt
RUN wget https://ja.osdn.net/projects/vlgothic/downloads/62375/VLGothic-20141206.tar.xz -P /tmp/ && \
    tar Jxfv /tmp/VLGothic-20141206.tar.xz -C /usr/share/fonts/
RUN wget  -O CRF++-0.58.tar.gz "https://drive.google.com/uc?export=download&id=0B4y35FiV1wh7QVR6VXJ5dWExSTQ" && \
    tar zxfv CRF++-0.58.tar.gz && \
    cd CRF++-0.58 && \
    ./configure && \
    make && make install
COPY cabocha-0.69.tar.bz2 /root/cabocha-0.69.tar.bz2
RUN echo "/usr/local/lib" >> /etc/ld.so.conf.d/lib.conf && ldconfig && \
    cd /root/ && \
    tar jxvf cabocha-0.69.tar.bz2 && \
    cd cabocha-0.69 && \
    ./configure --with-mecab-config=`which mecab-config` --with-charset=UTF8 && \
    make && make install && \
    cd python && \
    python setup.py build && \
    python setup.py install
RUN echo "ldconfig" >> /root/.bashrc

CMD ["/bin/bash"]
