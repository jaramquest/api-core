FROM jaramquest/api-base

COPY ../requirements.txt ./
COPY requirements.dev.txt ./
RUN pip install --no-cache-dir -r ./requirements.txt && \
    pip install --no-cache-dir -r ./requirements.dev.txt

ARG USERNAME=vscode
ARG INSTALL_ZSH="true"
ARG USER_UID=1000
ARG USER_GID=$USER_UID
ARG COMMON_SCRIPT_SOURCE="https://raw.githubusercontent.com/microsoft/vscode-dev-containers/master/script-library/common-alpine.sh"
ARG COMMON_SCRIPT_SHA="dev-mode"

RUN apk update \
    && apk add --no-cache curl ca-certificates \
    && curl -sSL  ${COMMON_SCRIPT_SOURCE} -o /tmp/common-setup.sh \
    && if [ "$COMMON_SCRIPT_SHA" != "dev-mode" ]; then echo "$COMMON_SCRIPT_SHA */tmp/common-setup.sh" | sha256sum -c - ; fi \
    && /bin/ash /tmp/common-setup.sh "${INSTALL_ZSH}" "${USERNAME}" "${USER_UID}" "${USER_GID}" \
    && rm /tmp/common-setup.sh
