#Instalação do ambiente virtual 
python -m venv .venv
source ./venv/bin/activate


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
