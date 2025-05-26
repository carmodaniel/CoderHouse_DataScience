# Sistema de Cadastro de Usuários

## Descrição
Sistema em Python para cadastro e gerenciamento de usuários com validações robustas e interface de linha de comando. O programa permite registrar usuários com validação de dados, listar usuários cadastrados em formato de tabela e gerenciar o fluxo através de um menu interativo.

## Funcionalidades

### Validações Implementadas
- **Nome de usuário**: 8 a 16 caracteres, verificação de duplicidade
- **E-mail**: Validação básica com presença do símbolo "@"
- **Data de nascimento**: Formato dd/mm/aaaa, verificação de maioridade (18+ anos)
- **Senha**: 8 a 16 caracteres com mínimo de 2 caracteres especiais

### Funcionalidades do Sistema
- Cadastro de usuários com múltiplas validações
- Listagem de usuários em formato de tabela
- Sistema de tentativas limitadas (máximo 3 por campo)
- Login usuário
- Menu interativo para navegação