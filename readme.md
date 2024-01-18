# Scraping Centralizador de Vagas InHire

Este projeto é uma prova de conceito (POC) que tem como objetivo centralizar todos os subdomínios .inhire e realizar o scraping de vagas. Ele permite coletar informações sobre vagas de emprego a partir de vários subdomínios da plataforma InHire e armazenar esses dados de forma organizada.

## Funcionalidades

- **Centralização de Subdomínios**: O projeto identifica automaticamente todos os subdomínios .inhire a partir de um texto de entrada e os utiliza para fazer requisições às APIs correspondentes.

- **Coleta de Vagas**: Para cada subdomínio encontrado, o sistema faz uma requisição à API da InHire para coletar informações sobre as vagas de emprego disponíveis.

- **Tratamento de Dados**: Os dados coletados são tratados para criar URLs válidas para cada vaga, eliminando caracteres especiais e substituindo espaços por hifens.

- **Armazenamento em JSON**: As informações coletadas são armazenadas em um arquivo JSON para fácil consulta e análise.

## Pré-requisitos

Certifique-se de ter as seguintes bibliotecas instaladas a partir do arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Atenção!

    Atualmente, ainda não faço o scraping por meio de automação dos resultados no google. É necessário para o usuário abrir uma nova pesquisa no google com o texto "site:inhire.app" , realizar o scroll até o fim da página e COPIAR todo o texto (ctrl c e ctrl v), jogando o texto no arquivo input.txt. O sistema então fará o match por meio de regex em "https://xxxxx.inhire.app/" onde XXXXX é o domínio. Após isso, excluirá os links duplicados.

## Como Usar

1. Clone este repositório:

```bash
git clone https://github.com/seu-usuario/inhire-scraping.git
cd inhire-scraping
```

2. Execute o script principal:

```bash
python script.py
```

3. O script solicitará um arquivo de entrada contendo os subdomínios .inhire. Certifique-se de ter um arquivo de texto no formato especificado.

4. O script realizará as requisições aos subdomínios, coletará as informações das vagas e as salvará em um arquivo JSON.

5. Você poderá acessar os dados coletados no arquivo `inhire_jobs.json`.

## Contribuindo

Contribuições são bem-vindas! Se você deseja melhorar este projeto, sinta-se à vontade para abrir uma [issue](https://github.com/seu-usuario/inhire-scraping/issues) ou enviar um [pull request](https://github.com/seu-usuario/inhire-scraping/pulls).

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
