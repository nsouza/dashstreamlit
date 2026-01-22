#Instalação do ambiente virtual 
python -m venv .venv
source ./venv/bin/activate
env\Scripts\activate


#Bibliotecas instaladas
pip install pandas plotly streamlit

#fazer upload  para github
git init
git add .
git commit -m "Primeiro commit do projeto DASHSTREAMLIT"
git branch -M main
git remote add origin https://github.com/nsouza/dashstreamlit.git
git push -u origin main


git remote add origin https://github.com/nsouza/dashstreamlit.git
git branch -M main
git push -u origin main


#Para atualizar projeto apos criar ou excluir arquivos
git status
git add .
git commit -m "Descrição das atualizações feitas"
git push origin main


#Atualizar  o projeto entre um computador e outro suando a nuvem
Git branch (para saber a branch)
git pull (para baixar as atualizações)