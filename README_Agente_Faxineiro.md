# 🕵️‍♂️ Agente Davidflix v3.0 - Sistema de Monitoramento de Infraestrutura

## Documentação Oficial do Projeto de Automação e Monitoramento

### 📖 1. Visão Geral do Projeto

O Agente Davidflix é um software de monitoramento autônomo desenvolvido em Python. Ele foi criado com o objetivo de transformar um Mac Pro 2008 em um servidor inteligente e resiliente. O sistema vigia constantemente a saúde do hardware e utiliza uma integração com o Telegram para reportar incidentes em tempo real.

### 🏗️ 2. Arquitetura do Sistema

O projeto utiliza uma arquitetura baseada em Multithreading (Processamento em Paralelo), dividida em duas frentes:

Frente Web (Flask): Disponibiliza um Dashboard acessível via navegador na porta 5000 para conferência visual dos dados.

Frente de Vigilância (Backend): Um loop contínuo que roda em segundo plano, coletando dados dos sensores a cada 300 segundos (5 minutos) sem interferir na navegação do usuário.

### 🛠️ 3. Tecnologias e Ferramentas

| Ferramenta | Função no Projeto |
|----------|------------------|
| Python 3 | Linguagem principal e lógica do Agente |
| Flask | Criação da interface de Dashboard Web |
| Psutil | Biblioteca para leitura de RAM, CPU e Disco |
| Threading | Gerenciamento de tarefas simultâneas |
| Telegram API | Sistema de alertas e notificações mobile |
| Git/GitHub | Controle de versão e backup seguro na nuvem |

### 📊 4. Parâmetros de Monitoramento

O Agente está programado para disparar notificações automáticas quando os seguintes limites (Thresholds) são atingidos:

🧠 Memória RAM: Alerta enviado se o uso ultrapassar 70%.  
🔥 Temperatura: Alerta enviado se a CPU passar de 80°C.  
💾 Armazenamento (SSD): Alerta enviado se o espaço ocupado exceder 85%.

### 📦 5. Guia de Instalação e Execução

Passo 1: Instalar Dependências

No terminal do seu servidor, instale as bibliotecas necessárias:

```bash
pip install flask psutil requests 

```

Passo 2: Rodar em Modo Servidor (Background)

Para garantir que o Agente continue funcionando após você sair do terminal, utilize o comando nohup:

```
nohup python3 agente_faxineiro.py > log_agente.txt 2>&1 & 
```
Verificar Logs
Para ver o que o Agente está fazendo agora:

```
tail -f log_agente.txt
```

Liberar Porta 5000
Se o servidor retornar erro de "Port already in use":

```
sudo fuser -k 5000/tcp
```

Sincronizar com GitHub
```
git add .
git commit -m "update manual"
git push origin master
```

🎮 Filosofia do Desenvolvimento

Este projeto demonstra que hardware clássico, como o Mac Pro 2008, ainda é plenamente capaz quando aliado a uma camada de software inteligente.

O foco do desenvolvimento é:

Estabilidade

Visibilidade

Segurança dos dados

Desenvolvido por: David Alex
