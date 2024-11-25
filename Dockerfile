FROM python:3.13.0-alpine AS builder
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/
ADD pyproject.toml README.md src/ uv.lock /sanremo/
WORKDIR /sanremo
RUN uv sync --no-dev --frozen

FROM python:3.13.0-alpine
COPY --from=builder /sanremo /sanremo
ENTRYPOINT ["/sanremo/.venv/bin/sanremo"]
