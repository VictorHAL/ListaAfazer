# ✦ Lista de Afazeres

Protótipo de alta fidelidade de uma aplicação **To-Do List** desenvolvida com **Flask** (backend) e **HTML/CSS/JS** puro (frontend), com estética dark editorial.

Projeto entregue como protótipo funcional para apresentação em **07/04/2025**, com previsão de migração para Firebase após aprovação.

---

## 🖥️ Tecnologias

| Camada | Tecnologia |
|--------|-----------|
| Backend | Python 3 + Flask + Flask-CORS |
| Frontend | HTML5, CSS3, JavaScript (Vanilla) |
| Persistência | JSON local (→ Firebase Firestore em breve) |

---

## 📋 Requisitos Implementados

### ✅ Funcionais
- **Adicionar tarefas** — via campo de texto + botão ou tecla `Enter`
- **Remover tarefas** — botão de exclusão ao lado de cada item

### ✅ De Domínio
- **Validação de entrada** — impede tarefas com texto vazio
- **Persistência básica** — tarefas salvas em `tasks.json`, mantidas entre sessões

### ✅ Não-Funcionais
- **Responsividade** — layout adaptado para mobile e desktop
- **Usabilidade** — feedback visual via toasts para todas as ações

### ✅ Regras de Negócio
- **Limite de tarefas** — máximo de 10 tarefas simultâneas
- **Formatação automática** — primeira letra de cada tarefa capitalizada automaticamente

---

## 🚀 Como rodar localmente

**Pré-requisitos:** Python 3.8+

```bash
# 1. Clone o repositório
git clone https://github.com/VictorHAL/ListaAfazer.git
cd ListaAfazer

# 2. Instale as dependências
pip install -r requirements.txt

# 3. Inicie o servidor
python app.py
```

Acesse em: [http://localhost:5000](http://localhost:5000)

---

## 📁 Estrutura do Projeto

```
ListaAfazer/
├── app.py                  # Backend — rotas e regras de negócio
├── requirements.txt        # Dependências Python
├── tasks.json              # Persistência local (gerado automaticamente)
└── templates/
    └── index.html          # Frontend — interface da aplicação
```

---

## 🔌 Endpoints da API

| Método | Rota | Descrição |
|--------|------|-----------|
| `GET` | `/api/tasks` | Lista todas as tarefas |
| `POST` | `/api/tasks` | Cria uma nova tarefa |
| `PATCH` | `/api/tasks/<id>` | Alterna status (concluída/pendente) |
| `DELETE` | `/api/tasks/<id>` | Remove uma tarefa |

---

## 🗺️ Próximos Passos

- [ ] Adicionar edição da tarefa
- [ ] Adicionar data de conclusão da tarefa
- [ ] Alterar cores para tons claros pasteis
- [ ] Autenticação de usuários
- [ ] Migração para Firebase Firestore
- [ ] Deploy no Firebase Hosting
- [ ] Edição inline de tarefas
- [ ] Mover as tarefas de lugar 
- [ ] Separar tarefas concluidas de tarefas a serem feitas

---