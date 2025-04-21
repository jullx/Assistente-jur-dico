# 🤖 Assistente Jurídico Inteligente com IA

Este é um **projeto base** de um chatbot jurídico inteligente que responde perguntas com base em uma base de conhecimento pré-definida, utilizando modelos de linguagem da **FlagEmbedding (BGEM3)** para busca semântica.

O projeto foi feito com **Python** e usa a biblioteca **Streamlit** para criar uma interface simples e amigável no navegador.

---

## 🚀 Como funciona

1. O usuário digita uma pergunta jurídica (ex: "posso devolver um produto comprado online?")
2. A pergunta é transformada em vetor por um modelo de embedding semântico.
3. O sistema compara com vetores de uma base jurídica (ex: CDC).
4. A resposta mais parecida semanticamente é exibida.

---

## 📦 Tecnologias usadas

- [Python 3.8+](https://www.python.org/)
- [Streamlit](https://streamlit.io)
- [FlagEmbedding / BGE-M3](https://huggingface.co/BAAI/bge-m3)
- [NumPy](https://numpy.org/)

---

## ▶️ Como executar localmente

1. Clone este repositório:

```bash
git clone https://github.com/seu-usuario/assistente-juridico-ia.git
cd assistente-juridico-ia
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Execute o projeto:

```bash
streamlit run app.py
```

---

## 🌐 Quer compartilhar com outras pessoas?

- Suba este projeto no [Streamlit Cloud](https://streamlit.io/cloud)
- Ele criará um link público que você pode enviar para qualquer pessoa! 💬

---

## 📌 Status

Este projeto é uma **base inicial**, pronta para ser expandida com novas funcionalidades, novas áreas do direito, integração com bancos de dados jurídicos, etc.

Desenvolvido com 💻 e ⚖️ por Júlia.



---

## 📚 Referência Acadêmica

Este projeto utiliza o modelo BGE-M3, desenvolvido pelos autores:

@misc{bge-m3,  
  title={BGE M3-Embedding: Multi-Lingual, Multi-Functionality, Multi-Granularity Text Embeddings Through Self-Knowledge Distillation},  
  author={Jianlv Chen and Shitao Xiao and Peitian Zhang and Kun Luo and Defu Lian and Zheng Liu},  
  year={2024},  
  eprint={2402.03216},  
  archivePrefix={arXiv},  
  primaryClass={cs.CL}  
}

Disponível em: [https://arxiv.org/abs/2402.03216](https://arxiv.org/abs/2402.03216)

---

## 🙏 Agradecimentos

Agradeço aos desenvolvedores da FlagEmbedding e aos pesquisadores do modelo BGE-M3, que possibilitaram a criação de aplicações acessíveis e inteligentes com base em embeddings semânticos multilíngues.

