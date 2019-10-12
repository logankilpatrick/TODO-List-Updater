FROM debian:9.5-slim

LABEL "com.github.actions.name"="TODO List Updater"
LABEL "com.github.actions.description"="Keep an up to date todo.txt file in your code"
LABEL "com.github.actions.icon"="mic"
LABEL "com.github.actions.color"="purple"

LABEL "repository"="https://github.com/ChandlerKilpatrick1/TODO-List-Updater"
LABEL "homepage"="https://github.com/ChandlerKilpatrick1/TODO-List-Updater"
LABEL "maintainer"="Chandler Kilpatrick <kilpa@sas.upenn.edu>"

ADD entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
