# Projeto de Análise de Dados

Este projeto contém um notebook simples de análise de dados e uma estrutura de pastas para organizar código, dados e resultados.

## Estrutura

- `run.ipynb` - notebook principal
- `dataset/` - dados de entrada
- `scripts/` - código Python organizado em módulos
  - `scripts/input/` - carregamento de dados
  - `scripts/output/` - exportação e geração de resultados
- `image/` - imagens e gráficos salvos

## Criar ambiente virtual (Windows)

1. Abrir PowerShell ou terminal no diretório do projeto:
   ```powershell
   cd C:\Users\esped\Projects\classes
   ```
2. Criar o ambiente virtual:
   ```powershell
   python -m venv .venv
   ```
3. Ativar o ambiente virtual:
   ```powershell
   (Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned) ; (& .\.venv\Scripts\Activate.ps1) 
   ```
4. Instalar dependências (por exemplo `pandas` e `matplotlib`):
   ```powershell
   pip install pandas matplotlib
   ```

## Executar o notebook

- Abra `run.ipynb` no Jupyter Notebook ou JupyterLab.
- Certifique-se de usar o kernel Python do ambiente virtual `.venv`.

## Contribuindo

Para contribuir com este projeto:

1. Crie uma nova branch a partir de `main`
2. Faça suas alterações
3. Faça um commit com mensagem descritiva
4. Envie um Pull Request

## Observações

- Coloque seu arquivo CSV em `dataset/`.
- O notebook usa `dataset/supplement_impact_data.csv` por padrão.
