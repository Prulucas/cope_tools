# COPE Tools - Backend (API REST) 🚀

O **COPE Tools** é uma API REST robusta construída em Python utilizando o ecossistema **Django** e **Django Rest Framework (DRF)**. O objetivo principal deste projeto é fornecer serviços assíncronos de processamento de dados para aplicações Frontend, incluindo ferramentas úteis para o dia a dia, como um conversor dinâmico de strings e sorteadores personalizados.

O projeto está em produção e hospedado no **Render**, integrado de forma totalmente segura e assíncrona com um Frontend em React (Vite) hospedado na **Vercel**.

---

## 🛠️ Tecnologias e Dependências Utilizadas

* **Python 3.12+**
* **Django (v6.0+)** - Framework web principal.
* **Django Rest Framework (DRF)** - Criação de endpoints e serialização de dados de forma robusta.
* **Django CORS Headers** - Configuração de políticas de segurança para liberação de domínios em produção (CORS).
* **WhiteNoise** - Serviço otimizado para arquivos estáticos em ambiente de produção.

---

## 🔌 Endpoints da API

A API expõe os seguintes serviços (comunicação via JSON):

### 1. Conversor de Texto
* **Rota:** `/api/upper/`
* **Método:** `POST`
* **Payload Esperado:**
  ```json
  {
    "text": "exemplo de texto",
    "type": "MAIÚSCULAS"
  }


* **Rota:** `/api/lower/`
* **Método:** `POST`
* **Payload Esperado:**
  ```json
  {
    "text": "exemplo de texto",
    "type": "minúsculas"
  }
