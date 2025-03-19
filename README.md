# Gerador de Programas Fortran

## Descrição
Este é um gerador de programas Fortran que permite criar códigos baseados em diferentes cálculos matemáticos e físicos. Ele fornece uma interface interativa para que o usuário escolha o tipo de programa que deseja gerar, respondendo a perguntas e gerando automaticamente um código Fortran correspondente.

## Funcionalidades
- Interface interativa para escolha de programas
- Geração automática de códigos Fortran
- Suporte para diferentes cálculos matemáticos e físicos

## Requisitos
- Python 3.x
- Biblioteca `os` (inclusa no Python padrão)

## Instalação
Antes de executar o programa, instale as dependências necessárias:
```sh
pip install -r requirements.txt
```

## Como Usar
1. Clone este repositório:
   ```sh
   git clone https://github.com/tatudev1/seurepositorio.git
   ```
2. Navegue até o diretório do projeto:
   ```sh
   cd seurepositorio
   ```
3. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```
4. Execute o script Python:
   ```sh
   python gerador_fortran.py
   ```
5. Responda às perguntas para gerar o código desejado.
6. O código Fortran será salvo em um arquivo gerado automaticamente.

## Exemplo de Saída
Aqui está um exemplo de um código Fortran gerado pelo programa:
```fortran
program exemplo
  implicit none
  real :: a, b, resultado
  print *, 'Digite dois números:'
  read *, a, b
  resultado = a + b
  print *, 'Resultado:', resultado
end program exemplo
```

## Contribuição
Sinta-se à vontade para contribuir! Para isso:
1. Fork o repositório
2. Crie uma branch com sua feature (`git checkout -b minha-feature`)
3. Commite suas mudanças (`git commit -m 'Adicionando nova funcionalidade'`)
4. Faça um push para a branch (`git push origin minha-feature`)
5. Abra um Pull Request

## Licença
Este projeto está licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

