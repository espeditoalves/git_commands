# Plano de Treinamento: Git Merge, Rebase e Resolução de Conflitos

## Contexto
Este projeto será usado como laboratório prático para treinar git merge, rebase e resolução de conflitos. Baseado no artigo Medium sobre Git Merge e Rebase, criaremos múltiplas branches locais com situações de conflito reais para praticar.

---

## Fase 1: Preparação (Branches com Merge Conflicts)

### Cenário 1: Merge Conflict - Mudanças no mesmo arquivo
**Objetivo:** Praticar resolução manual de conflitos em merge

**Passos:**
1. Criar branch `feature/feature1` a partir de `main`
2. Editar arquivo (ex: README.md) - adicionar seção "Recursos"
3. Fazer commit: "Add resources section"
4. Voltar para `main` e criar branch `feature/feature2`
5. Editar o MESMO arquivo README.md em local diferente - adicionar seção "Contribuindo"
6. Fazer commit: "Add contributing section"
7. Tentar merge `feature/feature1` → `main` (sucesso, fast-forward)
8. Tentar merge `feature/feature2` → `main` (CONFLITO - mesmo arquivo, seções diferentes)
9. Resolver manualmente o conflito
10. Commit de merge: "Merge feature/feature2 with conflict resolution"
11. Fazer push para GitHub

**Arquivo alvo:** `README.md`

---

### Cenário 2: Merge Conflict - Mudanças na mesma linha
**Objetivo:** Praticar conflitos mais complexos

**Passos:**
1. Criar branch `bugfix/bug-fix-1` a partir de `main`
2. Editar `scripts/data_processor.py` - alterar comentário na linha 10
3. Commit: "Update documentation in processor"
4. Voltar para `main` e criar branch `bugfix/bug-fix-2`
5. Editar o MESMO arquivo, MESMA linha
6. Commit: "Fix typo in processor documentation"
7. Tentar merge `bugfix/bug-fix-1` (sucesso)
8. Tentar merge `bugfix/bug-fix-2` (CONFLITO na mesma linha)
9. Resolver o conflito escolhendo a melhor versão
10. Commit: "Merge bugfix/bug-fix-2 resolving line conflict"
11. Fazer push para GitHub

**Arquivo alvo:** `scripts/data_processor.py` (ou criar se não existir)

---

### Cenário 3: Conflito com Rebase
**Objetivo:** Praticar rebase interativo e conflitos durante rebase

**Passos:**
1. Criar branch `feature/rebase-feature` a partir de `main`
2. Criar 3 commits pequenos (ex: mudanças incrementais em requirements.txt)
3. Enquanto isso, `main` recebe um commit conflitante
4. Fazer `git rebase main` nessa branch (CONFLITO)
5. Resolver o conflito
6. Usar `git rebase --continue` para prosseguir
7. Repetir se houver mais conflitos
8. Após resolver tudo, fazer merge `feature/rebase-feature` → `main` (deve ser fast-forward)
9. Fazer push para GitHub

**Arquivo alvo:** `requirements.txt`

---

### Cenário 4: Multiple Branches em Paralelo (Complex Merge)
**Objetivo:** Simular trabalho paralelo com múltiplas branches

**Passos:**
1. Criar 3 branches simultâneas de `main`:
   - `dev/api-endpoints`
   - `dev/database-schema`
   - `dev/ui-components`
2. Cada branch modifica arquivos diferentes:
   - `scripts/api.py`
   - `scripts/database.py`
   - `scripts/ui.py`
3. Fazer commits em cada branch
4. Fazer merge de todas em `main` (sem conflitos inicialmente)
5. Fazer push para GitHub

**Arquivos alvo:** Criar novos arquivos em scripts/

---

### Cenário 5: Conflito na Resolução do Conflito (Meta!)
**Objetivo:** Praticar situação onde dois devs resolvem conflito diferente

**Passos:**
1. Criar branch `conflict/resolution-1` a partir de `main`
2. Fazer mudanças e commit
3. Criar branch `conflict/resolution-2` a partir de `main`
4. Fazer mudanças CONFLITANTES e commit
5. Merge `conflict/resolution-1` → `main` (sucesso)
6. Tentar merge `conflict/resolution-2` → `main` (CONFLITO)
7. Resolver conflito de UMA forma
8. Commit: "Merge conflict/resolution-2 - chose resolution-1 approach"
9. Criar branch `conflict/resolution-3` mostrando abordagem ALTERNATIVA
10. Tentar merge (segundo conflito)
11. Resolver de forma diferente
12. Commit: "Merge conflict/resolution-3 - alternative approach"
13. Fazer push para GitHub

**Arquivo alvo:** `README.md` ou novo arquivo

---

## Fase 2: Técnicas Avançadas

### Cenário 6: Cherry-pick com Conflito
**Objetivo:** Praticar cherry-pick e resolução de conflito

**Passos:**
1. Criar branch `cherry/source-branch` com vários commits
2. Criar branch `cherry/target-branch` 
3. Fazer `git cherry-pick` de um commit da source para target (CONFLITO)
4. Resolver manualmente
5. Usar `git cherry-pick --continue`
6. Fazer push para GitHub

---

### Cenário 7: Rebase Interativo com Modificação de Commits
**Objetivo:** Praticar rebase -i para limpar histórico

**Passos:**
1. Criar branch `refactor/interactive-rebase`
2. Criar 5 commits pequenos
3. Usar `git rebase -i HEAD~5`
4. Experimentar:
   - `pick`: manter commit
   - `reword`: alterar mensagem
   - `squash`: combinar com commit anterior
   - `drop`: remover commit
5. Resolver conflitos se houver
6. Fazer push (com force push para branch remota)

---

### Cenário 8: Visualizar Histórico com Git Log
**Objetivo:** Entender o histórico após merges e rebases

**Passos:**
1. Após todos os cenários, executar:
   - `git log --oneline --all --graph` (ver árvore completa)
   - `git log --oneline --decorate` (ver branches)
   - `git reflog` (ver histórico de operações)
2. Identificar:
   - Merge commits (com 2 pais)
   - Fast-forward merges
   - Rebase linear
   - Conflitos resolvidos

---

## Fase 3: Push para GitHub

Após completar todos os cenários:

1. Fazer push de todas as branches para GitHub:
   ```bash
   git push -u origin <branch-name>
   ```
   
2. Para branches com rebase que já existem remotamente:
   ```bash
   git push --force-with-lease origin <branch-name>
   ```

3. Criar Pull Requests no GitHub para cada branch (sem fazer merge)

4. Manter as branches remotas como registro do treinamento

---

## Estrutura de Branches Criadas

```
main (principal)
├── feature/feature1 (merge simples)
├── feature/feature2 (conflito - merge)
├── bugfix/bug-fix-1 (merge simples)
├── bugfix/bug-fix-2 (conflito - linha)
├── feature/rebase-feature (conflito - rebase)
├── dev/api-endpoints (merge sem conflito)
├── dev/database-schema (merge sem conflito)
├── dev/ui-components (merge sem conflito)
├── conflict/resolution-1 (conflito duplo)
├── conflict/resolution-2 (conflito duplo)
├── conflict/resolution-3 (conflito duplo)
├── cherry/source-branch (cherry-pick)
├── cherry/target-branch (cherry-pick com conflito)
└── refactor/interactive-rebase (rebase -i)
```

---

## Conceitos Chave a Praticar (baseado no artigo)

### ✅ Git Merge
- **Fast-forward**: Branch move direto sem novo commit
- **Non-fast-forward**: Cria commit de merge com 2 pais (histórico completo)
- Quando usar: Preservar contexto de branches colaborativas

### ✅ Git Rebase
- **Conceito**: "Recreating your work from one branch onto another"
- **Vantagem**: Histórico linear, sem merge commits
- **Risco**: NUNCA rebase branches compartilhadas (quebra repositórios de outros)
- Quando usar: Branches locais antes de compartilhar

### ✅ Resolução de Conflitos
- Markers de conflito: `<<<<<<<`, `=======`, `>>>>>>>`
- Resolução manual: editar arquivo e manter linhas corretas
- Após resolver: `git add` + `git commit` (ou `git rebase --continue`)

### ✅ Visualização
- `git log --graph`: Entender estrutura de branches
- `git show <commit>`: Ver detalhes de cada commit
- `git diff`: Ver diferenças durante conflito

---

## Ordem Recomendada de Execução

1. ✅ Cenário 1 (Merge simples + conflito fácil)
2. ✅ Cenário 2 (Conflito na mesma linha)
3. ✅ Cenário 3 (Rebase com conflito)
4. ✅ Cenário 4 (Multiple branches)
5. ✅ Cenário 5 (Meta conflito)
6. ✅ Cenário 6 (Cherry-pick)
7. ✅ Cenário 7 (Rebase interativo)
8. ✅ Cenário 8 (Análise do histórico)
9. ✅ Push para GitHub

---

## Verificação e Testes

**Após cada cenário:**
- Executar `git log --oneline --all --graph` para ver mudanças
- Verificar que não há conflitos não resolvidos
- Confirmar que `git status` mostra "working tree clean"

**Após todos os cenários:**
- Verificar que todas as branches estão em GitHub
- Usar GitHub interface para visualizar PRs (com histórico de conflitos resolvidos)
- Executar `git branch -a` para confirmar tudo foi sincronizado

---

## Notas Importantes

- **Nunca force push em `main`** - apenas em branches de feature
- **Use `--force-with-lease`** em vez de `--force` para mais segurança
- **Documente cada resolução** - escreva boas mensagens de commit
- **Revise o histórico regularmente** - use `git log --graph` para aprender padrões
