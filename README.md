Ez a projekt teljes körűen futtatható GitHub Codespaces környezetben.
A repó tartalmaz egy .devcontainer mappát, amely automatikusan beállítja: a Python 3.11 fejlesztőkörnyezetet, a projekt függőségeit (requirements.txt alapján), a szükséges portokat és környezeti változókat, valamint a konténer indításához szükséges beállításokat.

.devcontainer/
 -devcontainer.json
 -Dockerfile
HelloWorld.py
requirements.txt

Indítás GitHub Codespaces-ben

A GitHub repóban kattints:
Code → Open with Codespaces → New Codespace
GitHub automatikusan felépíti a .devcontainer alapján a környezetet.
A Codespaces termináljában futtasd: python HelloWorld.py

Dev Container működése
A Dockerfile telepíti a Python 3.11-et és a függőségeket.
A devcontainer.json: a Dockerfile-t használja a konténer felépítéséhez, átirányítja a 8080-as portot, beállítja a környezeti változókat, konténer indulás után lefuttat egy rövid státusz üzenetet.

A Dev Containerben a kód automatikusan a /workspace könyvtárba mountolódik – itt kell futtatni: python HelloWorld.py
