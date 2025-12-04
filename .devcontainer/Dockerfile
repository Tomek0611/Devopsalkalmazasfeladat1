# Dev container base image (VS Code devcontainer base)
FROM mcr.microsoft.com/vscode/devcontainers/python:3.11

# Beállítjuk a munkakönyvtárat (itt fog a projekt mountolódni)
WORKDIR /workspace

# Másoljuk be a requirements fájlt a build során, így a pip cache használható
COPY requirements.txt /tmp/requirements.txt

# Telepítjük a Python függőségeket (build lépésben)
RUN python -m pip install --upgrade pip \
    && pip install --no-cache-dir -r /tmp/requirements.txt

# (opcionális) Hozzáadhatsz eszközöket / csomagokat:
# RUN apt-get update && apt-get install -y git curl

# Állítsuk be, hogy a vscode felhasználó legyen az alapértelmezett
ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID

# Bizonyos alap image-ek már létrehozzák a vscode usert; ha nem, itt lehet megtenni.
# (a base image már tartalmazza ezt; a sorok biztonsági okból vannak)
RUN if id -u ${USERNAME} >/dev/null 2>&1; then echo "user exists"; else \
    groupadd --gid ${USER_GID} ${USERNAME} \
    && useradd -s /bin/bash --uid ${USER_UID} --gid ${USER_GID} -m ${USERNAME}; \
    fi

# Munka könyvtár engedélyek
RUN chown -R ${USERNAME}:${USERNAME} /workspace

USER ${USERNAME}

# EXPOSE csak dokumentációs célból
EXPOSE 8080

# Alapértelmezett parancs nincs; a fejlesztő a terminálból indítja az appot:
# e.g. python app.py

