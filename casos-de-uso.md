## Casos de Uso:

### Caso de uso 1: Efetuar cadastro.

#### Atores:

- Cliente.

#### Regras de uso:

- O e-mail deve ser único no sistema.
- A senha deve ter no mínimo 8 caracteres.
- Não é permitido registrar com campos vazios.
  
#### Fluxo principal:

- O cliente seleciona a opção "Criar conta".
  
- O sistema leva o usuário até a tela de registro contendo um formulário.
  
- O cliente preenche os campos do formulário (informando nome, e-mail e criando uma senha).
  
- O sistema consulta o banco de dados para verificar a disponibilidade das informações fornecidas.
  
- O banco de dados retorna uma confirmação positiva.
  
- O sistema realiza o cadastro, salvando os dados do novo usuário.
  
- O sistema encaminha o usuário para a página principal do site.




### Caso de Uso 2: Efetuar login.

#### Atores: 

- Usuário.

#### Regras de uso:

- O usuário deve estar registrado no sistema.
- Email e senha são obrigatórios.
- O sistema deve bloquear a conta após 3 tentativas falhadas.

#### Fluxo principal:

- O usuário seleciona a opção "Login".

- O sistema leva o usuário até a tela de preenchimento de senha e email.

- O usuário preenche os campos da tela.

- O sistema consulta o banco de dados para a confirmação dos dados inseridos.

- O banco de dados retorna uma confirmação positiva.

- O sistema encaminha o usuário para a página principal do site.




### Caso de Uso 3: Buscar livros.

#### Atores: 

- Usuário.

#### Regras de uso:

- A busca não diferencia maiúsculas de minúsculas.
- É possível buscar por título, gênero ou autor.
- O sistema exibe no máximo 20 livros por página.
- Os resultados são ordenados por relevância.

#### Fluxo principal: 

- O sistema apresenta a página inicial do site.

- O usuário aperta na barra de pesquisa.

- O usuário digita o livro que deseja, o gênero de livro que deseja ou o autor.

- O usuário aperta no botão "Enter".

- O sistema consulta o banco de dados.

- O banco retorna os livros.

- Os livros são exibidos.




### Caso de Uso 4: Comentar.
 
#### Atores: 

- Usuário.

#### Regras de uso:

- O cliente pode comentar e apagar apenas seus próprios comentários.
- O administrador pode apagar qualquer comentário.
- Comentários devem ter entre 1 e 500 caracteres.
- Não é permitido comentários vazios.

#### Fluxo principal:  

- O cliente abre a aba de um livro específico.

- O cliente aperta em um botão de comentário.

- O sistema abre uma página de comentários do tal livro.

- O cliente escreve o seu comentário.

- O cliente aperta em um botão de publicar em comentário.

- O sistema pede confirmação do usuário.

- O cliente confirma a publicação.

- O sistema publica o comentário.




### Caso de Uso 5: Efetuar aluguel.

#### Atores: 

- Administrador.

#### Regras de uso:

- O livro deve estar disponível para aluguel.
- O cliente não pode ter aluguéis com multa em aberto.
- O prazo de aluguel é de 14 dias.
- Um cliente só pode alugar no máximo 5 livros simultaneamente.

#### Fluxo principal:  

- O administrador inicia o processo de aluguel.

- O administrador preenche o código do livro a ser alugado.

- O sistema exibe os dados do livro a ser alugado.

- O administrador preenche a identificação do cliente.

- O sistema exibe um prazo para devolução. 
  
- O administrador finaliza o aluguel e é redirecionado para a página inicial.


 

### Caso de Uso 6: Finalizar aluguel.

#### Atores: 

- Administrador.

#### Regras de uso:

- Apenas aluguéis em andamento podem ser finalizados.
- O livro deve estar no estado "alugado" no sistema.
- A data de devolução é registrada automaticamente.

#### Fluxo principal:  

- O administrador abre a página de aluguéis do cliente.

- O administrador clica na opção de dar baixa no livro.

- O sistema pede confirmação.

- O administrador confirma.

- O sistema volta para página inicial.




### Caso de Uso 7: Gerenciar livros.

#### Atores: 

- Administrador.

#### Regras de uso:

- Apenas administradores podem editar informações dos livros.
- Não é permitido deixar campos obrigatórios vazios.
- ISBN deve ser único para cada livro.
- O preço de aluguel deve ser maior que zero.

#### Fluxo principal:  

- O administrador abre a página de um livro.

- O administrador aperta no botão de editar livro.

- O administrador escolhe o que quer editar.

- O administrador edita.

- O administrador aperta no botão de salvar.

- O sistema pede confirmação.

- O administrador confirma.

- O sistema avisa que a edição foi feita.




### Caso de Uso 8: Gerenciar usuários.

#### Atores: 

- Administrador.

#### Regras de uso:

- Apenas administradores podem deletar usuários.
- Um usuário com aluguéis em andamento não pode ser deletado.
- A exclusão é permanente e não pode ser desfeita.
- Um log de exclusão é registrado no sistema.

#### Fluxo principal: 

- O administrador vai para a página de usuários.

- O administrador escolhe um usuário.

- O administrador clica no perfil do usuário.

- O administrador entra no perfil do usuário.

- O administrador clica no botão de apagar usuário.

- O sistema pede confirmação.

- O administrador confirma.

- O sistema apaga o usuário.

- O sistema manda uma mensagem de que o usuário foi apagado.




### Caso de Uso 9: Gerenciar perfil.

#### Atores:

- Cliente.

#### Regras de uso:

- Apenas o próprio cliente pode editar seu perfil.
- Email não pode ser alterado se já estiver vinculado a outra conta.
- Senha deve ter no mínimo 8 caracteres ao ser alterada.
- Campo de telefone é opcional.

#### Fluxo principal:

- O cliente clica no ícone do próprio perfil.

- O sistema abre a página do perfil do cliente.

- O cliente clica em editar informações do perfil.

- O cliente edita as informações do perfil.

- O cliente clica no botão de salvar.

- O sistema pede confirmação.

- O cliente confirma.

- O sistema edita as informações.

- O sistema manda uma mensagem dizendo que a edição foi feita.




### Caso de Uso 10: Efetuar multa.

#### Atores:

- Administrador.

#### Regras de uso:

- A multa é calculada automaticamente: R$ 5,00 por dia de atraso.
- Multas só podem ser aplicadas após o prazo de devolução ter expirado.
- O cliente deve ser notificado da multa aplicada.
- A multa deve ser paga antes de fazer um novo aluguel.

#### Fluxo principal: 

- O administrador entra no perfil do usuário.

- O administrador verifica que ele passou do prazo.

- O administrador clica em multar o usuário.

- O sistema pede confirmação.

- O administrador confirma.

- O sistema multa o usuário.

- O sistema manda uma mensagem dizendo que a multa foi feita.
