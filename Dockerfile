FROM debian:stable-slim AS builder
COPY . /sanremo
WORKDIR /sanremo
RUN apt-get update &&\
    apt-get install -y curl &&\
    curl -sSf https://rye.astral.sh/get | RYE_INSTALL_OPTION=--yes bash &&\
    /root/.rye/shims/rye build

FROM python:3.12.4-alpine
COPY --from=builder /sanremo/dist/sanremo*.tar.gz /sanremo/
RUN pip install /sanremo/sanremo*.tar.gz

ENTRYPOINT ["/usr/local/bin/sanremo"]
