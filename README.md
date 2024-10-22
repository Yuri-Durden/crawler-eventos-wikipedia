# Crawler de Eventos Comemorativos da Wikipédia

Este é um crawler desenvolvido em Python que extrai eventos comemorativos da página principal da Wikipédia em português. O script utiliza a biblioteca BeautifulSoup para realizar a raspagem dos dados.

## Pré-requisitos

- Python 3 ou superior
- Bibliotecas necessárias:
  - `requests`
  - `beautifulsoup4`

## Instrução de Uso

### 1. Clone este repositório:
```bash
git clone https://github.com/seuusuario/seurepositorio.git
```

### 2. Navegue até o diretório do projeto:
```bash
cd seurepositorio
```

### 3. Instale as bibliotecas necessárias:
Você pode instalar as bibliotecas necessárias executando o seguinte comando no terminal:

```bash
pip install -r requirements.txt
```

### 4. Execute o script:
```bash
python crawler_wikipedia.py
```
O script irá acessar a página inicial da Wikipédia em português, encontrar o link para a página do dia e extrair os eventos comemorativos listados na seção "Brasil".


## Exemplo de uso

Após executar o script, a saída será algo assim:

```bash
Dia do Professor
Dia Internacional de Algo
Outra data comemorativa...
```

O crawler faz uma busca pelos eventos comemorativos relacionados ao Brasil listados na página principal da Wikipédia em português, permitindo que você veja as datas comemorativas do dia em questão.



