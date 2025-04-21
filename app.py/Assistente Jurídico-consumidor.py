from FlagEmbedding import BGEM3FlagModel
import numpy as np

# Carrega o modelo
model = BGEM3FlagModel('BAAI/bge-small-en-v1.5', use_fp16=True)  # Modelo menor e mais leve

# Base de conhecimento jurídico
base_conhecimento = [
    "O consumidor pode trocar produtos com defeito dentro de 30 dias.",
    "O direito de arrependimento garante 7 dias para desistência em compras online.",
    "Em caso de cobrança indevida, o valor deve ser devolvido em dobro, com correção monetária e juros legais.",
    "A garantia legal de um produto é de no mínimo 90 dias.",
    "A propaganda enganosa é vedada pelo Código de Defesa do Consumidor.",
]

# Codifica a base
embeddings_base = model.encode(base_conhecimento)['dense_vecs']

# Loop de perguntas no terminal
print("🔍 Assistente Jurídico Inteligente")
print("Digite sua pergunta (ou 'sair' para encerrar):")

while True:
    pergunta = input("\nVocê: ")
    
    if pergunta.lower() in ['sair', 'exit', 'quit']:
        print("👋 Até logo!")
        break

    # Codifica a pergunta
    emb_pergunta = model.encode([pergunta])['dense_vecs']

    # Calcula similaridade
    similaridades = emb_pergunta @ embeddings_base.T
    indice_resposta = np.argmax(similaridades)

    resposta = base_conhecimento[indice_resposta]
    print(f"🧠 Resposta: {resposta}")
