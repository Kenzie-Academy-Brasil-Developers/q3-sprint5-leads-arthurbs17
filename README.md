# Leads

## Rota /api/leads [GET]

### Retornos:

Lista de todos os Leads por ordem de visitas

### Exc:

Quando vazio retorna a mensagem:

```json
{ "message": "Nenhum dado inserido ainda!" }
```

---

## Rota /api/leads [POST]

### Body da requisição:

```json
{
  "name": "John Doe",
  "email": "john@email.com",
  "phone": "(41)90000-0000"
}
```

### Retorna:

```json
{
  "name": "John Doe",
  "email": "john@email.com",
  "phone": "(41)90000-0000",
  "creation_date": "Fri, 10 Sep 2021 17:53:25 GMT",
  "last_visit": "Fri, 10 Sep 2021 17:53:25 GMT",
  "visits": 1
}
```

### Exc:

**Quando já existe o mesmo email ou telefone:**

```json
{ "message": "Email ou telefone já cadastrados!" }
```

**Quando o formato do telefone está errado:**

```json
{
  "correct_format": "(xx)xxxxx-xxxx",
  "your_requisition": 123123213
}
```

---

## Rota /api/leads [PATCH]

### A rota utiliza o email cadastrado para atualizar as informações visits e last_visit

### Body da requisição:

```json
{
  "email": "john@email.com"
}
```

### Retorno:

Aumenta a quantidade de visits em 1 e atualiza a data do last_visit para a data atual.

### Exc:

**Corpo da requisição apenas com email:**

```json
{
  "available_key": "email",
  "your_requisition_keys": ["phone", "email", "name"]
}
```

**Valor passado em formato diferente de string:**

```json
{ "message": "O valor deve ser passado em string" }
```

**Email não encontrado no banco:**

```json
{ "message": "Dado não encontrado no banco" }
```

---

## Rota /api/leads [DELETE]

### A rota utiliza o email cadastrado para deletar as informações

### Body da requisição:

```json
{
  "email": "john@email.com"
}
```

### Retorno:

No body returned for response.

### Exc:

**Corpo da requisição apenas com email:**

```json
{
  "available_key": "email",
  "your_requisition_keys": ["phone", "email", "name"]
}
```

**Valor passado em formato diferente de string:**

```json
{ "message": "O valor deve ser passado em string" }
```

**Email não encontrado no banco:**

```json
{ "message": "Dado não encontrado no banco" }
```
